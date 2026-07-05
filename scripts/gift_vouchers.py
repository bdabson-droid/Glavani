"""
Gift voucher catalogue — adult pricing for all vouchers (no children's tiers).
Online checkout posts to the legacy glavanipark.com payment endpoint.
"""

import json

GIFT_VOUCHER_SLUGS = {"en": "gift-voucher", "hr": "poklon-bon"}
GIFT_VOUCHER_CHECKOUT_SLUGS = {"en": "buy", "hr": "kupnja"}

# Legacy payment form slots (kids products kept at zero for API compatibility).
LEGACY_VOUCHER_SLOTS = [
    {"field": "quant0[1]", "pk": 65},
    {"field": "quant1[1]", "pk": 66},
    {"field": "quant2[1]", "pk": 67},
    {"field": "quant3[1]", "pk": 68},
    {"field": "quant4[1]", "pk": 15},
    {"field": "quant5[1]", "pk": 18},
]

GIFT_VOUCHERS = [
    {
        "id": "training-2",
        "price": 30,
        "legacy_pk": 66,
        "legacy_field": "quant1[1]",
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
        "legacy_pk": 68,
        "legacy_field": "quant3[1]",
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
        "legacy_pk": 18,
        "legacy_field": "quant5[1]",
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
            "and full adrenaline days in Istria. Adult pricing for all vouchers. Purchase online or by phone."
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
            "<p>Purchase online with card payment, or call "
            "<a href=\"tel:+385918964525\">+385 91 896 4525</a> / "
            "<a href=\"tel:+38598224314\">+385 98 224 314</a> if you prefer to order by phone. "
            "The park is open daily <strong>9 AM–5 PM</strong> (last entry <strong>3 PM</strong>).</p>"
        ),
        "buy_label": "Buy online",
        "checkout_label": "Buy gift vouchers online",
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
            "i puni adrenalinski dan u Istri. Cijene za odrasle za sve bonove. Kupnja online ili telefonom."
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
            "<p>Kupite online karticom ili nazovite "
            "<a href=\"tel:+385918964525\">+385 91 896 4525</a> / "
            "<a href=\"tel:+38598224314\">+385 98 224 314</a> za narudžbu telefonom. "
            "Park radi svaki dan <strong>9–17 h</strong> (posljednji ulaz <strong>15 h</strong>).</p>"
        ),
        "buy_label": "Kupi online",
        "checkout_label": "Kupi poklon bon online",
        "call_label": "Pozovite za kupnju",
        "redeem_heading": "Kako iskoristiti bon",
        "redeem_text": (
            "Pokažite kod bona ili isprintani poklon bon na blagajni pri dolasku. "
            "Osoblje će ga primijeniti na odgovarajući paket. "
            "Pogledajte <a href=\"{prices}\">pakete i cijene</a> za detalje aktivnosti."
        ),
    },
}

