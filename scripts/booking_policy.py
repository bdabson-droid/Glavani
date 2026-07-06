"""Shared visitor booking policy copy — off-season visits are pre-book only."""

BOOKING_POLICY = {
    "en": {
        "faq_question": "Can I visit without a booking?",
        "faq_answer": (
            "From the <strong>end of September until the start of July</strong>, all visits must be booked in advance; "
            "<strong>no walk-ins</strong> during that period. "
            "From the start of July through the end of September, walk-ins may be accepted during opening hours "
            "(9 AM–5 PM, last entry 3 PM), subject to availability — "
            "<strong>book in advance to guarantee your slot and avoid disappointment</strong>. "
            'Use the <a href="{book}">online booking form</a> or call +385 91 896 4525.'
        ),
        "activity_answer": (
            "From the end of September until the start of July, "
            "{name} and all other attractions require advance booking; walk-ins are not accepted. "
            "From July through the end of September, walk-ins may be accepted during opening hours "
            "(9 AM–5 PM, last entry 3 PM), subject to availability — "
            "book in advance to guarantee your slot and avoid disappointment."
        ),
        "home_notice": (
            "From late September to early July, all visits must be booked in advance — no walk-ins. "
            "In peak season (July–September) we may accept walk-ins during opening hours, subject to availability — "
            "book ahead to guarantee your slot and avoid disappointment."
        ),
        "book_page": (
            "<strong>Booking policy:</strong> From the end of September until the start of July, all visits require "
            "advance booking; walk-ins are not accepted. From July through the end of September, walk-ins may be "
            "accepted during opening hours (9 AM–5 PM, last entry 3 PM), subject to availability — "
            "we recommend booking in advance to guarantee your slot and avoid disappointment."
        ),
        "info_strip_label": "Booking policy",
        "info_strip_value": "Oct–Jun: pre-book only",
        "summary_paragraph": (
            "Glavani Park is open daily from 9 AM to 5 PM with last entry at 3 PM. "
            "From the <strong>end of September until the start of July</strong>, all visits require advance booking; "
            "walk-ins are not accepted. From July through the end of September, walk-ins may be accepted during "
            "opening hours, subject to availability — book in advance to guarantee your slot and avoid disappointment. "
            "English-speaking staff are on hand throughout the season."
        ),
        "peak_walkin_note": (
            "From July through the end of September, walk-ins may be accepted during opening hours "
            "(9 AM–5 PM, last entry 3 PM), subject to availability — "
            "book in advance to guarantee your slot and avoid disappointment."
        ),
        "off_season_note": (
            "From the end of September until the start of July, all visits require advance booking; "
            "walk-ins are not accepted."
        ),
    },
    "hr": {
        "faq_question": "Mogu li doći bez rezervacije?",
        "faq_answer": (
            "Od <strong>kraja rujna do početka srpnja</strong> svi posjeti moraju biti unaprijed rezervirani; "
            "<strong>dolazak bez rezervacije nije moguć</strong> u tom razdoblju. "
            "Od početka srpnja do kraja rujna dolazak bez rezervacije moguć je tijekom radnog vremena "
            "(9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — "
            "<strong>rezervirajte unaprijed kako biste osigurali termin i izbjegli razočaranje</strong>. "
            'Koristite <a href="{book}">online obrazac za rezervaciju</a> ili nazovite +385 98 224 314.'
        ),
        "activity_answer": (
            "Od kraja rujna do početka srpnja {name} i sve ostale atrakcije zahtijevaju unaprijednu rezervaciju; "
            "dolazak bez rezervacije nije moguć. Od srpnja do kraja rujna dolazak bez rezervacije moguć je "
            "tijekom radnog vremena (9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — "
            "rezervirajte unaprijed kako biste osigurali termin i izbjegli razočaranje."
        ),
        "home_notice": (
            "Od kraja rujna do početka srpnja svi posjeti moraju biti rezervirani — bez dolaska bez najave. "
            "U vrhu sezone (srpanj–rujan) dolazak bez rezervacije moguć je tijekom radnog vremena, ovisno o dostupnosti — "
            "rezervirajte unaprijed kako biste osigurali termin i izbjegli razočaranje."
        ),
        "book_page": (
            "<strong>Pravila rezervacije:</strong> od kraja rujna do početka srpnja svi posjeti zahtijevaju "
            "unaprijednu rezervaciju; dolazak bez rezervacije nije moguć. Od srpnja do kraja rujna dolazak bez "
            "rezervacije moguć je tijekom radnog vremena (9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — "
            "preporučujemo unaprijednu rezervaciju kako biste osigurali termin i izbjegli razočaranje."
        ),
        "info_strip_label": "Rezervacije",
        "info_strip_value": "Lis–lip: samo najava",
        "summary_paragraph": (
            "Glavani Park radi svaki dan od 9 do 17 sati, posljednji ulaz u 15 sati. "
            "Od <strong>kraja rujna do početka srpnja</strong> svi posjeti moraju biti unaprijed rezervirani; "
            "dolazak bez rezervacije nije moguć. Od srpnja do kraja rujna dolazak bez rezervacije moguć je "
            "tijekom radnog vremena, ovisno o dostupnosti — rezervirajte unaprijed kako biste osigurali termin "
            "i izbjegli razočaranje. Instruktori govore hrvatski i engleski."
        ),
        "peak_walkin_note": (
            "Od srpnja do kraja rujna dolazak bez rezervacije moguć je tijekom radnog vremena "
            "(9–17 h, posljednji ulaz 15 h), ovisno o dostupnosti — "
            "rezervirajte unaprijed kako biste osigurali termin i izbjegli razočaranje."
        ),
        "off_season_note": (
            "Od kraja rujna do početka srpnja svi posjeti moraju biti unaprijed rezervirani; "
            "dolazak bez rezervacije nije moguć."
        ),
    },
}


def activity_booking_answer(lang: str, activity_name: str) -> str:
    template = BOOKING_POLICY[lang]["activity_answer"]
    return template.format(name=activity_name)
