#!/usr/bin/env python3
"""One-shot migration of Pelican content (rst + imported md) into Hugo posts.

Input dirs (already extracted from the `source` branch of masayukig.github.io):
  SRC_RST      content/*.rst              (hand-written posts, Pelican rst metadata)
  SRC_IMPORTED content/imported/*.md      (old blog import, Pelican md metadata)

Output: OUT_DIR/*.md  (Hugo posts with TOML-ish YAML front matter)

Not a general rst->md converter -- only handles the constructs actually
present in this specific 25-file corpus (checked by hand beforehand).
"""

import os
import re
import yaml
from datetime import datetime

SCRATCH = "/tmp/claude-1000/-home-migawa-git-masayukig-github-io/b2b8e519-df23-4636-8578-aa96fc92e13e/scratchpad"
SRC_RST = os.path.join(SCRATCH, "rst")
SRC_IMPORTED = os.path.join(SCRATCH, "imported")
OUT_DIR = os.path.expanduser("~/git/igawa-io/content/posts")
REVIEW_LOG = os.path.join(SCRATCH, "migration_review.txt")

os.makedirs(OUT_DIR, exist_ok=True)

review_notes = []
seen_slugs = set()


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[<>:\"/\\|?*#\[\]]", "", text)
    text = re.sub(r"[!'(),.、。「」『』？！：；…　]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "post"


def unique_slug(base):
    slug = base
    i = 2
    while slug in seen_slugs:
        slug = f"{base}-{i}"
        i += 1
    seen_slugs.add(slug)
    return slug


def dump_front_matter(meta):
    # Keep key order stable/readable.
    ordered = {}
    for k in ("title", "date", "lastmod", "slug", "categories", "tags", "draft"):
        if k in meta:
            ordered[k] = meta[k]
    return (
        "---\n"
        + yaml.safe_dump(ordered, allow_unicode=True, sort_keys=False)
        + "---\n\n"
    )


# ---------------------------------------------------------------------------
# imported/*.md  (Pelican "Field: value" metadata, body already Markdown)
# ---------------------------------------------------------------------------


def parse_imported(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    meta = {}
    i = 0
    while i < len(lines) and lines[i].strip() != "":
        m = re.match(r"^([A-Za-z]+):\s*(.*)$", lines[i])
        if not m:
            break
        meta[m.group(1).lower()] = m.group(2).strip()
        i += 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    body = "\n".join(lines[i:]).strip() + "\n"
    return meta, body


def migrate_imported():
    files = sorted(f for f in os.listdir(SRC_IMPORTED) if f.endswith(".md"))
    count = 0
    for fname in files:
        path = os.path.join(SRC_IMPORTED, fname)
        meta, body = parse_imported(path)

        title = meta.get("title", fname)
        date_raw = meta.get("date", "")
        try:
            dt = datetime.strptime(date_raw, "%Y-%m-%d %H:%M")
        except ValueError:
            review_notes.append(f"[imported] {fname}: unparseable date {date_raw!r}")
            dt = datetime(1970, 1, 1)
        date_str = dt.strftime("%Y-%m-%dT%H:%M:%S+09:00")

        base_slug = slugify(meta.get("slug") or title)
        slug = unique_slug(base_slug)

        fm = {
            "title": title,
            "date": date_str,
            "slug": slug,
            "draft": meta.get("status", "published").lower() != "published",
        }
        if meta.get("category"):
            fm["categories"] = [meta["category"]]
        if meta.get("tags"):
            fm["tags"] = [t.strip() for t in meta["tags"].split(",") if t.strip()]

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(dump_front_matter(fm))
            f.write(body)
        count += 1
    return count


# ---------------------------------------------------------------------------
# content/*.rst  (Pelican rst field-list metadata + reStructuredText body)
# ---------------------------------------------------------------------------

UNDERLINE_RE = re.compile(r"^([=\-+])\1{2,}$")


def rst_to_md(lines, fname):
    # Pass 1: collect hyperlink targets  .. _label: url
    targets = {}
    kept = []
    for line in lines:
        m = re.match(r"^\.\. _(.+?):\s+(\S+)\s*$", line)
        if m:
            targets[m.group(1).strip().lower()] = m.group(2).strip()
        else:
            kept.append(line)
    lines = kept

    out = []
    i = 0
    n = len(lines)
    underline_levels = {}  # char -> markdown level

    def level_for(ch):
        if ch not in underline_levels:
            underline_levels[ch] = "#" * (2 + len(underline_levels))
        return underline_levels[ch]

    while i < n:
        line = lines[i]

        # Section header: text line followed by underline of repeated char.
        if (
            i + 1 < n
            and line.strip()
            and UNDERLINE_RE.match(lines[i + 1].strip())
            and len(lines[i + 1].strip()) >= len(line.strip())
        ):
            ch = lines[i + 1].strip()[0]
            out.append(f"{level_for(ch)} {line.strip()}")
            i += 2
            continue

        # .. raw:: html  -> passthrough indented block (goldmark unsafe=true)
        if re.match(r"^\.\. raw:: html\s*$", line.strip()):
            i += 1
            block = []
            while i < n and (lines[i].strip() == "" or lines[i].startswith(" ")):
                block.append(lines[i][1:] if lines[i].startswith(" ") else lines[i])
                i += 1
            out.append("\n".join(block).strip())
            out.append("")
            continue

        # .. note:: -> blockquote
        if re.match(r"^\.\. note::\s*$", line.strip()):
            i += 1
            block = []
            while i < n and (
                lines[i].strip() == ""
                or lines[i].startswith(" ")
                or lines[i].startswith("\t")
            ):
                if lines[i].strip() == "":
                    if block and block[-1] == "":
                        i += 1
                        continue
                    block.append("")
                else:
                    block.append(lines[i].lstrip())
                i += 1
            while block and block[-1] == "":
                block.pop()
            out.extend(f"> {b}" if b else ">" for b in block)
            out.append("")
            continue

        # .. image:: url  (optionally followed by indented :option: lines, e.g. :alt:)
        m = re.match(r"^\.\. image:: (\S+)\s*$", line.strip())
        if m:
            url = m.group(1).replace("{static}/images/", "/images/")
            i += 1
            alt = ""
            while i < n and (
                lines[i].strip() == "" or re.match(r"^\s+:\w+:", lines[i])
            ):
                opt = re.match(r"^\s+:alt:\s*(.*)$", lines[i])
                if opt:
                    alt = opt.group(1).strip()
                i += 1
            out.append(f"![{alt}]({url})")
            out.append("")
            continue

        # unhandled rst comment/directive -> drop, flag for manual review
        if line.strip().startswith(".. "):
            review_notes.append(
                f"[rst] {fname}: dropped directive/comment: {line.strip()!r}"
            )
            i += 1
            continue

        # literal block: paragraph ending in `::` then blank then indented block
        stripped = line.rstrip()
        if stripped.endswith("::") and i + 1 < n and lines[i + 1].strip() == "":
            lead_text = stripped[:-2].rstrip()
            j = i + 2
            block = []
            while j < n and (lines[j].startswith("  ") or lines[j].strip() == ""):
                if lines[j].strip() == "":
                    block.append("")
                else:
                    block.append(lines[j])
                j += 1
            while block and block[-1] == "":
                block.pop()
            indent = min(
                (len(b) - len(b.lstrip()) for b in block if b.strip()), default=0
            )
            block = [b[indent:] if b.strip() else b for b in block]
            if lead_text:
                out.append(
                    lead_text + ":" if not lead_text.endswith(":") else lead_text
                )
                out.append("")
            out.append("```")
            out.extend(block)
            out.append("```")
            i = j
            continue

        out.append(line)
        i += 1

    md = "\n".join(out)

    # Inline explicit hyperlinks: `text <url>`_
    md = re.sub(r"`([^`<]+?)\s*<(\S+?)>`_", r"[\1](\2)", md)

    # Named references: `text`_  (resolve via targets collected above)
    def resolve_named(m):
        text = m.group(1)
        url = targets.get(text.strip().lower())
        if url is None:
            review_notes.append(f"[rst] {fname}: unresolved reference `{text}`_")
            return f"[{text}](#TODO-unresolved-link)"
        return f"[{text}]({url})"

    md = re.sub(r"`([^`]+?)`_", resolve_named, md)

    return md.strip() + "\n"


def parse_rst(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    title = lines[0].strip()
    meta = {}
    i = 2  # skip title + underline
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines):
        m = re.match(r"^:(\w[\w -]*):\s*(.*)$", lines[i])
        if not m:
            break
        meta[m.group(1).lower()] = m.group(2).strip()
        i += 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    body_lines = lines[i:]
    return title, meta, body_lines


def migrate_rst():
    # disclaimer.rst / presentations.rst come from content/pages/ (static
    # pages, no Pelican field-list metadata) -- handled separately, not posts.
    PAGE_FILES = {"disclaimer.rst", "presentations.rst"}
    files = sorted(
        f for f in os.listdir(SRC_RST) if f.endswith(".rst") and f not in PAGE_FILES
    )
    count = 0
    for fname in files:
        path = os.path.join(SRC_RST, fname)
        title, meta, body_lines = parse_rst(path)

        date_raw = meta.get("date", "")
        try:
            dt = datetime.strptime(date_raw, "%Y-%m-%d")
        except ValueError:
            review_notes.append(f"[rst] {fname}: unparseable date {date_raw!r}")
            dt = datetime(1970, 1, 1)
        date_str = dt.strftime("%Y-%m-%dT00:00:00+09:00")

        base_slug = slugify(meta.get("slug") or title)
        slug = unique_slug(base_slug)

        fm = {
            "title": title,
            "date": date_str,
            "slug": slug,
            "draft": meta.get("status", "published").lower() != "published",
        }
        if meta.get("category"):
            fm["categories"] = [meta["category"]]
        if meta.get("tags"):
            fm["tags"] = [t.strip() for t in meta["tags"].split(",") if t.strip()]
        if meta.get("modified"):
            try:
                mdt = datetime.strptime(meta["modified"], "%Y-%m-%d %H:%M")
                fm["lastmod"] = mdt.strftime("%Y-%m-%dT%H:%M:%S+09:00")
            except ValueError:
                pass

        body_md = rst_to_md(body_lines, fname)

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(dump_front_matter(fm))
            f.write(body_md)
        count += 1
    return count


if __name__ == "__main__":
    n_imported = migrate_imported()
    n_rst = migrate_rst()
    with open(REVIEW_LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(review_notes) + "\n")
    print(f"imported: {n_imported}, rst: {n_rst}, total: {n_imported + n_rst}")
    print(f"review notes: {len(review_notes)} -> {REVIEW_LOG}")
