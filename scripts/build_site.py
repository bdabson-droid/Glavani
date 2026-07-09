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
from activities import ACTIVITIES, ACTIVITY_SLUG_MAP, activity_faqs  # noqa: E402
from reviews import (  # noqa: E402
    FACEBOOK_URL,
    TRIPADVISOR_URL,
    aggregate_rating,
    render_review_badge,
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
from group_events import EVENT_EXTERNAL_IMAGES, EVENT_PAGES, EVENT_SLUGS_EN, EVENT_SLUGS_HR  # noqa: E402
from booking_policy import BOOKING_POLICY  # noqa: E402
from brand_voice import (  # noqa: E402
    BOOKING_EMAIL,
    CALL_FOR_GROUPS_ABOVE,
    ONLINE_BOOKING_MAX,
    PHONES,
    VISITOR,
)
from packages import (  # noqa: E402
    PRICES_COPY,
    PRICES_SLUGS,
    BOOKING_SLUGS,
    booking_page_href as booking_href,
    children_pricing_notice,
    conversion_cta_note,
    price_summary,
    prices_offer_schema,
    render_price_sections,
    render_children_pricing_ticker,
    render_large_group_booking_notice,
)
from open_status import park_status  # noqa: E402
from activity_reviews import render_activity_reviews  # noqa: E402
from activity_seo import render_activity_seo_footer  # noqa: E402
from trust_signals import book_cta_labels, render_trust_strip  # noqa: E402
from visitor_gallery import ACTIVITY_GALLERY_MAP, GALLERY_BY_IMAGE, VISITOR_GALLERY  # noqa: E402
from migration_redirects import render_redirect_script, render_redirects_file  # noqa: E402

PRODUCTION_BASE = "https://www.glavanipark.com"
BASE = os.environ.get("SITE_BASE", PRODUCTION_BASE).rstrip("/")
TODAY = date.today().isoformat()


def site_path_from_base() -> str:
    """Path prefix when the site is hosted below a domain root (e.g. /Glavani on GitHub Pages)."""
    from urllib.parse import urlparse

    return urlparse(BASE).path.rstrip("/")


def footer_site_link() -> tuple[str, str]:
    """Footer home link (href, label)."""
    if BASE == PRODUCTION_BASE:
        return f"{PRODUCTION_BASE}/", "www.glavanipark.com"
    host = BASE.replace("https://", "").replace("http://", "")
    return f"{BASE}/", host


def render_site_redirect_script() -> str:
    script = render_redirect_script()
    prefix = site_path_from_base()
    if not prefix:
        return script
    return script.replace("location.replace(target);", f"location.replace('{prefix}' + target);")

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

PAGE_SCRIPTS = {
    "open-status": "/assets/js/open-status.js",
    "photo-gallery": "/assets/js/photo-gallery-carousel.js",
    "prices-book": "/assets/js/prices-book.js",
    "booking-app": "/assets/js/booking-app.js",
    "location-map": "/assets/js/location-map.js",
}


def render_page_scripts(*needs: str) -> str:
    """Emit script tags only for the bundles a page actually uses."""
    seen: set[str] = set()
    lines: list[str] = []
    for key in needs:
        if key in seen:
            continue
        path = PAGE_SCRIPTS.get(key)
        if path:
            seen.add(key)
            lines.append(f'<script src="{path}" defer></script>')
    return "\n".join(lines)

# Reverse map EN slug -> HR slug
EN_TO_HR = {v: k for k, v in SLUG_MAP.items()}
EN_TO_HR.update({v: k for k, v in ACTIVITY_SLUG_MAP.items()})
EN_TO_HR["reservation"] = "rezervacija"
EN_TO_HR["faq"] = "cesta-pitanja"
EN_TO_HR["prices"] = "cijene"

HR_TO_EN = dict(SLUG_MAP)
HR_TO_EN.update(ACTIVITY_SLUG_MAP)
HR_TO_EN["rezervacija"] = "reservation"
HR_TO_EN["cesta-pitanja"] = "faq"
HR_TO_EN["cijene"] = "prices"

IMAGES = [
    ("glavani-park-adventure-istria-croatia.jpg", "Glavani Park", (26, 61, 46), (45, 106, 79)),
    ("12-5m-high-swing-glavani-park-istria.webp", "12.5m High Swing", (234, 88, 12), (180, 83, 9)),
    ("zipline-120m-glavani-park-istria-croatia.webp", "Zipline 120m", (74, 85, 104), (45, 55, 72)),
    ("climbing-wall-outdoor-activities-istria.webp", "Climbing Wall", (64, 145, 108), (26, 61, 46)),
    ("quick-jump-20m-free-fall-istria.webp", "Quick Jump 20m", (124, 58, 237), (76, 29, 149)),
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
    ("ybePV3n9uks", "high-swing-youtube-still.webp"),
    ("TDl0ffqPj3U", "training-route-youtube-still.webp"),
    ("cQpPtOe481I", "valley-zipline-youtube-still.webp", 10 / 7),
]

EXTERNAL_IMAGES = [
    (
        "https://www.glavanipark.com/upload/katalog/2017-9-5_zip_line__most_s_monociklom.JPG",
        "devils-causeway-unicycle-glavani-park.webp",
    ),
    (
        "https://www.glavanipark.com/upload/katalog/68-poklon-bon-400-8173762334.JPG",
        "gift-voucher-50-whole-park.webp",
    ),
    (
        "https://www.glavanipark.com/upload/katalog/2017-8-22_nigel.jpg",
        "nigel-simpson-glavanipark.webp",
    ),
    (
        "https://www.glavanipark.com/upload/katalog/2017-8-22_nevenko.jpg",
        "nevenko-bulic-glavanipark.webp",
    ),
]
EXTERNAL_IMAGES.extend(EVENT_EXTERNAL_IMAGES)
EXTERNAL_IMAGES.extend((item["url"], item["image"]) for item in VISITOR_GALLERY if item.get("url"))
EXTERNAL_IMAGES.extend(
    [
        (
            "https://www.tripadvisor.co.uk/img/cdsi/img2/awards/CoE2017_WidgetAsset-14348-2.png",
            "tripadvisor-certificate-excellence.webp",
        ),
        (
            "https://www.glavanipark.com/images/kroatide.png",
            "kroatide-travel-guide.webp",
        ),
        (
            "https://www.glavanipark.com/images/pitchup_logo.jpg",
            "pitchup-partner.webp",
        ),
    ]
)


def fetch_external_images() -> None:
    """Download and convert catalog images from the live Glavani Park site."""
    import io
    import urllib.request

    img_dir = ROOT / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    for url, filename in EXTERNAL_IMAGES:
        path = img_dir / filename
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = response.read()
            img = Image.open(io.BytesIO(data)).convert("RGB")
            img.save(path, "WEBP", quality=86, method=6)
            print(f"  image: {path.name} (external)")
        except OSError as exc:
            print(f"  warn: could not fetch {filename}: {exc}")


def center_crop_to_aspect(img: Image.Image, aspect: float) -> Image.Image:
    """Crop an image to aspect ratio (width / height), keeping the centre."""
    width, height = img.size
    current_aspect = width / height
    if current_aspect > aspect:
        new_width = int(height * aspect)
        left = (width - new_width) // 2
        return img.crop((left, 0, left + new_width, height))
    if current_aspect < aspect:
        new_height = int(width / aspect)
        top = (height - new_height) // 2
        return img.crop((0, top, width, top + new_height))
    return img


def fetch_youtube_stills() -> None:
    """Download high-quality YouTube thumbnails for activity tiles."""
    import io
    import urllib.request

    img_dir = ROOT / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    for entry in YOUTUBE_STILLS:
        video_id, filename = entry[0], entry[1]
        crop_aspect = entry[2] if len(entry) > 2 else None
        path = img_dir / filename
        for quality in ("maxresdefault", "hqdefault"):
            url = f"https://i.ytimg.com/vi/{video_id}/{quality}.jpg"
            try:
                with urllib.request.urlopen(url, timeout=20) as response:
                    data = response.read()
                if len(data) < 1000:
                    continue
                img = Image.open(io.BytesIO(data)).convert("RGB")
                if crop_aspect:
                    img = center_crop_to_aspect(img, crop_aspect)
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
        query = ""
        if "?" in rest:
            rest, query = rest.split("?", 1)
            query = "?" + query
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
        return f'href="{path}{frag}{query}"'

    html = re.sub(rf'href="/{lang}/([^"]*)"', same_lang_link, html)
    return html


def relativize_root_paths(html: str) -> str:
    """Root-level pages (404.html) — assets and language folders without a leading slash."""
    import re

    html = re.sub(r'(href|src)="/assets/', r'\1="assets/', html)
    html = re.sub(r'(href|src)="/images/', r'\1="images/', html)
    html = html.replace('href="/manifest.webmanifest"', 'href="manifest.webmanifest"')
    html = re.sub(r'href="/(en|hr)/([^"]*)"', r'href="\1/\2"', html)
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
            text = text.replace('url=/en/', 'url=hr/')
            text = text.replace("location.replace('/en/", "location.replace('hr/")
            text = text.replace('href="/en/"', 'href="hr/"')
            html_file.write_text(text, encoding="utf-8")
            continue
        if rel == Path("404.html"):
            text = html_file.read_text(encoding="utf-8")
            html_file.write_text(relativize_root_paths(text), encoding="utf-8")
            continue
        if rel.parts[-1] != "index.html" or rel.parts[0] not in ("en", "hr"):
            continue
        depth = len(rel.parts) - 1
        lang = rel.parts[0]
        text = html_file.read_text(encoding="utf-8")
        html_file.write_text(relativize_paths(text, depth, lang), encoding="utf-8")

    print("  applied relative paths for GitHub Pages compatibility")


def contact_link(
    person: dict,
    *,
    css_class: str = "contact-link",
    show_photo: bool = False,
    image_class: str = "contact-link__photo",
) -> str:
    photo = ""
    if show_photo:
        photo = (
            f'<img class="{image_class}" src="/images/{person["image"]}" '
            f'alt="{person["name"]}" width="36" height="36" loading="lazy">'
        )
    return (
        f'<a class="{css_class}" href="tel:{person["tel"]}">'
        f"{photo}"
        f'<span class="contact-link__text"><strong>{person["name"]}</strong> '
        f'<span class="contact-link__number">{person["display"]}</span></span>'
        f"</a>"
    )


def location_contact_link(lang: str) -> str:
    href = "/hr/sto-raditi-kod-pule/#location-map" if lang == "hr" else "/en/things-to-do-near-pula/#location-map"
    if lang == "hr":
        label = "Lokacija i upute"
        detail = "30 min iz Pule · karta i GPS"
        alt = "Lokacija Glavani Parka"
    else:
        label = "Location & Directions"
        detail = "30 min from Pula · map & GPS"
        alt = "Glavani Park location"
    photo = (
        f'<img class="contact-link__photo" src="/images/glavani-park-adventure-istria-croatia.jpg" '
        f'alt="{alt}" width="36" height="36" loading="lazy">'
    )
    return (
        f'<a class="info-strip__contact" href="{href}">'
        f"{photo}"
        f'<span class="contact-link__text"><strong>{label}</strong> '
        f'<span class="contact-link__number">{detail}</span></span>'
        f"</a>"
    )


def render_info_strip_contacts(lang: str) -> str:
    contacts = "".join(
        f'<div class="info-strip__item info-strip__item--contact">{contact_link(p, css_class="info-strip__contact", show_photo=True)}</div>'
        for p in PHONES
    )
    location = (
        f'<div class="info-strip__item info-strip__item--contact">{location_contact_link(lang)}</div>'
    )
    return contacts + location


def render_home_booking_policy(lang: str) -> str:
    return BOOKING_POLICY[lang]["home_notice"]


def quick_actions(lang: str) -> str:
    book_href = booking_href(lang)
    labels = book_cta_labels(lang)
    if lang == "hr":
        call = "Pozovite"
        find = "Karta"
    else:
        call = "Call"
        find = "Map"
    primary = PHONES[1] if lang == "hr" else PHONES[0]
    return f"""
  <nav class="quick-actions" aria-label="{'Brze radnje' if lang == 'hr' else 'Quick actions'}">
    <a class="btn-book-now" href="{book_href}">
      <span aria-hidden="true">🎟️</span> {labels['book_tickets']}
    </a>
    <a class="btn-call" href="tel:{primary['tel']}" aria-label="{'Pozovite Glavani Park' if lang == 'hr' else 'Call Glavani Park now'}">
      <span aria-hidden="true">📞</span> {call}
    </a>
    <a class="btn-find" href="https://www.google.com/maps?q=45.021389,13.951111" target="_blank" rel="noopener noreferrer">
      <span aria-hidden="true">📍</span> {find}
    </a>
  </nav>"""


def render_visit_cta_bar(lang: str) -> str:
    labels = book_cta_labels(lang)
    status = park_status(lang)
    book_href = booking_href(lang)
    primary = PHONES[1] if lang == "hr" else PHONES[0]
    visit_aria = (
        "Posjetite danas — nazovite za dostupnost"
        if lang == "hr"
        else "Visit today — call for availability"
    )
    aria = "Rezervacija i današnji status" if lang == "hr" else "Book tickets and today's status"
    return f"""
  <div class="visit-cta-bar" aria-label="{aria}">
    <div class="visit-cta-bar__inner">
      <p class="visit-cta-bar__status visitor-bar__status visitor-bar__status--{status['state']}">
        <span class="visitor-bar__icon" aria-hidden="true">●</span>
        <span data-open-status data-lang="{lang}">{status['message']}</span>
      </p>
      <div class="visit-cta-bar__actions">
        <a class="btn-primary btn-primary--xl btn-book-tickets" href="{book_href}">{labels['book_tickets']}</a>
        <a class="btn-visit-today" href="tel:{primary['tel']}" aria-label="{visit_aria}">{labels['visit_today']}</a>
      </div>
    </div>
  </div>"""


def page_chrome(lang: str, *, is_home: bool = False) -> str:
    return f"""{quick_actions(lang)}
{render_visit_cta_bar(lang)}
{site_header(lang)}
{visitor_bar(lang)}
{site_nav(lang, is_home=is_home)}"""


def visitor_bar(lang: str) -> str:
    copy = VISITOR[lang]
    status = park_status(lang)
    return f"""
  <div class="visitor-bar" aria-label="{copy['visitor_bar_aria']}">
    <div class="visitor-bar__inner">
      <p class="visitor-bar__status visitor-bar__status--{status['state']}">
        <span class="visitor-bar__icon" aria-hidden="true">●</span>
        <span data-open-status data-lang="{lang}">{status['message']}</span>
      </p>
      <p class="visitor-bar__hours">
        <span class="visitor-bar__icon" aria-hidden="true">🕐</span>
        <strong>{copy['hours_label']}</strong> {copy['hours']}
      </p>
    </div>
  </div>"""


def site_header(lang: str) -> str:
    copy = VISITOR[lang]
    home = f"/{lang}/"
    return f"""
  <header class="site-header">
    <a class="site-header__brand" href="{home}">
      <img class="site-header__logo-img" src="/images/glavani-park-logo.png" alt="{copy['logo_alt']}" width="200" height="115" loading="eager">
    </a>
    <p class="site-header__tagline">{copy['tagline']}</p>
  </header>"""


def site_nav(lang: str, is_home: bool = False) -> str:
    prefix = f"/{lang}/"
    other = "en" if lang == "hr" else "hr"
    other_label = "English" if lang == "hr" else "Hrvatski"
    if lang == "hr":
        links = [
            ("Aktivnosti", f"{prefix}#activities" if is_home else activities_hub_path(lang)),
            ("Cijene", f"{prefix}{PRICES_SLUGS['hr']}/"),
            ("Lokacija", f"{prefix}sto-raditi-kod-pule/#location-map"),
            ("Grupe", f"{prefix}team-building-istri/"),
            ("Pitanja", f"{prefix}{FAQ_SLUGS['hr']}/"),
            ("Sigurnost", f"{prefix}sigurnost/"),
        ]
        book_label = book_cta_labels("hr")["book_tickets"]
        book_href = booking_href("hr")
    else:
        links = [
            ("Activities", f"{prefix}#activities" if is_home else activities_hub_path(lang)),
            ("Prices", f"{prefix}{PRICES_SLUGS['en']}/"),
            ("Location", f"{prefix}things-to-do-near-pula/#location-map"),
            ("Groups", f"{prefix}team-building-istria/"),
            ("FAQ", f"{prefix}{FAQ_SLUGS['en']}/"),
            ("Safety", f"{prefix}safety/"),
        ]
        book_label = book_cta_labels("en")["book_tickets"]
        book_href = booking_href("en")
    items = "".join(f'<a href="{href}">{label}</a>' for label, href in links)
    return f"""
  <nav class="site-nav" aria-label="{'Glavna navigacija' if lang == 'hr' else 'Main navigation'}">
    <div class="site-nav__inner">
      {items}
      <a class="site-nav__cta" href="{book_href}">{book_label}</a>
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
    footer_href, footer_label = footer_site_link()
    return f"""
{render_trust_strip(lang, in_footer=True)}
  <footer class="site-footer">
    <p>&copy; <time datetime="2026">2026</time> {copy}</p>
    <ul class="site-footer__links">
      <li><a href="{footer_href}">{footer_label}</a></li>
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
    early_head: str = "",
    robots: str = "index, follow",
    body_class: str = "theme-page",
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
{early_head}
  <title>{safe_title}</title>
  <meta name="description" content="{safe_desc}">
  <meta name="keywords" content="{safe_keywords}">
  <meta name="robots" content="{robots}">
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
<body class="{body_class}">"""


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


def site_org_id(lang: str) -> str:
    return f"{BASE}/{lang}/#glavani-park"


def webpage_schema(url: str, name: str, description: str, lang: str) -> dict:
    org = site_org_id(lang)
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": name,
        "description": description,
        "inLanguage": "hr-HR" if lang == "hr" else "en-GB",
        "isPartOf": {"@id": org},
        "about": {"@id": org},
    }


def activity_page_schema(activity: dict, lang: str, url: str) -> list[dict]:
    data = activity[lang]
    org = site_org_id(lang)
    schemas: list[dict] = [
        {
            "@context": "https://schema.org",
            "@type": "TouristAttraction",
            "@id": f"{url}#attraction",
            "name": data["h1"],
            "description": data["meta_description"],
            "url": url,
            "image": f"{BASE}/images/{activity['image']}",
            "isPartOf": {"@id": org},
            "touristType": "Adventure traveler",
        }
    ]
    single_price = activity.get("single_price")
    if single_price:
        book_slug = BOOKING_SLUGS[lang]
        schemas.append(
            {
                "@context": "https://schema.org",
                "@type": "Offer",
                "name": data["h1"],
                "price": str(single_price),
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "url": f"{BASE}/{lang}/{book_slug}/",
                "seller": {"@id": org},
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
        elif path == f"/hr/{BOOKING_SLUGS['hr']}/":
            en_url = f"{BASE}/en/{BOOKING_SLUGS['en']}/"
        else:
            hr_slug = path.replace("/hr/", "").strip("/")
            en_url = f"{BASE}/en/{HR_TO_EN.get(hr_slug, hr_slug)}/"
        return en_url, hr_url
    en_url = loc
    if path == "/en/":
        hr_url = f"{BASE}/hr/"
    elif path == f"/en/{BOOKING_SLUGS['en']}/":
        hr_url = f"{BASE}/hr/{BOOKING_SLUGS['hr']}/"
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
            "<li><strong>Poreč</strong> ~50 min vožnje</li>"
            "<li><strong>Rabac</strong> ~45 min vožnje</li>"
            "<li><strong>Medulin</strong> ~35 min vožnje</li>"
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
            "<li><strong>Poreč</strong> ~50 min drive</li>"
            "<li><strong>Rabac</strong> ~45 min drive</li>"
            "<li><strong>Medulin</strong> ~35 min drive</li>"
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
    map_head = LOCATION_MAP_HEAD if page.get("location_map") else ""
    page_scripts = render_page_scripts(
        "open-status",
        *("location-map",) if page.get("location_map") else (),
    )
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
{page_chrome(lang)}
{crumbs}
<main>
  <section class="hero hero--landing">
    <div class="hero__inner">
      <p class="hero__badge">{page['hero_badge']}</p>
      <h1>{page['h1']}</h1>
      <p class="hero__subtitle">{page['hero_subtitle']}</p>
      <div class="activity-banner__actions">
        <a class="btn-primary" href="{booking_href(lang)}">{book_cta_labels(lang)['book_tickets']}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </div>
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
      <div class="pricing-teaser__actions">
        <a class="btn-primary" href="{booking_href(lang)}">{book_cta_labels(lang)['book_tickets']}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </div>
    </div>
  </section>
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (page['h1'], None)])}
{faq_schema}
{json_ld_script(webpage_schema(canonical, page['h1'], page['meta_description'], lang))}
{page_scripts}
</body>
</html>"""
    return body


SKIP_LANDING_SLUGS = {
    "en": {"adventure-park-croatia"} | EVENT_SLUGS_EN,
    "hr": {"avanturisticki-park-hrvatska"} | EVENT_SLUGS_HR,
}

ACTIVITIES_HUB_SLUGS = {"en": "adventure-park-croatia", "hr": "avanturisticki-park-hrvatska"}

ACTIVITIES_HUB_COPY = {
    "en": {
        "title": "Adventure Park Istria | Zipline & Adrenaline Park Croatia",
        "meta_description": (
            "Glavani Park — adventure park, zipline park and adrenaline park in Istria, Croatia. "
            "Nine outdoor attractions near Pula: training routes, Human Catapult, High Swing, ziplines, Devil's Causeway Course, climbing wall, Aerotrim. Open 9 AM–5 PM."
        ),
        "keywords": (
            "adventure park Istria, zipline park Croatia, adrenaline park Istria, outdoor activities Istria Croatia, "
            "Glavani Park activities, high ropes Pula, forest zipline Istria"
        ),
        "h1": "Our Activities",
        "lead": "Nine signature outdoor attractions — adventure park, zipline courses and adrenaline rides in Istria",
        "intro": (
            "Glavani Park near Barban covers 1.5 hectares of oak forest with nine instructor-led attractions — "
            "from the family yellow training route and 120 m ziplines to the Human Catapult, Devil's Causeway Course, Aerotrim, and 12.5 m high swing. "
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
            "Devet atrakcija na otvorenom kod Pule: trening rute, katapulta, ljuljačka, zipline, Staza Vražjeg puta, penjački zid, Aerotrim. Otvoreno 9–17 h."
        ),
        "keywords": (
            "avanturistički park Istria, zipline park Hrvatska, adrenalinski park Istria, aktivnosti na otvorenom Istria, "
            "Glavani Park aktivnosti, visoke staze Pula, zipline šuma Istria"
        ),
        "h1": "Naše aktivnosti",
        "lead": "Devet atrakcija na otvorenom — avantura, zipline i adrenalin u Istri",
        "intro": (
            "Glavani Park kod Barbana prostire se na 1,5 ha hrastove šume s devet atrakcija pod nadzorom instruktora — "
            "od obiteljske žute trening rute i ziplinea od 120 m do ljudske katapulata, Staze Vražjeg puta, Aerotrima i ljuljačke od 12,5 m. "
            "Otvoreno 9–17 h, otprilike 30 minuta od Pule."
        ),
        "family_link": "obiteljske-aktivnosti-istri",
        "family_label": "Vodič za obiteljske aktivnosti",
        "family_desc": "Žuta staza za djecu, zipline za tinejdžere — planirajte obiteljski dan",
    },
}


def activities_hub_slug(lang: str) -> str:
    return ACTIVITIES_HUB_SLUGS[lang]


def activities_hub_path(lang: str) -> str:
    return f"/{lang}/{activities_hub_slug(lang)}/"


def activity_price_hint(activity: dict, lang: str) -> str:
    single = activity.get("single_price")
    if single:
        return f"€{single}"
    return "€20/€30"


def render_conversion_cta(lang: str, *, compact: bool = False) -> str:
    prefix = f"/{lang}/"
    book_href = booking_href(lang)
    prices_href = f"{prefix}{PRICES_SLUGS[lang]}/"
    labels = book_cta_labels(lang)
    if lang == "hr":
        prices_label = "Pogledajte cijene"
        heading = "" if compact else "<h2 class=\"section-cta__heading\">Spremni za avanturu?</h2>"
    else:
        prices_label = "See Prices"
        heading = "" if compact else "<h2 class=\"section-cta__heading\">Ready for your adventure?</h2>"
    note = conversion_cta_note(lang)
    mod = " section-cta--compact" if compact else ""
    return f"""<div class="section-cta{mod}">
      {heading}
      <p class="section-cta__note">{note}</p>
      <div class="section-cta__actions">
        <a class="btn-primary" href="{book_href}">{labels['book_tickets']}</a>
        <a class="btn-secondary" href="{prices_href}">{prices_label}</a>
      </div>
    </div>"""


def render_home_distances(lang: str) -> str:
    map_href = "/hr/sto-raditi-kod-pule/#location-map" if lang == "hr" else "/en/things-to-do-near-pula/#location-map"
    if lang == "hr":
        aria = "Vrijeme vožnje od popularnih turističkih destinacija"
        lead = "Lako stignete iz Pule, Rovinja, Poreča, Rabca i Medulina"
        map_label = "Karta i upute"
    else:
        aria = "Driving time from popular tourist towns"
        lead = "An easy day trip from Pula, Rovinj, Poreč, Rabac, and Medulin"
        map_label = "Map & directions"
    towns = [
        ("Pula", "30 min"),
        ("Rovinj", "45 min"),
        ("Poreč", "50 min"),
        ("Rabac", "45 min"),
        ("Medulin", "35 min"),
    ]
    chips = "".join(
        f'<li class="distance-chip"><strong>{town}</strong><span>{time}</span></li>'
        for town, time in towns
    )
    return f"""<div class="home-distances">
      <p class="home-distances__lead">{lead}</p>
      <ul class="distance-chips" aria-label="{aria}">
        {chips}
      </ul>
      <p class="home-distances__map"><a href="{map_href}">{map_label}</a></p>
    </div>"""


def render_home_location_section(lang: str) -> str:
    map_href = "/hr/sto-raditi-kod-pule/#location-map" if lang == "hr" else "/en/things-to-do-near-pula/#location-map"
    if lang == "hr":
        heading = "Posjetite nas u Istri"
        sub = "Glavani 10, 52207 Barban · besplatno parkiranje"
        maps = "Otvori u Google Maps"
    else:
        heading = "Visit Us in Istria"
        sub = "Glavani 10, 52207 Barban · free parking on site"
        maps = "Open in Google Maps"
    return f"""<section class="section" aria-labelledby="location-heading" id="location">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="location-heading">{heading}</h2>
          <p>{sub}</p>
        </div>
        {render_home_distances(lang)}
        <p class="home-location__maps">
          <a class="btn-secondary map-link" href="{GLAVANI_MAPS_LINK}" target="_blank" rel="noopener noreferrer">{maps}</a>
          <a class="btn-primary map-link" href="{map_href}">{'Karta i upute' if lang == 'hr' else 'Interactive map'}</a>
        </p>
      </div>
    </section>"""


def render_activity_hub_grid(lang: str, *, compact: bool = False) -> str:
    prefix = f"/{lang}/"
    cards = []
    for act in ACTIVITIES:
        slug = act["hr_slug"] if lang == "hr" else act["en_slug"]
        label = act["hr"]["h1"] if lang == "hr" else act["en"]["h1"]
        mod = act["tile_mod"]
        hint = activity_price_hint(act, lang)
        cards.append(
            f'<a class="hub-card hub-card--{mod}" href="{prefix}{slug}/">'
            f'<h3>{label}</h3>'
            f'<p class="hub-card__price">{hint}</p></a>'
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
            f'<h3>{label}</h3></a>'
        )
    return f"""
    <section class="section section--theme-adrenaline">
      <div class="section__inner">
        <div class="section__heading"><h2>{heading}</h2></div>
        <div class="hub-grid activity-showcase--compact">{''.join(cards)}</div>
        {render_conversion_cta(lang, compact=True)}
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

    family_href = f"{prefix}{copy['family_link']}/"
    family_card = (
        f'<a class="topic-link" href="{family_href}">{copy["family_label"]}'
        f'<span>{copy["family_desc"]}</span></a>'
    )

    return f"""{head_meta(lang, copy['title'], copy['meta_description'], copy['keywords'], canonical, en_slug, hr_slug)}
{page_chrome(lang)}
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
      {render_conversion_cta(lang)}
      <div class="activities-hub-packages">
        <div class="section__heading">
          <h2>{PRICES_COPY[lang]['h1']}</h2>
          <p>{PRICES_COPY[lang]['lead']}</p>
        </div>
        {render_children_pricing_ticker(lang)}
        {render_large_group_booking_notice(lang)}
        {render_price_sections(lang)}
        <p class="activities-hub-packages__note">{PRICES_COPY[lang]['book_note']}</p>
      </div>
      <div class="topic-grid" style="margin-top:1.5rem;max-width:760px;margin-left:auto;margin-right:auto;">
        {family_card}
      </div>
    </div>
  </section>
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (copy['h1'], None)])}
{json_ld_script(webpage_schema(canonical, copy['h1'], copy['meta_description'], lang))}
{json_ld_script(activities_hub_itemlist_schema(lang, canonical))}
{render_page_scripts("open-status", "prices-book")}
</body>
</html>"""


def inject_after_nth_paragraph(html: str, insert: str, count: int = 2) -> str:
    """Insert HTML after the nth closing </p> tag."""
    if not insert or count < 1:
        return html
    pos = 0
    found = 0
    lower = html.lower()
    while found < count:
        idx = lower.find("</p>", pos)
        if idx == -1:
            return html + insert
        found += 1
        pos = idx + 4
    return html[:pos] + insert + html[pos:]


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
    notice = data.get("video_notice")
    notice_html = (
        f'<p class="activity-video__notice">{notice}</p>' if notice else ""
    )
    return f"""
        <div class="activity-video__slot" data-activity-video="{activity['en_slug']}">
          <iframe
            src="https://www.youtube.com/embed/{video_id}"
            title="{title}"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
            loading="lazy"
            referrerpolicy="strict-origin-when-cross-origin"></iframe>
        </div>{notice_html}
        <p class="activity-video__youtube-link">
          <a href="{youtube_url}" target="_blank" rel="noopener noreferrer">{watch_label}</a>
        </p>"""


def render_activity_video_section(activity: dict, data: dict, lang: str) -> str:
    if activity.get("hide_video"):
        return ""
    return f"""
      <section class="activity-video activity-video--inline" aria-labelledby="activity-video-heading">
        <h2 id="activity-video-heading">{data['video_heading']}</h2>
        {render_activity_video(activity, data, lang)}
      </section>"""


def render_activity_page(activity: dict, lang: str) -> str:
    data = activity["hr" if lang == "hr" else "en"]
    en_slug = activity["en_slug"]
    hr_slug = activity["hr_slug"]
    slug = hr_slug if lang == "hr" else en_slug
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    activities_label = "Aktivnosti" if lang == "hr" else "Activities"
    book_label = book_cta_labels(lang)["book_tickets"]
    book_href = booking_href(lang)
    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"
    img = activity["image"]
    mod = activity["tile_mod"]
    use_banner_header = bool(activity.get("youtube_id"))

    activities_href = activities_hub_path(lang)
    activities_url = f"{BASE}{activities_href}"

    prose = render_prose_blocks(data["paragraphs"])
    video_section = render_activity_video_section(activity, data, lang)
    if video_section:
        prose = inject_after_nth_paragraph(prose, video_section, count=2)
    prose += render_activity_seo_footer(activity, lang)
    prices_href = f"{prefix}{PRICES_SLUGS[lang]}/"
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
    else:
        hint = activity_price_hint(activity, lang)
        included = (
            "Uključeno u pakete parka"
            if lang == "hr"
            else "Included in park packages"
        )
        price_html = (
            f'\n        <p class="activity-banner__price">{hint} · {included}</p>'
        )

    banner_actions = f"""
        <div class="activity-banner__actions">
          <a class="btn-primary" href="{book_href}">{book_label}</a>
          <a class="btn-secondary" href="{prices_href}">{prices_label}</a>
        </div>"""

    feature_img = f"""      <figure class="feature-img">
        <img src="/images/{img}" alt="{data['image_alt']}" width="800" height="560" loading="eager">
      </figure>"""

    if use_banner_header:
        page_header = ""
        article_open = f"""      <header class="activity-banner activity-banner--{mod}" aria-labelledby="activity-heading">
        <p class="activity-banner__badge">{data['hero_badge']}</p>
        <h1 id="activity-heading">{data['h1']}</h1>{price_html}{banner_actions}
      </header>"""
        if activity.get("feature_image"):
            article_open += f"\n{feature_img}"
    else:
        page_header = f"""  <section class="hero hero--landing hero--activity">
    <div class="hero__inner">
      <p class="hero__badge">{data['hero_badge']}</p>
      <h1>{data['h1']}</h1>{price_html}
      <div class="activity-banner__actions">
        <a class="btn-primary" href="{book_href}">{book_label}</a>
        <a class="btn-secondary" href="{prices_href}">{prices_label}</a>
      </div>
    </div>
  </section>"""
        article_open = feature_img

    inline_cta = render_conversion_cta(lang, compact=True)
    review_teaser = render_activity_reviews(activity, lang)
    visitor_photos = render_activity_visitor_photos(activity, lang)
    page_scripts = render_page_scripts(
        "open-status",
        *("photo-gallery",) if visitor_photos else (),
    )

    return f"""{head_meta(lang, data['title'], data['meta_description'], data['keywords'], canonical, en_slug, hr_slug, og_image=img, og_image_alt=data['image_alt'])}
{page_chrome(lang)}
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
      {inline_cta}
      {review_teaser}
      {visitor_photos}
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
{page_scripts}
</body>
</html>"""


def render_photo_gallery(event: dict, lang: str) -> str:
    data = event["hr" if lang == "hr" else "en"]
    alt_key = "hr_alt" if lang == "hr" else "en_alt"
    prev_label = "Prethodna fotografija" if lang == "hr" else "Previous photo"
    next_label = "Sljedeća fotografija" if lang == "hr" else "Next photo"
    slides = []
    for item in event["gallery"]:
        alt = esc(item[alt_key])
        slides.append(
            f"""        <figure class="photo-gallery__slide">
          <img src="/images/{item['image']}" alt="{alt}" width="800" height="560" loading="lazy">
        </figure>"""
        )
    return f"""
  <section class="section section--alt photo-gallery-section" aria-labelledby="photo-gallery-heading">
    <div class="section__inner">
      <div class="section__heading">
        <h2 id="photo-gallery-heading">{data['gallery_heading']}</h2>
      </div>
      <div class="photo-gallery" data-photo-gallery>
        <button type="button" class="photo-gallery__nav photo-gallery__nav--prev" aria-label="{prev_label}" data-gallery-prev>‹</button>
        <div class="photo-gallery__track" tabindex="0" data-gallery-track>
{chr(10).join(slides)}
        </div>
        <button type="button" class="photo-gallery__nav photo-gallery__nav--next" aria-label="{next_label}" data-gallery-next>›</button>
      </div>
    </div>
  </section>"""


def render_event_page(event: dict, lang: str) -> str:
    data = event["hr" if lang == "hr" else "en"]
    en_slug = event["en_slug"]
    hr_slug = event["hr_slug"]
    slug = hr_slug if lang == "hr" else en_slug
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    book_label = "Rezervirajte" if lang == "hr" else "Book Your Visit"
    book_href = booking_href(lang)
    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"
    img = event["image"]

    prose = "".join(f"<p>{p}</p>" for p in data["paragraphs"])
    prices_href = f"{prefix}prices/" if lang == "en" else f"{prefix}cijene/"
    prices_label = "Packages &amp; prices" if lang == "en" else "Paketi i cijene"
    prose += (
        f'<p><a href="{book_href}">{book_label}</a> · '
        f'<a href="{prices_href}">{prices_label}</a></p>'
    )

    page_faqs = data.get("faqs") or []
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
            build_faq_schema(page_faqs, lang, url=canonical, name=data["h1"], description=data["meta_description"])
        )

    gallery_block = render_photo_gallery(event, lang)
    has_gallery = bool(event.get("gallery"))
    page_scripts = render_page_scripts(
        "open-status",
        *("photo-gallery",) if has_gallery else (),
    )

    return f"""{head_meta(lang, data['title'], data['meta_description'], data['keywords'], canonical, en_slug, hr_slug, og_image=img, og_image_alt=data['image_alt'])}
{page_chrome(lang)}
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li>{data['h1']}</li>
    </ol>
  </nav>
