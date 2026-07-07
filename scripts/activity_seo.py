"""Extra SEO body copy for activity pages — keeps rankings during migration."""

from __future__ import annotations

from packages import PRICES_SLUGS, BOOKING_SLUGS, pricing_visit_footer_line  # noqa: E402


def _shared_footer(lang: str, h1: str) -> str:
    prefix = f"/{lang}/"
    prices = f"{prefix}{PRICES_SLUGS[lang]}/"
    book = f"{prefix}{BOOKING_SLUGS[lang]}/"
    if lang == "hr":
        return f"""
<h2>Planiranje posjeta</h2>
<p>Glavani Park se nalazi u Glavanima 10, Barban — otprilike <strong>30 minuta vožnje od Pule</strong>, 45 minuta od Rovinja i Rabca te 50 minuta od Poreča. Besplatno parkiranje je na licu mjesta. Park radi <strong>svaki dan 9–17 h</strong>; posljednji ulaz u <strong>15 h</strong>, stoga planirajte tri do četiri sata za cijeli park.</p>
<p>Za {h1.lower()} i ostale atrakcije možete <a href="{book}">rezervirati ulaznice online</a> za grupe do 6 osoba ili nazvati za veće grupe s popustom. Pogledajte <a href="{prices}">pakete i cijene</a> — {pricing_visit_footer_line("hr")}.</p>
<h2>Sigurnost i oprema</h2>
<p>Svaka aktivnost u Glavani Parku vodi se pod nadzorom kvalificiranih instruktora. Oprema je CE certificirana i provjerava se dnevno. Prije početka dobivate harnes, kacigu i jasnu obuku. Više o standardima pročitajte na našoj <a href="{prefix}sigurnost/">stranici o sigurnosti</a>.</p>"""
    return f"""
<h2>Planning your visit</h2>
<p>Glavani Park is at Glavani 10, Barban — about <strong>30 minutes from Pula</strong>, 45 minutes from Rovinj and Rabac, and 50 minutes from Poreč. Free parking is on site. The park is open <strong>daily 9 AM–5 PM</strong> with <strong>last entry at 3 PM</strong>, so allow three to four hours for the whole park.</p>
<p>For {h1} and our other attractions you can <a href="{book}">book tickets online</a> for groups up to 6 or call ahead for larger parties with group discounts. See <a href="{prices}">packages and prices</a> — {pricing_visit_footer_line("en")}.</p>
<h2>Safety and equipment</h2>
<p>Every activity at Glavani Park is instructor-led. Equipment is CE-certified and checked daily. You receive a harness, helmet, and clear briefing before you start. Read more on our <a href="{prefix}safety/">safety page</a>.</p>"""


