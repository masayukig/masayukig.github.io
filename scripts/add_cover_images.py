#!/usr/bin/env python3
"""Set front matter `cover.image` to the first image found in each post's
body, so PaperMod shows a thumbnail on the home page list and post header.
Posts with no embedded image are left untouched (no cover shown).
"""

import glob
import os
import re

import yaml

POSTS_DIR = os.path.expanduser("~/git/masayukig.github.io/content/posts")

IMG_RE = re.compile(r"!\[([^\]]*)\]\((https?://\S+?|/images/\S+?)\)")

updated = 0
for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    fm_text, body = m.group(1), text[m.end() :]
    fm = yaml.safe_load(fm_text)

    img = IMG_RE.search(body)
    if not img:
        continue

    alt, url = img.group(1).strip(), img.group(2).strip()
    fm["cover"] = {"image": url, "alt": alt or fm.get("title", "")}

    new_fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n" + new_fm_text + "---\n" + body)
    updated += 1

print(f"updated {updated} posts with cover.image")
