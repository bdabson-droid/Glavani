#!/usr/bin/env python3
"""Build Glavani Park static SEO site: pages, images, sitemap, robots.txt."""

from __future__ import annotations

import json
import os
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from pages_en import HOME as HOME_EN, PAGES as PAGES_EN  # noqa: E402
from pages_hr import HOME as HOME_HR, PAGES as PAGES_HR, SLUG_MAP  # noqa: E402
from activities import ACTIVITIES, ACTIVITY_SLUG_MAP  # noqa: E402
from reviews import render_reviews_section  # noqa: E402
from faqs import FAQ_COPY, FAQ_SLUGS, SMALL_GROUP_FAQS, render_faq_list  # noqa: E402

BASE = "https://www.glavanipark.com"
TODAY = date.today().isoformat()

GLAVANI_LAT = 45.021389
GLAVANI_LNG = 13.951111
GLAVANI_ADDRESS = "Glavani 10, 52207 Barban, Istria, Croatia"
GLAVANI_MAPS_QUERY = "Glavani+Park,+Glavani+10,+52207+Barban,+Croatia"
GLAVANI_MAPS_DIRECTIONS = (
    f"https://www.google.com/maps/dir/?api=1&destination={GLAVANI_LAT}%2C{GLAVANI_LNG}"
)
GLAVANI_MAPS_LINK = f"https://www.google.com/maps?q={GLAVANI_LAT},{GLAVANI_LNG}"
LOCATION_MAP_HEAD = """
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="">
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin="" defer></script>"""

# Istria overview bounds (lat_min, lat_max, lng_min, lng_max)
ISTRIA_MAP_BOUNDS = (44.62, 45.52, 13.42, 14.28)

ISTRIA_OUTLINE = [
    (45.50, 13.52),
    (45.44, 13.58),
    (45.36, 13.55),
    (45.26, 13.60),
    (45.16, 13.62),
    (45.08, 13.64),
    (44.98, 13.68),
    (44.88, 13.74),
    (44.78, 13.84),
    (44.76, 13.92),
    (44.82, 14.02),
    (44.90, 14.12),
    (45.00, 14.20),
    (45.12, 14.24),
    (45.24, 14.22),
    (45.34, 14.14),
    (45.42, 14.02),
    (45.48, 13.86),
    (45.50, 13.70),
]

ISTRIA_MAP_LOCATIONS = [
    {"name": "Glavani Park", "lat": GLAVANI_LAT, "lng": GLAVANI_LNG, "primary": True, "label": (10, 10)},
    {"name": "Barban", "lat": 45.0475, "lng": 14.0147, "primary": False, "label": (10, -18)},
    {"name": "Vodnjan", "lat": 44.9597, "lng": 13.8492, "primary": False, "label": (-62, 2)},
    {"name": "Pula", "lat": 44.8666, "lng": 13.8496, "primary": False, "label": (10, 12)},
    {"name": "Rovinj", "lat": 45.0812, "lng": 13.6387, "primary": False, "label": (10, -18)},
]

# Reverse map EN slug -> HR slug
EN_TO_HR = {v: k for k, v in SLUG_MAP.items()}
EN_TO_HR.update({v: k for k, v in ACTIVITY_SLUG_MAP.items()})
EN_TO_HR["book"] = "rezervacija"
EN_TO_HR["faq"] = "cesta-pitanja"

HR_TO_EN = dict(SLUG_MAP)
HR_TO_EN.update(ACTIVITY_SLUG_MAP)
HR_TO_EN["rezervacija"] = "book"
HR_TO_EN["cesta-pitanja"] = "faq"

IMAGES = [
    ("glavani-park-adventure-istria-croatia.jpg", "Glavani Park", (26, 61, 46), (45, 106, 79)),
    ("12-5m-high-swing-glavani-park-istria.webp", "12.5m High Swing", (234, 88, 12), (180, 83, 9)),
    ("human-catapult-adrenaline-park-croatia.webp", "Human Catapult", (234, 88, 12), (120, 53, 15)),
    ("zipline-120m-glavani-park-istria-croatia.webp", "Zipline 120m", (74, 85, 104), (45, 55, 72)),
    ("climbing-wall-outdoor-activities-istria.webp", "Climbing Wall", (64, 145, 108), (26, 61, 46)),
    ("quick-jump-20m-free-fall-istria.webp", "Quick Jump 20m", (124, 58, 237), (76, 29, 149)),
    ("glavani-park-logo.png", "GLAVANI PARK", (26, 61, 46), (251, 191, 36)),
    ("partner-badge-glavani-park.webp", "Partner", (26, 61, 46), (251, 191, 36)),
]


