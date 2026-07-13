"""
Individual activity pages — brief copy and video placeholder per attraction.
"""

from booking_policy import activity_booking_answer
from brand_voice import ONLINE_BOOKING_MAX
from packages import booking_page_href
from packages import package_price_faq_answer

ACTIVITY_SLUG_MAP = {
    "ljudska-katapulta": "human-catapult",
    "visoka-ljuljacka": "high-swing",
    "pad-s-20m": "20m-drop",
    "dolinski-zipline": "valley-zipline",
    "niski-zipline": "low-zipline",
    "penjacki-zid": "climbing-wall",
    "trening-ruta": "training-route",
    "most-s-monociklom": "devils-causeway",
}

ACTIVITIES = [
    {
        "en_slug": "human-catapult",
        "hr_slug": "ljudska-katapulta",
        "tile_mod": "catapult",
        "youtube_id": "X2bRA2Bur-M",
        "youtube_url": "https://youtu.be/X2bRA2Bur-M",
        "single_price": 40,
        "image": "human-catapult-youtube-still.webp",
        "en": {
            "title": "Human Catapult | Glavani Park Istria",
            "h1": "Human Catapult",
            "meta_description": (
                "Launch from 0 to 100 km/h in one second on the Human Catapult at Glavani Park, Istria. "
                "Instructor-led, CE-certified safety. Open daily 9 AM–5 PM near Pula."
            ),
            "keywords": "human catapult Croatia, adrenaline park Istria, Glavani Park catapult, adventure near Pula",
            "hero_badge": "0–100 km/h in one second",
            "image_alt": "Human Catapult launch at Glavani Park adrenaline park, Istria Croatia",
            "paragraphs": [
                "Feel race-car acceleration in a single second on Croatia's only Human Catapult — one of only a handful of horizontal catapult rides in Europe. Strap in, hold the release, and go from 0 to around 100 km/h quicker than an F1 car off the line.",
                "Staff fit your harness, run a full safety briefing, and supervise every launch. More than 9,000 catapults have been completed at Glavani Park and almost every guest loves it. Minimum age, height and weight limits apply — ask at the ticket desk or call ahead if you are unsure.",
            ],
            "video_heading": "Human Catapult video",
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Ljudska katapulta | Glavani Park Istria",
            "h1": "Ljudska katapulta",
            "meta_description": (
                "Lansiranje s 0 na 100 km/h u jednoj sekundi na ljudskoj katapulti u Glavani Parku, Istria. "
                "Pod nadzorom instruktora, CE certificirana oprema. Otvoreno 9–17 h kod Pule."
            ),
            "keywords": "ljudska katapulta Hrvatska, adrenalinski park Istria, Glavani Park katapulta, avantura kod Pule",
            "hero_badge": "0–100 km/h u jednoj sekundi",
            "image_alt": "Lansiranje ljudske katapulata u Glavani Parku, Istria Hrvatska",
            "paragraphs": [
                "Osjetite ubrzanje trkaćeg automobila u jednoj sekundi na jedinoj ljudskoj katapulti u Hrvatskoj — jedna od rijetkih horizontalnih katapulti u Europi. Zavežite se, povucite za puštanje i krenite s 0 na oko 100 km/h brže nego Formula 1 s mjesta.",
                "Osoblje prilagođava harnes, provodi sigurnosnu obuku i nadzire svako lansiranje. U Glavani Parku je obavljeno više od 9.000 lansiranja i gotovo svi gosti odlaze oduševljeni. Primjenjuju se minimalna dob, visina i težina — pitajte na blagajni ili nazovite unaprijed.",
            ],
            "video_heading": "Video ljudske katapulata",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
        "extra_faqs": {
            "en": [
                {
                    "q": "Is the Human Catapult scary?",
                    "a": (
                        "For most people, no. The sensation is intense but brief — many visitors arrive "
                        "nervous and leave thrilled. You can watch others go first, and staff explain every step."
                    ),
                },
                {
                    "q": "How fast is the Human Catapult?",
                    "a": (
                        "You accelerate from 0 to around 100 km/h in roughly one second — quicker than "
                        "a Formula 1 car from a standing start."
                    ),
                },
                {
                    "q": "Can I book just the Human Catapult?",
                    "a": (
                        "Yes. The Human Catapult is €40 as a single activity. "
                        f'<a href="{booking_page_href("en")}">Book online</a> for up to {ONLINE_BOOKING_MAX} people or call for larger groups.'
                    ),
                },
                {
                    "q": "Can spectators watch the Human Catapult?",
                    "a": (
                        "Yes. Friends and family can watch from the viewing area — many grab a drink or "
                        "ice cream while they wait. It is often as fun to watch as to ride."
                    ),
                },
                {
                    "q": "Can I film my Human Catapult ride?",
                    "a": (
                        "Yes. Use a friend to film or a securely attached action camera. "
                        "We cannot be held responsible for damage to personal equipment."
                    ),
                },
            ],
            "hr": [
                {
                    "q": "Je li ljudska katapulta zastrašujuća?",
                    "a": (
                        "Za većinu ljudi ne. Osjećaj je intenzivan ali kratak — mnogi dolaze nervozni "
                        "i odlaze oduševljeni. Možete gledati druge prije nego odlučite, a osoblje objašnjava svaki korak."
                    ),
                },
                {
                    "q": "Koliko je brza ljudska katapulta?",
                    "a": (
                        "Ubrzanje ide s 0 na oko 100 km/h u otprilike jednoj sekundi — brže nego Formula 1 s mjesta."
                    ),
                },
                {
                    "q": "Mogu li rezervirati samo ljudsku katapultu?",
                    "a": (
                        "Da. Ljudska katapulta košta €40 kao pojedinačna aktivnost. "
                        f'<a href="{booking_page_href("hr")}">Rezervirajte online</a> za do {ONLINE_BOOKING_MAX} osoba ili nazovite za veće grupe.'
                    ),
                },
                {
                    "q": "Mogu li gledatelji promatrati katapultu?",
                    "a": (
                        "Da. Prijatelji i obitelj mogu gledati s vidikovca — mnogi uzmu piće ili sladoled dok čekaju. "
                        "Često je jednako zabavno gledati kao voziti."
                    ),
                },
                {
                    "q": "Mogu li snimati vožnju na katapulti?",
                    "a": (
                        "Da. Koristite prijatelja za snimanje ili sigurno pričvršćenu action kameru. "
                        "Ne možemo preuzeti odgovornost za oštećenje osobne opreme."
                    ),
                },
            ],
        },
    },
    {
        "en_slug": "high-swing",
        "hr_slug": "visoka-ljuljacka",
        "tile_mod": "swing",
        "youtube_id": "ybePV3n9uks",
        "youtube_url": "https://youtu.be/ybePV3n9uks?is=C_7duYUFbJqnBY6T",
        "image": "high-swing-youtube-still.webp",
        "en": {
            "title": "12.5 m High Swing | Glavani Park Istria",
            "h1": "High Swing",
            "meta_description": (
                "Swing 12.5 metres above the forest floor at Glavani Park, Istria. "
                "A classic park thrill with harness and instructor briefing. Near Pula, open daily."
            ),
            "keywords": "high swing Istria, giant swing Croatia, Glavani Park swing, adventure park near Pula",
            "hero_badge": "12.5 m above the forest",
            "image_alt": "12.5 metre high swing at Glavani Park adventure park, Istria",
            "paragraphs": [
                "Climb 12.5 metres, pull the release cord yourself, and experience one of the biggest swings in Croatia. Arc through the oak treetops on a long pendulum that mixes weightlessness at the top with speed at the bottom.",
                "Instructors secure your harness, explain body position and signals, and guide each release. The high swing suits confident teenagers and adults who meet height requirements — a favourite alongside the ziplines and Human Catapult for a mixed-adrenaline day out.",
            ],
            "video_heading": "High Swing video",
            "video_notice": (
                "The swing shown in this video is an earlier version. Our high swing has since been upgraded — "
                "today's ride is <strong>12.5 m</strong> high."
            ),
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Visoka ljuljačka 12,5 m | Glavani Park Istria",
            "h1": "Visoka ljuljačka",
            "meta_description": (
                "Ljuljajte se 12,5 m iznad šumskog tla u Glavani Parku, Istria. "
                "Klasičan adrenalin s harnesom i obukom instruktora. Kod Pule, otvoreno svaki dan."
            ),
            "keywords": "visoka ljuljačka Istria, ljuljačka Hrvatska, Glavani Park ljuljačka, avanturistički park kod Pule",
            "hero_badge": "12,5 m iznad šume",
            "image_alt": "Visoka ljuljačka 12,5 m u Glavani Parku, Istria",
            "paragraphs": [
                "Penjite se 12,5 metara, povucite užad za puštanje sami i osjetite jednu od najvećih ljuljački u Hrvatskoj. Letite kroz hrastove krošnje u dugom zamašaju koji spaja nježnost na vrhu s brzinom na dnu.",
                "Instruktori pričvršćuju harnes, objašnjavaju položaj tijela i signale te vode svako puštanje. Ljuljačka pogoduje samouvjerenim tinejdžerima i odraslima koji zadovoljavaju uvjete visine — omiljena uz zipline i ljudsku katapultu.",
            ],
            "video_heading": "Video visoke ljuljačke",
            "video_notice": (
                "Ljuljačka u ovom videu raniji je model. Atrakcija je nakon toga nadograđena — "
                "današnja vožnja na ljuljačici visokoj <strong>12,5 m</strong>."
            ),
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "training-route",
        "hr_slug": "trening-ruta",
        "tile_mod": "training",
        "youtube_id": "TDl0ffqPj3U",
        "youtube_url": "https://youtu.be/TDl0ffqPj3U?is=E0eGJvpDww76o7MV",
        "image": "training-route-youtube-still.webp",
        "en": {
            "title": "Yellow Training Route (High Ropes) | Glavani Park Istria",
            "h1": "Training Route",
            "meta_description": (
                "Try the 2-metre yellow training route at Glavani Park, Istria — a family-friendly high-ropes "
                "course with harness and instructor briefing. Near Pula, open daily 9 AM–5 PM."
            ),
            "keywords": "training route Istria, yellow high ropes Croatia, family adventure park Pula, Glavani Park courses",
            "hero_badge": "2 m yellow route · all ages with adult",
            "image_alt": "Yellow training route high-ropes course at Glavani Park, Istria Croatia",
            "paragraphs": [
                "Glavani Park's yellow training route is a certified high-ropes course at 2 metres above the forest floor — the perfect introduction for younger children, first-time climbers, and families who want to build confidence before the blue and black routes.",
                "You stay on continuous belay from start to finish while instructors explain harness fit, safety signals, and how to tackle balance obstacles and rope bridges. The training route is included in the Training route + 2 games package — all park games except the Human Catapult, €20 for children and €30 for adults.",
            ],
            "video_heading": "Training Route video",
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Žuta trening ruta (visoke staze) | Glavani Park Istria",
            "h1": "Trening ruta",
            "meta_description": (
                "Isprobajte žutu trening rutu na 2 m u Glavani Parku, Istria — obiteljska visoka staza s harnesom "
                "i obukom instruktora. Kod Pule, otvoreno svaki dan 9–17 h."
            ),
            "keywords": "trening ruta Istria, žuta visoka staza Hrvatska, obiteljski avanturistički park Pula, Glavani Park staze",
            "hero_badge": "Žuta staza 2 m · uz odraslog",
            "image_alt": "Žuta trening ruta visokih staza u Glavani Parku, Istria Hrvatska",
            "paragraphs": [
                "Žuta trening ruta u Glavani Parku certificirana je visoka staza na 2 metra iznad šumskog tla — savršen uvod za mlađu djecu, početnike i obitelji koje žele steći samopouzdanje prije plave i crne staze.",
                "Ostajete na kontinuiranom osiguranju od početka do kraja dok instruktori objašnjavaju harnes, sigurnosne signale i kako savladati prepreke ravnoteže i mostove od užadi. Trening ruta uključena je u paket Trening ruta + 2 igre — sve igre parka osim katapulata, €20 za djecu i €30 za odrasle.",
            ],
            "video_heading": "Video trening rute",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "low-zipline",
        "hr_slug": "niski-zipline",
        "tile_mod": "zipline-low",
        "hide_video": True,
        "banner_header": True,
        "image": "visitor-gallery-treetop-course-guest-27.webp",
        "en": {
            "title": "Treetop Course | Glavani Park Istria",
            "h1": "Treetop Course",
            "meta_description": (
                "Glavani Park's blue Treetop Course — high ropes and a 113 m zipline at 6 m above the forest. "
                "Instructor-led treetop adventure near Pula. Open daily."
            ),
            "keywords": "treetop course Istria, blue high ropes Croatia, Glavani Park treetop course, adventure near Pula",
            "hero_badge": "113 m on the blue course · 6 m high",
            "image_alt": "Treetop high-ropes course and zipline at Glavani Park, Istria",
            "paragraphs": [
                "The Treetop Course is Glavani Park's blue high-ropes route at 6 metres above the ground. The 113-metre zipline section links platforms on the course, so you stay on continuous belay from climb to landing.",
                "It is a great introduction for visitors moving up from the family yellow route or those who want zipline speed without the full valley height. Instructors guide you at entry and exit points. Access is included when you complete the blue course circuit.",
            ],
            "video_heading": "Treetop Course video",
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Staza u krošnjama | Glavani Park Istria",
            "h1": "Staza u krošnjama",
            "meta_description": (
                "Plava Staza u krošnjama Glavani Parka — visoke staze i zipline od 113 m na 6 m iznad šume. "
                "Avantura u krošnjama pod nadzorom instruktora kod Pule. Otvoreno svaki dan."
            ),
            "keywords": "staza u krošnjama Istria, plava visoka staza Hrvatska, Glavani Park krošnje, avantura kod Pule",
            "hero_badge": "113 m na plavoj stazi · 6 m visine",
            "image_alt": "Staza u krošnjama — visoka staza i zipline u Glavani Parku, Istria",
            "paragraphs": [
                "Staza u krošnjama plava je visoka staza Glavani Parka na 6 metara iznad tla. Dio od 113 metara povezuje platforme na stazi — ostajete na kontinuiranom osiguranju od penjanja do slijetanja.",
                "Odličan je uvod za posjetitelje koji prelaze s obiteljske žute staze ili žele brzinu ziplinea bez pune visine doline. Instruktori vode na ulazu i izlazu. Pristup je uključen kada obavite plavu stazu.",
            ],
            "video_heading": "Video staze u krošnjama",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "valley-zipline",
        "hr_slug": "dolinski-zipline",
        "tile_mod": "zipline-valley",
        "youtube_id": "cQpPtOe481I",
        "youtube_url": "https://youtu.be/cQpPtOe481I",
        "image": "visitor-gallery-valley-zipline-staff-22.webp",
        "en": {
            "title": "Valley Zipline (Big Zipline) | Glavani Park Istria",
            "h1": "Valley Zipline (Big Zipline)",
            "meta_description": (
                "Fly 120 metres through the valley on Glavani Park's standalone zipline, up to 20 m high. "
                "Instructor-led launches in Istria near Pula. Open daily 9 AM–5 PM."
            ),
            "keywords": "zipline Istria, 120m zipline Croatia, valley zipline Glavani Park, zipline near Pula",
            "hero_badge": "120 m · up to 20 m high",
            "image_alt": "Guest on the Valley Zipline (Big Zipline) at Glavani Park, Istria",
            "paragraphs": [
                "Glavani Park's Valley Zipline (Big Zipline) sends you on two zipline runs back and forth over the valley through the oak forest, reaching heights of up to 20 metres. You clip in with park staff, receive a launch briefing, and glide between platforms with views across the valley.",
                "The course is popular with first-time zipliners and returning visitors alike. Harness and helmet are provided; wear closed shoes and comfortable clothing. Combine with the Treetop Course on the high-ropes routes for a full zipline experience in one visit.",
            ],
            "video_heading": "Valley Zipline video",
            "video_notice": (
                "The course shown in this video is an earlier version. The Valley Zipline has since been upgraded — "
                "today's experience includes <strong>two ziplines</strong> back and forth over the valley."
            ),
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Dolinski zipline | Glavani Park Istria",
            "h1": "Dolinski zipline",
            "meta_description": (
                "Let 120 metara kroz dolinu na samostalnom ziplineu Glavani Parka, do 20 m visine. "
                "Polasci pod nadzorom instruktora u Istri kod Pule. Otvoreno 9–17 h."
            ),
            "keywords": "zipline Istria, zipline 120 m Hrvatska, dolinski zipline Glavani Park, zipline kod Pule",
            "hero_badge": "120 m · do 20 m visine",
            "image_alt": "Gost na dolinskoj zipline stazi u Glavani Parku, Istria",
            "paragraphs": [
                "Dolinski zipline u Glavani Parku vodi vas na dva zipline leta naprijed-natrag preko doline kroz hrastovu šumu, do visine od 20 metara. Osoblje vas spaja na užad, provodi obuku i letite između platformi s pogledom na dolinu.",
                "Staza je popularna i među početnicima i među onima koji se vraćaju. Harnes i kaciga su osigurani; nosite zatvorenu obuću i udobnu odjeću. Kombinirajte sa Stazom u krošnjama na visokim stazama za puno zipline iskustvo u jednom posjetu.",
            ],
            "video_heading": "Video dolinskog ziplinea",
            "video_notice": (
                "Staza u ovom videu ranija je verzija. Dolinski zipline je nakon toga nadograđen — "
                "današnje iskustvo uključuje <strong>dva ziplinea</strong> naprijed-natrag preko doline."
            ),
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "devils-causeway",
        "hr_slug": "most-s-monociklom",
        "tile_mod": "causeway",
        "image": "devils-causeway-unicycle-glavani-park.webp",
        "hide_video": True,
        "banner_header": True,
        "en": {
            "title": "Devil's Causeway Course | Glavani Park Istria",
            "h1": "Devil's Causeway Course",
            "meta_description": (
                "Cross the Devil's Causeway Course at Glavani Park, Istria — skateboard, wooden bridge, "
                "unicycle and Japanese bridge after the yellow and blue routes. Weight limit 85 kg. Near Pula."
            ),
            "keywords": (
                "Devil's Causeway Course Istria, unicycle bridge Croatia, Glavani Park high ropes, "
                "adventure park near Pula, black route Istria"
            ),
            "hero_badge": "Devil's Path · unicycle crossing · 85 kg limit",
            "image_alt": "Guest on the Devil's Causeway Course at Glavani Park, Istria Croatia",
            "paragraphs": [
                "Once you've completed the yellow and blue routes — or when you're already experienced at our adventure park — it's time to head to the Devil's Causeway Course and cross it on a unicycle. You ride a skateboard first, then cross a wooden slatted bridge before the unicycle — the most difficult part of the park.",
                "If you weigh more than 85 kg or aren't tall enough to reach the unicycle pedals, this game may not be suitable; you can walk on the wire instead. Staff guide you through seat adjustment, balance, and pedalling — hold the safety rope with one hand and the seat with the other. After the unicycle, complete a ropeline and a simple Japanese bridge. The giant swing is the best game to do next.",
            ],
        },
        "hr": {
            "title": "Staza Vražjeg puta | Glavani Park Istria",
            "h1": "Staza Vražjeg puta",
            "meta_description": (
                "Prijeđite Stazu Vražjeg puta u Glavani Parku, Istria — skateboard, drveni most, "
                "monocikl i japanski most nakon žute i plave staze. Ograničenje težine 85 kg. Kod Pule."
            ),
            "keywords": (
                "staza Vražjeg puta Istria, monocikl most Hrvatska, Glavani Park visoke staze, "
                "avanturistički park kod Pule, crna staza Istria"
            ),
            "hero_badge": "Vražji put · monocikl · limit 85 kg",
            "image_alt": "Gost na Stazi Vražjeg puta u Glavani Parku, Istria Hrvatska",
            "paragraphs": [
                "Kada ste prošli žutu, plavu i crnu stazu, vrijeme je da nastavite na najdužu zip liniju i Stazu Vražjeg puta. Zip liniju može svatko proći jer je do nje vrlo jednostavno doći; za most s monociklom vrijede ograničenja — osobe teže od 85 kg ne bi trebale ići na most, a mala djeca moraju dohvatiti pedale monocikla.",
                "Prije monocikla čeka vas skateboard, malo veći i brži, te mostić kojeg je najlakše pretrčati — kroz cijelo razdoblje slušajte upute osoblja. Monocikl je najzahtjevniji dio u Glavani Parku: namjestite visinu sjedala, jednom rukom držite horizontalnu špagu, drugom se čvrsto držite ispod sjedala. Nakon toga slijede slackline i most; vratite se najdužom zip linijom ili kraćom, bržom do 11 m visoke ljuljačke.",
            ],
        },
    },
    {
        "en_slug": "climbing-wall",
        "hr_slug": "penjacki-zid",
        "tile_mod": "climbing",
        "youtube_id": "Uhbf2TF8PYE",
        "youtube_url": "https://youtu.be/Uhbf2TF8PYE?is=LwH9p2u6W_SQ_UCZ",
        "image": "climbing-wall-youtube-still.webp",
        "en": {
            "title": "Outdoor Climbing Wall | Glavani Park Istria",
            "h1": "Climbing Wall",
            "meta_description": (
                "Climb the outdoor wall at Glavani Park, Istria — routes for different abilities with harness and helmet. "
                "Near Pula, open daily. Call ahead for groups."
            ),
            "keywords": "climbing wall Istria, outdoor climbing Croatia, Glavani Park climbing, family activities near Pula",
            "hero_badge": "Outdoor routes · all skill levels",
            "image_alt": "Outdoor climbing wall at Glavani Park adventure park, Istria",
            "paragraphs": [
                "Glavani Park's outdoor climbing wall offers several routes on a purpose-built structure in the forest clearing. Staff fit your harness and helmet, explain belay signals, and support you whether it is your first climb or you are building confidence for the high-ropes courses.",
                "The wall works well for families, school groups warming up, and visitors taking a break between bigger rides. Wear trainers with a good grip. Younger children can often climb with instructor assistance — ask on arrival about suitability.",
            ],
            "video_heading": "Climbing Wall video",
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Vanjski penjački zid | Glavani Park Istria",
            "h1": "Penjački zid",
            "meta_description": (
                "Penjajte se na vanjskom zidu u Glavani Parku, Istria — smjerovi za različite razine s harnesom i kacigom. "
                "Kod Pule, otvoreno svaki dan. Nazovite unaprijed za grupe."
            ),
            "keywords": "penjački zid Istria, penjanje na otvorenom Hrvatska, Glavani Park penjanje, obiteljske aktivnosti kod Pule",
            "hero_badge": "Smjerovi na otvorenom · sve razine",
            "image_alt": "Vanjski penjački zid u Glavani Parku, Istria",
            "paragraphs": [
                "Vanjski penjački zid u Glavani Parku nudi nekoliko smjerova na namjenskoj konstrukciji u šumskoj čistini. Osoblje prilagođava harnes i kacigu, objašnjava signale i podržava vas bez obzira je li prvo penjanje ili gradite samopouzdanje za visoke staze.",
                "Zid je odličan za obitelji, školske grupe na zagrijavanju i posjetitelje između većih vožnji. Nosite tenisice s dobrim gripom. Mlađa djeca često mogu penjati uz pomoć instruktora — pitajte na ulazu o prikladnosti.",
            ],
            "video_heading": "Video penjačkog zida",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "aerotrim",
        "hr_slug": "aerotrim",
        "tile_mod": "aerotrim",
        "hide_video": True,
        "banner_header": True,
        "image": "visitor-gallery-aerotrim-guest-19.webp",
        "en": {
            "title": "Aerotrim | Glavani Park Istria",
            "h1": "Aerotrim",
            "meta_description": (
                "Try the Aerotrim human gyroscope at Glavani Park, Istria — multi-axis spins with instructor "
                "supervision in the oak forest near Pula. Open daily 9 AM–5 PM."
            ),
            "keywords": "Aerotrim Croatia, human gyroscope Istria, Glavani Park Aerotrim, adventure park near Pula",
            "hero_badge": "Human gyroscope · multi-axis spins",
            "image_alt": (
                "Participant spinning in the Aerotrim human gyroscope at Glavani Park, Istria — "
                "red and yellow rings with instructor at an outdoor adventure park near Pula"
            ),
            "paragraphs": [
                "Strap into Glavani Park's Aerotrim — a human gyroscope that spins you through multiple axes while you stay secured in the frame. Staff set the pace, explain how to hold your body, and supervise every session in the forest clearing.",
                "It is a unique sensation between thrill and disorientation — popular with teenagers and adults who want something different from the ziplines and catapult. Height, age, and health restrictions apply; ask at the ticket desk before you book.",
            ],
            "video_heading": "Aerotrim video",
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Aerotrim | Glavani Park Istria",
            "h1": "Aerotrim",
            "meta_description": (
                "Isprobajte Aerotrim ljudski žiroskop u Glavani Parku, Istria — okretanje u više osi pod nadzorom "
                "instruktora u hrastovoj šumi kod Pule. Otvoreno svaki dan 9–17 h."
            ),
            "keywords": "Aerotrim Hrvatska, ljudski žiroskop Istria, Glavani Park Aerotrim, avanturistički park kod Pule",
            "hero_badge": "Ljudski žiroskop · više osi",
            "image_alt": (
                "Sudionik u Aerotrima ljudskom žiroskopu u Glavani Parku, Istria — "
                "crveni i žuti prstenovi s instruktorom u avanturističkom parku na otvorenom kod Pule"
            ),
            "paragraphs": [
                "Zavežite se u Aerotrim Glavani Parka — ljudski žiroskop koji vas okreće u više osi dok ste sigurno pričvršćeni u okviru. Osoblje određuje tempo, objašnjava položaj tijela i nadzire svaku vožnju u šumskoj čistini.",
                "Jedinstven je spoj adrenalina i dezorijentacije — popularan među tinejdžerima i odraslima koji žele nešto drugačije od ziplinea i katapulata. Primjenjuju se ograničenja visine, dobi i zdravlja; pitajte na blagajni prije rezervacije.",
            ],
            "video_heading": "Video Aerotrima",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "20m-drop",
        "hr_slug": "pad-s-20m",
        "tile_mod": "drop",
        "youtube_id": "W5CWJfZlW2o",
        "youtube_url": "https://youtu.be/W5CWJfZlW2o?is=zZJA4POSAJsYONMr",
        "image": "quick-jump-youtube-still.webp",
        "en": {
            "title": "20 m Drop (Quick Jump) | Glavani Park Istria",
            "h1": "20m Drop",
            "meta_description": (
                "Experience a controlled 20-metre free fall on the Quick Jump at Glavani Park, Istria. "
                "Professional descender system and instructor briefing. Open daily near Pula."
            ),
            "keywords": "Quick Jump Croatia, 20m free fall Istria, Glavani Park drop, adrenaline near Pula",
            "hero_badge": "20 m controlled free fall",
            "image_alt": "Quick Jump 20 metre controlled free fall at Glavani Park, Istria",
            "paragraphs": [
                "The 20m Drop — known as Quick Jump — lets you step off a platform high in the trees and feel genuine free fall before a certified descender system brings you smoothly to the ground. It is one of the most intense standalone rides in the park.",
                "A full briefing covers harness fit, launch position, and what to expect on the way down. Health and age restrictions apply; staff will advise at check-in. Pair the drop with the Human Catapult or high swing for a full adrenaline session.",
            ],
            "video_heading": "20m Drop video",
            "video_placeholder": "Activity video coming soon — paste a YouTube embed or video file here.",
        },
        "hr": {
            "title": "Pad s 20 m (Quick Jump) | Glavani Park Istria",
            "h1": "Pad s 20 m",
            "meta_description": (
                "Kontrolirani slobodni pad s 20 metara na Quick Jumpu u Glavani Parku, Istria. "
                "Profesionalni sustav usporavanja i obuka instruktora. Otvoreno svaki dan kod Pule."
            ),
            "keywords": "Quick Jump Hrvatska, slobodni pad Istria, Glavani Park pad, adrenalin kod Pule",
            "hero_badge": "Kontrolirani pad s 20 m",
            "image_alt": "Quick Jump kontrolirani pad s 20 m u Glavani Parku, Istria",
            "paragraphs": [
                "Pad s 20 m — Quick Jump — omogućuje korak s platforme visoko u krošnjama i pravi osjećaj slobodnog pada prije nego certificirani sustav usporavanja nježno spusti na tlo. Jedna je od najintenzivnijih samostalnih atrakcija u parku.",
                "Potpuna obuka pokriva harnes, položaj i što očekivati tijekom spusta. Primjenjuju se zdravstvena i dobna ograničenja; osoblje savjetuje na ulazu. Kombinirajte s katapultom ili ljuljačkom za puni adrenalinski dan.",
            ],
            "video_heading": "Video pada s 20 m",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
]


def activity_faqs(activity: dict, lang: str) -> list[dict]:
    """Three concise FAQs per activity page for SEO and AI extraction."""
    data = activity[lang]
    h1 = data["h1"]
    single_price = activity.get("single_price")
    prefix = f"/{lang}/"

    if lang == "en":
        price_a = package_price_faq_answer("en", prefix, single_price=single_price)
        faqs = [
            {
                "q": f"How much does {h1} cost at Glavani Park?",
                "a": price_a,
            },
            {
                "q": f"Do I need to book {h1} in advance?",
                "a": activity_booking_answer("en", h1),
            },
            {
                "q": f"Is {h1} safe at Glavani Park?",
                "a": (
                    f"Yes. {h1} at Glavani Park is instructor-led with CE-certified harnesses and helmets, "
                    "daily equipment checks, and a full briefing before you start. Read our "
                    f"<a href=\"{prefix}safety/\">safety page</a> for full standards."
                ),
            },
        ]
        faqs.extend(activity.get("extra_faqs", {}).get("en", []))
        return faqs

    price_a = package_price_faq_answer("hr", prefix, single_price=single_price)
    faqs = [
        {
            "q": f"Koliko košta {h1} u Glavani Parku?",
            "a": price_a,
        },
        {
            "q": f"Trebam li unaprijed rezervirati {h1}?",
            "a": activity_booking_answer("hr", h1),
        },
        {
            "q": f"Je li {h1} siguran u Glavani Parku?",
            "a": (
                f"Da. {h1} u Glavani Parku vodi instruktor s CE certificiranim harnesom i kacigom, "
                "dnevnom provjerom opreme i potpunom obukom prije početka. Više na "
                f"<a href=\"{prefix}sigurnost/\">stranici o sigurnosti</a>."
            ),
        },
    ]
    faqs.extend(activity.get("extra_faqs", {}).get("hr", []))
    return faqs
