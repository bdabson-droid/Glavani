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

BASE = "https://www.glavanipark.com"
TODAY = date.today().isoformat()
# Set PATH_PREFIX=/Glavani when deploying to GitHub Pages (project sites)
PATH_PREFIX = os.environ.get("PATH_PREFIX", "").rstrip("/")

# Reverse map EN slug -> HR slug
EN_TO_HR = {v: k for k, v in SLUG_MAP.items()}
EN_TO_HR.update({v: k for k, v in ACTIVITY_SLUG_MAP.items()})
EN_TO_HR["book"] = "rezervacija"

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


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def u(path: str) -> str:
    """Prefix root-absolute paths (for GitHub Pages subdirectory deploy)."""
    if path.startswith("/") and PATH_PREFIX:
        return f"{PATH_PREFIX}{path}"
    return path


def apply_path_prefix() -> None:
    """Rewrite root-absolute paths in HTML and CSS when PATH_PREFIX is set."""
    if not PATH_PREFIX:
        return
    import re
    prefix = PATH_PREFIX
    for html_file in ROOT.rglob("*.html"):
        if "scripts" in html_file.parts:
            continue
        text = html_file.read_text(encoding="utf-8")
        text = text.replace(f"{prefix}{prefix}", prefix)
        text = re.sub(r'(href|src|content="0; url=)="/', rf'\1="{prefix}/', text)
        text = text.replace(f"location.replace('/", f"location.replace('{prefix}/")
        html_file.write_text(text, encoding="utf-8")

    css_path = ROOT / "assets" / "css" / "site.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        css = css.replace(f'url("{prefix}{prefix}/', f'url("{prefix}/')
        css = re.sub(r'url\("/', rf'url("{prefix}/', css)
        css_path.write_text(css, encoding="utf-8")

    manifest = ROOT / "manifest.webmanifest"
    if manifest.exists():
        text = manifest.read_text(encoding="utf-8")
        text = text.replace(f"{prefix}{prefix}", prefix)
        text = re.sub(r'"/', f'"{prefix}/', text)
        manifest.write_text(text, encoding="utf-8")

    print(f"  applied PATH_PREFIX={prefix}")


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
            ("Aktivnosti", f"{prefix}#activities" if is_home else f"{prefix}avanturisticki-park-hrvatska/"),
            ("Obitelj", f"{prefix}obiteljske-aktivnosti-istri/"),
            ("Grupe", f"{prefix}team-building-istri/"),
            ("Cijene", f"{prefix}rezervacija/"),
            ("Lokacija", f"{prefix}#location" if is_home else f"{prefix}sto-raditi-kod-pule/"),
            ("FAQ", f"{prefix}#faq" if is_home else f"{prefix}sigurnost/"),
        ]
    else:
        links = [
            ("Activities", f"{prefix}#activities" if is_home else f"{prefix}adventure-park-croatia/"),
            ("Family", f"{prefix}family-activities-istria/"),
            ("Groups", f"{prefix}team-building-istria/"),
            ("Prices", f"{prefix}book/"),
            ("Location", f"{prefix}#location" if is_home else f"{prefix}things-to-do-near-pula/"),
            ("FAQ", f"{prefix}#faq" if is_home else f"{prefix}safety/"),
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


def render_faqs(faqs: list, lang: str) -> str:
    items = []
    for faq in faqs:
        items.append(f"""
        <details class="faq-item">
          <summary>{faq['q']}</summary>
          <div class="faq-item__answer"><p>{faq['a']}</p></div>
        </details>""")
    heading = "Često postavljana pitanja" if lang == "hr" else "Frequently Asked Questions"
    return f"""
    <section class="section section--alt" id="faq">
      <div class="section__heading"><h2>{heading}</h2></div>
      <div class="faq-list">{''.join(items)}</div>
    </section>"""


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


def faq_schema(faqs: list, page_url: str) -> str:
    entities = []
    for faq in faqs:
        entities.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {"@type": "Answer", "text": faq["a"]},
        })
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": f"{page_url}#faq",
        "mainEntity": entities,
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


