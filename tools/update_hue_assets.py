#!/usr/bin/env python3
"""
Refresh the hue preview images in docs/assets/hues from the current hues.mul.

Every hue ID 1-3000 has two images on the Hues page:

    <id>.png        hued robe item (46x47)
    robe-<id>.png   paperdoll wearing the hued robe and mask (97x210)

Rather than re-rendering art and gumps, this re-hues the existing images.
Pixels that look the same in every hue's image (skin, hair, transparency)
are never hued and are copied as they are. Every other pixel is mapped back
to its hue index (0-31) using a reference hue whose 32 colours are all
distinct, then painted with the target hue's colour at that index. Colours
are converted from RGB555 with round(c * 255 / 31), which is how the
original images were made.

Only images that differ from what the current hues.mul gives are rewritten,
so running it again after a hues.mul update touches just the changed hues.

Usage:
    python tools/update_hue_assets.py --dry-run
    python tools/update_hue_assets.py --hues "C:/Programming/New Dawn/Data/hues.mul"
"""

import argparse
import struct
import sys
from pathlib import Path

from PIL import Image

HUE_COUNT = 3000
BLOCK_HEADER = 4
ENTRY_SIZE = 88  # 32 colours + table start + table end (u16 each) + 20-byte name
ENTRIES_PER_BLOCK = 8

# Hue 1072 ("Moocowmoo") has 32 distinct colours and is unchanged since the
# original client files, so its images give a clean gray-index map.
REFERENCE_HUE = 1072
# Hues compared to find the pixels that are never hued.
MASK_SAMPLE = range(1, HUE_COUNT + 1, 50)

KINDS = ("{}.png", "robe-{}.png")

DEFAULT_HUES = Path("C:/Programming/New Dawn/Data/hues.mul")
DEFAULT_ASSETS = Path(__file__).resolve().parent.parent / "docs" / "assets" / "hues"


def load_hues(path):
    data = path.read_bytes()
    hues = []
    off = 0
    while off + BLOCK_HEADER + ENTRY_SIZE * ENTRIES_PER_BLOCK <= len(data):
        off += BLOCK_HEADER
        for _ in range(ENTRIES_PER_BLOCK):
            colours = struct.unpack_from("<32H", data, off)
            name = data[off + 68:off + 88].split(b"\0")[0].decode("latin1")
            hues.append((colours, name))
            off += ENTRY_SIZE
    if len(hues) < HUE_COUNT:
        sys.exit(f"{path} has {len(hues)} hues, expected at least {HUE_COUNT}")
    return hues


def to_rgb(c):
    return tuple(round(((c >> shift) & 31) * 255 / 31) for shift in (10, 5, 0))


def read_pixels(path):
    with Image.open(path) as im:
        im = im.convert("RGBA")
        return im.size, list(im.getdata())


class Template:
    """Unhued mask plus gray-index map for one image kind."""

    def __init__(self, assets, kind, hues):
        self.kind = kind
        self.size, ref = read_pixels(assets / kind.format(REFERENCE_HUE))
        samples = [read_pixels(assets / kind.format(h))[1] for h in MASK_SAMPLE]

        inverse = {to_rgb(c): i for i, c in enumerate(hues[REFERENCE_HUE - 1][0])}
        if len(inverse) != 32:
            sys.exit(f"Reference hue {REFERENCE_HUE} no longer has 32 distinct colours")

        self.base = ref
        self.index = []
        for i, px in enumerate(ref):
            constant = all(s[i] == px for s in samples)
            if constant or px[3] == 0:
                self.index.append(None)
                continue
            idx = inverse.get(px[:3])
            if idx is None:
                sys.exit(f"{kind.format(REFERENCE_HUE)}: pixel {i} {px} is not a colour of hue {REFERENCE_HUE}")
            self.index.append(idx)

        if self.render(hues[REFERENCE_HUE - 1][0]) != ref:
            sys.exit(f"{kind.format(REFERENCE_HUE)} does not round-trip; template is wrong")

    def render(self, colours):
        rgb = [to_rgb(c) for c in colours]
        return [
            px if idx is None else rgb[idx] + (px[3],)
            for px, idx in zip(self.base, self.index)
        ]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hues", type=Path, default=DEFAULT_HUES, help="path to hues.mul")
    ap.add_argument("--assets", type=Path, default=DEFAULT_ASSETS, help="folder holding the hue PNGs")
    ap.add_argument("--dry-run", action="store_true", help="list what would change without writing")
    args = ap.parse_args()

    hues = load_hues(args.hues)
    templates = [Template(args.assets, kind, hues) for kind in KINDS]

    changed_ids = []
    files = 0
    for hue_id in range(1, HUE_COUNT + 1):
        colours, name = hues[hue_id - 1]
        hit = False
        for t in templates:
            path = args.assets / t.kind.format(hue_id)
            pixels = t.render(colours)
            if path.exists() and read_pixels(path)[1] == pixels:
                continue
            hit = True
            files += 1
            if not args.dry_run:
                im = Image.new("RGBA", t.size)
                im.putdata(pixels)
                im.save(path, optimize=True)
        if hit:
            changed_ids.append(hue_id)
            print(f"{hue_id:>5}  {name}")

    verb = "would update" if args.dry_run else "updated"
    print(f"\n{len(changed_ids)} hues, {files} files {verb}.")


if __name__ == "__main__":
    main()
