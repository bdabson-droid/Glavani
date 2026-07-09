"""Extra SEO body copy for activity pages — keeps rankings during migration."""

from __future__ import annotations

from activities import ACTIVITIES
from brand_voice import ONLINE_BOOKING_MAX
from faqs import FAQ_SLUGS
from packages import BOOKING_SLUGS, PRICES_SLUGS, booking_page_href, pricing_visit_footer_line


def _activity_href(lang: str, en_slug: str) -> str:
    for activity in ACTIVITIES:
        if activity["en_slug"] == en_slug:
            slug = activity["hr_slug"] if lang == "hr" else activity["en_slug"]
            return f"/{lang}/{slug}/"
    return f"/{lang}/"


def _links(lang: str) -> dict[str, str]:
    prefix = f"/{lang}/"
    return {
        "book": booking_page_href(lang),
        "prices": f"{prefix}{PRICES_SLUGS[lang]}/",
        "safety": f"{prefix}{'sigurnost' if lang == 'hr' else 'safety'}/",
        "faq": f"{prefix}{FAQ_SLUGS[lang]}/",
        "activities": f"{prefix}{'avanturisticki-park-hrvatska' if lang == 'hr' else 'adventure-park-croatia'}/",
        "high_swing": _activity_href(lang, "high-swing"),
        "valley_zipline": _activity_href(lang, "valley-zipline"),
        "drop_20m": _activity_href(lang, "20m-drop"),
        "training_route": _activity_href(lang, "training-route"),
        "low_zipline": _activity_href(lang, "low-zipline"),
        "devils_causeway": _activity_href(lang, "devils-causeway"),
        "climbing_wall": _activity_href(lang, "climbing-wall"),
        "aerotrim": _activity_href(lang, "aerotrim"),
        "human_catapult": _activity_href(lang, "human-catapult"),
        "pula": f"{prefix}{'sto-raditi-kod-pule' if lang == 'hr' else 'things-to-do-near-pula'}/",
        "istria": f"{prefix}{'sto-raditi-u-istri' if lang == 'hr' else 'things-to-do-in-istria'}/",
    }


def _shared_footer(lang: str, h1: str) -> str:
    links = _links(lang)
    online_max = ONLINE_BOOKING_MAX
    if lang == "hr":
        return f"""
<h2>Planiranje posjeta</h2>
<p>Glavani Park se nalazi u Glavanima 10, Barban — otprilike <strong>30 minuta vožnje od Pule</strong>, 45 minuta od Rovinja i Rabca te 50 minuta od Poreča. Besplatno parkiranje je na licu mjesta. Park radi <strong>svaki dan 9–17 h</strong>; posljednji ulaz u <strong>15 h</strong>, stoga planirajte tri do četiri sata za cijeli park.</p>
<p>Za {h1.lower()} i ostale atrakcije možete <a href="{links['book']}">rezervirati ulaznice online</a> za grupe do {online_max} osoba ili nazvati za veće grupe. Pogledajte <a href="{links['prices']}">pakete i cijene</a> — {pricing_visit_footer_line("hr")}.</p>
<h2>Sigurnost i oprema</h2>
<p>Svaka aktivnost u Glavani Parku vodi se pod nadzorom kvalificiranih instruktora. Oprema je CE certificirana i provjerava se dnevno. Prije početka dobivate harnes, kacigu i jasnu obuku. Više o standardima pročitajte na našoj <a href="{links['safety']}">stranici o sigurnosti</a>.</p>"""
    return f"""
<h2>Planning your visit</h2>
<p>Glavani Park is at Glavani 10, Barban — about <strong>30 minutes from Pula</strong>, 45 minutes from Rovinj and Rabac, and 50 minutes from Poreč. Free parking is on site. The park is open <strong>daily 9 AM–5 PM</strong> with <strong>last entry at 3 PM</strong>, so allow three to four hours for the whole park.</p>
<p>For {h1} and our other attractions you can <a href="{links['book']}">book tickets online</a> for groups up to {online_max} or call ahead for larger parties. See <a href="{links['prices']}">packages and prices</a> — {pricing_visit_footer_line("en")}.</p>
<h2>Safety and equipment</h2>
<p>Every activity at Glavani Park is instructor-led. Equipment is CE-certified and checked daily. You receive a harness, helmet, and clear briefing before you start. Read more on our <a href="{links['safety']}">safety page</a>.</p>"""


