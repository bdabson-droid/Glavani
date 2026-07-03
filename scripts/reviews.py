"""Visitor reviews carousel — Google & TripAdvisor 5-star excerpts with named reviewers."""

GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Glavani+Park+Barban"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Search?q=Glavani+Park+Barban"

# Authors and quotes from published TripAdvisor reviews (via Tripadvisor / Peek aggregation).
REVIEWS = [
    {
        "source": "tripadvisor",
        "author": "Sandra",
        "en": "A day full of adrenaline for our 15-year-old! The human catapult alone is worth the visit — unique in Croatia. The swing, zipline and free fall make it a real experience. 100% recommended!",
        "hr": "Dan pun adrenalina za našeg 15-godišnjaka! Ljudska katapulta sama po sebi vrijedi posjeta — jedinstvena u Hrvatskoj. Ljuljačka, zipline i slobodan pad čine pravo iskustvo. 100% preporuka!",
    },
    {
        "source": "tripadvisor",
        "author": "Hans F.",
        "en": "The human slingshot was absolutely the best! The hospitality of the host was very good — a nice guy to meet. It looks like it should be scary, but it's just fast.",
        "hr": "Ljudska katapulta je bila apsolutno najbolja! Gostoprimstvo domaćina bilo je vrlo dobro. Izgleda zastrašujuće, ali jednostavno je brzo.",
    },
    {
        "source": "tripadvisor",
        "author": "Renate V.",
        "en": "We came back with our daughters, now 14, 12 and 10. The oldest even did the catapult — what a victory! The youngest couldn't get enough of it. Thanks for this wonderful day — we will definitely be back!",
        "hr": "Vratili smo se s kćerima, sada 14, 12 i 10 godina. Najstarija je čak probala katapultu — prava pobjeda! Mlađa nije mogla dočekati ponovno. Hvala na prekrasan dan — sigurno se vraćamo!",
    },
    {
        "source": "tripadvisor",
        "author": "Margot K.",
        "en": "We came with our kids aged 10, 8 and 6. Good explanation and support on the routes, then the giant swing together. Because you only pay for what you do, it is very affordable. Calm, helpful staff — a great day.",
        "hr": "Došli smo s djecom od 10, 8 i 6 godina. Odlična objašnjenja i podrška na stazama, zatim zajedno na veliku ljuljačku. Plaćate samo ono što radite, što je vrlo pristupačno. Mirno, korisno osoblje — sjajan dan.",
    },
    {
        "source": "tripadvisor",
        "author": "Pieter G.",
        "en": "Fun park, fantastic staff. We had a great time — nice climbing and a fun catapult. We enjoyed this during our summer holiday.",
        "hr": "Zabavan park, fantastično osoblje. Odlično smo se proveli — lijepo penjanje i zabavna katapulta. Uživali smo tijekom ljetnog odmora.",
    },
    {
        "source": "tripadvisor",
        "author": "Georg B.",
        "en": "Been here for the second time — it's great! Nigel's team is very accommodating and competent. Fully recommended. We will come back!",
        "hr": "Drugi put ovdje — odlično je! Nigelov tim je vrlo susretljiv i stručan. Potpuna preporuka. Vratit ćemo se!",
    },
    {
        "source": "tripadvisor",
        "author": "Béatrice",
        "en": "Together with our kids aged 9 and 12 we had an amazing day out. The catapult accelerates so fast and the swing was fun for everyone! The best thing we have done in Istria — absolutely must do.",
        "hr": "S djecom od 9 i 12 godina proveli smo nevjerojatan dan. Katapulta je nevjerojatno brza, a ljuljačka je bila zabavna za sve! Najbolje što smo radili u Istri — apsolutno obavezno.",
    },
    {
        "source": "tripadvisor",
        "author": "Skipper479",
        "en": "We spent a lovely day with two children aged 9 and 12. The staff is very friendly and helpful. Anyone can try each attraction at their own pace.",
        "hr": "Proveli smo divan dan s dvoje djece od 9 i 12 godina. Osoblje je vrlo ljubazno i korisno. Svaki može isprobati atrakcije vlastitim tempom.",
    },
    {
        "source": "tripadvisor",
        "author": "Flyer13696210721",
        "en": "Super nice park — different from the average climbing parks. Here you can choose a catapult or swing. We were four boys aged 16 and 18 and they enjoyed it. Nice guidance.",
        "hr": "Super park — drugačiji od prosječnih penjačkih parkova. Možete odabrati katapultu ili ljuljačku. Bila su četiri dečka od 16 i 18 godina i uživali su. Odlično vodstvo.",
    },
    {
        "source": "tripadvisor",
        "author": "Typingalong22",
        "en": "A great adventure park in Croatia — really fun to explore all the different attractions. I would recommend it to any thrill seekers visiting the Istrian peninsula.",
        "hr": "Odličan avanturistički park u Hrvatskoj — zabavno je istraživati sve atrakcije. Toplo preporučujem svim ljubiteljima adrenalina na Istarskom poluotoku.",
    },
    {
        "source": "tripadvisor",
        "author": "Cruiser20282053316",
        "en": "We had a great experience at the park! The instructors were friendly and gave clear instructions. And in the end we got some nice cold soft drinks.",
        "hr": "Odlično iskustvo u parku! Instruktori su bili ljubazni i dali jasne upute. Na kraju smo dobili i hladno piće.",
    },
    {
        "source": "tripadvisor",
        "author": "Piccolop126",
        "en": "This was an amazing experience! The crew is amazing and the activities are great. Good stuff to do — thanks guys.",
        "hr": "Ovo je bilo nevjerojatno iskustvo! Ekipa je super, a aktivnosti su odlične. Ima puno toga za raditi — hvala ekipi.",
    },
]

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


def _source_badge(source: str, labels: dict) -> str:
    mod = "google" if source == "google" else "tripadvisor"
    name = labels["google"] if source == "google" else labels["tripadvisor"]
    return f'<span class="review-card__source review-card__source--{mod}">{name}</span>'


def render_reviews_section(lang: str) -> str:
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    cards = []
    for review in REVIEWS:
        cards.append(
            f"""<article class="review-card">
          {_source_badge(review["source"], labels)}
          <div class="review-card__stars" aria-label="{labels['stars']}">★★★★★</div>
          <blockquote class="review-card__quote"><p>{review[quote_key]}</p></blockquote>
          <cite class="review-card__author">{review['author']}</cite>
        </article>"""
        )
    cards_html = "\n        ".join(cards)
    return f"""<section class="section section--wide section--theme-reviews" id="reviews" aria-labelledby="reviews-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="reviews-heading">{labels['heading']}</h2>
        </div>
        <div class="reviews-carousel" data-reviews-carousel>
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