def generate_images() -> None:
    img_dir = ROOT / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    for filename, label, c1, c2 in IMAGES:
        path = img_dir / filename
        w, h = (800, 560) if "logo" not in filename else (400, 120)
        img = Image.new("RGB", (w, h), c1)
        draw = ImageDraw.Draw(img)
        for y in range(h):
            t = y / h
            r = int(c1[0] + (c2[0] - c1[0]) * t)
            g = int(c1[1] + (c2[1] - c1[1]) * t)
            b = int(c1[2] + (c2[2] - c1[2]) * t)
            draw.line([(0, y), (w, y)], fill=(r, g, b))
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
            small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        except OSError:
            font = ImageFont.load_default()
            small = font
        draw.text((40, h // 2 - 30), label, fill=(255, 255, 255), font=font)
        draw.text((40, h // 2 + 20), "Glavani Park · Istria, Croatia", fill=(240, 253, 244), font=small)
        if filename.endswith(".webp"):
            img.save(path, "WEBP", quality=82, method=6)
        elif filename.endswith(".png"):
            img.save(path, "PNG", optimize=True)
        else:
            img.save(path, "JPEG", quality=85, optimize=True)
        print(f"  image: {path.name}")


def _map_latlng_to_xy(lat: float, lng: float, w: int, h: int, padding: int = 52) -> tuple[int, int]:
    lat_min, lat_max, lng_min, lng_max = ISTRIA_MAP_BOUNDS
    x = padding + (lng - lng_min) / (lng_max - lng_min) * (w - 2 * padding)
    y = padding + (lat_max - lat) / (lat_max - lat_min) * (h - 2 * padding)
    return int(x), int(y)


def _draw_map_pin(draw: ImageDraw.ImageDraw, x: int, y: int, *, primary: bool = False) -> None:
    if primary:
        draw.ellipse([x - 14, y - 34, x + 14, y - 6], fill=(220, 38, 38))
        draw.polygon([(x, y + 6), (x - 12, y - 8), (x + 12, y - 8)], fill=(180, 28, 28))
        draw.ellipse([x - 5, y - 26, x + 5, y - 16], fill=(255, 255, 255))
    else:
        draw.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(26, 61, 46))
        draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(251, 191, 36))


def _draw_label(
    draw: ImageDraw.ImageDraw,
    text: str,
    x: int,
    y: int,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    *,
    primary: bool = False,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 6, 4
    bg = (220, 38, 38) if primary else (255, 255, 255)
    fg = (255, 255, 255) if primary else (26, 61, 46)
    draw.rounded_rectangle(
        [x - pad_x, y - pad_y, x + tw + pad_x, y + th + pad_y],
        radius=6,
        fill=bg,
        outline=(26, 61, 46) if not primary else None,
    )
    draw.text((x, y), text, fill=fg, font=font)


def generate_location_map_image() -> None:
    """Create an Istria overview map with Glavani Park and nearby towns."""
    img_dir = ROOT / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    path = img_dir / LOCATION_MAP_IMAGE
    w, h = 800, 560
    img = Image.new("RGB", (w, h), (120, 178, 210))
    draw = ImageDraw.Draw(img)

    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except OSError:
        title_font = label_font = small_font = ImageFont.load_default()

    land = (186, 205, 156)
    land_edge = (120, 148, 98)
    outline_xy = [_map_latlng_to_xy(lat, lng, w, h) for lat, lng in ISTRIA_OUTLINE]
    draw.polygon(outline_xy, fill=land, outline=land_edge)

    for i in range(len(outline_xy) - 1):
        x1, y1 = outline_xy[i]
        x2, y2 = outline_xy[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=land_edge, width=2)

    draw.rounded_rectangle([18, 18, 250, 52], radius=8, fill=(255, 255, 255))
    draw.text((28, 24), "Istria, Croatia", fill=(26, 61, 46), font=title_font)

    park_xy = _map_latlng_to_xy(GLAVANI_LAT, GLAVANI_LNG, w, h)
    for town in ("Barban", "Vodnjan"):
        match = next(item for item in ISTRIA_MAP_LOCATIONS if item["name"] == town)
        tx, ty = _map_latlng_to_xy(match["lat"], match["lng"], w, h)
        draw.line([park_xy, (tx, ty)], fill=(234, 88, 12), width=2)

    for loc in ISTRIA_MAP_LOCATIONS:
        x, y = _map_latlng_to_xy(loc["lat"], loc["lng"], w, h)
        _draw_map_pin(draw, x, y, primary=loc["primary"])
        lx, ly = x + loc["label"][0], y + loc["label"][1]
        _draw_label(draw, loc["name"], lx, ly, label_font, primary=loc["primary"])

    draw.rounded_rectangle([18, h - 42, w - 18, h - 18], radius=8, fill=(255, 255, 255))
    draw.text(
        (28, h - 36),
        "Glavani Park · inland between Barban, Vodnjan, Pula & Rovinj · tap for directions",
        fill=(45, 55, 72),
        font=small_font,
    )

    img.save(path, "JPEG", quality=90, optimize=True)
    print(f"  image: {path.name}")


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def u(path: str) -> str:
    """Legacy helper — paths are relativized after build."""
    return path


def relativize_paths(html: str, depth: int, lang: str) -> str:
    """Convert root-absolute paths to relative so the site works on any host/path."""
    import re
    up = "../" * depth
    other = "hr" if lang == "en" else "en"

    html = re.sub(r'(href|src)="/assets/', rf'\1="{up}assets/', html)
    html = re.sub(r'(href|src)="/images/', rf'\1="{up}images/', html)
    html = html.replace('href="/manifest.webmanifest"', f'href="{up}manifest.webmanifest"')

    def other_lang_link(match: re.Match[str]) -> str:
        rest = match.group(1)
        return f'href="{up}{other}/"' if rest == "" else f'href="{up}{other}/{rest}"'

    html = re.sub(rf'href="/{other}/([^"]*)"', other_lang_link, html)

    def same_lang_link(match: re.Match[str]) -> str:
        rest = match.group(1)
        if rest.startswith("#"):
            return f'href="{rest}"' if depth == 1 else f'href="../{rest}"'
        if "#" in rest:
            slug, frag = rest.split("#", 1)
            frag = "#" + frag
        else:
            slug, frag = rest, ""
        slug = slug.strip("/")
        if depth == 1:
            path = f"{slug}/" if slug else "./"
        else:
            path = f"../{slug}/" if slug else "../"
        return f'href="{path}{frag}"'

    html = re.sub(rf'href="/{lang}/([^"]*)"', same_lang_link, html)
    return html


def relativize_site() -> None:
    """Rewrite internal links in all built HTML to be path-relative."""
    import re
    for html_file in ROOT.rglob("*.html"):
        if "scripts" in html_file.parts:
            continue
        rel = html_file.relative_to(ROOT)
        if rel == Path("index.html"):
            text = html_file.read_text(encoding="utf-8")
            text = text.replace('url=/en/', 'url=en/')
            text = text.replace("location.replace('/en/", "location.replace('en/")
            text = text.replace('href="/en/"', 'href="en/"')
            html_file.write_text(text, encoding="utf-8")
            continue
        if len(rel.parts) == 2 and rel.parts[1] == "index.html":
            depth, lang = 1, rel.parts[0]
        elif len(rel.parts) == 3 and rel.parts[2] == "index.html":
            depth, lang = 2, rel.parts[0]
        else:
            continue
        text = html_file.read_text(encoding="utf-8")
        html_file.write_text(relativize_paths(text, depth, lang), encoding="utf-8")

    print("  applied relative paths for GitHub Pages compatibility")


def quick_actions(lang: str) -> str:
    call = "Pozovite" if lang == "hr" else "Call Now"
    find = "Pronađite nas" if lang == "hr" else "Find Us"
    return f"""
  <nav class="quick-actions" aria-label="{'Brze radnje' if lang == 'hr' else 'Quick actions'}">
    <a class="btn-call" href="tel:+385918964525" aria-label="{'Pozovite Glavani Park' if lang == 'hr' else 'Call Glavani Park now'}">
      <span aria-hidden="true">📞</span> {call}
    </a>
    <a class="btn-find" href="https://www.google.com/maps?q=45.021389,13.951111" target="_blank" rel="noopener noreferrer">
      <span aria-hidden="true">📍</span> {find}
    </a>
  </nav>"""


def site_header(lang: str) -> str:
    tagline_en = "Adventure &amp; Adrenaline Park · Istria, Croatia · Near Pula, Barban &amp; Vodnjan"
    tagline_hr = "Avanturistički i adrenalinski park · Istria, Hrvatska · kod Pule, Barbana i Vodnjanja"
    home = f"/{lang}/"
    return f"""
  <header class="site-header">
    <p class="site-header__logo"><a href="{home}">Glavani Park</a></p>
    <p class="site-header__tagline">{tagline_hr if lang == 'hr' else tagline_en}</p>
  </header>"""


def site_nav(lang: str, is_home: bool = False) -> str:
    prefix = f"/{lang}/"
    other = "en" if lang == "hr" else "hr"
    other_label = "English" if lang == "hr" else "Hrvatski"
    if lang == "hr":
        links = [
            ("Aktivnosti", f"{prefix}#activities" if is_home else activities_hub_path(lang)),
            ("Grupe", f"{prefix}team-building-istri/"),
            ("Cijene", f"{prefix}rezervacija/"),
            ("Lokacija", f"{prefix}#location" if is_home else f"{prefix}sto-raditi-kod-pule/"),
            ("Pitanja", f"{prefix}{FAQ_SLUGS['hr']}/"),
            ("Sigurnost", f"{prefix}sigurnost/"),
        ]
    else:
        links = [
            ("Activities", f"{prefix}#activities" if is_home else activities_hub_path(lang)),
            ("Groups", f"{prefix}team-building-istria/"),
            ("Prices", f"{prefix}book/"),
            ("Location", f"{prefix}#location" if is_home else f"{prefix}things-to-do-near-pula/"),
            ("FAQ", f"{prefix}{FAQ_SLUGS['en']}/"),
            ("Safety", f"{prefix}safety/"),
        ]
    items = "".join(f'<a href="{href}">{label}</a>' for label, href in links)
    return f"""
  <nav class="site-nav" aria-label="{'Glavna navigacija' if lang == 'hr' else 'Main navigation'}">
    <div class="site-nav__inner">
      {items}
      <a href="/{other}/" hreflang="{other}">{other_label}</a>
    </div>
  </nav>"""


def footer(lang: str) -> str:
    prefix = f"/{lang}/"
    other = "hr" if lang == "en" else "en"
    if lang == "hr":
        copy = "Glavani Park · avanturistički park Istria · zipline Hrvatska"
        links = [
            ("Početna", prefix),
            ("English", f"/en/"),
            ("Partneri", f"{prefix}partneri/"),
            ("Link na nas", f"{prefix}link-na-nas/"),
            ("Sigurnost", f"{prefix}sigurnost/"),
        ]
    else:
        copy = "Glavani Park · Adventure Park Istria · Zipline Croatia"
        links = [
            ("Home", prefix),
            ("Hrvatski", f"/hr/"),
            ("Partners", f"{prefix}partners/"),
            ("Link to Us", f"{prefix}link-to-us/"),
            ("Safety", f"{prefix}safety/"),
        ]
    link_html = "".join(f"<li><a href=\"{h}\">{t}</a></li>" for t, h in links)
    return f"""
  <footer class="site-footer">
    <p>&copy; <time datetime="2026">2026</time> {copy}</p>
    <ul class="site-footer__links">
      <li><a href="{BASE}">www.glavanipark.com</a></li>
      {link_html}
    </ul>
  </footer>"""


def hreflang_tags(en_slug: str | None, hr_slug: str | None, is_home: bool = False) -> str:
    if is_home:
        en_url = f"{BASE}/en/"
        hr_url = f"{BASE}/hr/"
    else:
        en_url = f"{BASE}/en/{en_slug}/"
        hr_url = f"{BASE}/hr/{hr_slug}/"
    return f"""
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="hr" href="{hr_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">"""


def head_meta(
    lang: str,
    title: str,
    description: str,
    keywords: str,
    canonical: str,
    en_slug: str | None = None,
    hr_slug: str | None = None,
    is_home: bool = False,
    og_image: str = "glavani-park-adventure-istria-croatia.jpg",
    extra_head: str = "",
) -> str:
    og_locale = "hr_HR" if lang == "hr" else "en_GB"
    alt_locale = "en_GB" if lang == "hr" else "hr_HR"
    og_image_url = f"{BASE}/images/{og_image}"
    img_w, img_h = (400, 120) if "logo" in og_image else (800, 560)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
{hreflang_tags(en_slug, hr_slug, is_home)}
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:locale:alternate" content="{alt_locale}">
  <meta property="og:site_name" content="Glavani Park">
  <meta property="og:image" content="{og_image_url}">
  <meta property="og:image:width" content="{img_w}">
  <meta property="og:image:height" content="{img_h}">
  <meta property="og:image:alt" content="Glavani Park adventure and zipline park in Istria, Croatia">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image_url}">
  <link rel="stylesheet" href="/assets/css/site.css">
{extra_head}
</head>
<body class="theme-page">"""


def render_sections(sections: list) -> str:
    html = ['<div class="prose">']
    for sec in sections:
        if sec.get("h2"):
            html.append(f"<h2>{sec['h2']}</h2>")
        if sec.get("h3"):
            html.append(f"<h3>{sec['h3']}</h3>")
        for para in sec.get("paragraphs", []):
            if para.strip().startswith("<"):
                html.append(para)
            else:
                html.append(f"<p>{para}</p>")
    html.append("</div>")
    return "\n".join(html)


def render_related(related: list, lang: str) -> str:
    prefix = f"/{lang}/"
    cards = "".join(
        f'<a class="topic-link" href="{prefix}{r["slug"]}/">{r["title"]}<span>{r["desc"]}</span></a>'
        for r in related
    )
    heading = "Povezane stranice" if lang == "hr" else "Related Pages"
    return f"""
    <section class="section">
      <div class="section__heading"><h2>{heading}</h2></div>
      <div class="topic-grid">{cards}</div>
    </section>"""


def breadcrumb_schema(items: list) -> str:
    elements = []
    for i, (name, url) in enumerate(items, 1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if url:
            el["item"] = url
        elements.append(el)
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elements}
    return json_ld_script(data)


def json_ld_script(data: dict | list) -> str:
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


def faq_page_schema(faqs: list[dict]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq["q"],
                "acceptedAnswer": {"@type": "Answer", "text": faq["a"]},
            }
            for faq in faqs
        ],
    }


def sitemap_alternates(loc: str) -> tuple[str, str]:
    path = loc.replace(BASE, "")
    if path.startswith("/hr/"):
        hr_url = loc
        if path == "/hr/":
            en_url = f"{BASE}/en/"
        elif path == "/hr/rezervacija/":
            en_url = f"{BASE}/en/book/"
        else:
            hr_slug = path.replace("/hr/", "").strip("/")
            en_url = f"{BASE}/en/{HR_TO_EN.get(hr_slug, hr_slug)}/"
        return en_url, hr_url
    en_url = loc
    if path == "/en/":
        hr_url = f"{BASE}/hr/"
    elif path == "/en/book/":
        hr_url = f"{BASE}/hr/rezervacija/"
    else:
        en_slug = path.replace("/en/", "").strip("/")
        hr_url = f"{BASE}/hr/{EN_TO_HR.get(en_slug, en_slug)}/"
    return en_url, hr_url


def render_location_map(lang: str) -> str:
    if lang == "hr":
        heading = "Pronađite Glavani Park"
        lead = "Istra — Glavani Park u unutrašnjosti između Barbana, Vodnjanja, Pule i Rovinja"
        directions = "Upute za dolazak"
        open_maps = "Otvori u Google Maps"
        map_alt = "Interaktivna karta Istre s Glavani Parkom, Barbanom, Vodnjanom, Pulom i Rovinjem"
        map_hint = "Uhvatite ili scrollajte za zum · otvorite Google Maps za navigaciju"
        nearby = (
            "<ul class=\"location-map__towns\">"
            "<li><strong>Barban</strong> ~6 km</li>"
            "<li><strong>Vodnjan</strong> ~10 km</li>"
            "<li><strong>Pula</strong> ~30 min vožnje</li>"
            "<li><strong>Rovinj</strong> ~45 min vožnje</li>"
            "</ul>"
        )
    else:
        heading = "Find Glavani Park"
        lead = "Istria overview — Glavani Park inland between Barban, Vodnjan, Pula & Rovinj"
        directions = "Get directions"
        open_maps = "Open in Google Maps"
        map_alt = "Interactive map of Istria showing Glavani Park, Barban, Vodnjan, Pula, and Rovinj"
        map_hint = "Pinch or scroll to zoom · open Google Maps for turn-by-turn directions"
        nearby = (
            "<ul class=\"location-map__towns\">"
            "<li><strong>Barban</strong> ~6 km</li>"
            "<li><strong>Vodnjan</strong> ~10 km</li>"
            "<li><strong>Pula</strong> ~30 min drive</li>"
            "<li><strong>Rovinj</strong> ~45 min drive</li>"
            "</ul>"
        )
    return f"""
    <section class="section section--alt" id="location-map" aria-labelledby="location-map-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="location-map-heading">{heading}</h2>
          <p>{lead}</p>
        </div>
        <div class="location-map">
          <div class="location-map__embed">
            <div id="istria-map" class="istria-map" data-lang="{lang}" role="img" aria-label="{map_alt}"></div>
            <p class="location-map__hint">{map_hint}</p>
          </div>
          <div class="location-map__panel">
            <p class="location-map__pin" aria-hidden="true">📍</p>
            <address class="location-map__address">{GLAVANI_ADDRESS}</address>
            <p class="location-map__coords">GPS: {GLAVANI_LAT}, {GLAVANI_LNG}</p>
            {nearby}
            <div class="location-map__actions">
              <a class="btn-primary location-map__directions" href="{GLAVANI_MAPS_DIRECTIONS}" target="_blank" rel="noopener noreferrer">{directions}</a>
              <a class="btn-secondary location-map__open" href="{GLAVANI_MAPS_LINK}" target="_blank" rel="noopener noreferrer">{open_maps}</a>
            </div>
          </div>
        </div>
      </div>
    </section>
<script src="/assets/js/location-map.js" defer></script>"""


def render_landing(page: dict, lang: str, en_slug: str, hr_slug: str) -> str:
    prefix = f"/{lang}/"
    slug = page["slug"]
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"

    crumbs = f"""
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li>{page['h1']}</li>
    </ol>
  </nav>"""

    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"
    sidebar_title = "Brzo" if lang == "hr" else "Quick Info"
    sidebar = f"""
        <aside class="landing-sidebar">
          <h3>{sidebar_title}</h3>
          <ul>
            <li><strong>{'Otvoreno' if lang == 'hr' else 'Open'}:</strong> 9–17 h</li>
            <li><strong>{'Zadnji ulaz' if lang == 'hr' else 'Last entry'}:</strong> 15 h</li>
            <li><a href="tel:+385918964525">+385 91 896 4525</a></li>
            <li><a href="https://www.google.com/maps?q=45.021389,13.951111">Google Maps</a></li>
          </ul>
          <p style="margin-top:1rem;"><a class="btn-primary" href="tel:+385918964525" style="width:100%;font-size:0.875rem;">{cta}</a></p>
        </aside>"""

    img = page.get("image", "glavani-park-adventure-istria-croatia.jpg")
    location_map = render_location_map(lang) if page.get("location_map") else ""
    map_head = LOCATION_MAP_HEAD if page.get("location_map") else ""
    body = f"""{head_meta(lang, page['title'], page['meta_description'], page['keywords'], canonical, en_slug, hr_slug, og_image=img, extra_head=map_head)}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang)}
{crumbs}
<main>
  <section class="hero hero--landing">
    <div class="hero__inner">
      <p class="hero__badge">{page['hero_badge']}</p>
      <h1>{page['h1']}</h1>
      <p class="hero__subtitle">{page['hero_subtitle']}</p>
      <a class="btn-primary" href="tel:+385918964525">{cta}</a>
    </div>
  </section>
  {location_map}
  <div class="landing-layout section--theme-forest">
    <div class="landing-layout__inner">
    <article>
      <figure class="feature-img">
        <img src="/images/{img}" alt="{page['image_alt']}" width="800" height="560" loading="eager">
      </figure>
      {render_sections(page['sections'])}
    </article>
    {sidebar}
    </div>
  </div>
  {render_related(page.get('related', []), lang)}
  <section class="section section--alt">
    <div class="pricing-teaser">
      <h2>{'Rezervirajte avanturu' if lang == 'hr' else 'Book Your Adventure'}</h2>
      <p>{'Pozovite unaprijed za cijene i dostupnost termina.' if lang == 'hr' else 'Call ahead for pricing and availability — especially for groups.'}</p>
      <a class="btn-primary" href="tel:+385918964525">{cta}</a>
    </div>
  </section>
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (page['h1'], None)])}
</body>
</html>"""
    return body


SKIP_LANDING_SLUGS = {
    "en": {"family-activities-istria", "adventure-park-croatia"},
    "hr": {"obiteljske-aktivnosti-istri", "avanturisticki-park-hrvatska"},
}

ACTIVITIES_HUB_SLUGS = {"en": "adventure-park-croatia", "hr": "avanturisticki-park-hrvatska"}

ACTIVITIES_HUB_COPY = {
    "en": {
        "title": "Adventure Park Istria | Zipline & Adrenaline Park Croatia",
        "meta_description": (
            "Glavani Park — adventure park, zipline park and adrenaline park in Istria, Croatia. "
            "Six outdoor attractions near Pula: Human Catapult, High Swing, ziplines, climbing wall. Open 9 AM–5 PM."
        ),
        "keywords": (
            "adventure park Istria, zipline park Croatia, adrenaline park Istria, outdoor activities Istria Croatia, "
            "Glavani Park activities, high ropes Pula, forest zipline Istria"
        ),
        "h1": "Our Activities",
        "lead": "Six signature outdoor attractions — adventure park, zipline courses and adrenaline rides in Istria",
    },
    "hr": {
        "title": "Avanturistički park Istria | Zipline i adrenalinski park Hrvatska",
        "meta_description": (
            "Glavani Park — avanturistički park, zipline park i adrenalinski park u Istri, Hrvatska. "
            "Šest atrakcija na otvorenom kod Pule: katapulta, ljuljačka, zipline, penjački zid. Otvoreno 9–17 h."
        ),
        "keywords": (
            "avanturistički park Istria, zipline park Hrvatska, adrenalinski park Istria, aktivnosti na otvorenom Istria, "
            "Glavani Park aktivnosti, visoke staze Pula, zipline šuma Istria"
        ),
        "h1": "Naše aktivnosti",
        "lead": "Šest atrakcija na otvorenom — avantura, zipline i adrenalin u Istri",
    },
}

ACTIVITY_ICONS = {
    "catapult": "🚀",
    "swing": "🎢",
    "drop": "⬇️",
    "zipline-valley": "🪂",
    "zipline-low": "🌲",
    "climbing": "🧗",
}


def activities_hub_slug(lang: str) -> str:
    return ACTIVITIES_HUB_SLUGS[lang]


def activities_hub_path(lang: str) -> str:
    return f"/{lang}/{activities_hub_slug(lang)}/"


def render_activity_hub_grid(lang: str, *, compact: bool = False) -> str:
    prefix = f"/{lang}/"
    cards = []
    for act in ACTIVITIES:
        slug = act["hr_slug"] if lang == "hr" else act["en_slug"]
        label = act["hr"]["h1"] if lang == "hr" else act["en"]["h1"]
        mod = act["tile_mod"]
        icon = ACTIVITY_ICONS.get(mod, "🌲")
        cards.append(
            f'<a class="hub-card hub-card--{mod}" href="{prefix}{slug}/">'
            f'<span class="hub-card__icon" aria-hidden="true">{icon}</span>'
            f'<h3>{label}</h3></a>'
        )
    grid_class = "hub-grid activity-showcase--compact" if compact else "hub-grid"
    return f'<div class="{grid_class}">{"".join(cards)}</div>'


def render_activity_siblings(current_en_slug: str, lang: str) -> str:
    prefix = f"/{lang}/"
    heading = "Ostale aktivnosti" if lang == "hr" else "More Activities"
    cards = []
    for act in ACTIVITIES:
        if act["en_slug"] == current_en_slug:
            continue
        slug = act["hr_slug"] if lang == "hr" else act["en_slug"]
        label = act["hr"]["h1"] if lang == "hr" else act["en"]["h1"]
        mod = act["tile_mod"]
        icon = ACTIVITY_ICONS.get(mod, "🌲")
        cards.append(
            f'<a class="hub-card hub-card--{mod}" href="{prefix}{slug}/">'
            f'<span class="hub-card__icon" aria-hidden="true">{icon}</span>'
            f'<h3>{label}</h3></a>'
        )
    return f"""
    <section class="section section--theme-adrenaline">
      <div class="section__inner">
        <div class="section__heading"><h2>{heading}</h2></div>
        <div class="hub-grid activity-showcase--compact">{''.join(cards)}</div>
      </div>
    </section>"""


def render_activities_hub_page(lang: str) -> str:
    copy = ACTIVITIES_HUB_COPY[lang]
    en_slug = ACTIVITIES_HUB_SLUGS["en"]
    hr_slug = ACTIVITIES_HUB_SLUGS["hr"]
    slug = activities_hub_slug(lang)
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    book_href = f"{prefix}rezervacija/" if lang == "hr" else f"{prefix}book/"
    book_label = "Rezervirajte posjet" if lang == "hr" else "Book Your Visit"

    return f"""{head_meta(lang, copy['title'], copy['meta_description'], copy['keywords'], canonical, en_slug, hr_slug)}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang)}
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li>{copy['h1']}</li>
    </ol>
  </nav>