def _fmt(text: str, lang: str) -> str:
    """Interpolate link placeholders in SEO snippet strings."""
    return text.format(
        pricing_footer=pricing_visit_footer_line(lang),
        **_links(lang),
    )


def _human_catapult_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Osjetite 100 km/h u jednoj sekundi — jedina ljudska katapulta u Hrvatskoj</h2>",
            "<p>Ljudska katapulta u Glavani Parku jedna je od rijetkih horizontalnih katapulti u Europi. Ležite u sigurnom okviru dok elastična užad napinju — puštanje vas šalje s 0 na oko 100 km/h u otprilike jednoj sekundi. To nije vožnja koja traje minute: to je trenutak čistog adrenalina koji posjetitelji pamte godinama nakon odlaska iz Istre.</p>",
            "<p>Više od 9.000 lansiranja obavljeno je u Glavani Parku — i gotovo svi gosti odlaze s osmijehom (i ponekad krikom uzbuđenja). Ako tražite nešto što nećete naći na prosječnom obiteljskom parku u Hrvatskoj, ovo je to.</p>",
            "<h2>Što se događa kada se zavežete</h2>",
            "<p>Osoblje prilagođava harnes, provodi sigurnosnu obuku i nadzire svako lansiranje. Ležite u okviru dok se užad napinju; vi držite ručku za puštanje ili instruktor kontrolira trenutak — ovisno o postavci. Kad se užad otpuste, osjetit ćete ubrzanje trkaćeg automobila u jednom udaru — brže nego Formula 1 s mjesta. Zatim se nježno usporavate dok vas sustav vrati. Cijeli proces, uključujući obuku i čekanje u redu, obično traje 15–20 minuta po grupi.</p>",
            "<h2>Je li ljudska katapulta zastrašujuća?</h2>",
            "<p>Za većinu ljudi — ne. Mnogi posjetitelji dolaze nervozni i odlaze oduševljeni. Osjećaj je intenzivan, ali kratkotrajan: nema dugog visenja kao na nekim vrtoglavicama. Ako ste prošli zipline ili ljuljačku, katapulta je često sljedeći logičan korak. Ako ste potpuni početnik u adrenalinu, osoblje objašnjava svaki korak i možete gledati druge prije nego odlučite. Tinejdžeri i odrasli koji zadovoljavaju uvjete visine i dobi obično je vole.</p>",
            "<h2>Koliko je brza?</h2>",
            "<p>Lansiranje ide s 0 na oko 100 km/h u otprilike jednoj sekundi — ubrzanje brže nego kod Formule 1 s mjesta. To je ono što katapultu čini jedinstvenom: ne postepeno ubrzanje, nego trenutni naboj. Mnogi gosti kažu da je osjećaj uzbudljiviji od bungee skoka jer ubrzanje dolazi odmah, a ne nakon dugog pada.</p>",
            "<h2>Je li sigurna?</h2>",
            "<p>Da. Svako lansiranje vodi kvalificirani instruktor. Oprema je CE certificirana, provjerava se dnevno, a prije puštanja dobivate punu obuku i provjeru harnesa. Katapulta je projektirana za kontrolirano lansiranje i zaustavljanje — niste slobodni u zraku kao na bungeeju. Više o standardima na našoj <a href=\"{safety}\">stranici o sigurnosti</a>.</p>",
            "<h2>Tko može voziti? Dob, visina i težina</h2>",
            "<p>Primjenjuju se minimalna dob, visina i težina — pitajte na blagajni ili nazovite unaprijed ako niste sigurni. Osoblje provjerava svakog gosta prije lansiranja i savjetuje ako aktivnost nije prikladna. Djeca mlađa od tinejdžerske dobi obično ne ispunjavaju uvjete; stariji tinejdžeri i odrasli koji zadovoljavaju limite često uživaju u vožnji.</p>",
            "<h2>Koliko dugo traje iskustvo?</h2>",
            "<p>Sam lansirajući trenutak traje sekunde, ali osjećaj — ubrzanje brže od F1 automobila — ostaje s vama. Mnogi gosti kažu da je uzbudljiviji od bungee skoka jer ubrzanje osjetite odmah. Uključite vrijeme za obuku, prilagodbu harnesa i red: računajte 15–20 minuta po grupi na katapulti.</p>",
            "<h2>Mogu li gledatelji promatrati?</h2>",
            "<p>Da — i to je dio zabave. Prijatelji i obitelj mogu gledati s vidikovca uz osvježenja i sladoled dok čekaju vaš red. Često je jednako zabavno slušati reakciju nakon lansiranja kao i samo iskustvo. Savršeno za obiteljske grupe u kojima samo neki žele katapultu.</p>",
            "<h2>Cijene i paketi koji uključuju katapultu</h2>",
            "<p>Ljudska katapulta košta <strong>€40 po osobi</strong> kao pojedinačna aktivnost. Uključena je i u pakete cijelog parka s katapultom (€60 djeca / €70 odrasli), paket <strong>katapulta + ljuljačka</strong>, te obiteljske pakete za 4 ili 5 osoba. Pogledajte <a href=\"{prices}\">pakete i cijene</a> za cijeli pregled — {pricing_footer}.</p>",
            "<h2>Mogu li rezervirati samo katapultu?</h2>",
            f"<p>Da. Odaberite ljudsku katapultu kao pojedinačnu aktivnost (€40) na <a href=\"{{book}}\">stranici za rezervaciju</a> ili na blagajni u parku. Online rezervacija pokriva do {ONLINE_BOOKING_MAX} osoba; za veće grupe nazovite unaprijed.</p>",
            "<h2>Mogu li snimati vožnju?</h2>",
            "<p>Da — i mnogi gosti to rade. Trebat će vam prijatelj koji snima ili sigurno pričvršćena action kamera. Ne možemo preuzeti odgovornost za oštećenje vaše osobne opreme, stoga koristite pouzdano pričvršćenje. Lansiranje je spektakularno na videozapisu.</p>",
            "<h2>Kada je najbolje vrijeme?</h2>",
            "<p>Bilo kada tijekom radnog vremena parka (9–17 h, zadnji ulaz 15 h). Katapulta radi cijeli dan i redovi variraju — jutro i poslijepodne jednako su dobri. S više od 9.000 obavljenih lansiranja, gotovo svi gosti odlaze zadovoljni.</p>",
            "<h2>S čime kombinirati katapultu</h2>",
            "<p>Većina posjetitelja spaja katapultu s <a href=\"{high_swing}\">visokom ljuljačkom</a>, <a href=\"{valley_zipline}\">dolinskim ziplineom</a> ili <a href=\"{drop_20m}\">padom s 20 m</a> za puni adrenalinski dan. Pogledajte sve <a href=\"{activities}\">aktivnosti parka</a>, <a href=\"{faq}\">česta pitanja</a> ili vodič <a href=\"{istria}\">što raditi u Istri</a>.</p>",
        ]
    return [
        "<h2>Feel 100 km/h in one second on Croatia's only Human Catapult</h2>",
        "<p>The Human Catapult at Glavani Park is one of only a handful of horizontal catapult rides in Europe. You lie in a secure frame while elastic cables build tension — then release sends you from standstill to around 100 km/h in roughly one second. This is not a ride that lasts minutes: it is a moment of pure adrenaline that visitors remember for years after leaving Istria.</p>",
        "<p>More than 9,000 launches have been completed at Glavani Park — and almost every guest leaves smiling (and sometimes shouting with exhilaration). If you want something you will not find at an average family park in Croatia, this is it.</p>",
        "<h2>What happens when you strap in</h2>",
        "<p>Staff fit your harness, run a full safety briefing, and supervise every launch. You lie in the frame while the cables tension; you hold the release handle or the instructor controls the moment, depending on the setup. When the cables release, you feel race-car acceleration in a single hit — from standstill to around 100 km/h quicker than an F1 car off the line. Then you decelerate smoothly as the system brings you back. The whole process, including briefing and queue time, typically takes 15–20 minutes per group.</p>",
        "<h2>Is the Human Catapult scary?</h2>",
        "<p>For most people — no. Many visitors arrive nervous and leave thrilled. The sensation is intense but brief: there is no long hang time like on some fairground rides. If you have done a zipline or swing before, the catapult is often the next logical step. If you are completely new to adrenaline activities, staff explain every step and you can watch others go first. Teenagers and adults who meet the height and age requirements usually love it.</p>",
        "<h2>How fast does it go?</h2>",
        "<p>The launch takes you from 0 to around 100 km/h in roughly one second — quicker acceleration than a Formula 1 car from a standing start. That is what makes the catapult unique: not a gradual build-up, but an instant rush. Many guests say it feels more exhilarating than a bungee jump because you feel the acceleration immediately rather than after a long drop.</p>",
        "<h2>Is it safe?</h2>",
        "<p>Yes. Every launch is instructor-led. Equipment is CE-certified, checked daily, and you receive a full briefing and harness check before release. The catapult is engineered for controlled launch and deceleration — you are not free-falling like on a bungee. Read more about our standards on the <a href=\"{safety}\">safety page</a>.</p>",
        "<h2>Who can ride? Age, height and weight</h2>",
        "<p>Minimum age, height and weight limits apply — ask at the ticket desk or call ahead if you are unsure. Staff check every guest before launch and will advise if the activity is not suitable. Younger children typically do not meet the requirements; older teens and adults who fit the limits usually enjoy the ride.</p>",
        "<h2>How long does the experience take?</h2>",
        "<p>The launch itself lasts seconds, but the sensation — acceleration quicker than an F1 car — stays with you. Many guests say it is more exhilarating than a bungee jump because you feel the rush immediately. Allow time for briefing, harness fitting and queueing: plan on 15–20 minutes per group at the catapult.</p>",
        "<h2>Can spectators watch?</h2>",
        "<p>Yes — and it is part of the fun. Friends and family can watch from the viewing area with drinks and ice cream while they wait for your turn. It is often as entertaining to hear the reaction after launch as it is to ride. Perfect for family groups where only some want the catapult.</p>",
        "<h2>Prices and packages that include the catapult</h2>",
        "<p>The Human Catapult is <strong>€40 per person</strong> as a single activity. It is also included in whole-park packages with catapult (€60 children / €70 adults), the <strong>Human Catapult + High Swing</strong> combo, and family packages for 4 or 5 people. See <a href=\"{prices}\">packages and prices</a> for the full overview — {pricing_footer}.</p>",
        "<h2>Can I book the catapult on its own?</h2>",
        f"<p>Yes. Choose the Human Catapult as a single activity (€40) on the <a href=\"{{book}}\">booking page</a> or at the park ticket desk. Online booking covers up to {ONLINE_BOOKING_MAX} people; call ahead for larger groups.</p>",
        "<h2>Can I film my ride?</h2>",
        "<p>Yes — and many guests do. You will need a friend to film or a securely attached action camera. We cannot be held responsible for damage to your personal equipment, so use reliable mounting. The launch looks spectacular on video.</p>",
        "<h2>When is the best time to go?</h2>",
        "<p>Any time during park opening hours (9 AM–5 PM, last entry 3 PM). The catapult runs all day and queues vary — morning and afternoon are both good. With more than 9,000 launches completed, almost every guest leaves happy.</p>",
        "<h2>What to combine with the catapult</h2>",
        "<p>Most visitors pair the catapult with the <a href=\"{high_swing}\">12.5 m High Swing</a>, <a href=\"{valley_zipline}\">Valley Zip Line</a>, or <a href=\"{drop_20m}\">20 m Drop</a> for a full adrenaline day. Browse all <a href=\"{activities}\">park activities</a>, read our <a href=\"{faq}\">FAQ</a>, or see <a href=\"{istria}\">things to do in Istria</a> to plan your trip.</p>",
    ]


