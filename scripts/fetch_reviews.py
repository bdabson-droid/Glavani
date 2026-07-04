#!/usr/bin/env python3
"""Fetch Glavani Park TripAdvisor reviews and aggregate stats from Peek.com (TripAdvisor-sourced)."""

from __future__ import annotations

import html
import json
import re
import urllib.request
from pathlib import Path

PEEK_URL = (
    "https://www.peek.com/glavani-istarska-upanija-croatia/r0bvw97/"
    "glavani-park-largest-high-ropes-climbing-course-in-croatia-for-family-adventure/a0dpyrme"
)
TRIPADVISOR_URL = (
    "https://www.tripadvisor.com/Attraction_Review-g295382-d7377536-Reviews-Glavani_Park-Barban_Istria.html"
)
OUTPUT = Path(__file__).resolve().parent / "reviews_snapshot.json"

MONTHS = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
}

# Croatian excerpts where we already have good translations (matched by author).
HR_OVERRIDES = {
    "Flyer13696210721": (
        "Super park — drugačiji od prosječnih penjačkih parkova. Možete odabrati katapultu ili ljuljačku. "
        "Bila su četiri dečka od 16 i 18 godina i uživali su. Možete popiti piće i kupiti sladoled "
        "između aktivnosti. Odlično vodstvo."
    ),
    "Typingalong22": (
        "Odličan avanturistički park u Hrvatskoj — zabavno je istraživati sve atrakcije. "
        "Toplo preporučujem svim ljubiteljima adrenalina na Istarskom poluotoku."
    ),
    "Sandra": (
        "Dan pun adrenalina za našeg 15-godišnjaka! Osoblje je bilo super, korisno i uvijek dostupno. "
        "Ljudska katapulta sama po sebi vrijedi posjeta — jedinstvena u Hrvatskoj. Ljuljačka od 12 m, "
        "zipline od 120 m na 30 m visine i slobodan pad s 20 m čine pravo iskustvo. 100% preporuka!"
    ),
    "Cruiser20282053316": (
        "Odlično iskustvo u parku! Instruktori su bili ljubazni i dali jasne upute. Na kraju smo dobili i hladno piće."
    ),
    "Piccolop126": (
        "Ovo je bilo nevjerojatno iskustvo! Ekipa je super, a aktivnosti su odlične. Ima puno toga za raditi — hvala ekipi."
    ),
    "21renatev": (
        "Vratili smo se s kćerima, sada 14, 12 i 10 godina. Najstarija je čak probala katapultu — prava pobjeda! "
        "Osoblje je stvarno strpljivo i ljubazno, vrlo korisno kad nešto ne uspije odmah. "
        "Mlađa nije mogla dočekati ponovno. Hvala na prekrasan dan — sigurno se vraćamo!"
    ),
    "439pieterg": (
        "Zabavan park, fantastično osoblje. Odlično smo se proveli — lijepo penjanje i zabavna katapulta. "
        "Uživali smo tijekom ljetnog odmora."
    ),
    "Margok914": (
        "Došli smo s djecom od 10, 8 i 6 godina. Odlična objašnjenja i podrška na stazama, zatim zajedno na veliku ljuljačku. "
        "Plaćate samo ono što radite, što je vrlo pristupačno. Mirno, korisno osoblje — sjajan dan."
    ),
    "Georgb690": (
        "Drugi put ovdje — odlično je! Nigelov tim je vrlo susretljiv i stručan. Potpuna preporuka. Vratit ćemo se!"
    ),
    "Skipper479": (
        "Proveli smo divan dan s dvoje djece od 9 i 12 godina. Osoblje je vrlo ljubazno i korisno. "
        "Svaki može isprobati atrakcije vlastitim tempom."
    ),
}


def _parse_date(label: str) -> str:
    label = label.strip()
    match = re.match(r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})", label)
    if not match:
        return "2023-01-01"
    month, day, year = match.group(1), int(match.group(2)), match.group(3)
    return f"{year}-{MONTHS[month]}-{day:02d}"


def _display_author(author: str) -> str:
    mapping = {
        "21renatev": "Renate V.",
        "439pieterg": "Pieter G.",
        "Margok914": "Margot K.",
        "Georgb690": "Georg B.",
    }
    return mapping.get(author, author)


def fetch_peek_reviews() -> tuple[dict, list[dict]]:
    request = urllib.request.Request(PEEK_URL, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(request, timeout=30).read().decode("utf-8", errors="replace")

    agg = re.search(
        r'"aggregateRating":\{"@type":"AggregateRating","ratingCount":(\d+),"ratingValue":"([^"]+)"\}',
        raw,
    )
    if not agg:
        raise RuntimeError("Could not parse TripAdvisor aggregate rating from Peek.com")

    rating_count = int(agg.group(1))
    rating_value = round(float(agg.group(2)), 1)

    authors = re.findall(r'"author":\{"@type":"Person","name":"([^"]+)"\}', raw)
    texts = [
        html.unescape(re.sub(r"\s+", " ", block.strip()))
        for block in re.findall(
            r'class="my-2 prose plain-prose text-standard">\s*(.*?)\s*</div>',
            raw,
            re.S,
        )
    ]
    dates = [
        label.strip()
        for label in re.findall(
            r'class="ml-auto text-sm text-gray-700">\s*([^<]+)\s*</div>',
            raw,
        )
    ]

    if not (len(authors) == len(texts) == len(dates)):
        raise RuntimeError(
            f"Review parts mismatch: {len(authors)} authors, {len(texts)} texts, {len(dates)} dates"
        )

    reviews = []
    for author, text, date_label in zip(authors, texts, dates):
        display = _display_author(author)
        reviews.append(
            {
                "source": "tripadvisor",
                "author": display,
                "author_id": author,
                "date": _parse_date(date_label),
                "rating": 5,
                "en": text,
                "hr": HR_OVERRIDES.get(author, text),
            }
        )

    reviews.sort(key=lambda item: item["date"], reverse=True)

    aggregate = {
        "rating_value": rating_value,
        "rating_count": rating_count,
        "best_rating": 5,
        "worst_rating": 1,
        "source": "tripadvisor",
        "source_url": TRIPADVISOR_URL,
        "fetched_via": "peek.com",
    }
    return aggregate, reviews


def main() -> None:
    aggregate, reviews = fetch_peek_reviews()
    payload = {
        "aggregate": aggregate,
        "reviews": reviews,
        "fetched_review_count": len(reviews),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(reviews)} TripAdvisor reviews; aggregate {aggregate['rating_value']} / {aggregate['rating_count']}")


if __name__ == "__main__":
    main()
