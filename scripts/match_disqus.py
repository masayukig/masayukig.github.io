#!/usr/bin/env python3
"""Match each new Hugo post to its old (pre-Hugo) Disqus identifier so
existing comment threads keep working after the URL scheme changes.

Old site: Pelican set `disqus_identifier = {date:%Y-%m-%d}-{slug}` where
`slug` is Pelican's own (often mangled) auto-slug -- not something we can
recompute. Instead we scrape the identifier straight out of the old
generated HTML (checked out from the `main` branch) and match it back to
the corresponding new post by (date, normalized title).
"""
import glob
import os
import re
import unicodedata

import yaml

SCRATCH = "/tmp/claude-1000/-home-migawa-git-masayukig-github-io/b2b8e519-df23-4636-8578-aa96fc92e13e/scratchpad"
OLD_HTML_DIR = os.path.join(SCRATCH, "old_html")
POSTS_DIR = os.path.expanduser("~/git/igawa-io/content/posts")


def norm(text):
    text = unicodedata.normalize("NFKC", text).strip().lower()
    return re.sub(r"[\s\W]+", "", text)


# --- 1. scrape old identifiers -------------------------------------------------
old_by_date = {}  # date_prefix -> list of (identifier, title)
for path in glob.glob(os.path.join(OLD_HTML_DIR, "*.html")):
    with open(path, encoding="utf-8", errors="replace") as f:
        html = f.read()
    m_id = re.search(r"this\.page\.identifier = '([^']+)';", html)
    m_title = re.search(r"<title>(.*?)\s*-\s*What's done is done</title>", html)
    if not m_id or not m_title:
        continue
    identifier = m_id.group(1)
    title = m_title.group(1)
    date_prefix = identifier[:10]
    old_by_date.setdefault(date_prefix, []).append((identifier, title))

print(f"scraped {sum(len(v) for v in old_by_date.values())} old identifiers")

# --- 2. match against new posts ------------------------------------------------
matched = 0
ambiguous = []
unmatched = []

for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    fm_text, body = m.group(1), text[m.end():]
    fm = yaml.safe_load(fm_text)
    if fm.get("draft"):
        continue

    date_prefix = fm["date"][:10]
    candidates = old_by_date.get(date_prefix, [])

    identifier = None
    if len(candidates) == 1:
        identifier = candidates[0][0]
    elif len(candidates) > 1:
        target = norm(fm["title"])
        exact = [c for c in candidates if norm(c[1]) == target]
        if len(exact) == 1:
            identifier = exact[0][0]
        else:
            ambiguous.append((os.path.basename(path), fm["title"], candidates))
    if identifier:
        fm["disqus_identifier"] = identifier
        new_fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        with open(path, "w", encoding="utf-8") as f:
            f.write("---\n" + new_fm_text + "---\n" + body)
        matched += 1
    else:
        unmatched.append(os.path.basename(path))

print(f"matched: {matched}")
print(f"ambiguous: {len(ambiguous)}")
print(f"unmatched: {len(unmatched)}")

with open(os.path.join(SCRATCH, "disqus_match_report.txt"), "w", encoding="utf-8") as f:
    f.write("=== ambiguous ===\n")
    for fname, title, cands in ambiguous:
        f.write(f"{fname}  title={title!r}\n")
        for ident, ctitle in cands:
            f.write(f"    candidate: {ident}  ({ctitle!r})\n")
    f.write("\n=== unmatched ===\n")
    for fname in unmatched:
        f.write(f"{fname}\n")
