#!/usr/bin/env python3
"""Build Glavani Park static SEO site: pages, images, sitemap, robots.txt."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from pages_en import HOME as HOME_EN, PAGES as PAGES_EN  # noqa: E402
from pages_hr import HOME as HOME_HR, PAGES as PAGES_HR, SLUG_MAP  # noqa: E402
from activities import ACTIVITIES, ACTIVITY_SLUG_MAP, activity_faqs  # noqa: E402
from reviews import (  # noqa: E402
    FACEBOOK_URL,
    TRIPADVISOR_URL,
    aggregate_rating,
    render_reviews_section,
    review_list,
    reset_cache,
)
from faqs import (  # noqa: E402
    FAQ_COPY,
    FAQ_SLUGS,
    VISITOR_FAQS,
    build_faq_schema,
    render_faq_list,
    render_faq_related,
    render_page_faq_section,
)
from packages import PRICES_COPY, PRICES_SLUGS, prices_offer_schema, render_price_sections  # noqa: E402

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

# Reverse map EN slug -> HR slug
EN_TO_HR = {v: k for k, v in SLUG_MAP.items()}
EN_TO_HR.update({v: k for k, v in ACTIVITY_SLUG_MAP.items()})
EN_TO_HR["book"] = "rezervacija"
EN_TO_HR["faq"] = "cesta-pitanja"
EN_TO_HR["prices"] = "cijene"

HR_TO_EN = dict(SLUG_MAP)
HR_TO_EN.update(ACTIVITY_SLUG_MAP)
HR_TO_EN["rezervacija"] = "book"
HR_TO_EN["cesta-pitanja"] = "faq"
HR_TO_EN["cijene"] = "prices"

IMAGES = [
    ("glavani-park-adventure-istria-croatia.jpg", "Glavani Park", (26, 61, 46), (45, 106, 79)),
    ("12-5m-high-swing-glavani-park-istria.webp", "12.5m High Swing", (234, 88, 12), (180, 83, 9)),
    ("human-catapult-adrenaline-park-croatia.webp", "Human Catapult", (234, 88, 12), (120, 53, 15)),
    ("zipline-120m-glavani-park-istria-croatia.webp", "Zipline 120m", (74, 85, 104), (45, 55, 72)),
    ("climbing-wall-outdoor-activities-istria.webp", "Climbing Wall", (64, 145, 108), (26, 61, 46)),
    ("quick-jump-20m-free-fall-istria.webp", "Quick Jump 20m", (124, 58, 237), (76, 29, 149)),
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


YOUTUBE_STILLS = [
    ("X2bRA2Bur-M", "human-catapult-youtube-still.webp"),
    ("W5CWJfZlW2o", "quick-jump-youtube-still.webp"),
    ("Uhbf2TF8PYE", "climbing-wall-youtube-still.webp"),
]


def fetch_youtube_stills() -> None:
    """Download high-quality YouTube thumbnails for activity tiles."""
    import io
    import urllib.request

    img_dir = ROOT / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    for video_id, filename in YOUTUBE_STILLS:
        path = img_dir / filename
        for quality in ("maxresdefault", "hqdefault"):
            url = f"https://i.ytimg.com/vi/{video_id}/{quality}.jpg"
            try:
                with urllib.request.urlopen(url, timeout=20) as response:
                    data = response.read()
                if len(data) < 1000:
                    continue
                img = Image.open(io.BytesIO(data)).convert("RGB")
                img.save(path, "WEBP", quality=86, method=6)
                print(f"  image: {path.name} (YouTube {video_id})")
                break
            except OSError:
                continue


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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
    logo_alt = (
        "Glavani Park — A Great Place to Be"
        if lang == "en"
        else "Glavani Park — odlično mjesto za avanturu"
    )
    return f"""
  <header class="site-header">
    <a class="site-header__brand" href="{home}">
      <img class="site-header__logo-img" src="/images/glavani-park-logo.png" alt="{logo_alt}" width="200" height="115" loading="eager">
    </a>
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
            ("Cijene", f"{prefix}{PRICES_SLUGS['hr']}/"),
            ("Lokacija", f"{prefix}#location" if is_home else f"{prefix}sto-raditi-kod-pule/"),
            ("Pitanja", f"{prefix}{FAQ_SLUGS['hr']}/"),
            ("Sigurnost", f"{prefix}sigurnost/"),
        ]
    else:
        links = [
            ("Activities", f"{prefix}#activities" if is_home else activities_hub_path(lang)),
            ("Groups", f"{prefix}team-building-istria/"),
            ("Prices", f"{prefix}{PRICES_SLUGS['en']}/"),
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
            ("Aktivnosti", f"{prefix}avanturisticki-park-hrvatska/"),
            ("Cijene", f"{prefix}cijene/"),
            ("FAQ", f"{prefix}cesta-pitanja/"),
            ("English", f"/en/"),
            ("Partneri", f"{prefix}partneri/"),
            ("Link na nas", f"{prefix}link-na-nas/"),
            ("Sigurnost", f"{prefix}sigurnost/"),
        ]
    else:
        copy = "Glavani Park · Adventure Park Istria · Zipline Croatia"
        links = [
            ("Home", prefix),
            ("Activities", f"{prefix}adventure-park-croatia/"),
            ("Prices", f"{prefix}prices/"),
            ("FAQ", f"{prefix}faq/"),
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
    og_image_alt: str | None = None,
    extra_head: str = "",
) -> str:
    og_locale = "hr_HR" if lang == "hr" else "en_GB"
    alt_locale = "en_GB" if lang == "hr" else "hr_HR"
    og_image_url = f"{BASE}/images/{og_image}"
    img_w, img_h = (400, 120) if "logo" in og_image else (800, 560)
    image_alt = og_image_alt or "Glavani Park adventure and zipline park in Istria, Croatia"
    safe_title = esc(title)
    safe_desc = esc(description)
    safe_keywords = esc(keywords)
    safe_image_alt = esc(image_alt)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{safe_title}</title>
  <meta name="description" content="{safe_desc}">
  <meta name="keywords" content="{safe_keywords}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
{hreflang_tags(en_slug, hr_slug, is_home)}
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{safe_title}">
  <meta property="og:description" content="{safe_desc}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:locale:alternate" content="{alt_locale}">
  <meta property="og:site_name" content="Glavani Park">
  <meta property="og:image" content="{og_image_url}">
  <meta property="og:image:width" content="{img_w}">
  <meta property="og:image:height" content="{img_h}">
  <meta property="og:image:alt" content="{safe_image_alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{safe_title}">
  <meta name="twitter:description" content="{safe_desc}">
  <meta name="twitter:image" content="{og_image_url}">
  <meta name="twitter:image:alt" content="{safe_image_alt}">
  <link rel="icon" href="/images/glavani-park-logo-small.png" type="image/png">
  <link rel="apple-touch-icon" href="/images/glavani-park-logo.png">
  <meta name="theme-color" content="#0a0a0a">
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


