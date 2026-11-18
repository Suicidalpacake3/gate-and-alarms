"""Build the Gate & Alarms site.

Page bodies live in _source/pages. Shared header, footer and contact details
live in _source/partials.py. Run from anywhere:

    python _source/build.py

and the finished .html files are written to the site root.
"""
import re
from pathlib import Path

import partials as P

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent

TOKENS = {
    "{{PHONE}}": P.PHONE_DISPLAY,
    "{{PHONE_TEL}}": P.PHONE_TEL,
    "{{WHATSAPP}}": P.WHATSAPP,
    "{{EMAIL}}": P.EMAIL,
}
for k, v in P.ICON.items():
    TOKENS["{{ICON_%s}}" % k] = v


def build_page(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"<!-- title: (.*?) -->", text).group(1)
    desc = re.search(r"<!-- description: (.*?) -->", text).group(1)
    body = re.sub(r"<!-- (title|description): .*? -->\n", "", text)
    for k, v in TOKENS.items():
        body = body.replace(k, v)
    page = path.name
    html = P.head(title, desc, page) + P.header(page) + body + P.footer()
    left = re.findall(r"\{\{[A-Z_a-z]+\}\}", html)
    if left:
        raise SystemExit(f"{page}: unknown tokens {left}")
    if re.search("[–—]", html):
        raise SystemExit(f"{page}: contains an en or em dash")
    (ROOT / page).write_text(html, encoding="utf-8")
    print("built", page)


if __name__ == "__main__":
    for p in sorted((SRC / "pages").glob("*.html")):
        build_page(p)
