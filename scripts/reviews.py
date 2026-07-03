"""Visitor reviews carousel — Google & TripAdvisor 5-star excerpts with named reviewers."""

GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Glavani+Park+Barban"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Search?q=Glavani+Park+Barban"
CAROUSEL_VISIBLE = 12

# All unique published TripAdvisor reviews — one entry per reviewer visit (no duplicates).
# Dates from TripAdvisor / Peek publication dates.
_ALL_REVIEWS = [
    {
        "source": "tripadvisor",
        "author": "Flyer13696210721",
        "date": "2026-08-04",
        "en": "Super nice park — different from the average climbing parks. Here you can choose a catapult or swing. We were four boys aged 16 and 18 and they enjoyed it. You can drink and buy ice cream between activities. Nice guidance.",
        "hr": "Super park — drugačiji od prosječnih penjačkih parkova. Možete odabrati katapultu ili ljuljačku. Bila su četiri dečka od 16 i 18 godina i uživali su. Možete popiti piće i kupiti sladoled između aktivnosti. Odlično vodstvo.",
    },
    {
        "source": "tripadvisor",
        "author": "Typingalong22",
        "date": "2026-08-03",
        "en": "A great adventure park in Croatia — really fun to explore all the different attractions. I would recommend it to any thrill seekers visiting the Istrian peninsula.",
        "hr": "Odličan avanturistički park u Hrvatskoj — zabavno je istraživati sve atrakcije. Toplo preporučujem svim ljubiteljima adrenalina na Istarskom poluotoku.",
    },
    {
        "source": "tripadvisor",
        "author": "Sandra",
        "date": "2026-07-08",
        "en": "A day full of adrenaline for our 15-year-old! Staff on site were super nice, helpful and always on hand. The human catapult alone is worth the visit — unique in Croatia. The 12 m swing, 120 m zipline at 30 m height and 20 m free fall make it a real experience. 100% recommended!",
        "hr": "Dan pun adrenalina za našeg 15-godišnjaka! Osoblje je bilo super, korisno i uvijek dostupno. Ljudska katapulta sama po sebi vrijedi posjeta — jedinstvena u Hrvatskoj. Ljuljačka od 12 m, zipline od 120 m na 30 m visine i slobodan pad s 20 m čine pravo iskustvo. 100% preporuka!",
    },
    {
        "source": "tripadvisor",
        "author": "Cruiser20282053316",
        "date": "2024-07-26",
        "en": "We had a great experience at the park! The instructors were friendly and gave clear instructions. And in the end we got some nice cold soft drinks.",
        "hr": "Odlično iskustvo u parku! Instruktori su bili ljubazni i dali jasne upute. Na kraju smo dobili i hladno piće.",
    },
    {
        "source": "tripadvisor",
        "author": "Piccolop126",
        "date": "2023-10-10",
        "en": "This was an amazing experience! The crew is amazing and the activities are great. Good stuff to do — thanks guys.",
        "hr": "Ovo je bilo nevjerojatno iskustvo! Ekipa je super, a aktivnosti su odlične. Ima puno toga za raditi — hvala ekipi.",
    },
    {
        "source": "tripadvisor",
        "author": "Renate V.",
        "date": "2023-08-13",
        "en": "We came back with our daughters, now 14, 12 and 10. The oldest even did the catapult — what a victory! Staff are really patient and friendly, and very helpful if things don't work out. The youngest couldn't get enough of it. Thanks for this wonderful day — we will definitely be back!",
        "hr": "Vratili smo se s kćerima, sada 14, 12 i 10 godina. Najstarija je čak probala katapultu — prava pobjeda! Osoblje je stvarno strpljivo i ljubazno, vrlo korisno kad nešto ne uspije odmah. Mlađa nije mogla dočekati ponovno. Hvala na prekrasan dan — sigurno se vraćamo!",
    },
    {
        "source": "tripadvisor",
        "author": "Pieter G.",
        "date": "2023-08-10",
        "en": "Fun park, fantastic staff. We had a great time — nice climbing and a fun catapult. We enjoyed this during our summer holiday.",
        "hr": "Zabavan park, fantastično osoblje. Odlično smo se proveli — lijepo penjanje i zabavna katapulta. Uživali smo tijekom ljetnog odmora.",
    },
    {
        "source": "tripadvisor",
        "author": "Margot K.",
        "date": "2023-08-04",
        "en": "We came with our kids aged 10, 8 and 6. Good explanation and support on the routes, then the giant swing together. Because you only pay for what you do, it is very affordable. Calm, helpful staff — a great day.",
        "hr": "Došli smo s djecom od 10, 8 i 6 godina. Odlična objašnjenja i podrška na stazama, zatim zajedno na veliku ljuljačku. Plaćate samo ono što radite, što je vrlo pristupačno. Mirno, korisno osoblje — sjajan dan.",
    },
    {
        "source": "tripadvisor",
        "author": "Béatrice",
        "date": "2023-08-01",
        "en": "Together with our kids aged 9 and 12 we had an amazing day out. The catapult accelerates so fast and the swing was fun for everyone! The best thing we have done in Istria — absolutely must do.",
        "hr": "S djecom od 9 i 12 godina proveli smo nevjerojatan dan. Katapulta je nevjerojatno brza, a ljuljačka je bila zabavna za sve! Najbolje što smo radili u Istri — apsolutno obavezno.",
    },
    {
        "source": "tripadvisor",
        "author": "Béatrice & family",
        "date": "2023-08-01",
        "en": "Best adventure park and greatest experience with the catapult — don't miss it! Nigel and his whole team are so professional and welcoming. We come back year after year and love sharing Glavani Park with friends.",
        "hr": "Najbolji avanturistički park i najbolje iskustvo s katapultom — ne propustite! Nigel i cijeli tim su profesionalni i gostoljubivi. Vraćamo se iz godine u godinu i rado preporučujemo park prijateljima.",
    },
    {
        "source": "tripadvisor",
        "author": "Georg B.",
        "date": "2023-07-11",
        "en": "Been here for the second time — it's great! Nigel's team is very accommodating and competent. Fully recommended. We will come back!",
        "hr": "Drugi put ovdje — odlično je! Nigelov tim je vrlo susretljiv i stručan. Potpuna preporuka. Vratit ćemo se!",
    },
    {
        "source": "tripadvisor",
        "author": "Skipper479",
        "date": "2023-07-07",
        "en": "We spent a lovely day with two children aged 9 and 12. The staff is very friendly and helpful. Anyone can try each attraction at their own pace.",
        "hr": "Proveli smo divan dan s dvoje djece od 9 i 12 godina. Osoblje je vrlo ljubazno i korisno. Svaki može isprobati atrakcije vlastitim tempom.",
    },
    {
        "source": "tripadvisor",
        "author": "Hans F.",
        "date": "2021-07-01",
        "en": "The human slingshot was absolutely the best! The hospitality of the host was very good — a nice guy to meet. It looks like it should be scary, but it's just fast.",
        "hr": "Ljudska katapulta je bila apsolutno najbolja! Gostoprimstvo domaćina bilo je vrlo dobro. Izgleda zastrašujuće, ali jednostavno je brzo.",
    },
]