<main>
  <section class="hero hero--landing hero--activity">
    <div class="hero__inner">
      <p class="hero__badge">{data['hero_badge']}</p>
      <h1>{data['h1']}</h1>
      <div class="activity-banner__actions">
        <a class="btn-primary" href="{book_href}">{book_cta_labels(lang)['book_tickets']}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </div>
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
      <div class="activity-detail__actions">
        <a class="btn-primary" href="{book_href}">{book_cta_labels(lang)['book_tickets']}</a>
        <a class="btn-secondary" href="tel:+385918964525">{cta}</a>
      </div>
    </article>
  </div>
  {gallery_block}
  {render_related(data.get('related', []), lang)}
  {faq_block}
</main>
{footer(lang)}
{breadcrumb_schema([(home_label, f"{BASE}{prefix}"), (data['h1'], None)])}
{faq_schema}
{json_ld_script(webpage_schema(canonical, data['h1'], data['meta_description'], lang))}
{page_scripts}
</body>
</html>"""


def render_activity_visitor_photos(activity: dict, lang: str) -> str:
    alt_key = "hr_alt" if lang == "hr" else "en_alt"
    en_slug = activity["en_slug"]
    data = activity[lang]
    image_names = ACTIVITY_GALLERY_MAP.get(en_slug, [])
    if lang == "hr":
        heading = f"Fotografije posjetitelja — {data['h1']}"
        prev_label = "Prethodna fotografija"
        next_label = "Sljedeća fotografija"
    else:
        heading = f"Visitor photos — {data['h1']}"
        prev_label = "Previous photo"
        next_label = "Next photo"
    slides = []
    for image_name in image_names:
        item = GALLERY_BY_IMAGE.get(image_name)
        if not item:
            continue
        alt = esc(item[alt_key])
        slides.append(
            f"""        <figure class="photo-gallery__slide">
          <img src="/images/{image_name}" alt="{alt}" width="800" height="560" loading="lazy">
        </figure>"""
        )
    if not slides:
        return ""
    return f"""<section class="visitor-photos" aria-label="{heading}">
      <h2 class="visitor-photos__heading">{heading}</h2>
      <div class="photo-gallery" data-photo-gallery>
        <button type="button" class="photo-gallery__nav photo-gallery__nav--prev" aria-label="{prev_label}" data-gallery-prev>‹</button>
        <div class="photo-gallery__track" tabindex="0" data-gallery-track>
{chr(10).join(slides)}
        </div>
        <button type="button" class="photo-gallery__nav photo-gallery__nav--next" aria-label="{next_label}" data-gallery-next>›</button>
      </div>
    </section>"""


def render_prose_blocks(paragraphs: list[str]) -> str:
    parts = []
    for block in paragraphs:
        text = block.strip()
        if text.startswith("<"):
            parts.append(text)
        else:
            parts.append(f"<p>{text}</p>")
    return "".join(parts)


def render_activity_hub_cards(lang: str) -> str:
    prefix = f"/{lang}/"
    cards = []
    for act in ACTIVITIES:
        slug = act["hr_slug"] if lang == "hr" else act["en_slug"]
        label = act["hr"]["h1"] if lang == "hr" else act["en"]["h1"]
        mod = act["tile_mod"]
        hint = activity_price_hint(act, lang)
        cards.append(
            f'<a class="hub-card hub-card--{mod}" href="{prefix}{slug}/">'
            f'<h3>{label}</h3>'
            f'<p class="hub-card__price">{hint}</p></a>'
        )
    return "".join(cards)


def inject_home_extras(body: str, lang: str) -> str:
    summary = price_summary(lang)
    status = park_status(lang)
    replacements = {
        "<!-- HERO_OPEN_STATUS -->": (
            f'<span class="hero__open-status-row visitor-bar__status visitor-bar__status--{status["state"]}">'
            f'<span class="visitor-bar__icon" aria-hidden="true">●</span>'
            f'<span class="hero__open-status hero__open-status--{status["state"]}" '
            f'data-open-status data-lang="{lang}">{status["message"]}</span>'
            f"</span>"
        ),
        "<!-- HERO_REVIEW_BADGE -->": render_review_badge(lang),
        "<!-- HERO_PRICE_TEASER -->": (
            f'<p class="hero__price-teaser">{summary["hero_line"]} · '
            f'<a href="/{lang}/{PRICES_SLUGS[lang]}/">'
            f'{"Pogledajte cijene" if lang == "hr" else "See prices"}</a></p>'
        ),
        "<!-- ACTIVITY_HUB_GRID -->": render_activity_hub_cards(lang),
        "<!-- ACTIVITIES_CTA -->": render_conversion_cta(lang),
    }
    for marker, html in replacements.items():
        body = body.replace(marker, html)
    return body


def home_body_en() -> str:
    """English homepage main content (abbreviated structure with full SEO sections)."""
    body = open(ROOT / "scripts" / "home_en.html").read()
    body = body.replace("<!-- HOME_BOOKING_POLICY -->", render_home_booking_policy("en"))
    body = body.replace("<!-- INFO_STRIP_CONTACTS -->", render_info_strip_contacts("en"))
    return inject_home_extras(body, "en")


def home_body_hr() -> str:
    body = open(ROOT / "scripts" / "home_hr.html").read()
    body = body.replace("<!-- HOME_BOOKING_POLICY -->", render_home_booking_policy("hr"))
    body = body.replace("<!-- INFO_STRIP_CONTACTS -->", render_info_strip_contacts("hr"))
    return inject_home_extras(body, "hr")


def render_faq_page(lang: str) -> str:
    copy = FAQ_COPY[lang]
    slug = FAQ_SLUGS[lang]
    en_slug = FAQ_SLUGS["en"]
    hr_slug = FAQ_SLUGS["hr"]
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    book_href = booking_href(lang)
    book_label = "Rezervirajte posjet" if lang == "hr" else "Book Your Visit"
    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"

    return f"""{head_meta(lang, copy['title'], copy['meta_description'], copy['keywords'], canonical, en_slug, hr_slug)}
{page_chrome(lang)}
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
{render_page_scripts("open-status")}
</body>
</html>"""


NOT_FOUND_COPY = {
    "en": {
        "title": "Page Not Found | Glavani Park Istria",
        "description": (
            "This page could not be found. Browse Glavani Park prices, book tickets online, "
            "see our attractions, or check opening hours — Croatia's number 1 adventure park in Istria."
        ),
        "keywords": "Glavani Park, page not found, adventure park Istria, book tickets",
        "badge": "404",
        "h1": "We couldn't find that page",
        "lead": (
            "Don't worry — you're still at Glavani Park. "
            "Here are the pages visitors look for most:"
        ),
        "home": "Back to Home",
        "prices_title": "Looking for Prices?",
        "prices_desc": "Packages from €20 children / €30 adults · family deals from €150",
        "book_title": "Book Now",
        "book_desc": f"Reserve online for up to {ONLINE_BOOKING_MAX} people — or call for larger groups",
        "activities_title": "Attractions",
        "activities_desc": "Human catapult, ziplines, high swing, climbing wall & more",
        "hours_title": "Opening Hours",
        "hours_line": "Open daily 9 AM – 5 PM",
        "hours_entry": "Last entry 3 PM",
        "hours_link": "Visit info & FAQ",
        "cta_heading": "Still planning your visit?",
        "cta_note": "Call or book online — we're in the Istrian countryside, 30 minutes from Pula.",
    },
    "hr": {
        "title": "Stranica nije pronađena | Glavani Park Istria",
        "description": (
            "Ova stranica nije pronađena. Pogledajte cijene Glavani Parka, rezervirajte ulaznice online, "
            "pogledajte atrakcije ili radno vrijeme — broj 1 avanturistički park u Istri."
        ),
        "keywords": "Glavani Park, stranica nije pronađena, avanturistički park Istria, rezervacija",
        "badge": "404",
        "h1": "Nismo pronašli tu stranicu",
        "lead": (
            "Bez brige — još ste na Glavani Parku. "
            "Evo stranica koje posjetitelji najčešće traže:"
        ),
        "home": "Natrag na početnu",
        "prices_title": "Tražite cijene?",
        "prices_desc": "Paketi od €20 djeca / €30 odrasli · obiteljski paketi od €150",
        "book_title": "Rezervirajte sada",
        "book_desc": f"Online do {ONLINE_BOOKING_MAX} osoba — ili nazovite za veće grupe",
        "activities_title": "Atrakcije",
        "activities_desc": "Ljudska katapulta, zipline, visoka ljuljačka, penjački zid i više",
        "hours_title": "Radno vrijeme",
        "hours_line": "Otvoreno svaki dan 9–17 h",
        "hours_entry": "Posljednji ulaz 15 h",
        "hours_link": "Informacije za posjet & FAQ",
        "cta_heading": "Još planirate posjet?",
        "cta_note": "Nazovite ili rezervirajte online — u istarskom krajoliku, 30 minuta od Pule.",
    },
}


def not_found_bilingual(text_en: str, text_hr: str, *, block: bool = False) -> str:
    block_class = " block" if block else ""
    return (
        f'<span class="lang-en{block_class}" lang="en">{esc(text_en)}</span>'
        f'<span class="lang-hr{block_class}" lang="hr">{esc(text_hr)}</span>'
    )


def not_found_link(en_href: str, hr_href: str, inner: str, modifier: str = "") -> str:
    mod = f" not-found-card--{modifier}" if modifier else ""
    return (
        f'<a class="not-found-card{mod}" href="{en_href}" '
        f'data-en-href="{en_href}" data-hr-href="{hr_href}">{inner}</a>'
    )


def render_404_page() -> str:
    en = NOT_FOUND_COPY["en"]
    hr = NOT_FOUND_COPY["hr"]
    canonical = f"{BASE}/en/"
    status = park_status("en")
    status_hr = park_status("hr")
    en_prices = f"/en/{PRICES_SLUGS['en']}/"
    hr_prices = f"/hr/{PRICES_SLUGS['hr']}/"
    en_book = booking_href("en")
    hr_book = booking_href("hr")
    en_activities = activities_hub_path("en")
    hr_activities = activities_hub_path("hr")
    en_faq = f"/en/{FAQ_SLUGS['en']}/"
    hr_faq = f"/hr/{FAQ_SLUGS['hr']}/"
    en_home = "/en/"
    hr_home = "/hr/"
    phone_en = PHONES[0]
    phone_hr = PHONES[1]

    return f"""{head_meta("en", en["title"], en["description"], en["keywords"], canonical, is_home=True, robots="noindex, follow", body_class="theme-page page-404", early_head=render_site_redirect_script())}
{quick_actions("en")}
  <div class="visit-cta-bar" aria-label="Book tickets and today's status">
    <div class="visit-cta-bar__inner">
      <p class="visit-cta-bar__status visitor-bar__status visitor-bar__status--{status['state']}">
        <span class="visitor-bar__icon" aria-hidden="true">●</span>
        <span data-open-status data-lang="en" class="lang-en">{status['message']}</span>
        <span data-open-status data-lang="hr" class="lang-hr">{status_hr['message']}</span>
      </p>
      <div class="visit-cta-bar__actions">
        <a class="btn-primary btn-primary--xl btn-book-tickets not-found-link" href="{en_book}" data-en-href="{en_book}" data-hr-href="{hr_book}">
          <span class="lang-en">{book_cta_labels('en')['book_tickets']}</span>
          <span class="lang-hr">{book_cta_labels('hr')['book_tickets']}</span>
        </a>
        <a class="btn-visit-today not-found-link" href="tel:{phone_en['tel']}" data-en-href="tel:{phone_en['tel']}" data-hr-href="tel:{phone_hr['tel']}">
          <span class="lang-en">{book_cta_labels('en')['visit_today']}</span>
          <span class="lang-hr">{book_cta_labels('hr')['visit_today']}</span>
        </a>
      </div>
    </div>
  </div>
{site_header("en")}
{visitor_bar("en")}
{site_nav("en")}
<main class="page-404">
  <section class="hero hero--landing hero--404">
    <div class="hero__inner">
      <p class="hero__badge">404</p>
      <h1>{not_found_bilingual(en['h1'], hr['h1'], block=True)}</h1>
      <p class="hero__subtitle">{not_found_bilingual(en['lead'], hr['lead'], block=True)}</p>
      <p class="page-404__home">
        <a class="btn-secondary not-found-link" href="{en_home}" data-en-href="{en_home}" data-hr-href="{hr_home}">
          {not_found_bilingual(en['home'], hr['home'])}
        </a>
      </p>
    </div>
  </section>
  <section class="section section--theme-forest" aria-labelledby="not-found-help-heading">
    <div class="section__inner">
      <h2 id="not-found-help-heading" class="visually-hidden">
        {not_found_bilingual("Helpful links", "Korisne poveznice")}
      </h2>
      <div class="not-found-grid">
        {not_found_link(
            en_prices,
            hr_prices,
            f'<span class="not-found-card__icon" aria-hidden="true">€</span>'
            f"<h3>{not_found_bilingual(en['prices_title'], hr['prices_title'], block=True)}</h3>"
            f'<p>{not_found_bilingual(en["prices_desc"], hr["prices_desc"], block=True)}</p>',
            "prices",
        )}
        {not_found_link(
            en_book,
            hr_book,
            f'<span class="not-found-card__icon" aria-hidden="true">🎟️</span>'
            f"<h3>{not_found_bilingual(en['book_title'], hr['book_title'], block=True)}</h3>"
            f'<p>{not_found_bilingual(en["book_desc"], hr["book_desc"], block=True)}</p>',
            "book",
        )}
        {not_found_link(
            en_activities,
            hr_activities,
            f'<span class="not-found-card__icon" aria-hidden="true">🎯</span>'
            f"<h3>{not_found_bilingual(en['activities_title'], hr['activities_title'], block=True)}</h3>"
            f'<p>{not_found_bilingual(en["activities_desc"], hr["activities_desc"], block=True)}</p>',
            "activities",
        )}
        <article class="not-found-card not-found-card--hours">
          <span class="not-found-card__icon" aria-hidden="true">🕐</span>
          <h3>{not_found_bilingual(en['hours_title'], hr['hours_title'], block=True)}</h3>
          <p>
            <strong>{not_found_bilingual(en['hours_line'], hr['hours_line'], block=True)}</strong>
            <span class="not-found-card__hours-break" aria-hidden="true"><br></span>
            {not_found_bilingual(en['hours_entry'], hr['hours_entry'], block=True)}
          </p>
          <a class="not-found-card__link not-found-link" href="{en_faq}" data-en-href="{en_faq}" data-hr-href="{hr_faq}">
            {not_found_bilingual(en['hours_link'], hr['hours_link'])}
          </a>
        </article>
      </div>
      <div class="section-cta section-cta--compact">
        <h2 class="section-cta__heading">{not_found_bilingual(en['cta_heading'], hr['cta_heading'])}</h2>
        <p class="section-cta__note">{not_found_bilingual(en['cta_note'], hr['cta_note'])}</p>
        <div class="section-cta__actions">
          <a class="btn-primary not-found-link" href="{en_book}" data-en-href="{en_book}" data-hr-href="{hr_book}">
            <span class="lang-en">{book_cta_labels('en')['book_tickets']}</span>
            <span class="lang-hr">{book_cta_labels('hr')['book_tickets']}</span>
          </a>
          <a class="btn-secondary not-found-link" href="{en_prices}" data-en-href="{en_prices}" data-hr-href="{hr_prices}">
            <span class="lang-en">See Prices</span>
            <span class="lang-hr">Pogledajte cijene</span>
          </a>
          <a class="btn-secondary not-found-link" href="tel:{phone_en['tel']}" data-en-href="tel:{phone_en['tel']}" data-hr-href="tel:{phone_hr['tel']}">
            <span class="lang-en">Call {phone_en['display']}</span>
            <span class="lang-hr">Pozovite {phone_hr['display']}</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</main>
{footer("en")}
<script>
(function () {{
  var hr = /\\/hr(\\/|$)/.test(location.pathname);
  if (hr) document.body.classList.add('is-hr');
  document.documentElement.lang = hr ? 'hr' : 'en';
  document.querySelectorAll('.not-found-link[data-en-href]').forEach(function (el) {{
    el.setAttribute('href', hr ? el.getAttribute('data-hr-href') : el.getAttribute('data-en-href'));
  }});
  document.querySelectorAll('[data-open-status]').forEach(function (el) {{
    el.hidden = el.classList.contains(hr ? 'lang-en' : 'lang-hr');
  }});
}})();
</script>
{render_page_scripts("open-status")}
</body>
</html>"""


def build_404() -> None:
    write_file(ROOT / "404.html", render_404_page())


def render_prices_page(lang: str) -> str:
    copy = PRICES_COPY[lang]
    slug = PRICES_SLUGS[lang]
    en_slug = PRICES_SLUGS["en"]
    hr_slug = PRICES_SLUGS["hr"]
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    book_href = booking_href(lang)
    book_label = "Rezervirajte posjet" if lang == "hr" else "Book Your Visit"
    cta = "Pozovite za rezervaciju" if lang == "hr" else "Call to Book"

    return f"""{head_meta(lang, copy['title'], copy['meta_description'], copy['keywords'], canonical, en_slug, hr_slug)}
{page_chrome(lang)}
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li>{copy['h1']}</li>
    </ol>
  </nav>
