"""Concise visitor FAQs for Glavani Park."""

FAQ_SLUGS = {"en": "faq", "hr": "cesta-pitanja"}

FAQ_COPY = {
    "en": {
        "title": "FAQ | Glavani Park Istria",
        "meta_description": (
            "Quick answers about Glavani Park — opening hours, booking, location near Pula, "
            "ages, safety, and what to expect at Istria's adventure park."
        ),
        "keywords": (
            "Glavani Park FAQ, adventure park Istria, zipline park Croatia, visit Glavani Park, "
            "booking Pula, outdoor activities Istria"
        ),
        "h1": "FAQ",
        "lead": "Quick answers for visitors planning a day at Glavani Park.",
        "book_note": "Ready to visit? Book online for up to 6 people, or call for larger groups.",
    },
    "hr": {
        "title": "Česta pitanja | Glavani Park Istria",
        "meta_description": (
            "Brzi odgovori o Glavani Parku — radno vrijeme, rezervacija, lokacija kod Pule, "
            "dob, sigurnost i što očekivati u avanturističkom parku u Istri."
        ),
        "keywords": (
            "Glavani Park FAQ, avanturistički park Istria, zipline park Hrvatska, posjet Glavani Parku, "
            "rezervacija Pula, aktivnosti na otvorenom Istria"
        ),
        "h1": "Česta pitanja",
        "lead": "Brzi odgovori za posjetitelje koji planiraju dan u Glavani Parku.",
        "book_note": "Spremni za posjet? Rezervirajte online do 6 osoba ili nazovite za veće grupe.",
    },
}

VISITOR_FAQS = {
    "en": [
        {
            "q": "What are your opening hours?",
            "a": "Open daily 9 AM–5 PM. Last entry is 3 PM — allow three to four hours for a full visit.",
        },
        {
            "q": "Do I need to book ahead?",
            "a": "Walk-ins are welcome, but booking ahead is recommended on weekends and in July and August. Fill in the online form and we'll confirm via SMS or WhatsApp as soon as possible.",
        },
        {
            "q": "How do I book online?",
            "a": "Choose a package on our Book page, pick a date, and send your details via WhatsApp or SMS. Within 48 hours of your visit date, please call to book instead.",
        },
        {
            "q": "How far is Glavani Park from Pula?",
            "a": "About 30 minutes by car from Pula, 45 from Rovinj, and 10 from Vodnjan. Free parking at Glavani 10, 52207 Barban.",
        },
        {
            "q": "What ages can take part?",
            "a": "The yellow training route suits younger children with adult supervision. Taller attractions such as the Human Catapult and Quick Jump have minimum age and height limits — call ahead if unsure.",
        },
        {
            "q": "What should we wear?",
            "a": "Closed-toe sports shoes, comfortable fitted clothing, no loose jewellery. Tie back long hair and bring sunscreen and water in summer.",
        },
        {
            "q": "Is the equipment safe?",
            "a": "Yes. Harnesses, helmets, and connections are CE-certified for adventure parks and checked daily before opening. Instructors brief every participant.",
        },
        {
            "q": "Is there food on site?",
            "a": "Coffee, soft drinks, and ice cream are available at a shaded picnic area. You may bring snacks; there is no full restaurant on site.",
        },
        {
            "q": "Can we book for a large group?",
            "a": "Online booking is for up to 6 people. For groups of 7 or more — corporate events, schools, or birthdays — call +385 91 896 4525 to arrange your visit.",
        },
    ],
    "hr": [
        {
            "q": "Koje je radno vrijeme?",
            "a": "Otvoreno svaki dan 9–17 h. Posljednji ulaz u 15 h — planirajte tri do četiri sata za puni posjet.",
        },
        {
            "q": "Trebam li rezervirati unaprijed?",
            "a": "Dolazak bez rezervacije moguć je, ali preporučujemo rezervaciju vikendom te u srpnju i kolovozu. Ispunite online obrazac — potvrdu šaljemo SMS-om ili WhatsAppom što prije.",
        },
        {
            "q": "Kako rezervirati online?",
            "a": "Odaberite paket na stranici Rezerviraj, odaberite datum i pošaljite podatke WhatsAppom ili SMS-om. Unutar 48 sati od termina molimo nazovite.",
        },
        {
            "q": "Koliko je park udaljen od Pule?",
            "a": "Otprilike 30 minuta automobilom iz Pule, 45 iz Rovinja i 10 iz Vodnjanja. Besplatno parkiranje na Glavani 10, 52207 Barban.",
        },
        {
            "q": "Koje dobne skupine mogu sudjelovati?",
            "a": "Žuta trening ruta odgovara mlađoj djeci pod nadzorom odrasle osobe. Više atrakcije imaju minimalnu dob i visinu — nazovite unaprijed ako niste sigurni.",
        },
        {
            "q": "Što trebamo obući?",
            "a": "Zatvorene sportske cipele, udobna pristrojena odjeća, bez labavog nakita. Duga kosa vezana; ljeti krema za sunce i voda.",
        },
        {
            "q": "Je li oprema sigurna?",
            "a": "Da. Harnes, kacige i spojnice CE su certificirani za avanturističke parkove i dnevno se provjeravaju prije otvaranja. Instruktori provode obuku svakog sudionika.",
        },
        {
            "q": "Ima li hrane u parku?",
            "a": "Kava, sokovi i sladoled dostupni su na osjenčanom piknik mjestu. Možete donijeti grickalice; nema punog restorana.",
        },
        {
            "q": "Možemo li rezervirati za veću grupu?",
            "a": "Online rezervacija vrijedi do 6 osoba. Za 7 i više — korporativne događaje, škole ili rođendane — nazovite +385 98 224 314.",
        },
    ],
}


def render_faq_list(lang: str) -> str:
    items = []
    for faq in VISITOR_FAQS[lang]:
        items.append(
            f'<details class="faq-item">'
            f'<summary>{faq["q"]}</summary>'
            f'<div class="faq-item__answer"><p>{faq["a"]}</p></div>'
            f"</details>"
        )
    return f'<div class="faq-list">{"".join(items)}</div>'
