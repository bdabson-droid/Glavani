#!/usr/bin/env python3
"""Generate a single migration banner that scales for mobile and desktop CMS use."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images" / "migration-banners"
LOGO = ROOT / "images" / "glavani-park-logo.png"

BLACK = (18, 18, 18, 255)
ORANGE = (232, 112, 34, 255)
LIME = (168, 212, 74, 255)
WHITE = (255, 255, 255, 255)
MUTED = (200, 200, 200, 255)

# Taller card so one asset stays readable when scaled to phone width.
WIDTH, HEIGHT = 800, 360


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    if bold:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
        ]
    else:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_banner(lang: str) -> Image.Image:
    if lang == "hr":
        headline = "Glavani Park ima novu web stranicu"
        sub = "Rezervirajte, pogledajte cijene i planirajte posjet online"
        gift = "Za kupnju poklon bona ostanite na ovoj stranici"
        cta = "Posjetite →"
    else:
        headline = "Glavani Park has a new website"
        sub = "Book, see prices and plan your visit online"
        gift = "To buy a gift certificate, stay on this website"
        cta = "Visit now →"

    url = "www.glavani-park.com"
    img = Image.new("RGBA", (WIDTH, HEIGHT), BLACK)
    draw = ImageDraw.Draw(img)

    pad = 8
    draw.rounded_rectangle(
        (pad, pad, WIDTH - pad - 1, HEIGHT - pad - 1),
        radius=18,
        outline=ORANGE,
        width=3,
    )

    # Top row: logo + CTA
    logo = Image.open(LOGO).convert("RGBA")
    logo_h = 100
    logo_w = int(logo.width * (logo_h / logo.height))
    logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    logo_x, logo_y = 32, 30
    img.alpha_composite(logo, (logo_x, logo_y))

    btn_font = font(24, bold=True)
    btn_pad_x, btn_pad_y = 24, 14
    bb = draw.textbbox((0, 0), cta, font=btn_font)
    btn_w = (bb[2] - bb[0]) + btn_pad_x * 2
    btn_h = (bb[3] - bb[1]) + btn_pad_y * 2
    btn_x = WIDTH - 32 - btn_w
    btn_y = logo_y + (logo_h - btn_h) // 2
    draw.rounded_rectangle(
        (btn_x, btn_y, btn_x + btn_w, btn_y + btn_h),
        radius=12,
        fill=ORANGE,
    )
    draw.text(
        (btn_x + btn_pad_x, btn_y + btn_pad_y - 1),
        cta,
        font=btn_font,
        fill=WHITE,
    )

    # Copy block — vertically centered in remaining space
    text_left = 32
    max_text_w = WIDTH - 64

    headline_font = font(32, bold=True)
    sub_font = font(21, bold=False)
    url_font = font(24, bold=True)
    gift_font = font(18, bold=False)

    lines = [
        (headline, headline_font, WHITE, 12),
        (sub, sub_font, LIME, 10),
        (url, url_font, ORANGE, 14),
        (gift, gift_font, MUTED, 0),
    ]

    # Pre-wrap and measure for vertical centering in lower area
    prepared: list[tuple[list[str], ImageFont.FreeTypeFont, tuple, int]] = []
    total_h = 0
    for text, fnt, color, gap_after in lines:
        words = text.split()
        wrapped: list[str] = []
        current = ""
        for word in words:
            trial = f"{current} {word}".strip()
            tw = draw.textbbox((0, 0), trial, font=fnt)[2]
            if tw <= max_text_w or not current:
                current = trial
            else:
                wrapped.append(current)
                current = word
        if current:
            wrapped.append(current)
        def line_h(line: str) -> int:
            bb = draw.textbbox((0, 0), line, font=fnt)
            return bb[3] - bb[1]

        block_h = 0
        for i, line in enumerate(wrapped):
            block_h += line_h(line)
            if i < len(wrapped) - 1:
                block_h += 4
        block_h += gap_after
        prepared.append((wrapped, fnt, color, gap_after))
        total_h += block_h

    area_top = logo_y + logo_h + 8
    area_bottom = HEIGHT - 28
    y = area_top + max(0, (area_bottom - area_top - total_h) // 2)

    for wrapped, fnt, color, gap_after in prepared:
        for i, line in enumerate(wrapped):
            draw.text((text_left, y), line, font=fnt, fill=color)
            bb = draw.textbbox((0, 0), line, font=fnt)
            y += bb[3] - bb[1]
            y += 4 if i < len(wrapped) - 1 else gap_after

    return img.convert("RGB")


def save(img: Image.Image, stem: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    png_path = OUT / f"{stem}.png"
    webp_path = OUT / f"{stem}.webp"
    img.save(png_path, "PNG", optimize=True)
    img.save(webp_path, "WEBP", quality=88, method=6)
    print(f"Wrote {png_path.name} ({img.size[0]}×{img.size[1]}, {png_path.stat().st_size} bytes)")
    print(f"Wrote {webp_path.name} ({webp_path.stat().st_size} bytes)")


def main() -> None:
    for lang in ("en", "hr"):
        save(draw_banner(lang), f"glavani-park-migration-{lang}")


if __name__ == "__main__":
    main()