def webpage_schema(url: str, name: str, description: str, lang: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": name,
        "description": description,
        "inLanguage": "hr-HR" if lang == "hr" else "en-GB",
        "isPartOf": {"@id": f"{BASE}/en/#glavani-park"},
        "about": {"@id": f"{BASE}/en/#glavani-park"},
    }


def activity_page_schema(activity: dict, lang: str, url: str) -> list[dict]:
    data = activity[lang]
    schemas: list[dict] = [
        {
            "@context": "https://schema.org",
            "@type": "TouristAttraction",
            "@id": f"{url}#attraction",
            "name": data["h1"],
            "description": data["meta_description"],
            "url": url,
            "image": f"{BASE}/images/{activity['image']}",
            "isPartOf": {"@id": f"{BASE}/en/#glavani-park"},
            "touristType": "Adventure traveler",
        }
    ]
    single_price = activity.get("single_price")
    if single_price:
        book_slug = "book" if lang == "en" else "rezervacija"
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Offer",
                "name": data["h1"],
                "price": str(single_price),
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "url": f"{BASE}/{lang}/{book_slug}/",
                "seller": {"@id": f"{BASE}/en/#glavani-park"},
            }
        )
    video_id = activity.get("youtube_id")
    if video_id:
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "VideoObject",
                "name": data["video_heading"],
                "description": data["meta_description"],
                "thumbnailUrl": f"{BASE}/images/{activity['image']}",
                "uploadDate": "2020-01-01",
                "contentUrl": activity.get("youtube_url", f"https://youtu.be/{video_id}"),
                "embedUrl": f"https://www.youtube.com/embed/{video_id}",
            }
        )
    return schemas


