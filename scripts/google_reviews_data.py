"""Curated Google reviews shown on activity pages (below TripAdvisor)."""

from __future__ import annotations

GOOGLE_REVIEWS: list[dict] = [
    {
        "author": "Charlotte",
        "date": "2026",
        "rating": 5,
        "featured_for": ["human-catapult"],
        "en": (
            "Nigel, Nivenko and the rest of their team were absolutely amazing. We called in the morning "
            "before heading to the park because we were quite a distance away, and it was forecasted to rain, "
            "but Nigel assured us that he would make it work for us, and it absolutely did!! It did not rain, "
            "and because we were a distance away, Nigel even so kindly offered to give us a lift! The park "
            "itself was barrels of fun, we did all the activities, and they did not disappoint. The human "
            "catapult was insane!! So fast, and so much fun!! The obstacles were challenging, but still "
            "placed at a suitable height, and can be enjoyed by both children and adults. I recommend trying "
            "all of the activities, and give yourself at least 4 hours on the park to do so. The park dog was "
            "also extremely adorable and friendly. We were sent off with some cake and strawberries that were "
            "so delicious. Many thanks to the Glavani Park team, and we'll definitely be back!"
        ),
        "hr": (
            "Nigel, Nivenko i cijeli tim bili su nevjerojatni. Nazvali smo ujutro prije dolaska jer smo bili "
            "dosta daleko, a prognozirala se kiša, ali Nigel nas je uvjerio da će sve biti u redu — i bilo je! "
            "Kiša nije padala, a budući da smo bili daleko, Nigel nam je ljubazno ponudio i prijevoz! Park je "
            "bio pun zabave, probali smo sve aktivnosti i nisu razočarale. Ljudska katapulta je bila "
            "nevjerojatna — tako brza i zabavna! Prepreke su bile izazovne, ali na prikladnoj visini za djecu "
            "i odrasle. Preporučujem sve aktivnosti i barem četiri sata u parku. Pas u parku bio je presladak "
            "i druželjubiv. Otišli smo s kolačem i jagodama — bilo je preukusno. Hvala timu Glavani Parka, "
            "definitivno se vraćamo!"
        ),
    },
    {
        "author": "N W",
        "date": "2025",
        "rating": 5,
        "featured_for": ["high-swing", "20m-drop"],
        "en": (
            "We had such a great time here at the park. All the rides here are very safe (that's our main "
            "concern). We had around 3 hours here and we end up went to all the rides, it was so much fun!!! "
            "Nigel and his crew will accompany you all the way so you are not doing this alone. Thanks again "
            "for such an amazing experience!"
        ),
        "hr": (
            "Odlično smo se proveli u parku. Sve atrakcije su vrlo sigurne — to nam je bila glavna briga. "
            "Bili smo oko tri sata i stigli smo na sve vožnje, bilo je super zabavno! Nigel i ekipa su uz "
            "vas cijelo vrijeme, niste sami. Hvala još jednom na nevjerojatnom iskustvu!"
        ),
    },
    {
        "author": "Rowan Hope",
        "date": "2026",
        "rating": 5,
        "featured_for": ["valley-zipline", "climbing-wall"],
        "en": (
            "I struggle to find the words to describe how pleasant a time my girlfriend and I had a Glavani "
            "park today. We called up the morning of our visit as we were unsure of the weather conditions "
            "and we understood that it was relatively late notice on our part. Nigel couldn't have been more "
            "kind and accommodating, assuring us that it would be fine and even recommended the ideal time "
            "to arrive. We paid for all of the games and rides, and I would recommend anyone who visits to "
            "do the same! The park boasts a perfect mixture of an adrenaline and calm. The climbing parts of "
            "the park are structured that the level of difficulty gradually increases, allowing for anyone who "
            "tackles it to get a feel for the equipment and prepares them for the more intense and challenging "
            "parts! And by golly are they intense! The zip-line (arguably the best in pula) and the catapult "
            "were insane! However the day was made perfect by the personalities of the staff at the park. The "
            "kindness and humour they bring give the park a certain charm that you simply won't find anywhere "
            "else. Would 100% recommend glavani park to any one visiting or native to Pula! Thank you guys !"
        ),
        "hr": (
            "Teško mi je opisati koliko smo se moja djevojka i ja danas ugodno proveli u Glavani Parku. "
            "Nazvali smo ujutro jer nismo bili sigurni u vrijeme, a znali smo da je kratka najava — Nigel "
            "nije mogao biti ljubazniji, uvjerio nas je da će biti u redu i preporučio idealno vrijeme dolaska. "
            "Platili smo sve igre i vožnje — svakome preporučujem isto! Park nudi savršen spoj adrenalina i "
            "mira. Dijelovi s penjanjem grade se postupno — težina raste, upoznajete opremu i pripremite se za "
            "intenzivnije dijelove! A intenzivni su! Zipline (vjerojatno najbolji kod Pule) i katapult bili "
            "su nevjerojatni! Dan su upotpunili ljubaznost i humor osoblja — šarm koji nećete naći drugdje. "
            "100% preporučujem Glavani Park svima u Puli i okolici! Hvala vam!"
        ),
    },
    {
        "author": "Michal Pysny",
        "date": "2025",
        "rating": 5,
        "featured_for": ["training-route", "low-zipline"],
        "en": (
            "We visited this gorgeous place with our 2 daughters - 6 & 7 years old. It was definitely worth "
            "of to travel 30 minutes from Pula. It is all but not overcrowded place. Calm and quiet atmosphere, "
            "professional and very friendly approach from experienced guides. Tracks were prepared and planned "
            "with professional attitude, girls experienced a lot of fun, learned technique and we were unable "
            "to stop them. Tracks were not easy, girls gave best of them. But in every moment we felt safe "
            "and secured. Tommorow it will be tough decision whether to come back or go to see ;)"
        ),
        "hr": (
            "Posjetili smo ovo prekrasno mjesto s dvije kćeri od 6 i 7 godina. Vrijedilo je putovati 30 "
            "minuta od Pule. Nije pretrpano — mirna atmosfera i profesionalan, vrlo prijateljski pristup "
            "iskusnih vodiča. Staze su bile dobro pripremljene, djevojčice su se odlično zabavile, naučile "
            "tehniku i nismo ih mogli zaustaviti. Staze nisu bile lake, ali smo se u svakom trenutku osjećali "
            "sigurno. Sutra će biti teška odluka — vratiti se ili ići negdje drugdje ;)"
        ),
    },
    {
        "author": "Xiao Chen",
        "date": "2024",
        "rating": 5,
        "featured_for": ["aerotrim"],
        "en": (
            "We had so much fun that the kids (5+6) wanted to go back again the next day - it was well worth "
            "the drive from Rovinj! Very friendly and helpful staff. Super chilled place. We will be back!"
        ),
        "hr": (
            "Djeca (5 i 6 godina) su se toliko zabavila da su htjela ponovno sljedeći dan — vrijedilo je "
            "vožnje iz Rovinja! Osoblje je vrlo ljubazno i korisno. Super opušteno mjesto. Vraćamo se!"
        ),
    },
    {
        "author": "Colin de Haar",
        "date": "2026",
        "rating": 5,
        "featured_for": ["climbing-wall", "low-zipline", "human-catapult"],
        "en": (
            "We spend a fantastic morning at Glavani Park. From entering the park it already had this great "
            "relaxed family feel to it. The staff was super nice and took their time to explain and help us "
            "where needed. Of course we had to do the catapult but all the attractions were great fun. "
            "Don't forget to do the climbing routes and zip lines in the shade of the trees and with some "
            "great music in the background. Pay them a visit!"
        ),
        "hr": (
            "Proveli smo fantastično jutro u Glavani Parku — već pri ulasku osjetite opuštenu obiteljsku "
            "atmosferu. Osoblje je bilo super i objašnjavalo sve što treba. Naravno, morali smo probati "
            "katapult, ali sve atrakcije su bile odlične. Ne propustite penjačke staze i zipline u hladu "
            "drveća uz odličnu glazbu. Posjetite ih!"
        ),
    },
    {
        "author": "Carsten Stauer",
        "date": "2026",
        "rating": 5,
        "featured_for": ["devils-causeway"],
        "en": (
            "A must for every adventurer and adrenaline junkie! Worth every penny! Better than any commercial "
            "theme park. And the staff/owners are incredibly welcoming."
        ),
        "hr": (
            "Obavezno za svakog avanturistu i ljubitelja adrenalina! Vrijedi svake kune — bolje od bilo "
            "kakvog komercijalnog tematskog parka. Osoblje i vlasnici nevjerojatno su gostoljubivi."
        ),
    },
]


def google_review_list() -> list[dict]:
    return GOOGLE_REVIEWS
