"""
mkdocs-macros module for the Custom Packs page.

Reads the manifest written by tools/build_packs.py (extra.packs_manifest in
mkdocs.yml, a local path or an https URL) and renders it as a card grid
styled by docs/stylesheets/packs.css.
"""

import datetime as dt
import html
import json
import logging
import os
import posixpath
import re
import urllib.parse
import urllib.request
from collections import defaultdict

log = logging.getLogger("mkdocs.plugins.macros.packs")

CATEGORY_TITLES = {
    "art": "Art",
    "gumps": "Gumps",
    "sounds": "Sounds",
    "maps": "Maps",
    "other": "Other",
}


def _load_manifest(source, root):
    if not source:
        return None
    try:
        if source.startswith(("http://", "https://")):
            with urllib.request.urlopen(source, timeout=10) as resp:
                return json.load(resp)
        path = source if os.path.isabs(source) else os.path.join(root, source)
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as e:
        log.warning("Custom packs manifest unavailable (%s): %s", source, e)
        return None


def _size(n):
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{n / 1024:.0f} KB"
    return f"{n / (1024 * 1024):.1f} MB"


def _date(value):
    try:
        d = dt.date.fromisoformat(value)
        return f"{d:%B} {d.day}, {d.year}"
    except (TypeError, ValueError):
        return value or "unknown"


URL_RE = re.compile(r"https?://[^\s<>\"']+[^\s<>\"'.,;:!?)]")


def _linkify(text):
    """Escape plain text and turn bare URLs into links."""
    out, pos = [], 0
    for m in URL_RE.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        url = m.group(0)
        label = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
        out.append(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(label)}</a>')
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)


def _card(p, link):
    e = html.escape
    meta = [f"v{p['version']}", _size(p["size"])]
    if p.get("author"):
        meta.append(p["author"])

    parts = ['<div class="nd-pack">']
    if p.get("preview"):
        parts.append(f'<img class="nd-pack__preview" src="{e(link(p["preview"]))}" alt="{e(p["name"])} preview" loading="lazy">')
    parts.append('<div class="nd-pack__body">')
    parts.append(f'<p class="nd-pack__title">{e(p["name"])}</p>')
    parts.append(f'<p class="nd-pack__meta">{" · ".join(e(m) for m in meta)}</p>')
    if p.get("description"):
        parts.append(f'<p class="nd-pack__desc">{e(p["description"])}</p>')
    if p.get("license"):
        parts.append(f'<p class="nd-pack__credit">Credit: {_linkify(p["license"].strip())}</p>')

    files = "<br>".join(f"<code>{e(f)}</code>" for f in p["files"])
    parts.append(
        '<details class="nd-pack__details">'
        f'<summary>Files and checksum ({len(p["files"])} files)</summary>'
        f'<div class="nd-pack__files">{files}</div>'
        f'<p class="nd-pack__hash">SHA-256: <code>{e(p["sha256"])}</code></p>'
        "</details>"
    )
    parts.append(
        '<div class="nd-pack__actions">'
        f'<a class="md-button md-button--primary" href="{e(link(p["url"]))}">Download ({_size(p["size"])})</a>'
        "</div>"
    )
    parts.append("</div></div>")
    return "".join(parts)


def define_env(env):
    root = os.path.dirname(env.conf["config_file_path"])
    extra = env.conf.get("extra", {})
    manifest = _load_manifest(extra.get("packs_manifest"), root)

    @env.macro
    def packs_updated():
        return _date(manifest.get("updated")) if manifest else "unknown"

    @env.macro
    def pack_catalog():
        if not manifest or not manifest.get("packs"):
            return '!!! note "Catalog unavailable"\n    The pack catalog could not be loaded. Check back soon.'

        packs = manifest["packs"]
        docs_dir = env.conf["docs_dir"]

        def link(url):
            # Files that ship in docs/ link relative to the page, so they also work under
            # mkdocs serve (which swaps site_url for the dev address) and before a deploy.
            path = urllib.parse.urlsplit(url).path.lstrip("/")
            if path and os.path.isfile(os.path.join(docs_dir, path)):
                return posixpath.relpath(path, env.page.url or ".")
            return url

        by_category = defaultdict(list)
        for p in packs:
            by_category[p["category"]].append(p)

        out = []
        for cat in sorted(by_category, key=lambda c: list(CATEGORY_TITLES).index(c) if c in CATEGORY_TITLES else 99):
            cards = "\n".join(_card(p, link) for p in sorted(by_category[cat], key=lambda p: p["name"].lower()))
            out.append(f"## {CATEGORY_TITLES.get(cat, cat.title())}\n\n<div class=\"nd-pack-grid\">\n{cards}\n</div>\n")
        return "\n".join(out)