def activities_hub_itemlist_schema(lang: str, url: str) -> dict:
    prefix = f"/{lang}/"
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": ACTIVITIES_HUB_COPY[lang]["h1"],
        "url": url,
        "numberOfItems": len(ACTIVITIES),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": act[lang]["h1"],
                "url": f"{BASE}{prefix}{act['hr_slug' if lang == 'hr' else 'en_slug']}/",
            }
            for i, act in enumerate(ACTIVITIES, 1)
        ],
    }


def faq_page_schema(faqs: list[dict], lang: str) -> dict:
    slug = FAQ_SLUGS[lang]
    url = f"{BASE}/{lang}/{slug}/"
    return build_faq_schema(
        faqs,
        lang,
        url=url,
        name=FAQ_COPY[lang]["h1"],
        description=FAQ_COPY[lang]["meta_description"],
    )


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
    page_faqs = page.get("faqs") or []
    faq_block = ""
    faq_schema = ""
    if page_faqs:
        faq_block = f"""
  <section class="section section--alt" aria-labelledby="page-faq-heading">
    <div class="section__inner">
      {render_page_faq_section(page_faqs, lang)}
    </div>
  </section>"""
        faq_schema = json_ld_script(
            build_faq_schema(
                page_faqs,
                lang,
                url=canonical,
                name=page["h1"],
                description=page["meta_description"],
            )
        )
    body = f"""{head_meta(lang, page['title'], page['meta_description'], page['keywords'], canonical, en_slug, hr_slug, og_image=img, og_image_alt=page.get('image_alt'), extra_head=map_head)}
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
  {faq_block}
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
{faq_schema}
{json_ld_script(webpage_schema(canonical, page['h1'], page['meta_description'], lang))}
</body>
</html>"""
    return body


SKIP_LANDING_SLUGS = {
    "en": {"adventure-park-croatia"},
    "hr": {"avanturisticki-park-hrvatska"},
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
        "intro": (
            "Glavani Park near Barban covers 1.5 hectares of oak forest with six instructor-led attractions — "
            "from the Human Catapult and 12.5 m high swing to 120 m ziplines and high-ropes routes. "
            "Open daily 9 AM–5 PM, about 30 minutes from Pula."
        ),
        "family_link": "family-activities-istria",
        "family_label": "Family activities guide",
        "family_desc": "Yellow route for kids, ziplines for teens — plan a family day",
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
        "intro": (
            "Glavani Park kod Barbana prostire se na 1,5 ha hrastove šume sa šest atrakcija pod nadzorom instruktora — "
            "od ljudske katapulata i ljuljačke od 12,5 m do ziplinea od 120 m i visokih staza. "
            "Otvoreno 9–17 h, otprilike 30 minuta od Pule."
        ),
        "family_link": "obiteljske-aktivnosti-istri",
        "family_label": "Vodič za obiteljske aktivnosti",
        "family_desc": "Žuta staza za djecu, zipline za tinejdžere — planirajte obiteljski dan",
    },
}

