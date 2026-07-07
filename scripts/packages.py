"""
Activity packages and single-activity prices for the prices page and booking app.
Keep assets/js/booking-app.js in sync when prices or options change.
"""

from booking_policy import BOOKING_POLICY
from brand_voice import CALL_FOR_GROUPS_ABOVE, ONLINE_BOOKING_MAX

PRICES_SLUGS = {"en": "prices", "hr": "cijene"}
BOOKING_SLUGS = {"en": "book", "hr": "rezervacija"}

WHOLE_PARK_SINGLE_ADULT = 70
CHILD_MAX_AGE = 10

GROUP_LABELS = {
    "en": {
        "small_group": "Small group — whole park incl. catapult",
        "packages": "Activity packages",
        "single": "Single activities",
    },
    "hr": {
        "small_group": "Mali paket — cijeli park uklj. katapultu",
        "packages": "Paketi aktivnosti",
        "single": "Pojedinačne aktivnosti",
    },
}

SMALL_GROUP_PACKAGES = [
    {"id": "whole-park-group-3", "size": 3, "price": 190},
    {"id": "whole-park-group-4", "size": 4, "price": 230},
    {"id": "whole-park-group-5", "size": 5, "price": 260},
    {"id": "whole-park-group-6", "size": 6, "price": 300},
]

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
            "Glavani Park packages from €20 for children and €30 for adults — whole park from €70, "
            "small group deals for 3–6 people from €190, and single activities. "
            f"Book online for up to {ONLINE_BOOKING_MAX} people or call for larger groups."
        ),
        "keywords": "Glavani Park prices, adventure park packages Istria, zipline park Croatia prices",
        "h1": "Activity Packages & Prices",
        "lead": (
            f"Adult and children's prices · small group whole-park deals for 3–6 · book online for up to "
            f"{ONLINE_BOOKING_MAX} people"
        ),
        "per_person": "per person",
        "group_total": "group total",
        "adults": "adults",
        "children": "children",
        "book": "Book",
        "people": "persons",
        "guests_minus": "Fewer people",
        "guests_plus": "More people",
        "book_note": BOOKING_POLICY["en"]["book_note"],
        "more_single": "More single activities coming soon.",
        "small_group_intro": (
            f"Fixed-price whole-park packages for exactly 3–6 people (all games incl. Human Catapult). "
            f"Each price works out below the €{WHOLE_PARK_SINGLE_ADULT} single-person rate — savings shown per person."
        ),
    },
    "hr": {
        "title": "Paketi aktivnosti i cijene | Glavani Park Istria",
        "meta_description": (
            "Paketi Glavani Parka od €20 za djecu i €30 za odrasle — cijeli park od €70, "
            "mali paketi za 3–6 osoba od €190 i pojedinačne aktivnosti. "
            f"Rezervirajte online do {ONLINE_BOOKING_MAX} osoba ili nazovite za veće grupe."
        ),
        "keywords": "Glavani Park cijene, paketi avanturistički park Istria, zipline park Hrvatska cijene",
        "h1": "Paketi aktivnosti i cijene",
        "lead": (
            f"Cijene za odrasle i djecu · mali paketi cijelog parka za 3–6 osoba · online do "
            f"{ONLINE_BOOKING_MAX} osoba"
        ),
        "per_person": "po osobi",
        "group_total": "ukupno za grupu",
        "adults": "odrasli",
        "children": "djeca",
        "book": "Rezerviraj",
        "people": "osoba",
        "guests_minus": "Manje osoba",
        "guests_plus": "Više osoba",
        "book_note": BOOKING_POLICY["hr"]["book_note"],
        "more_single": "Više pojedinačnih aktivnosti uskoro.",
        "small_group_intro": (
            f"Fiksne cijene cijelog parka za točno 3–6 osoba (sve igre uklj. ljudsku katapultu). "
            f"Svaka cijena je niža od €{WHOLE_PARK_SINGLE_ADULT} po osobi — ušteda je prikazana po osobi."
        ),
    },
}


def _format_euro(amount: float) -> str:
    if amount == int(amount):
        return f"€{int(amount)}"
    return f"€{amount:.2f}"


def small_group_rates(size: int, total: int, single: int = WHOLE_PARK_SINGLE_ADULT) -> tuple[float, float]:
    per_person = total / size
    saving = single - per_person
    return per_person, saving


def small_group_copy(opt: dict, lang: str, single: int = WHOLE_PARK_SINGLE_ADULT) -> dict:
    size = opt["size"]
    price = opt["price"]
    per_person, saving = small_group_rates(size, price, single)
    per_fmt = _format_euro(per_person)
    save_fmt = _format_euro(saving)
    if lang == "hr":
        return {
            "name": f"Cijeli park za {size} osoba — uklj. katapultu",
            "desc": (
                f"Sve igre za točno {size} osoba — {per_fmt} po osobi, "
                f"ušteda {save_fmt} po osobi u odnosu na €{single} pojedinačno."
            ),
            "saving": f"Ušteda {save_fmt} po osobi (vs €{single})",
        }
    return {
        "name": f"Whole park for {size} — incl. human catapult",
        "desc": (
            f"All games for exactly {size} people — {per_fmt} per person, "
            f"save {save_fmt} each vs the €{single} single rate."
        ),
        "saving": f"Save {save_fmt} per person (vs €{single})",
    }


def small_group_options() -> list[dict]:
    return [
        {
            "id": opt["id"],
            "group": "small_group",
            "size": opt["size"],
            "price": opt["price"],
            "en": small_group_copy(opt, "en"),
            "hr": small_group_copy(opt, "hr"),
        }
        for opt in SMALL_GROUP_PACKAGES
    ]