SNIPPETS: dict[str, dict[str, list[str]]] = {
    "human-catapult": {
        "en": [
            "<h2>What to expect on the Human Catapult</h2>",
            "<p>The Human Catapult is one of only a handful of horizontal catapult rides in Europe. You lie in a secure frame while elastic cables build tension — then release sends you from 0 to around 100 km/h in roughly one second. The whole experience, including harness fitting and briefing, typically takes 15–20 minutes per group.</p>",
            "<p>Most visitors pair the catapult with the 12.5 m high swing, valley ziplines, or the 20 m drop for a full adrenaline day. Families often watch from the viewing area while teenagers and adults take turns — it is a talking point long after you leave Istria.</p>",
        ],
        "hr": [
            "<h2>Što očekivati na ljudskoj katapulti</h2>",
            "<p>Ljudska katapulta jedna je od rijetkih horizontalnih katapulti u Europi. Ležite u sigurnom okviru dok elastična užad napinju — puštanje vas šalje s 0 na oko 100 km/h u otprilike jednoj sekundi. Cijelo iskustvo, uključujući harnes i obuku, obično traje 15–20 minuta po grupi.</p>",
            "<p>Većina posjetitelja kombinira katapultu s ljuljačkom od 12,5 m, dolinskim ziplineom ili padom s 20 m. Obitelji često gledaju s vidikovca dok tinejdžeri i odrasli mijenjaju redove — atrakcija o kojoj se priča i nakon odlaska iz Istre.</p>",
        ],
    },
    "high-swing": {
        "en": [
            "<h2>What to expect on the High Swing</h2>",
            "<p>After your harness check you climb to the launch platform 12.5 metres above the forest floor. The swing releases you into a long pendulum arc through the oak canopy — a mix of weightlessness at the top of the swing and speed at the bottom. Instructors control each release and guide you back to the platform.</p>",
            "<p>The high swing suits confident teenagers and adults. It is one of our most photographed attractions and works well as a first big thrill before moving on to the ziplines or Human Catapult.</p>",
        ],
        "hr": [
            "<h2>Što očekivati na visokoj ljuljački</h2>",
            "<p>Nakon provjere harnesa penjete se na platformu 12,5 metara iznad tla. Ljuljačka vas pušta u dugi zamašaj kroz hrastovu šumu — mješavina nježnosti na vrhu i brzine na dnu. Instruktori kontroliraju svako puštanje i vode vas natrag na platformu.</p>",
            "<p>Ljuljačka pogoduje samouvjerenim tinejdžerima i odraslima. Jedna je od najfotografiranijih atrakcija i odličan prvi veliki adrenalin prije ziplinea ili katapulata.</p>",
        ],
    },
    "training-route": {
        "en": [
            "<h2>Family-friendly introduction to high ropes</h2>",
            "<p>The yellow training route is where most families start at Glavani Park. At just 2 metres high, children can experience real high-ropes obstacles — rope bridges, balance beams, and cargo nets — while parents walk alongside on the forest path. Continuous belay keeps everyone connected from start to finish.</p>",
            "<p>Many visitors progress to the blue Treetop Course and black Devil's Causeway Course in the same visit. The training route is included in our popular Training route + 2 games package — €20 for children, €30 for adults.</p>",
        ],
        "hr": [
            "<h2>Obiteljski uvod u visoke staze</h2>",
            "<p>Žuta trening ruta je mjesto gdje većina obitelji počinje u Glavani Parku. Na samo 2 metra visine, djeca prolaze prave prepreke visokih staza — mostove, ravnotežu i mreže — dok roditelji hodaju uz stazu. Kontinuirano osiguranje drži sve povezane od početka do kraja.</p>",
            "<p>Mnogi posjetitelji istog dana prelaze na plavu Stazu u krošnjama i crnu Stazu Vražjeg puta. Trening ruta uključena je u popularni paket Trening ruta + 2 igre — €20 za djecu, €30 za odrasle.</p>",
        ],
    },
    "low-zipline": {
        "en": [
            "<h2>Blue high-ropes and treetop zipline</h2>",
            "<p>The Treetop Course combines classic high-ropes elements with a 113-metre zipline section at 6 metres above the ground. It is the natural step up from the yellow training route — more height and speed, but still manageable for older children and teens with an adult nearby.</p>",
            "<p>Expect 45–90 minutes on the course depending on queue and confidence. Instructors are positioned at key points to help with clipping and encouragement.</p>",
        ],
        "hr": [
            "<h2>Plave visoke staze i zipline u krošnjama</h2>",
            "<p>Staza u krošnjama spaja klasične elemente visokih staza sa ziplineom od 113 metara na 6 metara visine. Prirodan je korak nakon žute trening rute — više visine i brzine, ali i dalje pristupačno starijoj djeci i tinejdžerima uz odraslog.</p>",
            "<p>Računajte 45–90 minuta na stazi ovisno o redu i samopouzdanju. Instruktori su na ključnim točkama za pomoć pri spajanju i ohrabrenje.</p>",
        ],
    },
    "valley-zipline": {
        "en": [
            "<h2>120 metres through the valley</h2>",
            "<p>The Valley Zip Line Course is a standalone experience — two runs back and forth across the oak valley, reaching up to 20 metres high. You get views across the forest and the park grounds that photos rarely capture. First-timers receive extra guidance at the launch platform; returning visitors often cite this as their favourite ride.</p>",
            "<p>Closed shoes and comfortable clothing are essential. The valley zipline pairs naturally with the Treetop Course on the high-ropes routes for visitors who want both canopy and open-valley flying in one day.</p>",
        ],
        "hr": [
            "<h2>120 metara kroz dolinu</h2>",
            "<p>Dolinski zipline samostalno je iskustvo — dva leta naprijed-natrag preko hrastove doline, do 20 metara visine. Pogled na šumu i park koji fotografije rijetko prenose. Početnici dobivaju dodatne upute na platformi; stalni posjetitelji često ga navode kao omiljenu vožnju.</p>",
            "<p>Potrebna je zatvorena obuća i udobna odjeća. Dolinski zipline prirodno se kombinira sa Stazom u krošnjama za one koji žele i krošnje i let iznad doline u jednom danu.</p>",
        ],
    },
    "devils-causeway": {
        "en": [
            "<h2>The park's toughest challenge</h2>",
            "<p>The Devil's Causeway Course is the black-route finale — skateboard, wooden bridge, unicycle crossing, slackline, and Japanese bridge. It rewards visitors who have already built confidence on the yellow and blue routes. The unicycle section is unique in Croatia and the most technically demanding part of the park.</p>",
            "<p>Weight limit 85 kg applies to the unicycle bridge; staff can advise alternatives. Allow extra time for this course — many guests pause to watch others tackle the unicycle before trying themselves.</p>",
        ],
        "hr": [
            "<h2>Najzahtjevniji izazov parka</h2>",
            "<p>Staza Vražjeg puta završnica je crne staze — skateboard, drveni most, prijelaz monociklom, slackline i japanski most. Nagrađuje posjetitelje koji su stekli samopouzdanje na žutoj i plavoj stazi. Dio s monociklom jedinstven je u Hrvatskoj i najtehnički najzahtjevniji u parku.</p>",
            "<p>Na most s monociklom vrijedi limit 85 kg; osoblje može predložiti alternative. Ostavite dodatno vrijeme — mnogi gosti zastanu gledati druge prije nego sami probaju.</p>",
        ],
    },
    "climbing-wall": {
        "en": [
            "<h2>Outdoor climbing for all levels</h2>",
            "<p>Our outdoor climbing wall sits in a forest clearing with multiple routes from beginner-friendly holds to steeper challenges. It is ideal for warming up before high ropes, school groups building teamwork, or families taking a break between bigger rides.</p>",
            "<p>Sessions are instructor-supervised with harness and helmet provided. Younger children often climb with assistance — ask staff about age and height suitability when you arrive.</p>",
        ],
        "hr": [
            "<h2>Penjanje na otvorenom za sve razine</h2>",
            "<p>Vanjski penjački zid u šumskoj čistini nudi više smjerova — od početničkih držala do strmijih izazova. Idealno za zagrijavanje prije visokih staza, školske grupe ili obitelji između većih vožnji.</p>",
            "<p>Vožnje su pod nadzorom instruktora s harnesom i kacigom. Mlađa djeca često penju uz pomoć — pitajte osoblje o dobi i visini na ulazu.</p>",
        ],
    },
    "aerotrim": {
        "en": [
            "<h2>Human gyroscope in the forest</h2>",
            "<p>The Aerotrim spins you through multiple axes while you stay secured in the frame — a sensation unlike anything else in the park. Staff control the speed and explain how to position your body. Popular with teenagers looking for something different from ziplines and the catapult.</p>",
            "<p>Health, height, and age restrictions apply. If you are prone to motion sickness, consider watching a session first or pairing Aerotrim with a break at our refreshments area between rides.</p>",
        ],
        "hr": [
            "<h2>Ljudski žiroskop u šumi</h2>",
            "<p>Aerotrim vas okreće u više osi dok ste sigurno u okviru — osjećaj drugačiji od svega ostalog u parku. Osoblje kontrolira brzinu i objašnjava položaj tijela. Popularan među tinejdžerima koji traže nešto izvan ziplinea i katapulata.</p>",
            "<p>Primjenjuju se zdravstvena, visinska i dobna ograničenja. Ako ste osjetljivi na kretanje, pogledajte sesiju ili napravite pauzu uz osvježenje između vožnji.</p>",
        ],
    },
    "20m-drop": {
        "en": [
            "<h2>20 metres of controlled free fall</h2>",
            "<p>The Quick Jump lets you step off a platform high in the trees and experience genuine free fall before a certified descender brings you smoothly to the ground. The briefing covers harness fit, body position, and what to expect — staff will advise if health conditions are a concern.</p>",
            "<p>Many visitors combine the 20 m drop with the Human Catapult or high swing in one adrenaline session. It is one of the most intense standalone rides in the park and a favourite for returning guests.</p>",
        ],
        "hr": [
            "<h2>20 metara kontroliranog slobodnog pada</h2>",
            "<p>Quick Jump omogućuje korak s platforme visoko u krošnjama i pravi osjećaj slobodnog pada prije nego certificirani sustav nježno spusti na tlo. Obuka pokriva harnes, položaj i što očekivati — osoblje savjetuje ako su zdravstvena stanja problem.</p>",
            "<p>Mnogi kombiniraju pad s 20 m s katapultom ili ljuljačkom u jednoj adrenalinskoj sesiji. Jedna je od najintenzivnijih samostalnih atrakcija i omiljena stalnim gostima.</p>",
        ],
    },
}


def render_activity_seo_footer(activity: dict, lang: str) -> str:
    data = activity[lang]
    h1 = data["h1"]
    slug = activity["en_slug"]
    snippets = SNIPPETS.get(slug, {}).get(lang, [])

    def block(text: str) -> str:
        text = text.strip()
        if text.startswith("<"):
            return text
        return f"<p>{text}</p>"

    body = "".join(block(s) for s in snippets)
    return body + _shared_footer(lang, h1)
