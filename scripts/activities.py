"""
Individual activity pages — brief copy and video placeholder per attraction.
"""

from booking_policy import activity_booking_answer

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
                "Strap in and feel the rush as powerful elastic cables launch you from standstill to motorway speed in a single second. The Human Catapult at Glavani Park is one of the park's signature adrenaline rides — a controlled, instructor-led experience in the oak forest between Barban and Vodnjan.",
                "Staff fit your harness, run a full safety briefing, and supervise every launch. Minimum age and height requirements apply; ask at the ticket desk or call ahead if you are unsure. Allow time in your visit for briefing and queueing — the catapult is a highlight visitors often repeat.",
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
                "Zavežite se i osjetite naboj dok vas elastična užad lansiraju od mirovanja do brzine autoceste u jednoj sekundi. Ljudska katapulta u Glavani Parku jedna je od glavnih adrenalinskih atrakcija — kontrolirano iskustvo pod nadzorom instruktora u hrastovoj šumi između Barbana i Vodnjanja.",
                "Osoblje prilagođava harnes, provodi sigurnosnu obuku i nadzire svako lansiranje. Primjenjuju se minimalna dob i visina; pitajte na blagajni ili nazovite unaprijed. Ostavite dovoljno vremena za obuku i čekanje — katapulta je atrakcija koju posjetitelji često ponavljaju.",
            ],
            "video_heading": "Video ljudske katapulata",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
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
                "Step off the platform and arc through the treetops on Glavani Park's 12.5-metre high swing. The ride combines height, speed, and a long pendulum swing that gives you time to take in the forest canopy before the gentle return.",
                "Instructors secure your harness, explain body position and signals, and control each release. The high swing suits teenagers and adults who meet height requirements and is a favourite alongside the ziplines and catapult for a mixed-adrenaline day out.",
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
                "Korak s platforme i let kroz krošnje na ljuljački visokoj 12,5 metara u Glavani Parku. Vožnja spaja visinu, brzinu i dugi zamašaj koji vam daje trenutak pogleda na šumski krov prije nježnog povratka.",
                "Instruktori pričvršćuju harnes, objašnjavaju položaj tijela i signale te kontroliraju svako puštanje. Ljuljačka pogoduje tinejdžerima i odraslima koji zadovoljavaju uvjete visine i omiljena je uz zipline i katapultu.",
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
                "You stay on continuous belay from start to finish while instructors explain harness fit, safety signals, and how to tackle balance obstacles and rope bridges. The training route is included in day admission and the popular Training route + 2 games package from €30.",
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
                "Ostajete na kontinuiranom osiguranju od početka do kraja dok instruktori objašnjavaju harnes, sigurnosne signale i kako savladati prepreke ravnoteže i mostove od užadi. Trening ruta uključena je u dnevnu ulaznicu i popularni paket Trening ruta + 2 igre od 30 €.",
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
        "image": "gift-voucher-50-whole-park.webp",
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
        "image": "valley-zipline-youtube-still.webp",
        "en": {
            "title": "Valley Zip Line Course | Glavani Park Istria",
            "h1": "Valley Zip Line Course",
            "meta_description": (
                "Fly 120 metres through the valley on Glavani Park's standalone zipline, up to 20 m high. "
                "Instructor-led launches in Istria near Pula. Open daily 9 AM–5 PM."
            ),
            "keywords": "zipline Istria, 120m zipline Croatia, valley zipline Glavani Park, zipline near Pula",
            "hero_badge": "120 m · up to 20 m high",
            "image_alt": "120 metre valley zipline course at Glavani Park, Istria Croatia",
            "paragraphs": [
                "Glavani Park's Valley Zip Line Course sends you on two zip line runs back and forth over the valley through the oak forest, reaching heights of up to 20 metres. You clip in with park staff, receive a launch briefing, and glide between platforms with views across the valley.",
                "The course is popular with first-time zipliners and returning visitors alike. Harness and helmet are provided; wear closed shoes and comfortable clothing. Combine with the Treetop Course on the high-ropes routes for a full zipline experience in one visit.",
            ],
            "video_heading": "Valley Zip Line video",
            "video_notice": (
                "The course shown in this video is an earlier version. The Valley Zip Line has since been upgraded — "
                "today's experience includes <strong>two zip lines</strong> back and forth over the valley."
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
            "image_alt": "Dolinski zipline 120 m u Glavani Parku, Istria Hrvatska",
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
        "image": "aerotrim-glavanipark-istria.webp",
        "en": {
            "title": "Aerotrim | Glavani Park Istria",
            "h1": "Aerotrim",
            "meta_description": (
                "Try the Aerotrim human gyroscope at Glavani Park, Istria — multi-axis spins with instructor "
                "supervision in the oak forest near Pula. Open daily 9 AM–5 PM."
            ),
            "keywords": "Aerotrim Croatia, human gyroscope Istria, Glavani Park Aerotrim, adventure park near Pula",
            "hero_badge": "Human gyroscope · multi-axis spins",
            "image_alt": "Aerotrim human gyroscope at Glavani Park adventure park, Istria Croatia",
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
            "image_alt": "Aerotrim ljudski žiroskop u Glavani Parku, Istria Hrvatska",
            "paragraphs": [
                "Zavežite se u Aerotrim Glavani Parka — ljudski žiroskop koji vas okreće u više osi dok ste sigurno pričvršćeni u okviru. Osoblje određuje tempo, objašnjava položaj tijela i nadzire svaku vožnju u šumskoj čistini.",
                "Jedinstven je spoj adrenalina i dezorijentacije — popularan među tinejdžerima i odraslima koji žele nešto drugačije od ziplinea i katapulata. Primjenjuju se ograničenja visine, dobi i zdravlja; pitajte na blagajni prije rezervacije.",
            ],
            "video_heading": "Video Aerotrima",
            "video_placeholder": "Video uskoro — ovdje zalijepite YouTube embed ili video datoteku.",
        },
    },
    {
        "en_slug": "devils-causeway",
        "hr_slug": "most-s-monociklom",
        "tile_mod": "causeway",
        "image": "devils-causeway-unicycle-glavani-park.webp",
        "hide_video": True,
        "en": {
            "title": "Devil's Causeway with the Unicycle | Glavani Park Istria",
            "h1": "Devil's causeway with the unicycle",
            "meta_description": (
                "Cross the Devil's Path on a unicycle at Glavani Park, Istria — skateboard, wooden bridge, "
                "unicycle and Japanese bridge after the yellow and blue routes. Weight limit 85 kg. Near Pula."
            ),
            "keywords": (
                "Devil's causeway Istria, unicycle bridge Croatia, Glavani Park high ropes, "
                "adventure park near Pula, black route Istria"
            ),
            "hero_badge": "Devil's Path · unicycle crossing · 85 kg limit",
            "image_alt": "Guest crossing Devil's causeway with the unicycle at Glavani Park, Istria Croatia",
            "paragraphs": [
                "Once you've completed the yellow and blue routes — or when you're already experienced at our adventure park — it's time to head to the Devil's Path and cross it on a unicycle. You ride a skateboard first, then cross a wooden slatted bridge before the unicycle — the most difficult part of the park.",
                "If you weigh more than 85 kg or aren't tall enough to reach the unicycle pedals, this game may not be suitable; you can walk on the wire instead. Staff guide you through seat adjustment, balance, and pedalling — hold the safety rope with one hand and the seat with the other. After the unicycle, complete a ropeline and a simple Japanese bridge. The giant swing is the best game to do next.",
            ],
        },
        "hr": {
            "title": "Most s monociklom | Glavani Park Istria",
            "h1": "Most s monociklom",
            "meta_description": (
                "Prijeđite Vražji put na monociklu u Glavani Parku, Istria — skateboard, drveni most, "
                "monocikl i japanski most nakon žute i plave staze. Ograničenje težine 85 kg. Kod Pule."
            ),
            "keywords": (
                "most s monociklom Istria, monocikl most Hrvatska, Glavani Park visoke staze, "
                "avanturistički park kod Pule, crna staza Istria"
            ),
            "hero_badge": "Vražji put · monocikl · limit 85 kg",
            "image_alt": "Gost prelazi most s monociklom u Glavani Parku, Istria Hrvatska",
            "paragraphs": [
                "Kada ste prošli žutu, plavu i crnu stazu, vrijeme je da nastavite na najdužu zip liniju i most s monociklom. Zip liniju može svatko proći jer je do nje vrlo jednostavno doći; za most s monociklom vrijede ograničenja — osobe teže od 85 kg ne bi trebale ići na most, a mala djeca moraju dohvatiti pedale monocikla.",
                "Prije monocikla čeka vas skateboard, malo veći i brži, te mostić kojeg je najlakše pretrčati — kroz cijelo razdoblje slušajte upute osoblja. Monocikl je najzahtjevniji dio u Glavani Parku: namjestite visinu sjedala, jednom rukom držite horizontalnu špagu, drugom se čvrsto držite ispod sjedala. Nakon toga slijede slackline i most; vratite se najdužom zip linijom ili kraćom, bržom do 11 m visoke ljuljačke.",
            ],
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
        price_a = (
            f"The Human Catapult is €{single_price} as a single activity, or included in whole-park packages from €30. "
            f"See <a href=\"{prefix}prices/\">packages and prices</a> or <a href=\"{prefix}book/\">book online</a>."
            if single_price
            else f"Access is included in Glavani Park day admission and packages from €30 per person. "
            f"See <a href=\"{prefix}prices/\">packages and prices</a>."
        )
        return [
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

    price_a = (
        f"Ljudska katapulta košta {single_price} € kao pojedinačna aktivnost ili je uključena u pakete cijelog parka od 30 €. "
        f"Pogledajte <a href=\"{prefix}cijene/\">pakete i cijene</a> ili <a href=\"{prefix}rezervacija/\">rezervirajte online</a>."
        if single_price
        else f"Pristup je uključen u dnevnu ulaznicu i pakete Glavani Parka od 30 € po osobi. "
        f"Pogledajte <a href=\"{prefix}cijene/\">pakete i cijene</a>."
    )
    return [
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