<main>
  <section class="section section--theme-adrenaline" id="activities" aria-labelledby="activities-heading">
    <div class="section__inner">
      <div class="section__heading">
        <h1 id="activities-heading">{copy['h1']}</h1>
        <p>{copy['lead']}</p>
      </div>
      {render_activity_hub_grid(lang)}
      <p style="margin-top:1.5rem;text-align:center;">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
      </p>
    </div>
  </section>
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (copy['h1'], None)])}
</body>
</html>"""


def render_activity_page(activity: dict, lang: str) -> str:
    data = activity["hr" if lang == "hr" else "en"]
    en_slug = activity["en_slug"]
    hr_slug = activity["hr_slug"]
    slug = hr_slug if lang == "hr" else en_slug
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    activities_label = "Aktivnosti" if lang == "hr" else "Activities"
    book_label = "Rezervirajte" if lang == "hr" else "Book Your Visit"
    book_href = f"{prefix}rezervacija/" if lang == "hr" else f"{prefix}book/"
    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"
    img = activity["image"]

    activities_href = activities_hub_path(lang)
    activities_url = f"{BASE}{activities_href}"

    prose = "".join(f"<p>{p}</p>" for p in data["paragraphs"])

    return f"""{head_meta(lang, data['title'], data['meta_description'], data['keywords'], canonical, en_slug, hr_slug, og_image=img)}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang)}
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li><a href="{activities_href}">{activities_label}</a></li>
      <li>{data['h1']}</li>
    </ol>
  </nav>
