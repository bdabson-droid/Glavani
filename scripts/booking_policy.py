"""Shared visitor booking policy copy — off-season visits are pre-book only."""

from brand_voice import ONLINE_BOOKING_MAX

BOOKING_POLICY = {
    "en": {
        "faq_question": "Can I visit without a booking?",
        "faq_answer": (
            "From the start of July through the end of September, <strong>walk-ins are welcome</strong> during opening hours "
            "(9 AM–5 PM, last entry 3 PM), <strong>subject to availability</strong> — call ahead to avoid disappointment, "
            "especially when we have a large group booking. "
            "From the <strong>end of September until the start of July</strong>, all visits must be booked in advance; "
            "<strong>no walk-ins</strong> during that period. "
            'Use the <a href="{book}">online booking form</a> or call +385 91 896 4525.'
        ),
        "activity_answer": (
            "From July through the end of September, walk-ins are welcome during opening hours "
            "(9 AM–5 PM, last entry 3 PM), subject to availability — call ahead to avoid disappointment, "
            "as we may not be able to accommodate walk-ins when we have a large group booking. "
            "From the end of September until the start of July, "
            "{name} and all other attractions require advance booking; walk-ins are not accepted."
        ),
        "home_notice": (
            "From July through September, walk-ins are welcome during opening hours, subject to availability — "
            "call ahead to avoid disappointment, especially on busy days or when we have large group bookings. "
            "From late September to early July, all visits must be booked in advance — no walk-ins."
        ),
        "book_note": (
            "From July through September, walk-ins are welcome during opening hours, subject to availability — "
            "call ahead to avoid disappointment, especially when we have large group bookings. "
            "From late September to early July, advance booking is required — no walk-ins. "
            f"Book online for up to {ONLINE_BOOKING_MAX} people, or call for larger groups."
        ),
        "book_page": (
            "<strong>Booking policy:</strong> From July through the end of September, walk-ins are welcome during "
            "opening hours (9 AM–5 PM, last entry 3 PM), subject to availability — call ahead to avoid disappointment, "
            "as we may not be able to accommodate walk-ins when we have a large group booking. "
            "From the end of September until the start of July, all visits require advance booking; "
            "walk-ins are not accepted."
        ),
        "peak_walkin_note": (
            "From July through September, walk-ins are welcome during opening hours "
            "(9 AM–5 PM, last entry 3 PM), subject to availability — call ahead to avoid disappointment."
        ),
        "off_season_note": (
            "From late September to early July, all visits must be booked in advance — no walk-ins."
        ),
    },
    "hr": {
        "faq_question": "Mogu li doći bez rezervacije?",
        "faq_answer": (
            "Od početka srpnja do kraja rujna <strong>dolazak bez rezervacije je dobrodošao</strong> tijekom radnog vremena "
            "(9–17 h, posljednji ulaz 15 h), <strong>ovisno o dostupnosti</strong> — nazovite unaprijed kako ne biste "
            "ostali razočarani, posebno ako imamo rezervaciju velike grupe. "
            "Od <strong>kraja rujna do početka srpnja</strong> svi posjeti moraju biti unaprijed rezervirani; "
            "<strong>dolazak bez rezervacije nije moguć</strong> u tom razdoblju. "
            'Koristite <a href="{book}">online obrazac za rezervaciju</a> ili nazovite +385 98 224 314.'
        ),
        "activity_answer": (
            "Od srpnja do kraja rujna dolazak bez rezervacije moguć je tijekom radnog vremena "
            "(9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — nazovite unaprijed kako ne biste ostali "
            "razočarani, jer ponekad ne možemo primiti dolazak bez rezervacije ako imamo rezervaciju velike grupe. "
            "Od kraja rujna do početka srpnja {name} i sve ostale atrakcije zahtijevaju unaprijednu rezervaciju; "
            "dolazak bez rezervacije nije moguć."
        ),
        "home_notice": (
            "Od srpnja do rujna dolazak bez rezervacije dobrodošao je tijekom radnog vremena, ovisno o dostupnosti — "
            "nazovite unaprijed kako ne biste ostali razočarani, posebno u prometnim danima ili kad imamo velike grupe. "
            "Od kraja rujna do početka srpnja svi posjeti moraju biti rezervirani — bez dolaska bez najave."
        ),
        "book_note": (
            "Od srpnja do rujna dolazak bez rezervacije dobrodošao je tijekom radnog vremena, ovisno o dostupnosti — "
            "nazovite unaprijed kako ne biste ostali razočarani, posebno kad imamo velike grupe. "
            "Od kraja rujna do početka srpnja potrebna je unaprijedna rezervacija — bez dolaska bez najave. "
            f"Rezervirajte online do {ONLINE_BOOKING_MAX} osoba ili nazovite za veće grupe."
        ),
        "book_page": (
            "<strong>Pravila rezervacije:</strong> od srpnja do kraja rujna dolazak bez rezervacije moguć je tijekom "
            "radnog vremena (9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — nazovite unaprijed kako ne biste "
            "ostali razočarani, jer ponekad ne možemo primiti dolazak bez rezervacije ako imamo rezervaciju velike grupe. "
            "Od kraja rujna do početka srpnja svi posjeti zahtijevaju unaprijednu rezervaciju; "
            "dolazak bez rezervacije nije moguć."
        ),
        "peak_walkin_note": (
            "Od srpnja do rujna dolazak bez rezervacije dobrodošao je tijekom radnog vremena "
            "(9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — nazovite unaprijed kako ne biste ostali razočarani."
        ),
        "off_season_note": (
            "Od kraja rujna do početka srpnja svi posjeti moraju biti unaprijed rezervirani — bez dolaska bez najave."
        ),
    },
}


def activity_booking_answer(lang: str, activity_name: str) -> str:
    template = BOOKING_POLICY[lang]["activity_answer"]
    return template.format(name=activity_name)
