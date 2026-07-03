"""Visitor reviews carousel — Google & TripAdvisor 5-star excerpts with named reviewers."""

GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Glavani+Park+Barban"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Search?q=Glavani+Park+Barban"
CAROUSEL_VISIBLE = 12

# Pool of published TripAdvisor reviews — carousel shows 12 at random per visit.
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
    {
        "source": "tripadvisor",
        "author": "Béatrice & family",
        "en": "Best adventure park and greatest experience with the catapult — don't miss it! Nigel and his whole team are so professional and welcoming. We come back year after year and love sharing Glavani Park with friends.",
        "hr": "Najbolji avanturistički park i najbolje iskustvo s katapultom — ne propustite! Nigel i cijeli tim su profesionalni i gostoljubivi. Vraćamo se iz godine u godinu i rado preporučujemo park prijateljima.",
    },
    {
        "source": "tripadvisor",
        "author": "Sandra",
        "en": "Staff on site were super nice, helpful and always on hand. The 12 m swing, 120 m zipline at 30 m height and 20 m free fall — several attractions make the park a real experience.",
        "hr": "Osoblje je bilo super, korisno i uvijek dostupno. Ljuljačka od 12 m, zipline od 120 m na 30 m visine i slobodan pad s 20 m — nekoliko atrakcija čini pravo iskustvo.",
    },
    {
        "source": "tripadvisor",
        "author": "Renate V.",
        "en": "Staff are really patient and friendly — also very helpful if things don't work out. The children dared even more this time. When we are in the area again, we will definitely come back!",
        "hr": "Osoblje je stvarno strpljivo i ljubazno — vrlo korisno kad nešto ne uspije odmah. Djeca su se ovaj put usuđivala još više. Kad budemo opet u okolici, sigurno se vraćamo!",
    },
    {
        "source": "tripadvisor",
        "author": "Margot K.",
        "en": "We expected crowds but were one of the few families — very nice. Routes from 2 m up to 6 and 9 m. If you come back within a week, you don't pay again for attractions you already did.",
        "hr": "Očekivali smo gužvu, ali bili smo jedna od rijetkih obitelji — jako lijepo. Staze od 2 m do 6 i 9 m. Ako se vratite unutar tjedna, ne plaćate ponovo već odrađene atrakcije.",
    },
    {
        "source": "tripadvisor",
        "author": "Hans F.",
        "en": "Free beers after the parkour. The human slingshot was absolutely the best! The hospitality of the host was very good — a nice guy to meet.",
        "hr": "Besplatno pivo nakon parkoura. Ljudska katapulta je bila apsolutno najbolja! Gostoprimstvo domaćina bilo je vrlo dobro.",
    },
    {
        "source": "tripadvisor",
        "author": "Georg B.",
        "en": "We spent a few hours here on our second visit. Nigel's team is accommodating and competent — fully recommended for families who want real adventure.",
        "hr": "Proveli smo nekoliko sati ovdje na drugom posjetu. Nigelov tim je susretljiv i stručan — potpuna preporuka za obitelji koje žele pravu avanturu.",
    },
    {
        "source": "tripadvisor",
        "author": "Béatrice",
        "en": "The staff, led by a wonderfully laid-back Englishman, was very friendly and helpful. Beverages are really low price and the facilities are very clean. Absolutely must do in Istria!",
        "hr": "Osoblje, predvođeno opuštenim Englezom, bilo je vrlo ljubazno i korisno. Pića su vrlo jeftina, a prostorije čiste. Apsolutno obavezno u Istri!",
    },
    {
        "source": "tripadvisor",
        "author": "Flyer13696210721",
        "en": "You can drink and buy ice cream between activities. Different from average climbing parks — here you choose a catapult or swing. Nice guidance throughout.",
        "hr": "Možete popiti piće i kupiti sladoled između aktivnosti. Drugačije od prosječnih parkova — birate katapultu ili ljuljačku. Odlično vodstvo.",
    },
    {
        "source": "tripadvisor",
        "author": "Skipper479",
        "en": "Anyone can make one or the other attraction — or all of them — at their discretion and decide gradually. Lovely day with children aged 9 and 12.",
        "hr": "Svaki može odabrati jednu ili sve atrakcije — postupno i po želji. Divan dan s djecom od 9 i 12 godina.",
    },
    {
        "source": "tripadvisor",
        "author": "Pieter G.",
        "en": "Nice climbing and a fun catapult during our summer holiday. Fantastic staff made it a highlight of our trip to Istria.",
        "hr": "Lijepo penjanje i zabavna katapulta tijekom ljetnog odmora. Fantastično osoblje — vrhunac našeg putovanja u Istri.",
    },
    {
        "source": "tripadvisor",
        "author": "Typingalong22",
        "en": "Really fun to look around and see all of the different attractions. A great day out for thrill seekers on the Istrian peninsula.",
        "hr": "Zabavno je obići i vidjeti sve različite atrakcije. Odličan izlet za ljubitelje adrenalina na Istarskom poluotoku.",
    },
    {
        "source": "tripadvisor",
        "author": "Cruiser20282053316",
        "en": "Friendly instructors and clear instructions from start to finish. A welcoming park with a relaxed feel — we left with cold drinks and big smiles.",
        "hr": "Ljubazni instruktori i jasne upute od početka do kraja. Gostoljubiv park s opuštenom atmosferom — otišli smo s hladnim pićem i velikim osmijehom.",
    },
    {
        "source": "tripadvisor",
        "author": "Piccolop126",
        "en": "Amazing experience from start to finish. The crew keeps everything running smoothly and the activities are brilliant for a full day out.",
        "hr": "Nevjerojatno iskustvo od početka do kraja. Ekipa sve drži pod kontrolom, a aktivnosti su odlične za cijeli dan.",
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
