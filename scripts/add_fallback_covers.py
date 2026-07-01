#!/usr/bin/env python3
"""Give posts that have no embedded image a category-based fallback cover,
using free (Pixabay) photos fetched into static/images/covers/.
"""
import glob
import os

import yaml

POSTS_DIR = os.path.expanduser("~/git/masayukig.github.io/content/posts")
COVERS_DIR = os.path.expanduser("~/git/masayukig.github.io/static/images/covers")

available = {os.path.splitext(f)[0] for f in os.listdir(COVERS_DIR)}
ext_by_name = {os.path.splitext(f)[0]: os.path.splitext(f)[1] for f in os.listdir(COVERS_DIR)}

updated = 0
for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = __import__("re").match(r"^---\n(.*?\n)---\n", text, __import__("re").DOTALL)
    fm_text, body = m.group(1), text[m.end():]
    fm = yaml.safe_load(fm_text)

    if fm.get("cover"):
        continue  # already has a real image

    cats = [c.lower() for c in fm.get("categories", [])]
    match = next((c for c in cats if c in available), None) or "uncategorized"
    ext = ext_by_name[match]

    fm["cover"] = {"image": f"/images/covers/{match}{ext}", "alt": fm.get("title", "")}
    new_fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n" + new_fm_text + "---\n" + body)
    updated += 1

print(f"updated {updated} posts with fallback cover")
