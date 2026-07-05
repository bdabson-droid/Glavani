"""Shared visitor booking policy copy — Saturdays and off-season are pre-book only."""

BOOKING_POLICY = {
    "en": {
        "faq_question": "Can I visit without a booking?",
        "faq_answer": (
            "<strong>Saturdays are pre-booking only</strong> — we do not accept walk-ins. "
            "From the <strong>end of September until the start of July</strong>, all visits must be booked in advance; "
            "<strong>no walk-ins</strong> during that period. "
            "From the start of July through the end of September, walk-ins are welcome "
            "<strong>Sunday to Friday</strong>, subject to availability. "
            "Use the <a href=\"{book}\">online booking form</a> or call +385 91 896 4525."
        ),
        "activity_answer": (
            "Saturdays are pre-booking only — no walk-ins. From the end of September until the start of July, "
            "{name} and all other attractions require advance booking; walk-ins are not accepted. "
            "From July through the end of September, walk-ins may be accepted Sunday to Friday "
            "(9 AM–5 PM, last entry 3 PM), subject to availability — book online or call +385 91 896 4525."
        ),
        "home_notice": (
            "<strong>Saturdays: pre-booking only.</strong> From late September to early July, all visits must be "
            "booked in advance — no walk-ins. Walk-ins Sunday to Friday may be accepted in peak season (July–September) only."
        ),
        "book_page": (
            "<strong>Booking policy:</strong> Saturdays are pre-booking only — no walk-ins. From the end of September "
            "until the start of July, all visits require advance booking; walk-ins are not accepted. Walk-ins Sunday to Friday "
            "may be accepted from July through the end of September, subject to availability."
        ),
        "info_strip_label": "Booking policy",
        "info_strip_value": "Sat & Oct–Jun: pre-book only",
        "summary_paragraph": (
            "Glavani Park is open daily from 9 AM to 5 PM with last entry at 3 PM. "
            "<strong>Saturdays are pre-booking only</strong> — no walk-ins. "
            "From the <strong>end of September until the start of July</strong>, all visits require advance booking; "
            "walk-ins are not accepted. From July through the end of September, walk-ins are welcome Sunday to Friday, "
            "subject to availability. English-speaking staff are on hand throughout the season."
        ),
    },
    "hr": {
        "faq_question": "Mogu li doći bez rezervacije?",
        "faq_answer": (
            "<strong>Subotom je moguća samo unaprijedna rezervacija</strong> — ne primamo dolazak bez najave. "
            "Od <strong>kraja rujna do početka srpnja</strong> svi posjeti moraju biti unaprijed rezervirani; "
            "<strong>dolazak bez rezervacije nije moguć</strong> u tom razdoblju. "
            "Od početka srpnja do kraja rujna dolazak bez rezervacije moguć je "
            "<strong>od nedjelje do petka</strong>, ovisno o dostupnosti. "
            "Koristite <a href=\"{book}\">online obrazac za rezervaciju</a> ili nazovite +385 98 224 314."
        ),
        "activity_answer": (
            "Subotom je moguća samo unaprijedna rezervacija — bez dolaska bez najave. Od kraja rujna do početka srpnja "
            "{name} i sve ostale atrakcije zahtijevaju unaprijednu rezervaciju; dolazak bez rezervacije nije moguć. "
            "Od srpnja do kraja rujna dolazak bez rezervacije moguć je od nedjelje do petka "
            "(9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — rezervirajte online ili nazovite +385 98 224 314."
        ),
        "home_notice": (
            "<strong>Subotom samo unaprijedna rezervacija.</strong> Od kraja rujna do početka srpnja svi posjeti moraju "
            "biti rezervirani — bez dolaska bez najave. Dolazak bez rezervacije moguć je od nedjelje do petka u vrhu sezone "
            "(srpanj–rujan)."
        ),
        "book_page": (
            "<strong>Pravila rezervacije:</strong> subotom je moguća samo unaprijedna rezervacija — bez dolaska bez najave. "
            "Od kraja rujna do početka srpnja svi posjeti zahtijevaju unaprijednu rezervaciju; dolazak bez rezervacije nije "
            "moguć. Dolazak bez rezervacije moguć je od nedjelje do petka od srpnja do kraja rujna, ovisno o dostupnosti."
        ),
        "info_strip_label": "Rezervacije",
        "info_strip_value": "Sub & lis–lip: samo najava",
        "summary_paragraph": (
            "Glavani Park radi svaki dan od 9 do 17 sati, posljednji ulaz u 15 sati. "
            "<strong>Subotom je moguća samo unaprijedna rezervacija</strong> — bez dolaska bez najave. "
            "Od <strong>kraja rujna do početka srpnja</strong> svi posjeti moraju biti unaprijed rezervirani; "
            "dolazak bez rezervacije nije moguć. Od srpnja do kraja rujna dolazak bez rezervacije moguć je od nedjelje do petka, "
            "ovisno o dostupnosti. Instruktori govore hrvatski i engleski."
        ),
    },
}


def activity_booking_answer(lang: str, activity_name: str) -> str:
    template = BOOKING_POLICY[lang]["activity_answer"]
    return template.format(name=activity_name)