def _high_swing_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Penjite se 12,5 metara, povucite užad i osjetite najveću ljuljačku u Hrvatskoj</h2>",
            "<p>Visoka ljuljačka u Glavani Parku jedna je od najvećih ljuljački u Hrvatskoj. Nakon provjere harnesa penjete se na platformu 12,5 metara iznad šumskog tla, povlačite užad za puštanje sami i letite kroz hrastovu šumu u dugom zamašaju — mješavina nježnosti na vrhu i brzine na dnu.</p>",
            "<h2>Što očekivati</h2>",
            "<p>Instruktori pričvršćuju harnes, objašnjavaju položaj tijela i signale te kontroliraju svako puštanje i povratak na platformu. Vožnja traje nekoliko minuta uključujući penjanje i obuku. Ljuljačka pogoduje samouvjerenim tinejdžerima i odraslima koji zadovoljavaju uvjete visine.</p>",
            "<h2>Je li zastrašujuća?</h2>",
            "<p>Intenzivnija je od obiteljskih vožnji, ali mnogi gosti koji su prošli zipline ili trening rutu uživaju u ljuljački kao sljedećem koraku. Možete gledati druge prije nego odlučite. Osoblje je strpljivo i vodi vas kroz svaki korak.</p>",
            "<h2>Sigurnost i tko može voziti</h2>",
            "<p>Svako puštanje pod nadzorom je instruktora s CE certificiranom opremom. Primjenjuju se minimalna dob i visina — pitajte na blagajni. Više na <a href=\"{safety}\">stranici o sigurnosti</a>.</p>",
            "<h2>Cijene i kombinacije</h2>",
            "<p>Ljuljačka je uključena u pakete cijelog parka ili je dostupna u kombinaciji s <a href=\"{human_catapult}\">ljudskom katapultom</a>. Pogledajte <a href=\"{prices}\">pakete i cijene</a> ili <a href=\"{book}\">rezervirajte online</a>. Kombinirajte s <a href=\"{valley_zipline}\">dolinskim ziplineom</a> i <a href=\"{drop_20m}\">padom s 20 m</a>.</p>",
        ]
    return [
        "<h2>Climb 12 metres, pull the release cord yourself, and experience Croatia's biggest swing</h2>",
        "<p>Glavani Park's High Swing is one of the largest swings in Croatia. After your harness check you climb to the launch platform 12.5 metres above the forest floor, pull the release cord yourself, and arc through the oak canopy in a long pendulum — a mix of weightlessness at the top and speed at the bottom.</p>",
        "<h2>What to expect</h2>",
        "<p>Instructors secure your harness, explain body position and signals, and control each release and return to the platform. The ride takes a few minutes including the climb and briefing. The high swing suits confident teenagers and adults who meet height requirements.</p>",
        "<h2>Is it scary?</h2>",
        "<p>More intense than family rides, but many guests who have done the ziplines or training route enjoy the swing as a next step. You can watch others first. Staff are patient and guide you through every stage.</p>",
        "<h2>Safety and who can ride</h2>",
        "<p>Every release is instructor-led with CE-certified equipment. Minimum age and height apply — ask at the ticket desk. Read more on our <a href=\"{safety}\">safety page</a>.</p>",
        "<h2>Prices and combinations</h2>",
        "<p>The swing is included in whole-park packages or available in a combo with the <a href=\"{human_catapult}\">Human Catapult</a>. See <a href=\"{prices}\">packages and prices</a> or <a href=\"{book}\">book online</a>. Pair with the <a href=\"{valley_zipline}\">Valley Zip Line</a> and <a href=\"{drop_20m}\">20 m Drop</a> for a full adrenaline day.</p>",
    ]


