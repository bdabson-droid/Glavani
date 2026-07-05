"""Concise visitor FAQs for Glavani Park."""

import re

from booking_policy import BOOKING_POLICY

BASE = "https://www.glavanipark.com"

FAQ_SLUGS = {"en": "faq", "hr": "cesta-pitanja"}

FAQ_LINKS = {
    "en": {
        "book": "/en/book/",
        "prices": "/en/prices/",
        "safety": "/en/safety/",
        "location": "/en/things-to-do-near-pula/#location-map",
        "groups": "/en/team-building-istria/",
    },
    "hr": {
        "book": "/hr/rezervacija/",
        "prices": "/hr/cijene/",
        "safety": "/hr/sigurnost/",
        "location": "/hr/sto-raditi-kod-pule/#location-map",
        "groups": "/hr/team-building-istri/",
    },
}

FAQ_COPY = {
    "en": {
        "title": "Glavani Park FAQ — Hours, Booking & Visit Info | Istria Croatia",
        "meta_description": (
            "Common questions about visiting Glavani Park — Istria's adventure and zipline park near Pula. "
            "Opening hours, online booking, ages, safety, parking, food, and group visits."
        ),
        "keywords": (
            "Glavani Park FAQ, adventure park Istria, zipline park Croatia, visit Glavani Park, "
            "Glavani Park opening hours, booking Pula, outdoor activities Istria"
        ),
        "h1": "Glavani Park FAQ",
        "lead": (
            "Planning a day at Istria's adventure park near Pula? "
            "Quick answers on hours, booking, location, ages, safety, and groups."
        ),
        "intro": (
            "Glavani Park is an outdoor adventure and zipline park in Barban, Istria — "
            "about 30 minutes from Pula with ziplines, high ropes, and adrenaline rides. "
            "Below are the questions visitors ask most before they book."
        ),
        "list_heading": "Common questions",
        "book_note": (
            "Visits from late September to early July require advance booking — no walk-ins. "
            "Book online for up to 10 people, or call for larger groups."
        ),
        "related_heading": "Plan your visit",
    },
    "hr": {
        "title": "Glavani Park FAQ — radno vrijeme, rezervacija i posjet | Istria",
        "meta_description": (
            "Česta pitanja o posjetu Glavani Parku — avanturistički i zipline park u Istri kod Pule. "
            "Radno vrijeme, online rezervacija, dob, sigurnost, parkiranje, hrana i grupe."
        ),
        "keywords": (
            "Glavani Park FAQ, avanturistički park Istria, zipline park Hrvatska, posjet Glavani Parku, "
            "radno vrijeme Glavani Park, rezervacija Pula, aktivnosti na otvorenom Istria"
        ),
        "h1": "Glavani Park — česta pitanja",
        "lead": (
            "Planirate dan u avanturističkom parku u Istri kod Pule? "
            "Brzi odgovori o radnom vremenu, rezervaciji, lokaciji, dobi, sigurnosti i grupama."
        ),
        "intro": (
            "Glavani Park je avanturistički i zipline park na otvorenom u Barbanu, Istri — "
            "otprilike 30 minuta od Pule, sa ziplineovima, visokim stazama i adrenalinskim vožnjama. "
            "Ispod su pitanja koja posjetitelji najčešće postavljaju prije rezervacije."
        ),
        "list_heading": "Najčešća pitanja",
        "book_note": (
            "Od kraja rujna do početka srpnja potrebna je unaprijedna rezervacija — bez dolaska bez najave. "
            "Rezervirajte online do 10 osoba ili nazovite za veće grupe."
        ),
        "related_heading": "Planirajte posjet",
    },
}

FAQ_RELATED = {
    "en": [
        {"href": "prices", "title": "Packages & Prices", "desc": "Activity packages from €30 per person"},
        {"href": "location", "title": "Location & Directions", "desc": "Map, GPS, and free parking near Pula"},
        {"href": "safety", "title": "Safety & Equipment", "desc": "Harness standards and what to wear"},
        {"href": "groups", "title": "Team Building & Groups", "desc": "Corporate events, schools, and birthdays"},
    ],
    "hr": [
        {"href": "prices", "title": "Paketi i cijene", "desc": "Paketi aktivnosti od 30 € po osobi"},
        {"href": "location", "title": "Lokacija i upute", "desc": "Karta, GPS i besplatno parkiranje kod Pule"},
        {"href": "safety", "title": "Sigurnost i oprema", "desc": "Standardi opreme i što obući"},
        {"href": "groups", "title": "Team building i grupe", "desc": "Korporativni događaji, škole i rođendani"},
    ],
}

