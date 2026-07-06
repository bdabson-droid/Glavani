"""
Activity packages and single-activity prices for the prices page and booking app.
Keep assets/js/booking-app.js in sync when prices or options change.
"""

PRICES_SLUGS = {"en": "prices", "hr": "cijene"}
BOOKING_SLUGS = {"en": "book", "hr": "rezervacija"}

GROUP_LABELS = {
    "en": {"packages": "Activity packages", "single": "Single activities"},
    "hr": {"packages": "Paketi aktivnosti", "single": "Pojedinačne aktivnosti"},
}

BOOKING_OPTIONS = [
    {
        "id": "all-incl-catapult",
        "group": "packages",
        "price": 70,
        "child_price": 60,
        "en": {
            "name": "Whole park — all games incl. human catapult",
            "desc": "Full day access to every attraction including the Human Catapult.",
        },
        "hr": {
            "name": "Cijeli park — sve igre uklj. katapultu",
            "desc": "Cjelodnevni pristup svim atrakcijama uključujući ljudsku katapultu.",
        },
    },
    {
        "id": "catapult-swing",
        "group": "packages",
        "price": 50,
        "en": {
            "name": "Human catapult + 12.5 m swing",
            "desc": "Two signature adrenaline rides in one package.",
        },
        "hr": {
            "name": "Ljudska katapulta + ljuljačka 12,5 m",
            "desc": "Dvije glavne adrenalinske atrakcije u jednom paketu.",
        },
    },
    {
        "id": "all-no-catapult",
        "group": "packages",
        "price": 50,
        "child_price": 40,
        "en": {
            "name": "Whole park — all games (without catapult)",
            "desc": "Ziplines, high ropes, swing, drop, and climbing wall — catapult excluded.",
        },
        "hr": {
            "name": "Cijeli park — sve igre (bez katapulata)",
            "desc": "Zipline, visoke staze, ljuljačka, pad i penjački zid — bez katapulata.",
        },
    },
    {
        "id": "training-2",
        "group": "packages",
        "price": 30,
        "child_price": 20,
        "en": {
            "name": "Training route + 2 games",
            "desc": "Yellow training route plus two additional games.",
        },
        "hr": {
            "name": "Trening ruta + 2 igre",
            "desc": "Žuta trening ruta plus dvije dodatne igre.",
        },
    },
    {
        "id": "human-catapult",
        "group": "single",
        "price": 40,
        "en": {
            "name": "Human Catapult",
            "desc": "Single launch on the Human Catapult — instructor-led and harness fitted.",
        },
        "hr": {
            "name": "Ljudska katapulta",
            "desc": "Jedno lansiranje na ljudskoj katapulti — pod nadzorom instruktora.",
        },
    },
]

PRICES_COPY = {
    "en": {
        "title": "Activity Packages & Prices | Glavani Park Istria",
        "meta_description": (
            "Glavani Park packages from €20 for children and €30 for adults — whole park, training routes, "
            "and single activities. Book online for up to 10 people or call for larger groups."
        ),
        "keywords": "Glavani Park prices, adventure park packages Istria, zipline park Croatia prices",
        "h1": "Activity Packages & Prices",
        "lead": "Adult and children's prices for packages and single activities · book online for up to 10 people",
        "per_person": "per person",
        "adults": "adults",
        "children": "children",
        "book": "Book",
        "people": "persons",
        "guests_minus": "Fewer people",
        "guests_plus": "More people",
        "book_note": (
            "From late September to early July, advance booking is required — no walk-ins. "
            "In peak season (July–September) walk-ins may be accepted during opening hours, subject to availability — "
            "book ahead to guarantee your slot and avoid disappointment. "
            "Groups of more than 10 should call to check availability and pricing."
        ),
        "more_single": "More single activities coming soon.",
    },
    "hr": {
        "title": "Paketi aktivnosti i cijene | Glavani Park Istria",
        "meta_description": (
            "Paketi Glavani Parka od €20 za djecu i €30 za odrasle — cijeli park, trening rute "
            "i pojedinačne aktivnosti. Rezervirajte online do 10 osoba ili nazovite za grupe."
        ),
        "keywords": "Glavani Park cijene, paketi avanturistički park Istria, zipline park Hrvatska cijene",
        "h1": "Paketi aktivnosti i cijene",
        "lead": "Cijene za odrasle i djecu za pakete i pojedinačne aktivnosti · online do 10 osoba",
        "per_person": "po osobi",
        "adults": "odrasli",
        "children": "djeca",
        "book": "Rezerviraj",
        "people": "osoba",
        "guests_minus": "Manje osoba",
        "guests_plus": "Više osoba",
        "book_note": (
            "Od kraja rujna do početka srpnja potrebna je unaprijedna rezervacija — bez dolaska bez najave. "
            "U vrhu sezone (srpanj–rujan) dolazak bez rezervacije moguć je tijekom radnog vremena, ovisno o dostupnosti — "
            "rezervirajte unaprijed kako biste osigurali termin i izbjegli razočaranje. "
            "Grupe s više od 10 osoba neka nazovu radi dostupnosti i cijena."
        ),
        "more_single": "Više pojedinačnih aktivnosti uskoro.",
    },
}


