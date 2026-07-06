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
        "en": {
            "name": "Training route + 2 games",
            "desc": "Yellow training route plus two additional games — ideal for first visits.",
        },
        "hr": {
            "name": "Trening ruta + 2 igre",
            "desc": "Žuta trening ruta plus dvije dodatne igre — idealno za prvi posjet.",
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
            "Glavani Park activity packages from €30 per person — whole park, training routes, "
            "and single activities. Book online for up to 10 people or call for larger groups."
        ),
        "keywords": "Glavani Park prices, adventure park packages Istria, zipline park Croatia prices",
        "h1": "Activity Packages & Prices",
        "lead": "Per-person prices for packages and single activities · book online for up to 10 people",
        "per_person": "per person",
        "book": "Book",
        "book_note": "Visits from late September to early July require advance booking — no walk-ins. Groups of more than 10 should call to check availability and pricing.",
        "more_single": "More single activities coming soon.",
    },
    "hr": {
        "title": "Paketi aktivnosti i cijene | Glavani Park Istria",
        "meta_description": (
            "Paketi aktivnosti Glavani Parka od €30 po osobi — cijeli park, trening rute "
            "i pojedinačne aktivnosti. Rezervirajte online do 10 osoba ili nazovite za grupe."
        ),
        "keywords": "Glavani Park cijene, paketi avanturistički park Istria, zipline park Hrvatska cijene",
        "h1": "Paketi aktivnosti i cijene",
        "lead": "Cijene po osobi za pakete i pojedinačne aktivnosti · online do 10 osoba",
        "per_person": "po osobi",
        "book": "Rezerviraj",
        "book_note": "Od kraja rujna do početka srpnja potrebna je unaprijedna rezervacija — bez dolaska bez najave. Grupe s više od 10 osoba neka nazovu radi dostupnosti i cijena.",
        "more_single": "Više pojedinačnih aktivnosti uskoro.",
    },
}


def options_for_group(lang: str, group: str) -> list[dict]:
    items = [opt for opt in BOOKING_OPTIONS if opt["group"] == group]
    return sorted(items, key=lambda opt: opt["price"], reverse=True)


def render_price_sections(lang: str) -> str:
    copy = PRICES_COPY[lang]
    per_person = copy["per_person"]
    book_base = f"/{lang}/{BOOKING_SLUGS[lang]}/"
    sections = []
    for group in ("packages", "single"):
        items = options_for_group(lang, group)
        if not items:
            continue
        rows = []
        for opt in items:
            data = opt[lang]
            rows.append(
                f"""        <li class="price-list__item">
          <div class="price-list__info">
            <h3>{data['name']}</h3>
            <p>{data['desc']}</p>
          </div>
          <div class="price-list__aside">
            <p class="price-list__amount">€{opt['price']}<span>{per_person}</span></p>
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
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "@id": f"{url}#pricing",
        "name": name,
        "description": PRICES_COPY[lang]["meta_description"],
        "brand": {"@type": "Brand", "name": "Glavani Park"},
        "offers": offers,
    }