<main>
  <section class="hero hero--landing">
    <div class="hero__inner">
      <p class="hero__badge">{'Online do ' + str(ONLINE_BOOKING_MAX) + ' osoba · nazovite za ' + str(CALL_FOR_GROUPS_ABOVE + 1) + '+' if lang == 'hr' else f'Book online · up to {ONLINE_BOOKING_MAX} · call for {CALL_FOR_GROUPS_ABOVE + 1}+'}</p>
      <h1>{copy['h1']}</h1>
      <p class="hero__subtitle">{copy['lead']}</p>
    </div>
  </section>
  <section class="section section--theme-forest">
    <div class="section__inner">
      {render_children_pricing_ticker(lang)}
      {render_large_group_booking_notice(lang)}
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
{render_page_scripts("open-status", "prices-book")}
</body>
</html>"""


def render_booking_app(lang: str) -> str:
    slug = BOOKING_SLUGS[lang]
    en_slug = BOOKING_SLUGS["en"]
    hr_slug = BOOKING_SLUGS["hr"]
    if lang == "hr":
        title = "Rezerviraj | Glavani Park – odaberite paket i datum"
        desc = (
            f"Rezervirajte Glavani Park online za do {ONLINE_BOOKING_MAX} osoba. "
            f"Odaberite paket i datum, zatim otvorite e-mail s popunjenim detaljima i pošaljite na {BOOKING_EMAIL}. "
            f"Za grupe s više od {ONLINE_BOOKING_MAX} osoba ili posjet u sljedećih par dana, nazovite."
        )
        h1 = "Rezerviraj"
        lead = (
            "Odaberite paket, datum i svoje podatke — zatim otvorite e-mail aplikaciju s popunjenom rezervacijom "
            "i pošaljite je na info@glavanipark.com. Potvrdu nastojimo poslati u roku od 24 sata."
        )
        amenities = (
            "<strong>Plaćanje:</strong> kartice i gotovina u parku. "
            "<strong>U parku:</strong> osvježenja i sladoled."
        )
        policy = BOOKING_POLICY["hr"]["book_page"]
    else:
        title = "Book | Glavani Park – Pick Package & Date"
        desc = (
            f"Book Glavani Park online for up to {ONLINE_BOOKING_MAX} people. "
            f"Pick your package and date, then open a prefilled email to {BOOKING_EMAIL} to send your booking. "
            f"For parties of more than {ONLINE_BOOKING_MAX} or visits in the next couple of days, please call."
        )
        h1 = "Book"
        lead = (
            "Choose your package, date, and details — then open your email app with your booking filled in "
            "and send it to info@glavanipark.com. We aim to reply with confirmation within 24 hours."
        )
        amenities = (
            "<strong>Payment:</strong> card and cash accepted at the park. "
            "<strong>On site:</strong> refreshments and ice cream available."
        )
        policy = BOOKING_POLICY["en"]["book_page"]
    prefix = f"/{lang}/"
    canonical = f"{BASE}{prefix}{slug}/"
    home_label = "Početna" if lang == "hr" else "Home"
    extra = (
        '  <link rel="manifest" href="/manifest.webmanifest">\n'
        '  <meta name="theme-color" content="#0a0a0a">\n'
        '  <meta name="apple-mobile-web-app-capable" content="yes">'
    )
    return f"""{head_meta(lang, title, desc, "book glavani park, reservation istria", canonical, en_slug, hr_slug, extra_head=extra)}
{page_chrome(lang)}
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol><li><a href="{prefix}">{home_label}</a></li><li>{h1}</li></ol>
</nav>
<div class="book-app-hero">
  <h1>{h1}</h1>
  <p>{lead}</p>
  <p class="book-app-notice">{amenities}</p>
