#!/usr/bin/env python3
"""
Build New Dawn custom packs from a folder of pack folders.

Source layout (one folder per pack, PNG or BMP images inside):

    packs-src/
      ART_BetterReagents1/0x0F7A.png ...
      GUMP_GreenBags/0x003C.png ...

The folder prefix (ART_, GUMP_) picks the category and install folder from
packs.config.yml. Everything after the prefix becomes the display name
("ColoredSpellIcons2" -> "Colored Spell Icons 2") unless packs.meta.yml
overrides it.

A license.txt in a pack folder is the pack's credit and license. Its text goes
into packs.json (shown on the pack's card) and ships in the zip as
Data/Custom/Licenses/<id>.txt, next to the folders the client reads.

For each pack this writes to the output folder:

    <id>-<version>.zip            deterministic zip, ready to extract into the game folder
    previews/<id>-<version>.png   contact sheet of the pack's images
    packs.json                    the manifest the docs site and launcher read

Versions are automatic. The previous packs.json (in the output folder, or
passed with --previous) is compared by checksum: unchanged packs keep their
version, changed packs get a patch bump, new packs start at 1.0.0. Zips and
previews from older versions are removed from the output folder.

The output folder is docs/packs, so the docs site serves the packs at
https://codex.uonewdawn.com/packs/. Commit it and deploy as usual.

Usage:
    python tools/build_packs.py packs-src docs/packs
"""

import argparse
import datetime as dt
import hashlib
import io
import json
import os
import posixpath
import re
import sys
import urllib.request
import zipfile

import yaml
from PIL import Image

ZIP_TIME = (2020, 1, 1, 0, 0, 0)  # fixed so identical content gives an identical zip
PREVIEW_WIDTH = 1024  # about twice the card width, so previews stay sharp on high-DPI screens
PREVIEW_HEIGHT = PREVIEW_WIDTH * 3 // 8  # matches the 8:3 preview box in packs.css
PREVIEW_COLS = 8
PREVIEW_MAX_ZOOM = 4  # small icons are enlarged by whole steps at most this far
PREVIEW_MAX = 24
PREVIEW_BG = (24, 24, 28, 255)
KEY_COLORS = {(0, 0, 0), (255, 255, 255)}
IMAGE_EXTS = {".png", ".bmp"}  # what the client loads from Data/Custom
LICENSE_FILE = "license.txt"  # matched case-insensitively