<main>
  <section class="hero hero--landing hero--activity">
    <div class="hero__inner">
      <p class="hero__badge">{data['hero_badge']}</p>
      <h1>{data['h1']}</h1>
    </div>
  </section>
  <div class="activity-detail-wrap section--theme-forest">
    <article class="activity-detail">
      <figure class="feature-img">
        <img src="/images/{img}" alt="{data['image_alt']}" width="800" height="560" loading="eager">
      </figure>
      <div class="prose activity-detail__prose">
        {prose}
      </div>
      <section class="activity-video" aria-labelledby="activity-video-heading">
        <h2 id="activity-video-heading">{data['video_heading']}</h2>
        <div class="activity-video__slot" data-activity-video="{en_slug}">
          <!-- Replace the placeholder below with a <video> or embedded iframe when your clip is ready -->
          <div class="activity-video__placeholder">
            <span class="activity-video__icon" aria-hidden="true">▶</span>
            <p>{data['video_placeholder']}</p>
          </div>
        </div>
      </section>
      <div class="activity-detail__actions">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </div>
    </article>
  </div>
  {render_activity_siblings(en_slug, lang)}
</main>
{footer(lang)}
{breadcrumb_schema([
    (home_label, f"{BASE}{prefix}"),
    (activities_label, activities_url),
    (data['h1'], None),
])}
</body>
</html>"""


def inject_reviews_section(body: str, lang: str) -> str:
    marker = "<!-- REVIEWS_SECTION -->"
    if marker not in body:
        return body
    return body.replace(marker, render_reviews_section(lang))


def home_body_en() -> str:
    """English homepage main content (abbreviated structure with full SEO sections)."""
    return inject_reviews_section(open(ROOT / "scripts" / "home_en.html").read(), "en")


def home_body_hr() -> str:
    return inject_reviews_section(open(ROOT / "scripts" / "home_hr.html").read(), "hr")


def render_faq_page(lang: str) -> str:
    copy = FAQ_COPY[lang]
    slug = FAQ_SLUGS[lang]
    en_slug = FAQ_SLUGS["en"]
    hr_slug = FAQ_SLUGS["hr"]
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    book_href = f"{prefix}rezervacija/" if lang == "hr" else f"{prefix}book/"
    book_label = "Rezervirajte posjet" if lang == "hr" else "Book Your Visit"
    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"

    return f"""{head_meta(lang, copy['title'], copy['meta_description'], copy['keywords'], canonical, en_slug, hr_slug)}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang)}
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li>{copy['h1']}</li>
    </ol>
  </nav>