ACTIVITY_ICONS = {
    "catapult": "",
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


def render_hub_card_icon(mod: str) -> str:
    icon = ACTIVITY_ICONS.get(mod, "🌲")
    if not icon:
        return ""
    return f'<span class="hub-card__icon" aria-hidden="true">{icon}</span>'


def render_activity_hub_grid(lang: str, *, compact: bool = False) -> str:
    prefix = f"/{lang}/"
    cards = []
    for act in ACTIVITIES:
        slug = act["hr_slug"] if lang == "hr" else act["en_slug"]
        label = act["hr"]["h1"] if lang == "hr" else act["en"]["h1"]
        mod = act["tile_mod"]
        cards.append(
            f'<a class="hub-card hub-card--{mod}" href="{prefix}{slug}/">'
            f'{render_hub_card_icon(mod)}'
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
        cards.append(
            f'<a class="hub-card hub-card--{mod}" href="{prefix}{slug}/">'
            f'{render_hub_card_icon(mod)}'
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

    family_href = f"{prefix}{copy['family_link']}/"
    family_card = (
        f'<a class="topic-link" href="{family_href}">{copy["family_label"]}'
        f'<span>{copy["family_desc"]}</span></a>'
    )

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
        <p class="faq-intro">{copy['intro']}</p>
      </div>
      {render_activity_hub_grid(lang)}
      <div class="topic-grid" style="margin-top:1.5rem;max-width:760px;margin-left:auto;margin-right:auto;">
        {family_card}
      </div>
      <p style="margin-top:1.5rem;text-align:center;">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
      </p>
    </div>
  </section>
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (copy['h1'], None)])}
{json_ld_script(webpage_schema(canonical, copy['h1'], copy['meta_description'], lang))}
{json_ld_script(activities_hub_itemlist_schema(lang, canonical))}
</body>
</html>"""


def render_activity_video(activity: dict, data: dict, lang: str) -> str:
    video_id = activity.get("youtube_id")
    if not video_id:
        return f"""
        <div class="activity-video__slot" data-activity-video="{activity['en_slug']}">
          <div class="activity-video__placeholder">
            <span class="activity-video__icon" aria-hidden="true">▶</span>
            <p>{data['video_placeholder']}</p>
          </div>
        </div>"""
    title = esc(data["video_heading"])
    youtube_url = activity.get("youtube_url", f"https://youtu.be/{video_id}")
    watch_label = "Pogledajte na YouTubeu" if lang == "hr" else "Watch on YouTube"
    return f"""
        <div class="activity-video__slot" data-activity-video="{activity['en_slug']}">
          <iframe
            src="https://www.youtube.com/embed/{video_id}"
            title="{title}"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
            loading="lazy"
            referrerpolicy="strict-origin-when-cross-origin"></iframe>
        </div>
        <p class="activity-video__youtube-link">
          <a href="{youtube_url}" target="_blank" rel="noopener noreferrer">{watch_label}</a>
        </p>"""


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
    mod = activity["tile_mod"]
    use_banner_header = bool(activity.get("youtube_id"))

    activities_href = activities_hub_path(lang)
    activities_url = f"{BASE}{activities_href}"

    prose = "".join(f"<p>{p}</p>" for p in data["paragraphs"])
    prices_href = f"{prefix}prices/" if lang == "en" else f"{prefix}cijene/"
    prices_label = "Packages &amp; prices" if lang == "en" else "Paketi i cijene"
    prose += (
        f'<p><a href="{book_href}">{book_label}</a> · '
        f'<a href="{prices_href}">{prices_label}</a></p>'
    )
    page_faqs = activity_faqs(activity, lang)
    faq_block = f"""
  <section class="section section--alt" aria-labelledby="page-faq-heading">
    <div class="section__inner">
      {render_page_faq_section(page_faqs, lang)}
    </div>
  </section>"""
    faq_schema = json_ld_script(
        build_faq_schema(page_faqs, lang, url=canonical, name=data["h1"], description=data["meta_description"])
    )
    activity_schema_scripts = "".join(json_ld_script(s) for s in activity_page_schema(activity, lang, canonical))
    single_price = activity.get("single_price")
    price_html = ""
    if single_price:
        price_label = (
            f"€{single_price} po osobi"
            if lang == "hr"
            else f"€{single_price} per person"
        )
        price_html = f'\n        <p class="activity-banner__price">{price_label}</p>'

    if use_banner_header:
        page_header = ""
        article_open = f"""      <header class="activity-banner activity-banner--{mod}" aria-labelledby="activity-heading">
        <p class="activity-banner__badge">{data['hero_badge']}</p>
        <h1 id="activity-heading">{data['h1']}</h1>{price_html}
      </header>"""
    else:
        page_header = f"""  <section class="hero hero--landing hero--activity">
    <div class="hero__inner">
      <p class="hero__badge">{data['hero_badge']}</p>
      <h1>{data['h1']}</h1>
    </div>
  </section>"""
        article_open = f"""      <figure class="feature-img">
        <img src="/images/{img}" alt="{data['image_alt']}" width="800" height="560" loading="eager">
      </figure>"""

    return f"""{head_meta(lang, data['title'], data['meta_description'], data['keywords'], canonical, en_slug, hr_slug, og_image=img, og_image_alt=data['image_alt'])}
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
{page_header}
  <div class="activity-detail-wrap section--theme-forest">
    <article class="activity-detail">
{article_open}
      <div class="prose activity-detail__prose">
        {prose}
      </div>
      <section class="activity-video" aria-labelledby="activity-video-heading">
        <h2 id="activity-video-heading">{data['video_heading']}</h2>
        {render_activity_video(activity, data, lang)}
      </section>
      <div class="activity-detail__actions">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </div>
    </article>
  </div>
  {render_activity_siblings(en_slug, lang)}
  {faq_block}
