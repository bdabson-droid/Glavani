"""
Activity packages and single-activity prices for the prices page and booking app.
Keep assets/js/booking-app.js in sync when prices or options change.
"""

from booking_policy import BOOKING_POLICY
from brand_voice import CALL_FOR_GROUPS_ABOVE, ONLINE_BOOKING_MAX, PHONES

PRICES_SLUGS = {"en": "prices", "hr": "cijene"}
BOOKING_SLUGS = {"en": "reservation", "hr": "rezervacija"}


def booking_page_href(lang: str) -> str:
    """Booking page path (relativized at build time for GitHub Pages)."""
    return f"/{lang}/{BOOKING_SLUGS[lang]}/"

WHOLE_PARK_SINGLE_ADULT = 70
CHILD_MAX_AGE = 10

GROUP_LABELS = {
    "en": {
        "family": "Family packages — whole park incl. catapult",
        "packages": "Activity packages",
        "single": "Single activities",
    },
    "hr": {
        "family": "Obiteljski paketi — cijeli park uklj. katapultu",
        "packages": "Paketi aktivnosti",
        "single": "Pojedinačne aktivnosti",
    },
}

FAMILY_PACKAGES = [
    {"id": "whole-park-family-4", "size": 4, "price": 150, "catapults": 2},
    {"id": "whole-park-family-5", "size": 5, "price": 200, "catapults": 3},
]

WHOLE_PARK_CATAPULT_PACKAGE = "all-incl-catapult"

BOOKING_OPTIONS = [
    {
        "id": "all-incl-catapult",
        "group": "packages",
        "price": 70,
        "child_price": 60,
        "en": {
            "name": "Whole park — all games incl. human catapult",
            "desc": (
                "Full day access to every attraction including the Human Catapult. "
                "€70 adults · €60 children (under 10)."
            ),
        },
        "hr": {
            "name": "Cijeli park — sve igre uklj. katapultu",
            "desc": (
                "Cjelodnevni pristup svim atrakcijama uključujući ljudsku katapultu. "
                "€70 odrasli · €60 djeca (do 10 godina)."
            ),
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
            "desc": (
                "Ziplines, high ropes, swing, drop, climbing wall, Aerotrim, and more — catapult excluded. "
                "€50 adults · €40 children (under 10)."
            ),
        },
        "hr": {
            "name": "Cijeli park — sve igre (bez katapulata)",
            "desc": (
                "Zipline, visoke staze, ljuljačka, pad, penjački zid, Aerotrim i više — bez katapulata. "
                "€50 odrasli · €40 djeca (do 10 godina)."
            ),
        },
    },
    {
        "id": "training-2",
        "group": "packages",
        "price": 30,
        "child_price": 20,
        "en": {
            "name": "Training route + 2 games",
            "desc": (
                "All park games except the Human Catapult — training route, ziplines, high ropes, "
                "swing, drop, climbing wall, Aerotrim, and more."
            ),
        },
        "hr": {
            "name": "Trening ruta + 2 igre",
            "desc": (
                "Sve igre parka osim ljudske katapulti — trening ruta, zipline, visoke staze, "
                "ljuljačka, pad, penjački zid, Aerotrim i više."
            ),
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
            "Glavani Park packages from €20 for children and €30 for adults — all games except catapult. "
            "Whole park with catapult from €70. Family packages for 4 or 5 from €150. "
            f"Book online for up to {ONLINE_BOOKING_MAX} people or call for larger groups."
        ),
        "keywords": "Glavani Park prices, adventure park packages Istria, zipline park Croatia prices",
        "h1": "Activity Packages & Prices",
        "lead": (
            f"Adult and children's prices · book online for up to {ONLINE_BOOKING_MAX} people · "
            f"call to book for {CALL_FOR_GROUPS_ABOVE + 1}+"
        ),
        "per_person": "per person",
        "group_total": "package total",
        "adults": "adults",
        "children": "children",
        "book": "Book",
        "people": "persons",
        "guests_minus": "Fewer people",
        "guests_plus": "More people",
        "book_note": BOOKING_POLICY["en"]["book_note"],
        "more_single": "More single activities coming soon.",
        "family_intro": (
            "Fixed-price whole-park family packages for exactly 4 or 5 people — all games included, "
            "with extra Human Catapult launches for the group."
        ),
    },
    "hr": {
        "title": "Paketi aktivnosti i cijene | Glavani Park Istria",
        "meta_description": (
            "Paketi Glavani Parka od €20 za djecu i €30 za odrasle — sve igre osim katapulata. "
            "Cijeli park s katapultom od €70. Obiteljski paketi za 4 ili 5 osoba od €150. "
            f"Rezervirajte online do {ONLINE_BOOKING_MAX} osoba ili nazovite za veće grupe."
        ),
        "keywords": "Glavani Park cijene, paketi avanturistički park Istria, zipline park Hrvatska cijene",
        "h1": "Paketi aktivnosti i cijene",
        "lead": (
            f"Cijene za odrasle i djecu · online do {ONLINE_BOOKING_MAX} osoba · "
            f"nazovite za rezervaciju za {CALL_FOR_GROUPS_ABOVE + 1}+"
        ),
        "per_person": "po osobi",
        "group_total": "ukupno za paket",
        "adults": "odrasli",
        "children": "djeca",
        "book": "Rezerviraj",
        "people": "osoba",
        "guests_minus": "Manje osoba",
        "guests_plus": "Više osoba",
        "book_note": BOOKING_POLICY["hr"]["book_note"],
        "more_single": "Više pojedinačnih aktivnosti uskoro.",
        "family_intro": (
            "Fiksne cijene obiteljskog paketa cijelog parka za točno 4 ili 5 osoba — sve igre uključene, "
            "s dodatnim lansiranjima na ljudskoj katapulti za grupu."
        ),
    },
}