def load_yaml(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_previous(src):
    if not src:
        return {}
    try:
        if src.startswith(("http://", "https://")):
            with urllib.request.urlopen(src, timeout=15) as r:
                data = json.load(r)
        elif os.path.exists(src):
            with open(src, encoding="utf-8") as f:
                data = json.load(f)
        else:
            return {}
    except Exception as ex:  # a missing previous manifest just means "everything is new"
        print(f"warning: couldn't read previous manifest {src}: {ex}", file=sys.stderr)
        return {}
    return {p["id"]: p for p in data.get("packs", [])}


def split_words(s):
    s = re.sub(r"(?<=[a-z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Za-z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", s)
    return s.replace("_", " ").split()


def bump_patch(version):
    major, minor, patch = (int(x) for x in version.split("."))
    return f"{major}.{minor}.{patch + 1}"


def read_license(folder):
    for name in os.listdir(folder):
        if name.lower() == LICENSE_FILE and os.path.isfile(os.path.join(folder, name)):
            with open(os.path.join(folder, name), encoding="utf-8-sig") as f:
                return f.read().strip() or None
    return None


def build_zip(entries):
    """Deterministic zip from (path as installed, bytes) pairs: fixed timestamps, in the order given."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, data in entries:
            info = zipfile.ZipInfo(arc, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    return buf.getvalue()


def load_preview_image(path):
    with Image.open(path) as im:
        # Like the client: images without an alpha channel (BMPs) draw pure black and white as see-through.
        keyed = "A" not in im.getbands() and "transparency" not in im.info
        im = im.convert("RGBA")
    if keyed:
        px = im.load()
        for y in range(im.height):
            for x in range(im.width):
                if px[x, y][:3] in KEY_COLORS:
                    px[x, y] = (0, 0, 0, 0)
    bbox = im.getchannel("A").getbbox()
    return im.crop(bbox) if bbox else None  # trimmed to what's visible; None if it's all see-through


def build_preview(folder, files, out_path):
    images = []
    for name in files:
        im = load_preview_image(os.path.join(folder, name))
        if im:
            images.append(im)
        if len(images) == PREVIEW_MAX:
            break
    if not images:  # nothing visible to show, e.g. a pack that only blanks graphics out
        Image.new("RGB", (PREVIEW_WIDTH, PREVIEW_HEIGHT), PREVIEW_BG[:3]).save(out_path, optimize=True)
        return
    cols = min(len(images), PREVIEW_COLS)
    rows = (len(images) + cols - 1) // cols
    cell_w = PREVIEW_WIDTH // cols
    pad = max(8, cell_w // 16)
    room = cell_w - pad

    # One scale for the whole pack keeps its images in proportion to each other, sized
    # so the sheet fills the card's preview box.
    max_w = max(im.width for im in images)
    max_h = max(im.height for im in images)
    scale = min(room / max_w, (PREVIEW_HEIGHT / rows - pad) / max_h, PREVIEW_MAX_ZOOM)
    if scale >= 2:
        scale = int(scale)  # whole steps keep small pixel art crisp

    def fit(im):
        size = (max(1, round(im.width * scale)), max(1, round(im.height * scale)))
        if scale >= 2:
            return im.resize(size, Image.NEAREST)
        # Premultiplied so see-through pixels don't bleed dark fringes into the edges.
        return im.convert("RGBa").resize(size, Image.LANCZOS).convert("RGBA")

    cell_h = round(max_h * scale) + pad
    sheet = Image.new("RGBA", (cols * cell_w, rows * cell_h), PREVIEW_BG)
    for i, im in enumerate(images):
        im = fit(im)
        x = (i % cols) * cell_w + (cell_w - im.width) // 2
        y = (i // cols) * cell_h + (cell_h - im.height) // 2
        sheet.alpha_composite(im, (x, y))
    sheet.convert("RGB").save(out_path, optimize=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", help="folder containing one subfolder per pack")
    ap.add_argument("out", help="output folder to sync to the CDN")
    ap.add_argument("--config", default="packs.config.yml")
    ap.add_argument("--meta", default="packs.meta.yml")
    ap.add_argument("--previous", help="previous packs.json path or URL (default: <out>/packs.json)")
    args = ap.parse_args()

    config = load_yaml(args.config)
    meta = load_yaml(args.meta)
    cdn = config["cdn_base"].rstrip("/")
    prefixes = config["prefixes"]
    previous = load_previous(args.previous or os.path.join(args.out, "packs.json"))

    os.makedirs(os.path.join(args.out, "previews"), exist_ok=True)

    packs, skipped = [], []
    for folder_name in sorted(os.listdir(args.src)):
        folder = os.path.join(args.src, folder_name)
        if not os.path.isdir(folder):
            continue
        prefix, _, rest = folder_name.partition("_")
        rule = prefixes.get(prefix)
        if not rule or not rest:
            skipped.append(f"{folder_name} (unknown prefix '{prefix}')")
            continue

        files = sorted(
            f for f in os.listdir(folder)
            if os.path.splitext(f)[1].lower() in IMAGE_EXTS and os.path.isfile(os.path.join(folder, f))
        )
        if not files:
            skipped.append(f"{folder_name} (no images)")
            continue

        m = meta.get(folder_name, {}) or {}
        words = split_words(rest)
        pack_id = m.get("id") or "-".join([prefix.lower()] + [w.lower() for w in words])
        install_dir = rule.get("install_dir", "").strip("/")

        entries = []
        for name in files:
            with open(os.path.join(folder, name), "rb") as f:
                entries.append((f"{install_dir}/{name}" if install_dir else name, f.read()))
        license_text = read_license(folder)
        if license_text:
            licenses_dir = posixpath.join(posixpath.dirname(install_dir), "Licenses")
            entries.append((f"{licenses_dir}/{pack_id}.txt", license_text.encode("utf-8") + b"\n"))

        data = build_zip(entries)
        sha = hashlib.sha256(data).hexdigest()

        prev = previous.get(pack_id)
        if prev and prev["sha256"] == sha:
            version, released = prev["version"], prev.get("released")
        elif prev:
            version, released = bump_patch(prev["version"]), dt.date.today().isoformat()
        else:
            version, released = "1.0.0", dt.date.today().isoformat()

        zip_name = f"{pack_id}-{version}.zip"
        preview_name = f"previews/{pack_id}-{version}.png"
        with open(os.path.join(args.out, zip_name), "wb") as f:
            f.write(data)
        build_preview(folder, files, os.path.join(args.out, preview_name))

        pack = {
            "id": pack_id,
            "name": m.get("name") or " ".join(words),
            "version": version,
            "category": rule["category"],
            "author": m.get("author") or config.get("default_author"),
            "description": m.get("description"),
            "released": released,
            "url": f"{cdn}/{zip_name}",
            "sha256": sha,
            "size": len(data),
            "files": [arc for arc, _ in entries],
            "preview": f"{cdn}/{preview_name}",
            "tags": m.get("tags"),
            "changelog": m.get("changelog"),
            "license": license_text,
        }
        packs.append({k: v for k, v in pack.items() if v not in (None, "", [])})

        status = "unchanged" if prev and prev["sha256"] == sha else ("updated" if prev else "new")
        print(f"{status:9}  {pack_id:32} v{version:8} {len(files):4} files")

    manifest = {"schema_version": 1, "updated": dt.date.today().isoformat(), "packs": packs}
    with open(os.path.join(args.out, "packs.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    keep = {os.path.basename(p["url"]) for p in packs} | {os.path.basename(p["preview"]) for p in packs}
    for sub, ext in (("", ".zip"), ("previews", ".png")):
        folder = os.path.join(args.out, sub)
        for name in os.listdir(folder):
            if name.endswith(ext) and name not in keep:
                os.remove(os.path.join(folder, name))
                print(f"removed    {os.path.join(sub, name)}")

    for s in skipped:
        print(f"skipped    {s}", file=sys.stderr)
    print(f"\n{len(packs)} packs written to {args.out}")


if __name__ == "__main__":
    main()
