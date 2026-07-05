"""
Gift voucher catalogue — adult pricing for all vouchers (no children's tiers).
"""

GIFT_VOUCHER_SLUGS = {"en": "gift-voucher", "hr": "poklon-bon"}

GIFT_VOUCHERS = [
    {
        "id": "training-2",
        "price": 30,
        "image": "gift-voucher-30-training-route.webp",
        "en": {
            "name": "Gift voucher €30",
            "package": "Training Route + Two Games",
            "desc": (
                "Yellow training route plus two additional games. "
                "Extra games can be paid for directly at the park — we accept cards and cash."
            ),
        },
        "hr": {
            "name": "Poklon bon 30 €",
            "package": "Trasa treninga + dvije igre",
            "desc": (
                "Žuta trening ruta plus dvije dodatne igre. "
                "Za dodatne igre možete platiti direktno u parku. Primamo kartice i gotovinu."
            ),
        },
    },
    {
        "id": "all-no-catapult",
        "price": 50,
        "image": "gift-voucher-50-whole-park.webp",
        "en": {
            "name": "Gift voucher €50",
            "package": "Whole park — all games without catapult",
            "desc": (
                "All games in the park without the Human Catapult, "
                "or Human Catapult + 12.5 m swing (minimum age 10)."
            ),
        },
        "hr": {
            "name": "Poklon bon 50 €",
            "package": "Cijeli park — sve igre bez katapulta",
            "desc": (
                "Sve igre u parku bez katapulta "
                "ili katapult + ljuljačka (10+ godina)."
            ),
        },
    },
    {
        "id": "all-incl-catapult",
        "price": 70,
        "image": "gift-voucher-70-all-games.webp",
        "en": {
            "name": "Gift voucher €70",
            "package": "Whole park — all games incl. Human Catapult",
            "desc": "Every attraction in Glavani Park including the Human Catapult.",
        },
        "hr": {
            "name": "Poklon bon 70 €",
            "package": "Cijeli park — sve igre uklj. katapult",
            "desc": "Sve atrakcije u Glavani Parku uključujući ljudsku katapultu.",
        },
    },
]

GIFT_VOUCHER_COPY = {
    "en": {
        "title": "Gift Voucher | Glavani Park Istria",
        "meta_description": (
            "Buy a Glavani Park gift voucher from €30 — training routes, whole-park packages, "
            "and full adrenaline days in Istria. Adult pricing for all vouchers. Call to order."
        ),
        "keywords": (
            "Glavani Park gift voucher, adventure park gift card Istria, "
            "zipline park voucher Croatia, birthday gift Pula"
        ),
        "h1": "Gift voucher",
        "lead": "Surprise someone with an adventure in the oak forest — vouchers from €30 per person.",
        "intro": (
            "<p>Glavani Park gift vouchers are valid for our activity packages in Istria — "
            "high ropes, ziplines, swing, and adrenaline rides near Pula. "
            "All vouchers are priced at our standard adult rates and can be redeemed by any guest "
            "who meets the activity age and height requirements.</p>"
            "<p>The park is open daily <strong>9 AM–5 PM</strong> (last entry <strong>3 PM</strong>). "
            "Call <a href=\"tel:+385918964525\">+385 91 896 4525</a> or "
            "<a href=\"tel:+38598224314\">+385 98 224 314</a> to purchase a voucher or check availability before visiting.</p>"
        ),
        "buy_label": "Buy now",
        "call_label": "Call to purchase",
        "redeem_heading": "How to redeem",
        "redeem_text": (
            "Present your voucher code or printed gift card at the ticket desk on arrival. "
            "Staff will apply it to the matching package. "
            "See our <a href=\"{prices}\">packages and prices</a> for full activity details."
        ),
    },
    "hr": {
        "title": "Poklon bon | Glavani Park Istria",
        "meta_description": (
            "Kupite poklon bon za Glavani Park od 30 € — trening rute, paketi cijelog parka "
            "i puni adrenalinski dan u Istri. Cijene za odrasle za sve bonove. Nazovite za narudžbu."
        ),
        "keywords": (
            "Glavani Park poklon bon, poklon bon avanturistički park Istria, "
            "poklon bon zipline Hrvatska, poklon rođendan Pula"
        ),
        "h1": "Poklon bon",
        "lead": "Iznenadite nekoga avanturom u hrastovoj šumi — bonovi od 30 € po osobi.",
        "intro": (
            "<p>Poklon bonovi Glavani Parka vrijede za naše pakete aktivnosti u Istri — "
            "visoke staze, zipline, ljuljačka i adrenalinske vožnje kod Pule. "
            "Svi bonovi imaju standardne cijene za odrasle i mogu ih iskoristiti svi gosti "
            "koji zadovoljavaju dobne i visinske uvjete aktivnosti.</p>"
            "<p>Park radi svaki dan <strong>9–17 h</strong> (posljednji ulaz <strong>15 h</strong>). "
            "Nazovite <a href=\"tel:+385918964525\">+385 91 896 4525</a> ili "
            "<a href=\"tel:+38598224314\">+385 98 224 314</a> za kupnju bona ili provjeru dostupnosti prije posjeta.</p>"
        ),
        "buy_label": "Kupi sada",
        "call_label": "Pozovite za kupnju",
        "redeem_heading": "Kako iskoristiti bon",
        "redeem_text": (
            "Pokažite kod bona ili isprintani poklon bon na blagajni pri dolasku. "
            "Osoblje će ga primijeniti na odgovarajući paket. "
            "Pogledajte <a href=\"{prices}\">pakete i cijene</a> za detalje aktivnosti."
        ),
    },
}


def render_voucher_grid(lang: str) -> str:
    copy = GIFT_VOUCHER_COPY[lang]
    tel = "+385918964525" if lang == "en" else "+38598224314"
    cards = []
    for voucher in GIFT_VOUCHERS:
        data = voucher[lang]
        cards.append(
            f"""      <article class="voucher-card">
        <figure class="voucher-card__media">
          <img src="/images/{voucher['image']}" alt="{data['name']} — {data['package']}" width="400" height="280" loading="lazy">
        </figure>
        <div class="voucher-card__body">
          <h2 class="voucher-card__title">{data['name']}</h2>
          <p class="voucher-card__package">{data['package']}</p>
          <p class="voucher-card__desc">{data['desc']}</p>
          <p class="voucher-card__price">€{voucher['price']}</p>
          <a class="btn-primary voucher-card__buy" href="tel:{tel}">{copy['buy_label']}</a>
        </div>
      </article>"""
        )
    return f'<div class="voucher-grid">\n{chr(10).join(cards)}\n    </div>'


def gift_voucher_offer_schema(lang: str, url: str, name: str) -> dict:
    offers = []
    for voucher in GIFT_VOUCHERS:
        data = voucher[lang]
        offers.append(
            {
                "@type": "Offer",
                "name": data["name"],
                "description": f"{data['package']}. {data['desc']}",
                "price": str(voucher["price"]),
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "url": url,
                "seller": {"@type": "Organization", "name": "Glavani Park"},
            }
        )
    return {
        "@context": "https://schema.org",
        "@type": "Product",
        "@id": f"{url}#gift-vouchers",
        "name": name,
        "description": GIFT_VOUCHER_COPY[lang]["meta_description"],
        "brand": {"@type": "Brand", "name": "Glavani Park"},
        "offers": offers,
    }