def _format_euro(amount: float) -> str:
    if amount == int(amount):
        return f"€{int(amount)}"
    return f"€{amount:.2f}"


def _catapult_word(lang: str, count: int) -> str:
    if lang == "hr":
        return "katapult" if count == 1 else "katapulte"
    return "launch" if count == 1 else "launches"


def family_copy(opt: dict, lang: str) -> dict:
    size = opt["size"]
    catapults = opt["catapults"]
    catapult_label = _catapult_word(lang, catapults)
    if lang == "hr":
        return {
            "name": f"Obiteljski paket cijelog parka za {size}",
            "desc": (
                f"Sve igre za {size} osoba. "
                f"Uključuje {catapults} {catapult_label}."
            ),
            "includes": f"Uključuje {catapults} {catapult_label}",
        }
    return {
        "name": f"Whole park family package for {size}",
        "desc": (
            f"All games for {size} people. "
            f"Includes {catapults} Human Catapult {catapult_label}."
        ),
        "includes": f"Includes {catapults} Human Catapult {catapult_label}",
    }


def family_options() -> list[dict]:
    return [
        {
            "id": opt["id"],
            "group": "family",
            "size": opt["size"],
            "price": opt["price"],
            "catapults": opt["catapults"],
            "en": family_copy(opt, "en"),
            "hr": family_copy(opt, "hr"),
        }
        for opt in FAMILY_PACKAGES
    ]


def all_booking_options() -> list[dict]:
    return BOOKING_OPTIONS + family_options()


def render_children_pricing_ticker(lang: str) -> str:
    return f'<p class="packages-notice packages-notice--children">{children_pricing_notice(lang)}</p>'


def large_group_booking_notice(lang: str) -> str:
    phone = PHONES[1] if lang == "hr" else PHONES[0]
    if lang == "hr":
        return (
            f"<strong>Više od {ONLINE_BOOKING_MAX} osoba?</strong> "
            f"Online rezervacija vrijedi do {ONLINE_BOOKING_MAX} osoba. Za veće grupe "
            f'<a href="tel:{phone["tel"]}">nazovite za rezervaciju</a>.'
        )
    return (
        f"<strong>More than {ONLINE_BOOKING_MAX} people?</strong> "
        f"Book online for up to {ONLINE_BOOKING_MAX}. For larger groups, "
        f'<a href="tel:{phone["tel"]}">call to book</a>.'
    )


def render_large_group_booking_notice(lang: str) -> str:
    return f'<p class="packages-notice packages-notice--groups">{large_group_booking_notice(lang)}</p>'


def min_package_prices() -> tuple[int, int]:
    packages = [opt for opt in BOOKING_OPTIONS if opt["group"] == "packages"]
    min_adult = min(opt["price"] for opt in packages)
    child_prices = [opt["child_price"] for opt in packages if opt.get("child_price")]
    min_child = min(child_prices) if child_prices else min_adult
    return min_adult, min_child


def children_pricing_notice(lang: str, *, for_booking: bool = False) -> str:
    if lang == "hr":
        notice = (
            f"<strong>Dječje cijene (mlađi od {CHILD_MAX_AGE} godina):</strong> "
            "trening ruta + 2 igre (sve osim katapulata) €20 · cijeli park bez katapulata €40 · "
            "cijeli park s katapultom €60 po djetetu."
        )
        if for_booking:
            notice += " U obrascu odaberite broj odraslih i djece."
        return notice
    notice = (
        f"<strong>Children's prices (under {CHILD_MAX_AGE} years old):</strong> "
        "training route + 2 games (all games except catapult) €20 · whole park without catapult €40 · "
        "whole park incl. catapult €60 per child."
    )
    if for_booking:
        notice += " Select adults and children in the form."
    return notice


def conversion_cta_note(lang: str) -> str:
    min_adult, min_child = min_package_prices()
    if lang == "hr":
        return (
            f"Paketi od €{min_child} djeca / €{min_adult} odrasli · "
            f"online do {ONLINE_BOOKING_MAX} osoba"
        )
    return (
        f"Packages from €{min_child} children / €{min_adult} adults · "
        f"book online for up to {ONLINE_BOOKING_MAX}"
    )


