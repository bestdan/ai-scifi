# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.1"]
# ///
"""Render a typographic book cover (title and author only) as a JPEG.

Usage: uv run scripts/make_cover.py "<title>" "<author>" out.jpg

The cover carries nothing from the story but its title, so it can't give the
premise away. The background colour is picked from the title, so a story keeps
its cover across rebuilds and different stories look different on the shelf.
The size is Kindle's recommended 1600x2560.
"""

import hashlib
import shutil
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
MARGIN = 190

# (background, text, accent): muted jacket colours with enough contrast for a
# greyscale e-ink thumbnail.
PALETTES = [
    ("#1f3a4d", "#f3ead8", "#c9a96e"),  # deep teal
    ("#4a1f2a", "#f5e9e0", "#d6a46b"),  # oxblood
    ("#22382b", "#efe8d4", "#b9a46a"),  # forest
    ("#2b2540", "#efe9f2", "#c5a3c9"),  # indigo
    ("#5a3a1e", "#f6ecd9", "#e0b872"),  # umber
    ("#1d2b2f", "#e9efe9", "#8fb8a8"),  # slate
    ("#efe6d2", "#2a2420", "#9b3b2a"),  # paper with rust
    ("#3c4a55", "#f1ede4", "#e3b25a"),  # storm
]

# Tried in order before falling back to fontconfig, then to Pillow's own font.
TITLE_FONTS = [
    "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Baskerville.ttc",
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]
AUTHOR_FONTS = [
    "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf",
    "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
]


def palette(title: str) -> tuple[str, str, str]:
    digest = hashlib.sha256(title.encode("utf-8")).digest()
    return PALETTES[digest[0] % len(PALETTES)]


def font_path(candidates: list[str], pattern: str) -> str | None:
    for path in candidates:
        try:
            ImageFont.truetype(path, 10)
            return path
        except OSError:
            continue
    if shutil.which("fc-match"):
        out = subprocess.run(["fc-match", "-f", "%{file}", pattern],
                             capture_output=True, text=True).stdout.strip()
        if out:
            return out
    return None


def load(path: str | None, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size) if path else ImageFont.load_default(size)


def wrap(draw: ImageDraw.ImageDraw, text: str, font, width: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if line and draw.textlength(trial, font=font) > width:
            lines.append(line)
            line = word
        else:
            line = trial
    return lines + [line] if line else lines


def fit_title(draw, title, path, width, max_height):
    """Largest size at which the title fits in at most four lines."""
    for size in range(260, 60, -10):
        font = load(path, size)
        lines = wrap(draw, title, font, width)
        too_wide = any(draw.textlength(ln, font=font) > width for ln in lines)
        if len(lines) <= 4 and not too_wide and len(lines) * size * 1.2 <= max_height:
            return font, lines, size
    font = load(path, 60)
    return font, wrap(draw, title, font, width), 60


def render(title: str, author: str) -> Image.Image:
    bg, fg, accent = palette(title)
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    inner = W - 2 * MARGIN

    # A thin inset frame, like a cloth binding's blind stamp.
    draw.rectangle([90, 90, W - 90, H - 90], outline=accent, width=6)

    title_font, lines, size = fit_title(
        draw, title.upper(), font_path(TITLE_FONTS, "serif:bold"), inner, 1100)
    leading = int(size * 1.2)
    block = leading * len(lines)
    y = int(H * 0.40) - block // 2
    draw.line([W // 2 - 140, y - 120, W // 2 + 140, y - 120], fill=accent, width=6)
    for ln in lines:
        draw.text((W // 2, y), ln, font=title_font, fill=fg, anchor="ma")
        y += leading
    draw.line([W // 2 - 140, y + 80, W // 2 + 140, y + 80], fill=accent, width=6)

    author_font = load(font_path(AUTHOR_FONTS, "serif:italic"), 90)
    draw.text((W // 2, H - 330), author, font=author_font, fill=fg, anchor="ms")
    return img


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    title, author, out = sys.argv[1:]
    render(title, author).save(out, "JPEG", quality=90)
    print(out)


if __name__ == "__main__":
    main()