</div>
<div class="book-app-wrap">
  <script type="application/json" id="booking-app-config">{json.dumps({"lang": lang, "recipientEmail": BOOKING_EMAIL, "maxGuests": ONLINE_BOOKING_MAX, "callAbove": CALL_FOR_GROUPS_ABOVE})}</script>
  <div id="booking-app" aria-live="polite"></div>
  <p class="book-app-notice book-app-notice--children">{children_pricing_notice(lang, for_booking=True)}</p>
  <p class="book-app-notice book-app-notice--policy">{policy}</p>
</div>
{footer(lang)}
{render_page_scripts("open-status", "booking-app")}
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
{page_chrome(lang, is_home=True)}
{body_content}
{footer(lang)}
{json_ld_script(org_schema)}
{render_page_scripts("open-status")}
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
Disallow: /upload/

Sitemap: {BASE}/sitemap.xml
"""
    write_file(ROOT / "robots.txt", content)


def build_redirects() -> None:
    write_file(ROOT / "_redirects", render_redirects_file())


def build_root_redirect() -> None:
    content = f"""<!DOCTYPE html>
<html lang="hr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=hr/">
  <meta name="description" content="Glavani Park — avanturistički i zipline park u Istri, Hrvatska kod Pule.">
  <link rel="canonical" href="{BASE}/hr/">
  <link rel="alternate" hreflang="en" href="{BASE}/en/">
  <link rel="alternate" hreflang="hr" href="{BASE}/hr/">
  <link rel="alternate" hreflang="x-default" href="{BASE}/en/">
  <title>Glavani Park | Avanturistički park Istria, Hrvatska</title>
  <script>location.replace('hr/');</script>