def _training_route_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Obiteljski uvod u visoke staze — žuta ruta na 2 metra</h2>",
            "<p>Žuta trening ruta je mjesto gdje većina obitelji počinje u Glavani Parku. Na samo 2 metra visine djeca prolaze prave prepreke visokih staza — mostove, ravnotežu i mreže — dok roditelji hodaju uz stazu. Kontinuirano osiguranje drži sve povezane od početka do kraja.</p>",
            "<h2>Tko može sudjelovati</h2>",
            "<p>Ruta je dizajnirana za mlađu djecu i početnike uz odraslog. Instruktori objašnjavaju harnes, signale i kako savladati prepreke. Idealno za prvi posjet avanturističkom parku u Istri.</p>",
            "<h2>Sljedeći koraci u parku</h2>",
            "<p>Mnogi posjetitelji istog dana prelaze na <a href=\"{low_zipline}\">Stazu u krošnjama</a> i <a href=\"{devils_causeway}\">Stazu Vražjeg puta</a>. Paket Trening ruta + 2 igre obuhvaća sve igre osim katapulata — €20 za djecu, €30 za odrasle. Pogledajte <a href=\"{prices}\">cijene</a>.</p>",
        ]
    return [
        "<h2>Family-friendly introduction to high ropes — the 2-metre yellow route</h2>",
        "<p>The yellow training route is where most families start at Glavani Park. At just 2 metres high, children tackle real high-ropes obstacles — rope bridges, balance beams, and cargo nets — while parents walk alongside on the forest path. Continuous belay keeps everyone connected from start to finish.</p>",
        "<h2>Who can take part</h2>",
        "<p>The route is designed for younger children and first-timers with an adult nearby. Instructors explain harness fit, safety signals, and how to tackle each obstacle. Ideal for a first visit to an adventure park in Istria.</p>",
        "<h2>What to do next in the park</h2>",
        "<p>Many visitors progress to the <a href=\"{low_zipline}\">Treetop Course</a> and <a href=\"{devils_causeway}\">Devil's Causeway Course</a> the same day. The Training route + 2 games package covers all park games except the Human Catapult — €20 for children, €30 for adults. See <a href=\"{prices}\">prices</a>.</p>",
    ]