VISITOR_FAQS = {
    "en": [
        {
            "q": "What are Glavani Park opening hours?",
            "a": (
                "Glavani Park is open daily 9 AM–5 PM during the season. "
                "Last entry is 3 PM — allow three to four hours for a full visit."
            ),
        },
        {
            "q": BOOKING_POLICY["en"]["faq_question"],
            "a": BOOKING_POLICY["en"]["faq_answer"],
        },
        {
            "q": "How do I book Glavani Park online?",
            "a": (
                "Choose a package on the <a href=\"{book}\">Book page</a> or see "
                "<a href=\"{prices}\">packages and prices</a>, pick a date, and send your request by email. "
                "For all advance bookings we respond with an emailed invoice to confirm as soon as possible. "
                "If your visit is within 48 hours, please call to book instead."
            ),
        },
        {
            "q": "How far is Glavani Park from Pula?",
            "a": (
                "Glavani Park is about 30 minutes by car from Pula, 45 from Rovinj, and 10 from Vodnjan. "
                "Free parking at Glavani 10, 52207 Barban. "
                "See <a href=\"{location}\">location and directions</a>."
            ),
        },
        {
            "q": "What ages can take part at Glavani Park?",
            "a": (
                "The yellow training route at Glavani Park suits younger children with adult supervision. "
                "Taller attractions such as the Human Catapult and Quick Jump have minimum age and height limits — "
                "call +385 91 896 4525 if unsure."
            ),
        },
        {
            "q": "What should I wear at Glavani Park?",
            "a": (
                "Wear closed-toe sports shoes, comfortable fitted clothing, and no loose jewellery. "
                "Tie back long hair and bring sunscreen and water in summer. "
                "More detail on our <a href=\"{safety}\">safety page</a>."
            ),
        },
        {
            "q": "Is Glavani Park safe for first-time visitors?",
            "a": (
                "Yes. Every participant at Glavani Park receives a harness, helmet, and briefing from trained instructors. "
                "Equipment is CE-certified for adventure parks and checked daily before opening at 9 AM."
            ),
        },
        {
            "q": "Is there food at Glavani Park?",
            "a": (
                "Coffee, soft drinks, refreshments, and ice cream are available at a shaded picnic area at Glavani Park. "
                "You may bring snacks; there is no full restaurant on site."
            ),
        },
        {
            "q": "What payment methods do you accept at Glavani Park?",
            "a": (
                "We accept card and cash payments at the park ticket desk. "
                "Online gift vouchers can also be purchased by card on our gift voucher page."
            ),
        },
        {
            "q": "Can we book Glavani Park for a large group or birthday?",
            "a": (
                "Online booking covers up to 10 people. For groups of more than 10 — corporate events, schools, or birthdays — "
                "see <a href=\"{groups}\">team building and group packages</a> or call +385 91 896 4525."
            ),
        },
    ],
    "hr": [
        {
            "q": "Koje je radno vrijeme Glavani Parka?",
            "a": (
                "Glavani Park otvoren je svaki dan 9–17 h u sezoni. "
                "Posljednji ulaz u 15 h — planirajte tri do četiri sata za puni posjet."
            ),
        },
        {
            "q": BOOKING_POLICY["hr"]["faq_question"],
            "a": BOOKING_POLICY["hr"]["faq_answer"],
        },
        {
            "q": "Kako rezervirati Glavani Park online?",
            "a": (
                "Odaberite paket na stranici <a href=\"{book}\">Rezerviraj</a> ili pogledajte "
                "<a href=\"{prices}\">pakete i cijene</a>, odaberite datum i pošaljite zahtjev e-poštom. "
                "Za sve unaprijedne rezervacije odgovaramo e-računom za potvrdu što je prije moguće. "
                "Ako je posjet unutar 48 sati, molimo nazovite umjesto online obrasca."
            ),
        },
        {
            "q": "Koliko je Glavani Park udaljen od Pule?",
            "a": (
                "Glavani Park je otprilike 30 minuta automobilom iz Pule, 45 iz Rovinja i 10 iz Vodnjanja. "
                "Besplatno parkiranje na Glavani 10, 52207 Barban. "
                "Pogledajte <a href=\"{location}\">lokaciju i upute</a>."
            ),
        },
        {
            "q": "Koje dobne skupine mogu sudjelovati u Glavani Parku?",
            "a": (
                "Žuta trening ruta u Glavani Parku odgovara mlađoj djeci pod nadzorom odrasle osobe. "
                "Više atrakcije imaju minimalnu dob i visinu — nazovite +385 98 224 314 ako niste sigurni."
            ),
        },
        {
            "q": "Što trebam obući u Glavani Parku?",
            "a": (
                "Zatvorene sportske cipele, udobna pristrojena odjeća i bez labavog nakita. "
                "Duga kosa vezana; ljeti krema za sunce i voda. "
                "Više na stranici o <a href=\"{safety}\">sigurnosti</a>."
            ),
        },
        {
            "q": "Je li Glavani Park siguran za prvi posjet?",
            "a": (
                "Da. Svaki sudionik u Glavani Parku dobiva harnes, kacigu i obuku od instruktora. "
                "Oprema je CE certificirana za avanturističke parkove i dnevno se provjerava prije otvaranja u 9 h."
            ),
        },
        {
            "q": "Ima li hrane u Glavani Parku?",
            "a": (
                "Kava, bezalkoholna pića, osvježenja i sladoled dostupni su na osjenčanom piknik mjestu u Glavani Parku. "
                "Možete donijeti grickalice; nema punog restorana."
            ),
        },
        {
            "q": "Koje načine plaćanja prihvaćate u Glavani Parku?",
            "a": (
                "Na blagajni u parku prihvaćamo kartice i gotovinu. "
                "Poklon bon možete kupiti i online karticom na stranici poklon bona."
            ),
        },
        {
            "q": "Možemo li rezervirati Glavani Park za veću grupu ili rođendan?",
            "a": (
                "Online rezervacija vrijedi do 10 osoba. Za više od 10 — korporativne događaje, škole ili rođendane — "
                "pogledajte <a href=\"{groups}\">team building i grupne pakete</a> ili nazovite +385 98 224 314."
            ),
        },
    ],
}