def render_children_pricing_ticker(lang: str) -> str:
    return f'<p class="packages-notice packages-notice--children">{children_pricing_notice(lang)}</p>'


def min_package_prices() -> tuple[int, int]:
    packages = [opt for opt in BOOKING_OPTIONS if opt["group"] == "packages"]
    min_adult = min(opt["price"] for opt in packages)
    child_prices = [opt["child_price"] for opt in packages if opt.get("child_price")]
    min_child = min(child_prices) if child_prices else min_adult
    return min_adult, min_child


def children_pricing_notice(lang: str, *, for_booking: bool = False) -> str:
    if lang == "hr":
        notice = (
            "<strong>Dječje cijene:</strong> trening ruta + 2 igre €20 · cijeli park bez katapulata €40 · "
            "cijeli park s katapultom €60 po djetetu."
        )
        if for_booking:
            notice += " U obrascu odaberite broj odraslih i djece."
        return notice
    notice = (
        "<strong>Children's prices:</strong> training route + 2 games €20 · whole park without catapult €40 · "
        "whole park incl. catapult €60 per child."
    )
    if for_booking:
        notice += " Select adults and children in the form."
    return notice


def conversion_cta_note(lang: str) -> str:
    if lang == "hr":
        return "Paketi od €20 djeca / €30 odrasli · online do 10 osoba"
    return "Packages from €20 children / €30 adults · book online for up to 10"


def pricing_hub_blurb(lang: str) -> str:
    if lang == "hr":
        return "Paketi od €20 za djecu i €30 za odrasle · pojedinačne aktivnosti od €40"
    return "Packages from €20 for children and €30 for adults · single activities from €40"


def pricing_visit_footer_line(lang: str) -> str:
    if lang == "hr":
        return (
            "cijeli park €60–70 (djeca/odrasli), paketi bez katapulata od €40 za djecu, "
            "trening ruta + 2 igre od €20 za djecu"
        )
    return (
        "whole park €60–70 (children/adults), packages without catapult from €40 for children, "
        "training route + 2 games from €20 for children"
    )


def package_price_faq_answer(lang: str, prefix: str, *, single_price: int | None = None) -> str:
    prices_href = f"{prefix}{PRICES_SLUGS[lang]}/"
    book_href = f"{prefix}{BOOKING_SLUGS[lang]}/"
    if lang == "hr":
        if single_price:
            return (
                f"Ljudska katapulta košta {single_price} € kao pojedinačna aktivnost ili je uključena u pakete "
                f"cijelog parka (od €20 za djecu / €30 za odrasle). "
                f'Pogledajte <a href="{prices_href}">pakete i cijene</a> ili '
                f'<a href="{book_href}">rezervirajte online</a>.'
            )
        return (
            f"Pristup je uključen u pakete Glavani Parka — od €20 za djecu i €30 za odrasle. "
            f'Pogledajte <a href="{prices_href}">pakete i cijene</a>.'
        )
    if single_price:
        return (
            f"The Human Catapult is €{single_price} as a single activity, or included in whole-park packages "
            f"(from €20 for children / €30 for adults). "
            f'See <a href="{prices_href}">packages and prices</a> or <a href="{book_href}">book online</a>.'
        )
    return (
        f"Access is included in Glavani Park packages — from €20 for children and €30 for adults. "
        f'See <a href="{prices_href}">packages and prices</a>.'
    )


def price_summary(lang: str) -> dict:
    """Short pricing lines for hero and CTAs."""
    min_adult, min_child = min_package_prices()
    if lang == "hr":
        return {
            "hero_line": (
                f"Paketi od <strong>€{min_child}</strong> djeca · "
                f"<strong>€{min_adult}</strong> odrasli"
            ),
            "from": f"od €{min_child}",
        }
    return {
        "hero_line": (
            f"Packages from <strong>€{min_child}</strong> children · "
            f"<strong>€{min_adult}</strong> adults"
        ),
        "from": f"from €{min_child}",
    }


def options_for_group(lang: str, group: str) -> list[dict]:
    items = [opt for opt in BOOKING_OPTIONS if opt["group"] == group]
    return sorted(items, key=lambda opt: opt["price"], reverse=True)