def _low_zipline_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Plave visoke staze i zipline od 113 metara na 6 metara visine</h2>",
            "<p>Staza u krošnjama spaja klasične elemente visokih staza sa ziplineom od 113 metara. Prirodan je korak nakon <a href=\"{training_route}\">žute trening rute</a> — više visine i brzine, ali i dalje pristupačno starijoj djeci uz odraslog.</p>",
            "<h2>Što očekivati</h2>",
            "<p>Računajte 45–90 minuta na stazi ovisno o redu i samopouzdanju. Instruktori su na ključnim točkama. Ostajete na kontinuiranom osiguranju od penjanja do slijetanja.</p>",
            "<h2>Kombinirajte s drugim atrakcijama</h2>",
            "<p>Nakon plave staze mnogi prelaze na <a href=\"{valley_zipline}\">dolinski zipline</a> ili <a href=\"{devils_causeway}\">Stazu Vražjeg puta</a>. Pogledajte <a href=\"{activities}\">sve aktivnosti</a> i <a href=\"{prices}\">pakete</a>.</p>",
        ]
    return [
        "<h2>Blue high-ropes and a 113-metre treetop zipline at 6 metres high</h2>",
        "<p>The Treetop Course combines classic high-ropes elements with a 113-metre zipline section. It is the natural step up from the <a href=\"{training_route}\">yellow training route</a> — more height and speed, but still manageable for older children with an adult nearby.</p>",
        "<h2>What to expect</h2>",
        "<p>Allow 45–90 minutes on the course depending on queue and confidence. Instructors are positioned at key points. You stay on continuous belay from climb to landing.</p>",
        "<h2>Combine with other attractions</h2>",
        "<p>After the blue course many move on to the <a href=\"{valley_zipline}\">Valley Zip Line</a> or <a href=\"{devils_causeway}\">Devil's Causeway Course</a>. Browse all <a href=\"{activities}\">activities</a> and <a href=\"{prices}\">packages</a>.</p>",
    ]