def _faq_answer_html(lang: str, answer: str) -> str:
    links = FAQ_LINKS[lang]
    return answer.format(**links)


PAGE_FAQ_HEADINGS = {
    "en": "Frequently asked questions",
    "hr": "Često postavljana pitanja",
}


def resolve_faq_answer(lang: str, answer: str) -> str:
    if "{" in answer:
        return _faq_answer_html(lang, answer)
    return answer


def faq_answer_plain(lang: str, answer: str) -> str:
    html = resolve_faq_answer(lang, answer)
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()


def build_faq_schema(
    faqs: list[dict],
    lang: str,
    *,
    url: str,
    name: str,
    description: str | None = None,
) -> dict:
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": f"{url}#faq",
        "url": url,
        "name": name,
        "inLanguage": "hr-HR" if lang == "hr" else "en-GB",
        "isPartOf": {"@id": f"{BASE}/en/#glavani-park"},
        "about": {
            "@type": ["AmusementPark", "TouristAttraction"],
            "name": "Glavani Park",
            "url": f"{BASE}/en/",
        },
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_answer_plain(lang, faq["a"]),
                },
            }
            for faq in faqs
        ],
    }
    if description:
        schema["description"] = description
    return schema


def render_page_faq_section(faqs: list[dict], lang: str) -> str:
    if not faqs:
        return ""
    heading = PAGE_FAQ_HEADINGS[lang]
    items = []
    for faq in faqs:
        answer = resolve_faq_answer(lang, faq["a"])
        items.append(
            f'<details class="faq-item">'
            f'<summary>{faq["q"]}</summary>'
            f'<div class="faq-item__answer"><p>{answer}</p></div>'
            f"</details>"
        )
    return (
        f'<div class="faq-list-wrap">'
        f'<h2 id="page-faq-heading" class="faq-list__heading">{heading}</h2>'
        f'<div class="faq-list">{"".join(items)}</div>'
        f"</div>"
    )


def render_faq_list(lang: str) -> str:
    heading = FAQ_COPY[lang]["list_heading"]
    items = []
    for faq in VISITOR_FAQS[lang]:
        answer = resolve_faq_answer(lang, faq["a"])
        items.append(
            f'<details class="faq-item">'
            f'<summary>{faq["q"]}</summary>'
            f'<div class="faq-item__answer"><p>{answer}</p></div>'
            f"</details>"
        )
    return (
        f'<div class="faq-list-wrap">'
        f'<h2 class="faq-list__heading">{heading}</h2>'
        f'<div class="faq-list">{"".join(items)}</div>'
        f"</div>"
    )


def render_faq_related(lang: str) -> str:
    links = FAQ_LINKS[lang]
    heading = FAQ_COPY[lang]["related_heading"]
    cards = "".join(
        f'<a class="topic-link" href="{links[item["href"]]}">'
        f'{item["title"]}<span>{item["desc"]}</span></a>'
        for item in FAQ_RELATED[lang]
    )
    return f"""
    <section class="section section--alt">
      <div class="section__inner">
        <div class="section__heading"><h2>{heading}</h2></div>
        <div class="topic-grid">{cards}</div>
      </div>
    </section>"""
