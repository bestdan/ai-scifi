#!/usr/bin/env python3
"""Build an EPUB 3 file from a story's final.md, using only the standard library.

Usage: python3 scripts/make_epub.py stories/<slug>/final.md [out.epub]

It understands the small subset of Markdown the stories use: a `# Title`,
`## Section` headings, `*italic*`, paragraphs separated by blank lines, and a
`<p align="center">…</p>` line used as a scene-break mark.

The book gets a typographic cover (title and author only) rendered by
scripts/make_cover.py, which needs Pillow and so runs through `uv`. If that
fails, the EPUB is built without a cover and a warning is printed.
"""

import html
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

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


COVER_XHTML = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Cover</title>
<style>body { margin: 0; padding: 0; text-align: center; } svg { height: 100%; }</style></head>
<body epub:type="cover">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     version="1.1" width="100%" height="100%" viewBox="0 0 1600 2560"
     preserveAspectRatio="xMidYMid meet">
<image width="1600" height="2560" xlink:href="cover.jpg"/>
</svg>
</body>
</html>
"""


def read_title(md: str) -> str:
    return to_xhtml_body(md)[0]


def render_cover(title: str, author: str) -> bytes | None:
    """Run make_cover.py through uv and return the JPEG, or None on failure."""
    uv = shutil.which("uv")
    if not uv:
        print("make_epub: uv not found, building without a cover", file=sys.stderr)
        return None
    with tempfile.TemporaryDirectory() as tmp:
        jpg = Path(tmp) / "cover.jpg"
        result = subprocess.run(
            [uv, "run", "--quiet", "--script", str(HERE / "make_cover.py"),
             title, author, str(jpg)],
            capture_output=True, text=True)
        if result.returncode != 0 or not jpg.exists():
            print(f"make_epub: cover failed, building without one\n{result.stderr}",
                  file=sys.stderr)
            return None
        return jpg.read_bytes()


def build(src: Path, out: Path, author: str, cover: bytes | None = None) -> None:
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
    landmarks = ('<nav epub:type="landmarks"><ol>'
                 '<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
                 '<li><a epub:type="bodymatter" href="story.xhtml">Start</a></li>'
                 '</ol></nav>\n') if cover else ""
    # Kindle's converter still reads the EPUB 2 cover meta and guide entry, so
    # the cover is declared both ways.
    cover_meta = '\n    <meta name="cover" content="cover-image"/>' if cover else ""
    cover_items = ('\n    <item id="cover-image" href="cover.jpg" media-type="image/jpeg"'
                   ' properties="cover-image"/>'
                   '\n    <item id="cover" href="cover.xhtml"'
                   ' media-type="application/xhtml+xml" properties="svg"/>') if cover else ""
    cover_spine = '<itemref idref="cover"/>' if cover else ""
    guide = ('\n  <guide><reference type="cover" title="Cover" href="cover.xhtml"/>'
             '</guide>') if cover else ""
    nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>{t}</title></head>
<body><nav epub:type="toc"><ol><li><a href="story.xhtml">{t}</a></li></ol></nav>
{landmarks}</body>
</html>
"""
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="id">{book_id}</dc:identifier>
    <dc:title>{t}</dc:title>
    <dc:creator>{a}</dc:creator>
    <dc:language>en-GB</dc:language>
    <meta property="dcterms:modified">{modified}</meta>{cover_meta}
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="css" href="style.css" media-type="text/css"/>
    <item id="story" href="story.xhtml" media-type="application/xhtml+xml"/>{cover_items}
  </manifest>
  <spine>{cover_spine}<itemref idref="story"/></spine>{guide}
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
        if cover:
            z.writestr("OEBPS/cover.xhtml", COVER_XHTML, compress_type=zipfile.ZIP_DEFLATED)
            # JPEG is already compressed.
            z.writestr("OEBPS/cover.jpg", cover, compress_type=zipfile.ZIP_STORED)


def main() -> None:
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix(".epub")
    author = "ai-scifi"
    cover = render_cover(read_title(src.read_text(encoding="utf-8")), author)
    build(src, out, author=author, cover=cover)
    print(out)


if __name__ == "__main__":
    main()