def _valley_zipline_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>120 metara kroz dolinu — do 20 metara visine</h2>",
            "<p>Dolinski zipline samostalno je iskustvo — dva leta naprijed-natrag preko hrastove doline, do 20 metara visine. Pogled na šumu i park koji fotografije rijetko prenose. Početnici dobivaju dodatne upute na platformi.</p>",
            "<h2>Što ponijeti i koliko trajati</h2>",
            "<p>Potrebna je zatvorena obuća i udobna odjeća. Računajte 30–60 minuta uključujući obuku i red. Stalni posjetitelji često navode dolinski zipline kao omiljenu vožnju.</p>",
            "<h2>Kombinirajte dan</h2>",
            "<p>Prirodno se kombinira sa <a href=\"{low_zipline}\">Stazom u krošnjama</a>, <a href=\"{high_swing}\">visokom ljuljačkom</a> i <a href=\"{human_catapult}\">ljudskom katapultom</a>. <a href=\"{book}\">Rezervirajte</a> ili pogledajte <a href=\"{prices}\">cijene</a>.</p>",
        ]
    return [
        "<h2>120 metres through the valley — up to 20 metres high</h2>",
        "<p>The Valley Zip Line is a standalone experience — two runs back and forth across the oak valley, reaching up to 20 metres high. You get forest and park views that photos rarely capture. First-timers receive extra guidance at the launch platform.</p>",
        "<h2>What to wear and how long it takes</h2>",
        "<p>Closed shoes and comfortable clothing are essential. Allow 30–60 minutes including briefing and queue. Returning visitors often cite the valley zipline as their favourite ride.</p>",
        "<h2>Plan a full day</h2>",
        "<p>Pairs naturally with the <a href=\"{low_zipline}\">Treetop Course</a>, <a href=\"{high_swing}\">High Swing</a>, and <a href=\"{human_catapult}\">Human Catapult</a>. <a href=\"{book}\">Book</a> or see <a href=\"{prices}\">prices</a>.</p>",
    ]