GIFT_VOUCHER_CHECKOUT_COPY = {
    "en": {
        "title": "Buy Gift Voucher Online | Glavani Park Istria",
        "meta_description": (
            "Purchase Glavani Park gift vouchers online with secure card payment. "
            "Choose from €30, €50, or €70 packages — personalised voucher sent by email."
        ),
        "keywords": "buy Glavani Park gift voucher online, gift card payment Istria",
        "h1": "Buy gift voucher",
        "lead": "Choose your vouchers, enter your details, and pay securely online.",
        "notice": (
            "A personalised gift voucher will be sent by email to the address you provide. "
            "Use the comments field to say who the gift is for and which occasion it celebrates."
        ),
        "packages_heading": "Choose your vouchers",
        "details_heading": "Your details",
        "first_name": "First name",
        "last_name": "Surname",
        "address": "Address",
        "zip": "Postcode",
        "city": "City",
        "country": "Country",
        "phone": "Phone",
        "email": "Email",
        "comments": "Comments",
        "comments_ph": "Who is this gift for, and what is the occasion?",
        "total": "Total to pay",
        "submit": "Pay now",
        "select_one": "Please add at least one voucher.",
        "fill_required": "Please fill in all required fields.",
        "invalid_email": "Please enter a valid email address.",
        "each": "€{price} each",
        "line_total": "€{total}",
        "breadcrumb": "Buy online",
        "back": "Back to gift vouchers",
        "call_alt": "Prefer to order by phone?",
    },
    "hr": {
        "title": "Kupnja poklon bona online | Glavani Park Istria",
        "meta_description": (
            "Kupite poklon bon za Glavani Park online sigurnom kartičnom uplatom. "
            "Odaberite paket od 30 €, 50 € ili 70 € — personalizirani bon stiže e-poštom."
        ),
        "keywords": "kupnja poklon bona Glavani Park online, poklon bon kartica Istria",
        "h1": "Kupnja poklon bona",
        "lead": "Odaberite bonove, unesite podatke i platite sigurno online.",
        "notice": (
            "Personalizirani poklon bon bit će poslan e-poštom na adresu koju navedete. "
            "U polju za napomenu napišite za koga je poklon i povod."
        ),
        "packages_heading": "Odaberite bonove",
        "details_heading": "Vaši podaci",
        "first_name": "Ime",
        "last_name": "Prezime",
        "address": "Adresa",
        "zip": "Poštanski broj",
        "city": "Grad",
        "country": "Država",
        "phone": "Telefon",
        "email": "E-pošta",
        "comments": "Napomena",
        "comments_ph": "Za koga je poklon i koji je povod?",
        "total": "Ukupno za uplatu",
        "submit": "Plati sada",
        "select_one": "Dodajte barem jedan bon.",
        "fill_required": "Ispunite sva obavezna polja.",
        "invalid_email": "Unesite ispravnu e-mail adresu.",
        "each": "{price} € po komadu",
        "line_total": "{total} €",
        "breadcrumb": "Kupnja online",
        "back": "Natrag na poklon bonove",
        "call_alt": "Želite naručiti telefonom?",
    },
}


def checkout_path(lang: str) -> str:
    return f"/{lang}/{GIFT_VOUCHER_SLUGS[lang]}/{GIFT_VOUCHER_CHECKOUT_SLUGS[lang]}/"


def voucher_by_id(voucher_id: str) -> dict | None:
    for voucher in GIFT_VOUCHERS:
        if voucher["id"] == voucher_id:
            return voucher
    return None


def checkout_config(lang: str) -> dict:
    vouchers = []
    for voucher in GIFT_VOUCHERS:
        data = voucher[lang]
        vouchers.append(
            {
                "id": voucher["id"],
                "price": voucher["price"],
                "legacyPk": voucher["legacy_pk"],
                "legacyField": voucher["legacy_field"],
                "name": data["name"],
                "package": data["package"],
                "image": f"/images/{voucher['image']}",
            }
        )
    return {
        "lang": lang,
        "paymentUrl": "https://www.glavanipark.com/payment",
        "calculateUrl": "https://www.glavanipark.com/data/calculate",
        "vouchers": vouchers,
        "legacySlots": LEGACY_VOUCHER_SLOTS,
        "copy": GIFT_VOUCHER_CHECKOUT_COPY[lang],
    }


def render_voucher_grid(lang: str) -> str:
    copy = GIFT_VOUCHER_COPY[lang]
    checkout = checkout_path(lang)
    tel = "+385918964525" if lang == "en" else "+38598224314"
    cards = []
    for voucher in GIFT_VOUCHERS:
        data = voucher[lang]
        buy_href = f"{checkout}?v={voucher['id']}"
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
          <a class="btn-primary voucher-card__buy" href="{buy_href}">{copy['buy_label']}</a>
        </div>
      </article>"""
        )
    checkout_cta = (
        f"""      <p class="voucher-grid__checkout">
        <a class="btn-secondary" href="{checkout}">{copy['checkout_label']}</a>
        <a class="btn-secondary" href="tel:{tel}">{copy['call_label']}</a>
      </p>"""
    )
    return f'<div class="voucher-grid">\n{chr(10).join(cards)}\n    </div>\n{checkout_cta}'


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


def checkout_config_json(lang: str) -> str:
    return json.dumps(checkout_config(lang), ensure_ascii=False).replace("</", "<\\/")