def breadcrumb_schema(items: list) -> str:
    elements = []
    for i, (name, url) in enumerate(items, 1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if url:
            el["item"] = url
        elements.append(el)
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elements}
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


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
  {render_faqs(page.get('faqs', []), lang)}
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
{faq_schema(page.get('faqs', []), canonical)}
</body>
</html>"""
    return body


def render_activity_siblings(current_en_slug: str, lang: str) -> str:
    prefix = f"/{lang}/"
    heading = "Ostale aktivnosti" if lang == "hr" else "More Activities"
    icons = {
        "catapult": "🚀", "swing": "🎢", "drop": "⬇️",
        "zipline-valley": "🪂", "zipline-low": "🌲", "climbing": "🧗",
    }
    cards = []
    for act in ACTIVITIES:
        if act["en_slug"] == current_en_slug:
            continue
        slug = act["hr_slug"] if lang == "hr" else act["en_slug"]
        label = act["hr"]["h1"] if lang == "hr" else act["en"]["h1"]
        mod = act["tile_mod"]
        icon = icons.get(mod, "🌲")
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

    prose = "".join(f"<p>{p}</p>" for p in data["paragraphs"])

    return f"""{head_meta(lang, data['title'], data['meta_description'], data['keywords'], canonical, en_slug, hr_slug, og_image=img)}
{quick_actions(lang)}
{site_header(lang)}
{site_nav(lang)}
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="{prefix}">{home_label}</a></li>
      <li><a href="{prefix}#activities">{activities_label}</a></li>
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
    (activities_label, f"{BASE}{prefix}#activities"),
    (data['h1'], None),
])}
</body>
</html>"""


def home_body_en() -> str:
    """English homepage main content (abbreviated structure with full SEO sections)."""
    return open(ROOT / "scripts" / "home_en.html").read()


def home_body_hr() -> str:
    return open(ROOT / "scripts" / "home_hr.html").read()


def render_booking_app(lang: str) -> str:
    if lang == "hr":
        slug, en_slug, hr_slug = "rezervacija", "book", "rezervacija"
        title = "Rezervacija | Glavani Park – odaberite paket i datum"
        desc = "Rezervirajte Glavani Park online za do 6 osoba: odaberite paket (odrasla cijena), datum i pošaljite WhatsAppom ili SMS-om. Grupe 7+ nazovite."
        h1 = "Rezervirajte avanturu"
        lead = "Odaberite paket (do 6 osoba, odrasla cijena) i datum — WhatsApp, SMS ili poziv. Grupe 7+ nazovite."
    else:
        slug, en_slug, hr_slug = "book", "book", "rezervacija"
        title = "Book Your Visit | Glavani Park – Pick Package & Date"
        desc = "Book Glavani Park online for up to 6 people: choose a package (adult pricing), pick a date, and send via WhatsApp or SMS. Groups of 7+ please call."
        h1 = "Book Your Adventure"
        lead = "Choose a package for up to 6 people (adult pricing), pick your date, and send — WhatsApp, SMS, or call. Groups of 7+ please call to book."
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
  <meta http-equiv="refresh" content="0; url=/en/">
  <link rel="canonical" href="https://www.glavanipark.com/en/">
  <title>Glavani Park</title>
  <script>location.replace('/en/');</script>
</head>
<body><p><a href="/en/">Glavani Park – Adventure Park Istria</a></p></body>
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
    sitemap_urls = [(f"{BASE}/en/", "weekly"), (f"{BASE}/en/book/", "weekly")]
    for page in PAGES_EN:
        slug = page["slug"]
        hr_slug = EN_TO_HR.get(slug, slug)
        write_file(ROOT / "en" / slug / "index.html", render_landing(page, "en", slug, hr_slug))
        sitemap_urls.append((f"{BASE}/en/{slug}/", "monthly"))
    for activity in ACTIVITIES:
        slug = activity["en_slug"]
        hr_slug = activity["hr_slug"]
        write_file(ROOT / "en" / slug / "index.html", render_activity_page(activity, "en"))
        sitemap_urls.append((f"{BASE}/en/{slug}/", "monthly"))

    print("Building Croatian pages...")
    write_file(ROOT / "hr" / "index.html", render_home("hr"))
    write_file(ROOT / "hr" / "rezervacija" / "index.html", render_booking_app("hr"))
    sitemap_urls.append((f"{BASE}/hr/", "weekly"))
    sitemap_urls.append((f"{BASE}/hr/rezervacija/", "weekly"))
    for page in PAGES_HR:
        slug = page["slug"]
        en_slug = SLUG_MAP.get(slug, slug)
        write_file(ROOT / "hr" / slug / "index.html", render_landing(page, "hr", en_slug, slug))
        sitemap_urls.append((f"{BASE}/hr/{slug}/", "monthly"))
    for activity in ACTIVITIES:
        slug = activity["hr_slug"]
        write_file(ROOT / "hr" / slug / "index.html", render_activity_page(activity, "hr"))

    print("Writing robots.txt and sitemap.xml...")
    build_robots()
    build_sitemap(sitemap_urls)
    build_root_redirect()
    build_search_console_guide()
    apply_path_prefix()
    print("Done.")


if __name__ == "__main__":
    main()