def _devils_causeway_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Najzahtjevniji izazov parka — monocikl, slackline i japanski most</h2>",
            "<p>Staza Vražjeg puta završnica je crne staze — skateboard, drveni most, prijelaz monociklom, slackline i japanski most. Nagrađuje posjetitelje koji su stekli samopouzdanje na <a href=\"{training_route}\">žutoj</a> i <a href=\"{low_zipline}\">plavoj</a> stazi.</p>",
            "<h2>Monocikl i ograničenja</h2>",
            "<p>Dio s monociklom jedinstven je u Hrvatskoj. Na most s monociklom vrijedi limit 85 kg; mala djeca moraju dohvatiti pedale. Osoblje može predložiti alternative. Ostavite dodatno vrijeme — mnogi gosti zastanu gledati druge.</p>",
            "<h2>Sljedeći koraci</h2>",
            "<p>Nakon crne staze mnogi idu na <a href=\"{valley_zipline}\">dolinski zipline</a> ili adrenalin <a href=\"{human_catapult}\">katapultu</a>. Više o <a href=\"{safety}\">sigurnosti</a>.</p>",
        ]
    return [
        "<h2>The park's toughest challenge — unicycle, slackline and Japanese bridge</h2>",
        "<p>The Devil's Causeway Course is the black-route finale — skateboard, wooden bridge, unicycle crossing, slackline, and Japanese bridge. It rewards visitors who have built confidence on the <a href=\"{training_route}\">yellow</a> and <a href=\"{low_zipline}\">blue</a> routes.</p>",
        "<h2>The unicycle and restrictions</h2>",
        "<p>The unicycle section is unique in Croatia. Weight limit 85 kg applies to the unicycle bridge; younger children must reach the pedals. Staff can advise alternatives. Allow extra time — many guests pause to watch others.</p>",
        "<h2>What to do next</h2>",
        "<p>After the black route many head to the <a href=\"{valley_zipline}\">Valley Zip Line</a> or the <a href=\"{human_catapult}\">Human Catapult</a>. Read more about <a href=\"{safety}\">safety</a>.</p>",
    ]


def _climbing_wall_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Penjanje na otvorenom za sve razine</h2>",
            "<p>Vanjski penjački zid u šumskoj čistini nudi više smjerova — od početničkih držala do strmijih izazova. Idealno za zagrijavanje prije <a href=\"{training_route}\">visokih staza</a>, školske grupe ili obitelji između većih vožnji.</p>",
            "<h2>Tko može penjati</h2>",
            "<p>Vožnje su pod nadzorom instruktora s harnesom i kacigom. Mlađa djeca često penju uz pomoć — pitajte osoblje o dobi i visini na ulazu.</p>",
            "<h2>Uključeno u pakete</h2>",
            "<p>Penjački zid uključen je u pakete cijelog parka. Pogledajte <a href=\"{prices}\">cijene</a> i <a href=\"{book}\">rezervaciju</a>.</p>",
        ]
    return [
        "<h2>Outdoor climbing for all levels</h2>",
        "<p>Our outdoor climbing wall sits in a forest clearing with multiple routes from beginner-friendly holds to steeper challenges. Ideal for warming up before the <a href=\"{training_route}\">high ropes routes</a>, school groups, or families taking a break between bigger rides.</p>",
        "<h2>Who can climb</h2>",
        "<p>Sessions are instructor-supervised with harness and helmet provided. Younger children often climb with assistance — ask staff about age and height suitability when you arrive.</p>",
        "<h2>Included in packages</h2>",
        "<p>The climbing wall is included in whole-park packages. See <a href=\"{prices}\">prices</a> and <a href=\"{book}\">booking</a>.</p>",
    ]