def pricing_hub_blurb(lang: str) -> str:
    if lang == "hr":
        return "Paketi od €20 za djecu i €30 za odrasle · pojedinačne aktivnosti od €40"
    return "Packages from €20 for children and €30 for adults · single activities from €40"


def pricing_visit_footer_line(lang: str) -> str:
    if lang == "hr":
        return (
            "cijeli park s katapultom €60–70 (djeca/odrasli), cijeli park bez katapulata €40–50, "
            "trening ruta + 2 igre €20–30, obiteljski paketi od €150"
        )
    return (
        "whole park incl. catapult €60–70 (children/adults), whole park without catapult €40–50, "
        "training route + 2 games €20–30, family packages from €150"
    )


def package_price_faq_answer(lang: str, prefix: str, *, single_price: int | None = None) -> str:
    prices_href = f"{prefix}{PRICES_SLUGS[lang]}/"
    book_href = booking_page_href(lang)
    if lang == "hr":
        if single_price:
            return (
                f"Ljudska katapulta košta {single_price} € kao pojedinačna aktivnost ili je uključena u paket "
                f"cijelog parka s katapultom (€60 djeca / €70 odrasli). "
                f'Pogledajte <a href="{prices_href}">pakete i cijene</a> ili '
                f'<a href="{book_href}">rezervirajte online</a>.'
            )
        return (
            f"Pristup je uključen u paket trening ruta + 2 igre (sve osim katapulata, od €20/€30) "
            f"ili cijeli park bez katapulata (od €40/€50). "
            f'Pogledajte <a href="{prices_href}">pakete i cijene</a>.'
        )
    if single_price:
        return (
            f"The Human Catapult is €{single_price} as a single activity, or included in the whole-park "
            f"package with catapult (€60 children / €70 adults). "
            f'See <a href="{prices_href}">packages and prices</a> or <a href="{book_href}">book online</a>.'
        )
    return (
        f"Access is included in the Training route + 2 games package (all games except catapult, from €20/€30) "
        f"or whole park without catapult (from €40/€50). "
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
    if group == "family":
        items = family_options()
    else:
        items = [opt for opt in BOOKING_OPTIONS if opt["group"] == group]
    if group == "family":
        return sorted(items, key=lambda opt: opt["size"])
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


def render_price_amount(opt: dict, copy: dict, lang: str) -> str:
    if opt.get("group") == "family":
        data = opt[lang]
        return (
            f"""              <div class="price-list__amounts price-list__amounts--inline">
                <p class="price-list__amount price-list__amount--group-total">€{opt['price']}<span>{copy['group_total']}</span></p>
                <p class="price-list__saving">{data['includes']}</p>
              </div>"""
        )
    if opt.get("child_price"):
        return (
            f"""              <div class="price-list__amounts price-list__amounts--inline">
                <p class="price-list__amount">€{opt['price']}<span>{copy['adults']}</span></p>
                <p class="price-list__amount price-list__amount--child">€{opt['child_price']}<span>{copy['children']}</span></p>
              </div>"""
        )
    return f"""              <p class="price-list__amount">€{opt['price']}<span>{copy['per_person']}</span></p>"""


def render_price_sections(lang: str) -> str:
    copy = PRICES_COPY[lang]
    book_base = booking_page_href(lang)
    default_guests = 1
    sections = []
    for group in ("packages", "family", "single"):
        items = options_for_group(lang, group)
        if not items:
            continue
        rows = []
        for opt in items:
            data = opt[lang]
            if opt.get("group") == "family":
                data_attrs = f'data-fixed-guests="{opt["size"]}" data-flat-price'
            elif opt.get("child_price"):
                data_attrs = 'data-adults="1" data-children="0" data-has-child-price'
            else:
                data_attrs = f'data-guests="{default_guests}"'
            rows.append(
                f"""        <li class="price-list__item{' price-list__item--group' if opt.get('group') == 'family' else ''}" {data_attrs}>
          <div class="price-list__info">
            <h3>{data['name']}</h3>
            <p>{data['desc']}</p>
          </div>
          <div class="price-list__aside">
            <div class="price-list__meta">
{render_price_amount(opt, copy, lang)}
{'' if opt.get('group') == 'family' else render_price_qty(opt, copy)}
            </div>
            <a class="btn-primary price-list__book-btn" data-book-package="{opt['id']}" href="{book_base}">{copy['book']}</a>
          </div>
        </li>"""
            )
        intro = ""
        if group == "family":
            intro = f'        <p class="price-section__intro">{copy["family_intro"]}</p>\n'
        sections.append(
            f"""      <section class="price-section" aria-labelledby="price-{group}-heading">
        <h2 id="price-{group}-heading">{GROUP_LABELS[lang][group]}</h2>
{intro}        <ul class="price-list">
{chr(10).join(rows)}
        </ul>
      </section>"""
        )
    return "\n".join(sections)


def prices_offer_schema(lang: str, url: str, name: str) -> dict:
    """Product/Offer schema for packages and single activities."""
    offers = []
    for opt in all_booking_options():
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