<main>
  <section class="hero hero--landing">
    <div class="hero__inner">
      <p class="hero__badge">{'Obitelji · manje grupe · do 6 osoba' if lang == 'hr' else 'Families · Small Groups · Up to 6 People'}</p>
      <h1>{copy['h1']}</h1>
      <p class="hero__subtitle">{copy['lead']}</p>
    </div>
  </section>
  <section class="section section--theme-forest">
    <div class="section__inner">
      {render_faq_list(lang)}
      <p style="margin-top:1.5rem;text-align:center;color:var(--rock-mid);">{copy['book_note']}</p>
      <p style="margin-top:1rem;text-align:center;display:flex;flex-wrap:wrap;gap:0.75rem;justify-content:center;">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </p>
    </div>
  </section>
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (copy['h1'], None)])}
{json_ld_script(faq_page_schema(SMALL_GROUP_FAQS[lang]))}
</body>
</html>"""


def render_booking_app(lang: str) -> str:
    if lang == "hr":
        slug, en_slug, hr_slug = "rezervacija", "book", "rezervacija"
        title = "Rezervacija | Glavani Park – odaberite paket i datum"
        desc = "Rezervirajte Glavani Park online za do 6 osoba: odaberite paket, datum i pošaljite WhatsAppom ili SMS-om. Grupe 7+ nazovite."
        h1 = "Rezervirajte avanturu"
        lead = "Odaberite paket (do 6 osoba) i datum — WhatsApp, SMS ili poziv. Grupe 7+ nazovite."
    else:
        slug, en_slug, hr_slug = "book", "book", "rezervacija"
        title = "Book Your Visit | Glavani Park – Pick Package & Date"
        desc = "Book Glavani Park online for up to 6 people: choose a package, pick a date, and send via WhatsApp or SMS. Groups of 7+ please call."
        h1 = "Book Your Adventure"
        lead = "Choose a package for up to 6 people, pick your date, and send — WhatsApp, SMS, or call. Groups of 7+ please call to book."
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    extra = (
        '  <link rel="manifest" href="/manifest.webmanifest">\n'
        '  <meta name="theme-color" content="#1a3d2e">\n'
        '  <meta name="apple-mobile-web-app-capable" content="yes">'
    )
    return f"""{head_meta(lang, title, desc, "book glavani park, reservation istria", canonical, en_slug, hr_slug, extra_head=extra)}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang)}
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol><li><a href="{prefix}">{home_label}</a></li><li>{h1}</li></ol>
</nav>
<div class="book-app-hero">
  <h1>{h1}</h1>
  <p>{lead}</p>