def all_booking_options() -> list[dict]:
    return small_group_options() + BOOKING_OPTIONS


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
            f"<strong>Dječje cijene (mlađi od {CHILD_MAX_AGE} godina):</strong> "
            "trening ruta + 2 igre €20 · cijeli park bez katapulata €40 · "
            "cijeli park s katapultom €60 po djetetu."
        )
        if for_booking:
            notice += " U obrascu odaberite broj odraslih i djece."
        return notice
    notice = (
        f"<strong>Children's prices (under {CHILD_MAX_AGE} years old):</strong> "
        "training route + 2 games €20 · whole park without catapult €40 · "
        "whole park incl. catapult €60 per child."
    )
    if for_booking:
        notice += " Select adults and children in the form."
    return notice


def conversion_cta_note(lang: str) -> str:
    min_adult, min_child = min_package_prices()
    if lang == "hr":
        return (
            f"Paketi od €{min_child} djeca / €{min_adult} odrasli · mali paketi 3–6 od €190 · "
            f"online do {ONLINE_BOOKING_MAX} osoba"
        )
    return (
        f"Packages from €{min_child} children / €{min_adult} adults · small groups 3–6 from €190 · "
        f"book online for up to {ONLINE_BOOKING_MAX}"
    )


def pricing_hub_blurb(lang: str) -> str:
    if lang == "hr":
        return (
            "Paketi od €20 za djecu i €30 za odrasle · mali paketi cijelog parka 3–6 od €190 · "
            "pojedinačne aktivnosti od €40"
        )
    return (
        "Packages from €20 for children and €30 for adults · small group whole park 3–6 from €190 · "
        "single activities from €40"
    )


def pricing_visit_footer_line(lang: str) -> str:
    if lang == "hr":
        return (
            "cijeli park €60–70 (djeca/odrasli), mali paketi 3–6 od €190, paketi bez katapulata od €40 za djecu, "
            "trening ruta + 2 igre od €20 za djecu"
        )
    return (
        "whole park €60–70 (children/adults), small groups 3–6 from €190, packages without catapult from €40 for children, "
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
                f'Mali paketi za 3–6 osoba počinju od €190. '
                f'Pogledajte <a href="{prices_href}">pakete i cijene</a> ili '
                f'<a href="{book_href}">rezervirajte online</a>.'
            )
        return (
            f"Pristup je uključen u pakete Glavani Parka — od €20 za djecu i €30 za odrasle. "
            f'Mali paketi cijelog parka za 3–6 osoba od €190. '
            f'Pogledajte <a href="{prices_href}">pakete i cijene</a>.'
        )
    if single_price:
        return (
            f"The Human Catapult is €{single_price} as a single activity, or included in whole-park packages "
            f"(from €20 for children / €30 for adults). "
            f"Small group whole-park deals for 3–6 people start at €190. "
            f'See <a href="{prices_href}">packages and prices</a> or <a href="{book_href}">book online</a>.'
        )
    return (
        f"Access is included in Glavani Park packages — from €20 for children and €30 for adults. "
        f"Small group whole-park packages for 3–6 people start at €190. "
        f'See <a href="{prices_href}">packages and prices</a>.'
    )


def price_summary(lang: str) -> dict:
    """Short pricing lines for hero and CTAs."""
    min_adult, min_child = min_package_prices()
    if lang == "hr":
        return {
            "hero_line": (
                f"Paketi od <strong>€{min_child}</strong> djeca · "
                f"<strong>€{min_adult}</strong> odrasli · mali paketi 3–6 od <strong>€190</strong>"
            ),
            "from": f"od €{min_child}",
        }
    return {
        "hero_line": (
            f"Packages from <strong>€{min_child}</strong> children · "
            f"<strong>€{min_adult}</strong> adults · small groups 3–6 from <strong>€190</strong>"
        ),
        "from": f"from €{min_child}",
    }


def options_for_group(lang: str, group: str) -> list[dict]:
    if group == "small_group":
        items = small_group_options()
    else:
        items = [opt for opt in BOOKING_OPTIONS if opt["group"] == group]
    if group == "small_group":
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
    if opt.get("group") == "small_group":
        per_person, _ = small_group_rates(opt["size"], opt["price"])
        data = opt[lang]
        return (
            f"""              <div class="price-list__amounts price-list__amounts--group">
                <p class="price-list__amount price-list__amount--group-total">€{opt['price']}<span>{copy['group_total']}</span></p>
                <p class="price-list__amount price-list__amount--group-each">{_format_euro(per_person)}<span>{copy['per_person']}</span></p>
                <p class="price-list__saving">{data['saving']}</p>
              </div>"""
        )
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
    for group in ("small_group", "packages", "single"):
        items = options_for_group(lang, group)
        if not items:
            continue
        rows = []
        for opt in items:
            data = opt[lang]
            if opt.get("group") == "small_group":
                data_attrs = f'data-fixed-guests="{opt["size"]}" data-flat-price'
            elif opt.get("child_price"):
                data_attrs = 'data-adults="1" data-children="0" data-has-child-price'
            else:
                data_attrs = f'data-guests="{default_guests}"'
            rows.append(
                f"""        <li class="price-list__item{' price-list__item--group' if opt.get('group') == 'small_group' else ''}" {data_attrs}>
          <div class="price-list__info">
            <h3>{data['name']}</h3>
            <p>{data['desc']}</p>
          </div>
          <div class="price-list__aside">
            <div class="price-list__meta">
{render_price_amount(opt, copy, lang)}
            </div>
            <a class="btn-primary price-list__book-btn" data-book-package="{opt['id']}" href="{book_base}">{copy['book']}</a>
          </div>
        </li>"""
            )
        intro = ""
        if group == "small_group":
            intro = f'        <p class="price-section__intro">{copy["small_group_intro"]}</p>\n'
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
