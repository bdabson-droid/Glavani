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
from faqs import FAQ_COPY, FAQ_SLUGS, render_faq_list  # noqa: E402

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
LOCATION_MAP_IMAGE = "glavani-park-location-map.jpg"

# Reverse map EN slug -> HR slug
EN_TO_HR = {v: k for k, v in SLUG_MAP.items()}
EN_TO_HR.update({v: k for k, v in ACTIVITY_SLUG_MAP.items()})
EN_TO_HR["book"] = "rezervacija"
EN_TO_HR["faq"] = "cesta-pitanja"

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


def generate_location_map_image() -> None:
    """Create a map-style location image (links to Google Maps in the page)."""
    img_dir = ROOT / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    path = img_dir / LOCATION_MAP_IMAGE
    w, h = 800, 560
    img = Image.new("RGB", (w, h), (235, 228, 210))
    draw = ImageDraw.Draw(img)

    for y in range(h):
        t = y / h
        r = int(235 + (210 - 235) * t)
        g = int(228 + (200 - 228) * t)
        b = int(210 + (175 - 210) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    for x in range(0, w, 48):
        draw.line([(x, 0), (x, h)], fill=(220, 212, 195), width=1)
    for y in range(0, h, 48):
        draw.line([(0, y), (w, y)], fill=(220, 212, 195), width=1)

    forest = (45, 106, 79)
    draw.ellipse([80, 120, 340, 380], fill=(64, 145, 108))
    draw.ellipse([420, 80, 720, 420], fill=forest)
    draw.ellipse([260, 300, 580, 520], fill=(74, 124, 89))

    road = (250, 245, 235)
    draw.line([(0, h // 2 + 20), (w, h // 2 - 30)], fill=road, width=22)
    draw.line([(w // 3, 0), (w // 3 + 40, h)], fill=road, width=16)

    pin_x, pin_y = w // 2 + 30, h // 2 + 10
    draw.ellipse([pin_x - 18, pin_y - 44, pin_x + 18, pin_y - 8], fill=(220, 38, 38))
    draw.polygon(
        [(pin_x, pin_y + 8), (pin_x - 16, pin_y - 10), (pin_x + 16, pin_y - 10)],
        fill=(180, 28, 28),
    )
    draw.ellipse([pin_x - 7, pin_y - 34, pin_x + 7, pin_y - 20], fill=(255, 255, 255))

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
        small = font

    draw.text((40, 36), "Glavani Park", fill=(26, 61, 46), font=font)
    draw.text((40, 72), GLAVANI_ADDRESS, fill=(45, 55, 72), font=small)
    draw.text((40, h - 44), f"GPS {GLAVANI_LAT}, {GLAVANI_LNG}", fill=(45, 55, 72), font=small)
    draw.text((40, h - 22), "Tap for Google Maps directions", fill=(234, 88, 12), font=small)

    img.save(path, "JPEG", quality=88, optimize=True)
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
  <meta property="og:image" content="{BASE}/images/{og_image}">
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
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


def render_location_map(lang: str) -> str:
    if lang == "hr":
        heading = "Pronađite Glavani Park"
        lead = "Glavani 10, 52207 Barban · između Vodnjanja (10 km) i Barbana (6 km)"
        directions = "Upute za dolazak"
        open_maps = "Otvori u Google Maps"
        map_alt = "Karta lokacije Glavani Parka kod Barbana, Istria"
    else:
        heading = "Find Glavani Park"
        lead = "Glavani 10, 52207 Barban · between Vodnjan (10 km) and Barban (6 km)"
        directions = "Get directions"
        open_maps = "Open in Google Maps"
        map_alt = "Map showing Glavani Park location near Barban, Istria"
    return f"""
    <section class="section section--alt" id="location-map" aria-labelledby="location-map-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="location-map-heading">{heading}</h2>
          <p>{lead}</p>
        </div>
        <div class="location-map">
          <a class="location-map__embed" href="{GLAVANI_MAPS_LINK}" target="_blank" rel="noopener noreferrer" aria-label="{open_maps}">
            <img src="/images/{LOCATION_MAP_IMAGE}" alt="{map_alt}" width="800" height="560" loading="lazy">
          </a>
          <div class="location-map__panel">
            <p class="location-map__pin" aria-hidden="true">📍</p>
            <address class="location-map__address">{GLAVANI_ADDRESS}</address>
            <p class="location-map__coords">GPS: {GLAVANI_LAT}, {GLAVANI_LNG}</p>
            <div class="location-map__actions">
              <a class="btn-primary location-map__directions" href="{GLAVANI_MAPS_DIRECTIONS}" target="_blank" rel="noopener noreferrer">{directions}</a>
              <a class="btn-secondary location-map__open" href="{GLAVANI_MAPS_LINK}" target="_blank" rel="noopener noreferrer">{open_maps}</a>
            </div>
          </div>
        </div>
      </div>
    </section>"""


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
    body = f"""{head_meta(lang, page['title'], page['meta_description'], page['keywords'], canonical, en_slug, hr_slug, og_image=img)}
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
        "title": "Our Activities | Glavani Park Istria",
        "meta_description": (
            "Explore all six Glavani Park attractions — Human Catapult, High Swing, 20m Drop, "
            "ziplines, and climbing wall. Open daily 9 AM–5 PM near Pula."
        ),
        "keywords": "Glavani Park activities, adventure park Istria, human catapult, zipline Croatia, high swing",
        "h1": "Our Activities",
        "lead": "Six signature attractions — tap for details",
    },
    "hr": {
        "title": "Naše aktivnosti | Glavani Park Istria",
        "meta_description": (
            "Istražite svih šest atrakcija Glavani Parka — ljudska katapulta, visoka ljuljačka, "
            "pad s 20 m, zipline i penjački zid. Otvoreno 9–17 h kod Pule."
        ),
        "keywords": "Glavani Park aktivnosti, avanturistički park Istria, ljudska katapulta, zipline Hrvatska",
        "h1": "Naše aktivnosti",
        "lead": "Šest glavnih atrakcija — dodirnite za detalje",
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
                "@type": "AmusementPark",
                "name": "Glavani Park",
                "url": canonical,
                "telephone": "+385918964525",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Glavani 10",
                    "addressLocality": "Barban",
                    "postalCode": "52207",
                    "addressCountry": "HR",
                },
                "geo": {"@type": "GeoCoordinates", "latitude": 45.021389, "longitude": 13.951111},
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
<script type="application/ld+json">{json.dumps(org_schema, indent=2)}</script>
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
        en_path = loc.replace(BASE, "")
        hr_path = en_path.replace("/en/", "/hr/")
        if en_path.endswith("/en/"):
            hr_path = "/hr/"
        elif "/en/" in en_path:
            en_slug = en_path.split("/en/")[1].strip("/")
            hr_slug = EN_TO_HR.get(en_slug, en_slug)
            hr_path = f"/hr/{hr_slug}/"
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append("    <priority>0.8</priority>" if "/en/" in loc and loc.count("/") > 4 else "    <priority>1.0</priority>")
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{loc}"/>')
        hr_url = BASE + hr_path
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
    generate_location_map_image()

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

    print("Writing robots.txt and sitemap.xml...")
    build_robots()
    build_sitemap(sitemap_urls)
    build_root_redirect()
    build_search_console_guide()
    relativize_site()
    print("Done.")


if __name__ == "__main__":
    main()