</head>
<body><p><a href="hr/">Glavani Park – Avanturistički park Istria</a></p></body>
</html>"""
    write_file(ROOT / "index.html", content)


def main() -> None:
    print("Fetching TripAdvisor reviews...")
    from fetch_reviews import main as fetch_reviews_main

    fetch_reviews_main()
    reset_cache()

    print("Generating WebP/JPEG images...")
    generate_images()
    fetch_youtube_stills()
    fetch_external_images()

    print("Building English pages...")
    import shutil

    en_booking = BOOKING_SLUGS["en"]
    hr_booking = BOOKING_SLUGS["hr"]
    old_en_book = ROOT / "en" / "book"
    if old_en_book.exists():
        shutil.rmtree(old_en_book)

    write_file(ROOT / "en" / "index.html", render_home("en"))
    write_file(ROOT / "en" / en_booking / "index.html", render_booking_app("en"))
    write_file(ROOT / "en" / PRICES_SLUGS["en"] / "index.html", render_prices_page("en"))
    write_file(ROOT / "en" / FAQ_SLUGS["en"] / "index.html", render_faq_page("en"))
    sitemap_urls = [(f"{BASE}/en/", "weekly"), (f"{BASE}/en/{en_booking}/", "weekly")]
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
    for event in EVENT_PAGES:
        write_file(ROOT / "en" / event["en_slug"] / "index.html", render_event_page(event, "en"))
        sitemap_urls.append((f"{BASE}/en/{event['en_slug']}/", "monthly"))

    print("Building Croatian pages...")
    write_file(ROOT / "hr" / "index.html", render_home("hr"))
    write_file(ROOT / "hr" / hr_booking / "index.html", render_booking_app("hr"))
    write_file(ROOT / "hr" / PRICES_SLUGS["hr"] / "index.html", render_prices_page("hr"))
    write_file(ROOT / "hr" / FAQ_SLUGS["hr"] / "index.html", render_faq_page("hr"))
    sitemap_urls.append((f"{BASE}/hr/", "weekly"))
    sitemap_urls.append((f"{BASE}/hr/{hr_booking}/", "weekly"))
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
    for event in EVENT_PAGES:
        write_file(ROOT / "hr" / event["hr_slug"] / "index.html", render_event_page(event, "hr"))
        sitemap_urls.append((f"{BASE}/hr/{event['hr_slug']}/", "monthly"))

    print("Writing robots.txt, sitemap.xml, and migration redirects...")
    build_robots()
    build_sitemap(sitemap_urls)
    build_redirects()
    build_root_redirect()
    build_404()
    relativize_site()
    print("Done.")


if __name__ == "__main__":
    main()