</div>
<div class="book-app-wrap">
  <div id="booking-app" aria-live="polite"></div>
</div>
{footer(lang)}
<script src="/assets/js/booking-app.js" defer></script>
</body>
</html>"""


def render_home(lang: str) -> str:
    home = HOME_HR if lang == "hr" else HOME_EN
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}"
    body_content = home_body_hr() if lang == "hr" else home_body_en()
    org_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["AmusementPark", "TouristAttraction"],
                "@id": f"{canonical}#glavani-park",
                "name": "Glavani Park",
                "description": home["meta_description"],
                "url": canonical,
                "telephone": "+385918964525",
                "image": f"{BASE}/images/{home['image']}",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Glavani 10",
                    "addressLocality": "Barban",
                    "postalCode": "52207",
                    "addressRegion": "Istria",
                    "addressCountry": "HR",
                },
                "geo": {"@type": "GeoCoordinates", "latitude": GLAVANI_LAT, "longitude": GLAVANI_LNG},
                "hasMap": GLAVANI_MAPS_LINK,
                "openingHoursSpecification": {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": [
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday",
                        "Sunday",
                    ],
                    "opens": "09:00",
                    "closes": "17:00",
                },
                "areaServed": {"@type": "AdministrativeArea", "name": "Istria, Croatia"},
                "sameAs": [GLAVANI_MAPS_LINK],
                "keywords": home["keywords"],
            }
        ],
    }
    return f"""{head_meta(lang, home['title'], home['meta_description'], home['keywords'], canonical, is_home=True, og_image=home['image'])}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang, is_home=True)}
{body_content}
{footer(lang)}
<script src="/assets/js/reviews-carousel.js" defer></script>
{json_ld_script(org_schema)}
</body>
</html>"""


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  page: {path.relative_to(ROOT)}")


def build_sitemap(urls: list[tuple[str, str]]) -> None:
    """urls: list of (loc, changefreq)."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
    lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    for loc, freq in urls:
        en_url, hr_url = sitemap_alternates(loc)
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append("    <priority>0.8</priority>" if loc.count("/") > 4 else "    <priority>1.0</priority>")
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="hr" href="{hr_url}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    write_file(ROOT / "sitemap.xml", "\n".join(lines))