def render_price_qty(opt: dict, copy: dict) -> str:
    if opt.get("child_price"):
        return f"""              <div class="price-qty-set" data-price-qty-split>
                <div class="price-qty price-qty--role">
                  <button type="button" class="qty-btn price-qty__btn" data-qty-adults-minus aria-label="{copy['guests_minus']} ({copy['adults']})">−</button>
                  <span class="price-qty__value" data-qty-adults-value aria-live="polite">1</span>
                  <span class="price-qty__label">{copy['adults']}</span>
                  <button type="button" class="qty-btn price-qty__btn" data-qty-adults-plus aria-label="{copy['guests_plus']} ({copy['adults']})">+</button>
                </div>
                <div class="price-qty price-qty--role">
                  <button type="button" class="qty-btn price-qty__btn" data-qty-children-minus aria-label="{copy['guests_minus']} ({copy['children']})">−</button>
                  <span class="price-qty__value" data-qty-children-value aria-live="polite">0</span>
                  <span class="price-qty__label">{copy['children']}</span>
                  <button type="button" class="qty-btn price-qty__btn" data-qty-children-plus aria-label="{copy['guests_plus']} ({copy['children']})">+</button>
                </div>
              </div>"""
    return f"""              <div class="price-qty" data-price-qty>
                <button type="button" class="qty-btn price-qty__btn" data-qty-minus aria-label="{copy['guests_minus']}">−</button>
                <span class="price-qty__value" data-qty-value aria-live="polite">1</span>
                <span class="price-qty__label">{copy['people']}</span>
                <button type="button" class="qty-btn price-qty__btn" data-qty-plus aria-label="{copy['guests_plus']}">+</button>
              </div>"""


def render_price_amount(opt: dict, copy: dict) -> str:
    if opt.get("child_price"):
        return (
            f"""              <div class="price-list__amounts">
                <p class="price-list__amount">€{opt['price']}<span>{copy['adults']}</span></p>
                <p class="price-list__amount price-list__amount--child">€{opt['child_price']}<span>{copy['children']}</span></p>
              </div>"""
        )
    return f"""              <p class="price-list__amount">€{opt['price']}<span>{copy['per_person']}</span></p>"""


def render_price_sections(lang: str) -> str:
    copy = PRICES_COPY[lang]
    book_base = f"/{lang}/{BOOKING_SLUGS[lang]}/"
    default_guests = 1
    sections = []
    for group in ("packages", "single"):
        items = options_for_group(lang, group)
        if not items:
            continue
        rows = []
        for opt in items:
            data = opt[lang]
            if opt.get("child_price"):
                data_attrs = 'data-adults="1" data-children="0" data-has-child-price'
            else:
                data_attrs = f'data-guests="{default_guests}"'
            rows.append(
                f"""        <li class="price-list__item" {data_attrs}>
          <div class="price-list__info">
            <h3>{data['name']}</h3>
            <p>{data['desc']}</p>
          </div>
          <div class="price-list__aside">
            <div class="price-list__meta">
{render_price_amount(opt, copy)}
{render_price_qty(opt, copy)}
            </div>
            <a class="btn-primary price-list__book-btn" data-book-package="{opt['id']}" href="{book_base}">{copy['book']}</a>
          </div>
        </li>"""
            )
        sections.append(
            f"""      <section class="price-section" aria-labelledby="price-{group}-heading">
        <h2 id="price-{group}-heading">{GROUP_LABELS[lang][group]}</h2>
        <ul class="price-list">
{chr(10).join(rows)}
        </ul>
      </section>"""
        )
    return "\n".join(sections)


def prices_offer_schema(lang: str, url: str, name: str) -> dict:
    """Product/Offer schema for packages and single activities."""
    offers = []
    for opt in BOOKING_OPTIONS:
        data = opt[lang]
        offers.append(
            {
                "@type": "Offer",
                "name": data["name"],
                "description": data["desc"],
                "price": str(opt["price"]),
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "url": url,
                "seller": {"@type": "Organization", "name": "Glavani Park"},
            }
        )
        if opt.get("child_price"):
            offers.append(
                {
                    "@type": "Offer",
                    "name": f"{data['name']} ({PRICES_COPY[lang]['children']})",
                    "description": data["desc"],
                    "price": str(opt["child_price"]),
                    "priceCurrency": "EUR",
                    "availability": "https://schema.org/InStock",
                    "url": url,
                    "seller": {"@type": "Organization", "name": "Glavani Park"},
                }
            )
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "@id": f"{url}#pricing",
        "name": name,
        "description": PRICES_COPY[lang]["meta_description"],
        "brand": {"@type": "Brand", "name": "Glavani Park"},
        "offers": offers,
    }