</main>
{footer(lang)}
{breadcrumb_schema([
    (home_label, f"{BASE}{prefix}"),
    (activities_label, activities_url),
    (data['h1'], None),
])}
{faq_schema}
{activity_schema_scripts}
{json_ld_script(webpage_schema(canonical, data['h1'], data['meta_description'], lang))}
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
      <p class="hero__badge">{'Informacije za posjetitelje' if lang == 'hr' else 'Visitor information'}</p>
      <h1>{copy['h1']}</h1>
      <p class="hero__subtitle">{copy['lead']}</p>
    </div>
  </section>
  <section class="section section--theme-forest">
    <div class="section__inner">
      <p class="faq-intro">{copy['intro']}</p>
      {render_faq_list(lang)}
      <p style="margin-top:1.5rem;text-align:center;color:var(--rock-mid);">{copy['book_note']}</p>
      <p style="margin-top:1rem;text-align:center;display:flex;flex-wrap:wrap;gap:0.75rem;justify-content:center;">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </p>
    </div>
  </section>
  {render_faq_related(lang)}
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (copy['h1'], None)])}
{json_ld_script(faq_page_schema(VISITOR_FAQS[lang], lang))}
{json_ld_script(webpage_schema(canonical, copy['h1'], copy['meta_description'], lang))}
</body>
</html>"""


def render_prices_page(lang: str) -> str:
    copy = PRICES_COPY[lang]
    slug = PRICES_SLUGS[lang]
    en_slug = PRICES_SLUGS["en"]
    hr_slug = PRICES_SLUGS["hr"]
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
      <p class="hero__badge">{'Online do 6 osoba' if lang == 'hr' else 'Book online · up to 6 people'}</p>
      <h1>{copy['h1']}</h1>
      <p class="hero__subtitle">{copy['lead']}</p>
    </div>
  </section>
  <section class="section section--theme-forest">
    <div class="section__inner">
      {render_price_sections(lang)}
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
{json_ld_script(prices_offer_schema(lang, canonical, copy['h1']))}
{json_ld_script(webpage_schema(canonical, copy['h1'], copy['meta_description'], lang))}
</body>
</html>"""