def build_robots() -> None:
    content = f"""User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
"""
    write_file(ROOT / "robots.txt", content)


def build_root_redirect() -> None:
    content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=en/">
  <link rel="canonical" href="https://www.glavanipark.com/en/">
  <title>Glavani Park</title>
  <script>location.replace('en/');</script>
</head>
<body><p><a href="en/">Glavani Park – Adventure Park Istria</a></p></body>
</html>"""
    write_file(ROOT / "index.html", content)


def build_search_console_guide() -> None:
    content = """Google Search Console Setup for Glavani Park
=============================================

1. Go to https://search.google.com/search-console
2. Add property: https://www.glavanipark.com
3. Verify ownership (HTML file upload, DNS TXT record, or meta tag)
4. Submit sitemap: https://www.glavanipark.com/sitemap.xml
5. Request indexing for key URLs:
   - https://www.glavanipark.com/en/
   - https://www.glavanipark.com/hr/
   - https://www.glavanipark.com/en/things-to-do-in-istria/
   - https://www.glavanipark.com/en/zipline-croatia/

Backlink outreach (hotels, campsites, travel blogs):
- Use /en/partners/ for partnership programme details
- Use /en/link-to-us/ for embed codes and suggested anchor text
- Contact: info@glavanipark.com | +385 91 896 4525
"""
    write_file(ROOT / "search-console-setup.txt", content)


def main() -> None:
    print("Generating WebP/JPEG images...")
    generate_images()

    print("Building English pages...")
    write_file(ROOT / "en" / "index.html", render_home("en"))
    write_file(ROOT / "en" / "book" / "index.html", render_booking_app("en"))
    write_file(ROOT / "en" / FAQ_SLUGS["en"] / "index.html", render_faq_page("en"))
    sitemap_urls = [(f"{BASE}/en/", "weekly"), (f"{BASE}/en/book/", "weekly")]
    sitemap_urls.append((f"{BASE}/en/{FAQ_SLUGS['en']}/", "monthly"))
    for page in PAGES_EN:
        slug = page["slug"]
        if slug in SKIP_LANDING_SLUGS["en"]:
            continue
        hr_slug = EN_TO_HR.get(slug, slug)
        write_file(ROOT / "en" / slug / "index.html", render_landing(page, "en", slug, hr_slug))
        sitemap_urls.append((f"{BASE}/en/{slug}/", "monthly"))
    write_file(
        ROOT / "en" / activities_hub_slug("en") / "index.html",
        render_activities_hub_page("en"),
    )
    sitemap_urls.append((f"{BASE}/en/{activities_hub_slug('en')}/", "monthly"))
    for activity in ACTIVITIES:
        slug = activity["en_slug"]
        hr_slug = activity["hr_slug"]
        write_file(ROOT / "en" / slug / "index.html", render_activity_page(activity, "en"))
        sitemap_urls.append((f"{BASE}/en/{slug}/", "monthly"))

    print("Building Croatian pages...")
    write_file(ROOT / "hr" / "index.html", render_home("hr"))
    write_file(ROOT / "hr" / "rezervacija" / "index.html", render_booking_app("hr"))
    write_file(ROOT / "hr" / FAQ_SLUGS["hr"] / "index.html", render_faq_page("hr"))
    sitemap_urls.append((f"{BASE}/hr/", "weekly"))
    sitemap_urls.append((f"{BASE}/hr/rezervacija/", "weekly"))
    sitemap_urls.append((f"{BASE}/hr/{FAQ_SLUGS['hr']}/", "monthly"))
    for page in PAGES_HR:
        slug = page["slug"]
        if slug in SKIP_LANDING_SLUGS["hr"]:
            continue
        en_slug = SLUG_MAP.get(slug, slug)
        write_file(ROOT / "hr" / slug / "index.html", render_landing(page, "hr", en_slug, slug))
        sitemap_urls.append((f"{BASE}/hr/{slug}/", "monthly"))
    write_file(
        ROOT / "hr" / activities_hub_slug("hr") / "index.html",
        render_activities_hub_page("hr"),
    )
    sitemap_urls.append((f"{BASE}/hr/{activities_hub_slug('hr')}/", "monthly"))
    for activity in ACTIVITIES:
        slug = activity["hr_slug"]
        write_file(ROOT / "hr" / slug / "index.html", render_activity_page(activity, "hr"))
        sitemap_urls.append((f"{BASE}/hr/{slug}/", "monthly"))

    print("Writing robots.txt and sitemap.xml...")
    build_robots()
    build_sitemap(sitemap_urls)
    build_root_redirect()
    build_search_console_guide()
    relativize_site()
    print("Done.")


if __name__ == "__main__":
    main()
