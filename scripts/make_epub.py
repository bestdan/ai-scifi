#!/usr/bin/env python3
"""Build an EPUB 3 file from a story's final.md, using only the standard library.

Usage: python3 scripts/make_epub.py stories/<slug>/final.md [out.epub]

It understands the small subset of Markdown the stories use: a `# Title`,
`## Section` headings, `*italic*`, paragraphs separated by blank lines, and a
`<p align="center">…</p>` line used as a scene-break mark.
"""

import html
import re
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

CSS = """\
body { font-family: serif; line-height: 1.5; margin: 0 1em; }
h1 { text-align: center; margin: 2em 0 1.5em; font-weight: normal; }
h2 { text-align: center; font-size: 1em; font-weight: normal;
     font-variant: small-caps; letter-spacing: 0.1em; margin: 2em 0 1em; }
p { margin: 0; text-indent: 1.5em; }
h1 + p, h2 + p, p.break + p { text-indent: 0; }
p.break { text-align: center; text-indent: 0; margin: 1em 0; }
"""


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)


def to_xhtml_body(md: str) -> tuple[str, str]:
    title = "Untitled"
    parts = []
    for block in re.split(r"\n\s*\n", md.strip()):
        block = " ".join(line.strip() for line in block.splitlines())
        if block.startswith("# "):
            title = block[2:].strip()
            parts.append(f"<h1>{inline(title)}</h1>")
        elif block.startswith("## "):
            parts.append(f"<h2>{inline(block[3:].strip())}</h2>")
        elif m := re.fullmatch(r'<p align="center">(.*)</p>', block):
            parts.append(f'<p class="break">{html.escape(m.group(1))}</p>')
        else:
            parts.append(f"<p>{inline(block)}</p>")
    return title, "\n".join(parts)


def build(src: Path, out: Path, author: str) -> None:
    title, body = to_xhtml_body(src.read_text(encoding="utf-8"))
    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, str(src.resolve()))}"
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    t, a = html.escape(title), html.escape(author)

    story = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-GB" lang="en-GB">
<head><title>{t}</title><link rel="stylesheet" href="style.css"/></head>
<body>
{body}
</body>
</html>
"""
    nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>{t}</title></head>
<body><nav epub:type="toc"><ol><li><a href="story.xhtml">{t}</a></li></ol></nav></body>
</html>
"""
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="id">{book_id}</dc:identifier>
    <dc:title>{t}</dc:title>
    <dc:creator>{a}</dc:creator>
    <dc:language>en-GB</dc:language>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="css" href="style.css" media-type="text/css"/>
    <item id="story" href="story.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine><itemref idref="story"/></spine>
</package>
"""
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""
    with zipfile.ZipFile(out, "w") as z:
        # The mimetype entry must come first and be stored uncompressed.
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        for name, data in [("content.opf", opf), ("nav.xhtml", nav),
                           ("style.css", CSS), ("story.xhtml", story)]:
            z.writestr(f"OEBPS/{name}", data, compress_type=zipfile.ZIP_DEFLATED)


def main() -> None:
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix(".epub")
    build(src, out, author="ai-scifi")
    print(out)


if __name__ == "__main__":
    main()