def render_booking_app(lang: str) -> str:
    if lang == "hr":
        slug, en_slug, hr_slug = "rezervacija", "book", "rezervacija"
        title = "Rezerviraj | Glavani Park – odaberite paket i datum"
        desc = (
            "Rezervirajte Glavani Park online za do 6 osoba. Ispunite obrazac — "
            "potvrdu šaljemo WhatsAppom ili SMS-om. Unutar 48 sati od termina nazovite."
        )
        h1 = "Rezerviraj"
        lead = "Ispunite obrazac — potvrdu rezervacije šaljemo što prije WhatsAppom ili SMS-om."
        notice = "Rezervacija u roku 48 sati od željenog datuma posjeta? Molimo <a href=\"tel:+38598224314\">nazovite</a>."
    else:
        slug, en_slug, hr_slug = "book", "book", "rezervacija"
        title = "Book | Glavani Park – Pick Package & Date"
        desc = (
            "Book Glavani Park online for up to 6 people. Fill in the form — "
            "we confirm via SMS or WhatsApp ASAP. Within 48 hours of your visit date, please call to book."
        )
        h1 = "Book"
        lead = "Fill in the form below — we'll confirm your booking as soon as possible via SMS or WhatsApp."
        notice = "Booking within 48 hours of your requested visit date? Please <a href=\"tel:+385918964525\">call to book</a>."
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    extra = (
        '  <link rel="manifest" href="/manifest.webmanifest">\n'
        '  <meta name="theme-color" content="#0a0a0a">\n'
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
  <p class="book-app-notice">{notice}</p>
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
    quote_key = "hr" if lang == "hr" else "en"
    aggregate = aggregate_rating()
    reviews = review_list()
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
                "sameAs": [GLAVANI_MAPS_LINK, TRIPADVISOR_URL, FACEBOOK_URL],
                "keywords": home["keywords"],
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": str(aggregate["rating_value"]),
                    "bestRating": str(aggregate["best_rating"]),
                    "worstRating": str(aggregate["worst_rating"]),
                    "ratingCount": str(aggregate["rating_count"]),
                    "reviewCount": str(aggregate["rating_count"]),
                },
                "review": [
                    {
                        "@type": "Review",
                        "author": {"@type": "Person", "name": review["author"]},
                        "datePublished": review["date"],
                        "reviewBody": review[quote_key],
                        "reviewRating": {
                            "@type": "Rating",
                            "ratingValue": str(review.get("rating", 5)),
                            "bestRating": "5",
                        },
                        "publisher": {
                            "@type": "Organization",
                            "name": "TripAdvisor",
                        },
                    }
                    for review in reviews
                ],
            },
            {
                "@type": "WebPage",
                "@id": f"{canonical}#webpage",
                "url": canonical,
                "name": home["title"],
                "description": home["meta_description"],
                "inLanguage": "hr-HR" if lang == "hr" else "en-GB",
                "isPartOf": {"@id": f"{canonical}#glavani-park"},
                "about": {"@id": f"{canonical}#glavani-park"},
            },
        ],
    }
    return f"""{head_meta(lang, home['title'], home['meta_description'], home['keywords'], canonical, is_home=True, og_image=home['image'], og_image_alt="Glavani Park adventure and zipline park in Istria, Croatia")}
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
        lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}"/>')
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
  <meta name="description" content="Glavani Park — adventure and zipline park in Istria, Croatia near Pula.">
  <link rel="canonical" href="https://www.glavanipark.com/en/">
  <link rel="alternate" hreflang="en" href="https://www.glavanipark.com/en/">
  <link rel="alternate" hreflang="hr" href="https://www.glavanipark.com/hr/">
  <link rel="alternate" hreflang="x-default" href="https://www.glavanipark.com/en/">
  <title>Glavani Park | Adventure Park Istria, Croatia</title>
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
    print("Fetching TripAdvisor reviews...")
    from fetch_reviews import main as fetch_reviews_main

    fetch_reviews_main()
    reset_cache()

    print("Generating WebP/JPEG images...")
    generate_images()
    fetch_youtube_stills()

    print("Building English pages...")
    write_file(ROOT / "en" / "index.html", render_home("en"))
    write_file(ROOT / "en" / "book" / "index.html", render_booking_app("en"))
    write_file(ROOT / "en" / PRICES_SLUGS["en"] / "index.html", render_prices_page("en"))
    write_file(ROOT / "en" / FAQ_SLUGS["en"] / "index.html", render_faq_page("en"))
    sitemap_urls = [(f"{BASE}/en/", "weekly"), (f"{BASE}/en/book/", "weekly")]
    sitemap_urls.append((f"{BASE}/en/{PRICES_SLUGS['en']}/", "monthly"))
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
    write_file(ROOT / "hr" / PRICES_SLUGS["hr"] / "index.html", render_prices_page("hr"))
    write_file(ROOT / "hr" / FAQ_SLUGS["hr"] / "index.html", render_faq_page("hr"))
    sitemap_urls.append((f"{BASE}/hr/", "weekly"))
    sitemap_urls.append((f"{BASE}/hr/rezervacija/", "weekly"))
    sitemap_urls.append((f"{BASE}/hr/{PRICES_SLUGS['hr']}/", "monthly"))
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