def _aerotrim_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>Ljudski žiroskop u šumi</h2>",
            "<p>Aerotrim vas okreće u više osi dok ste sigurno u okviru — osjećaj drugačiji od ziplinea i katapulata. Osoblje kontrolira brzinu i objašnjava položaj tijela. Popularan među tinejdžerima koji traže nešto drugačije.</p>",
            "<h2>Zdravstvena ograničenja</h2>",
            "<p>Primjenjuju se zdravstvena, visinska i dobna ograničenja. Ako ste osjetljivi na kretanje, pogledajte sesiju ili napravite pauzu uz osvježenje između vožnji.</p>",
            "<h2>Kombinirajte</h2>",
            "<p>Često se spaja s <a href=\"{human_catapult}\">katapultom</a> i <a href=\"{high_swing}\">ljuljačkom</a>. <a href=\"{prices}\">Paketi</a> · <a href=\"{faq}\">Pitanja</a></p>",
        ]
    return [
        "<h2>Human gyroscope in the forest</h2>",
        "<p>The Aerotrim spins you through multiple axes while you stay secured in the frame — a sensation unlike the ziplines and catapult. Staff control the speed and explain how to position your body. Popular with teenagers looking for something different.</p>",
        "<h2>Health restrictions</h2>",
        "<p>Health, height, and age restrictions apply. If you are prone to motion sickness, consider watching a session first or taking a break at our refreshments area between rides.</p>",
        "<h2>Combine your visit</h2>",
        "<p>Often paired with the <a href=\"{human_catapult}\">Human Catapult</a> and <a href=\"{high_swing}\">High Swing</a>. <a href=\"{prices}\">Packages</a> · <a href=\"{faq}\">FAQ</a></p>",
    ]


def _20m_drop_snippets(lang: str) -> list[str]:
    if lang == "hr":
        return [
            "<h2>20 metara kontroliranog slobodnog pada</h2>",
            "<p>Quick Jump omogućuje korak s platforme visoko u krošnjama i pravi osjećaj slobodnog pada prije nego certificirani sustav nježno spusti na tlo. Jedna je od najintenzivnijih samostalnih atrakcija u parku.</p>",
            "<h2>Što očekivati</h2>",
            "<p>Obuka pokriva harnes, položaj i što očekivati tijekom spusta. Primjenjuju se zdravstvena i dobna ograničenja — osoblje savjetuje na ulazu.</p>",
            "<h2>Adrenalinski dan</h2>",
            "<p>Mnogi kombiniraju pad s <a href=\"{human_catapult}\">katapultom</a> ili <a href=\"{high_swing}\">ljuljačkom</a>. <a href=\"{book}\">Rezervirajte</a> · <a href=\"{prices}\">cijene</a></p>",
        ]
    return [
        "<h2>20 metres of controlled free fall</h2>",
        "<p>The Quick Jump lets you step off a platform high in the trees and experience genuine free fall before a certified descender brings you smoothly to the ground. It is one of the most intense standalone rides in the park.</p>",
        "<h2>What to expect</h2>",
        "<p>The briefing covers harness fit, body position, and what to expect during the descent. Health and age restrictions apply — staff advise at entry.</p>",
        "<h2>Build an adrenaline day</h2>",
        "<p>Many combine the drop with the <a href=\"{human_catapult}\">Human Catapult</a> or <a href=\"{high_swing}\">High Swing</a>. <a href=\"{book}\">Book</a> · <a href=\"{prices}\">prices</a></p>",
    ]


SNIPPET_BUILDERS: dict[str, callable] = {
    "human-catapult": _human_catapult_snippets,
    "high-swing": _high_swing_snippets,
    "training-route": _training_route_snippets,
    "low-zipline": _low_zipline_snippets,
    "valley-zipline": _valley_zipline_snippets,
    "devils-causeway": _devils_causeway_snippets,
    "climbing-wall": _climbing_wall_snippets,
    "aerotrim": _aerotrim_snippets,
    "20m-drop": _20m_drop_snippets,
}


def render_activity_seo_footer(activity: dict, lang: str) -> str:
    data = activity[lang]
    h1 = data["h1"]
    slug = activity["en_slug"]
    builder = SNIPPET_BUILDERS.get(slug)
    snippets = [_fmt(s, lang) for s in (builder(lang) if builder else [])]

    def block(text: str) -> str:
        text = text.strip()
        if text.startswith("<"):
            return text
        return f"<p>{text}</p>"

    body = "".join(block(s) for s in snippets)
    return body + _shared_footer(lang, h1)