def _dedupe_reviews(reviews: list[dict]) -> list[dict]:
    """Keep one entry per author and date, preferring the longer excerpt."""
    seen: dict[tuple[str, str], dict] = {}
    order: list[tuple[str, str]] = []
    for review in reviews:
        key = (review["author"], review["date"])
        if key not in seen:
            seen[key] = review
            order.append(key)
        elif len(review["en"]) > len(seen[key]["en"]):
            seen[key] = review
    return [seen[key] for key in order]


REVIEWS = _dedupe_reviews(_ALL_REVIEWS)

LABELS = {
    "en": {
        "heading": "What Visitors Say",
        "google": "Google",
        "tripadvisor": "TripAdvisor",
        "stars": "5 out of 5 stars",
        "prev": "Previous review",
        "next": "Next review",
        "read_google": "More on Google",
        "read_tripadvisor": "More on TripAdvisor",
    },
    "hr": {
        "heading": "Što kažu posjetitelji",
        "google": "Google",
        "tripadvisor": "TripAdvisor",
        "stars": "5 od 5 zvjezdica",
        "prev": "Prethodna recenzija",
        "next": "Sljedeća recenzija",
        "read_google": "Više na Googleu",
        "read_tripadvisor": "Više na TripAdvisoru",
    },
}


def _format_review_date(date_str: str, lang: str) -> str:
    year, month, _day = date_str.split("-")
    if lang == "hr":
        months = ["sij", "velj", "ožu", "tra", "svi", "lip", "srp", "kol", "ruj", "lis", "stu", "pro"]
        return f"{int(_day)}. {months[int(month) - 1]} {year}."
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{months[int(month) - 1]} {year}"


def _source_badge(source: str, labels: dict) -> str:
    mod = "google" if source == "google" else "tripadvisor"
    name = labels["google"] if source == "google" else labels["tripadvisor"]
    return f'<span class="review-card__source review-card__source--{mod}">{name}</span>'


def render_reviews_section(lang: str) -> str:
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    cards = []
    for review in REVIEWS:
        when = _format_review_date(review["date"], lang)
        cards.append(
            f"""<article class="review-card" data-review-author="{review['author']}" data-review-date="{review['date']}">
          {_source_badge(review["source"], labels)}
          <div class="review-card__stars" aria-label="{labels['stars']}">★★★★★</div>
          <blockquote class="review-card__quote"><p>{review[quote_key]}</p></blockquote>
          <cite class="review-card__author">{review['author']} · {when}</cite>
        </article>"""
        )
    cards_html = "\n        ".join(cards)
    return f"""<section class="section section--wide section--theme-reviews" id="reviews" aria-labelledby="reviews-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="reviews-heading">{labels['heading']}</h2>
        </div>
        <div class="reviews-carousel" data-reviews-carousel data-reviews-visible="{CAROUSEL_VISIBLE}">
          <button type="button" class="reviews-carousel__nav reviews-carousel__nav--prev" aria-label="{labels['prev']}" data-reviews-prev>‹</button>
          <div class="reviews-carousel__track" tabindex="0" data-reviews-track>
            {cards_html}
          </div>
          <button type="button" class="reviews-carousel__nav reviews-carousel__nav--next" aria-label="{labels['next']}" data-reviews-next>›</button>
        </div>
        <p class="reviews-carousel__links">
          <a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener noreferrer">{labels['read_google']}</a>
          <span aria-hidden="true">·</span>
          <a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer">{labels['read_tripadvisor']}</a>
        </p>
      </div>
    </section>"""
