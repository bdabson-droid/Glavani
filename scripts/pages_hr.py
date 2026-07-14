"""
Hrvatski sadržaj landing stranica za Glavani Park SEO web.
Svaka stranica sadrži 800–1200 riječi kvalitetnog turističkog i park sadržaja.
"""

from booking_policy import BOOKING_POLICY
from brand_voice import ONLINE_BOOKING_MAX

_HR_BOOKING = BOOKING_POLICY["hr"]

SLUG_MAP = {
    "sto-raditi-u-istri": "things-to-do-in-istria",
    "obiteljske-aktivnosti-istri": "family-activities-istria",
    "zipline-hrvatska": "zipline-croatia",
    "team-building-istri": "team-building-istria",
    "rodjendanske-zabave-istri": "birthday-parties-istria",
    "skolski-izleti-istri": "school-trips-istria",
    "sto-raditi-kod-pule": "things-to-do-near-pula",
    "avanturisticki-park-hrvatska": "adventure-park-croatia",
    "sigurnost": "safety",
    "partneri": "partners",
    "link-na-nas": "link-to-us",
    "cesta-pitanja": "faq",
}

HOME = {
    "title": 'Glavani Park | Broj 1 avanturistički park u Hrvatskoj · Istria',
    "meta_description": (
        'Glavani Park je broj 1 avanturistički park u Istri, Hrvatska — zipline, visoke staze, ljudska katapulta '
        'i aktivnosti na otvorenom kod Pule, Barbana i Vodnjanja. Otvoreno svaki dan 9–17 h, zadnji ulaz u 15 h. '
        f'Pozovite +385 98 224 314 ili rezervirajte online do {ONLINE_BOOKING_MAX} osoba.'
    ),
    "keywords": (
        'broj 1 avanturistički park Hrvatska, avanturistički park Istria, avanturistički park Hrvatska, '
        'zipline park Istria, zipline park Hrvatska, adrenalinski park Istria, aktivnosti na otvorenom Istria Hrvatska, '
        'visoke staze Hrvatska, obiteljske aktivnosti Istria, što raditi kod Pule, Glavani Park'
    ),
    "h1": 'Glavani Park – broj 1 avanturistički park u Hrvatskoj',
    "hero_badge": 'Broj 1 avanturistički park u Hrvatskoj',
    "hero_subtitle": (
        'Obiteljski avanturistički park u istarskom krajoliku — profesionalna i srdačna ekipa, '
        'zipline u šumi i uspomene o kojima ćete pričati godinama. Svratite na kavu prije nego krenete u avanturu.'
    ),
    "image": 'glavani-park-adventure-istria-croatia.jpg',
    "image_alt": 'Pogled iz zraka na Glavani Park, broj 1 avanturistički park u Istri, Hrvatska',
}

PAGES = [{'slug': 'sto-raditi-u-istri',
  'title': 'Što raditi u Istri | Vodič za obitelji i Glavani Park',
  'h1': 'Što raditi u Istri: potpuni vodič za posjetitelje',
  'meta_description': 'Otkrijte najbolje stvari za raditi u Istri — plaže, gradići na '
                      'brdu, gastronomiju i avanturu na otvorenom. Planirajte put s '
                      'Glavani Parkom kod Pule, Barbana i Vodnjanja. Otvoreno 9–17 h, '
                      'posljednji ulaz u 15 h.',
  'keywords': 'što raditi u Istri, atrakcije Istria, Istra s djecom, obiteljski odmor '
              'Istria, aktivnosti na otvorenom Istria, Glavani Park, avanturistički '
              'park Istria, izleti Istria Hrvatska',
  'hero_badge': 'Vodič za Istru · avantura na otvorenom',
  'hero_subtitle': 'Od rimske Pule i tartufnih šuma do ziplinea u šumi i '
                   'srednjovjekovnih gradova — Istra nagrađuje znatiželjne putnike. '
                   'Uključite Glavani Park u itinerar za cjelodnevni adrenalin između '
                   'Barbana i Vodnjanja.',
  'image': 'glavani-park-adventure-istria-croatia.jpg',
  'image_alt': 'Glavani Park avanturistički park u istarskom krajoliku kod Barbana i '
               'Pule',
  'sections': [{'h2': 'Zašto je Istra jedna od najsvestranijih destinacija u Hrvatskoj',
                'paragraphs': ['<p>Istra zauzima trokutasti poluotok na sjevernom rubu '
                               'Jadrana, gdje se talijanske, slavenske i '
                               'srednjoeuropske utjecaji stapaju u nešto jedinstveno. '
                               'Posjetitelji dolaze zbog obale — šarenih luka Rovinja, '
                               'stjenovitih uvala oko Pule i obiteljskih plaža '
                               'Medulina i Premanture — ali i unutrašnji krajolik '
                               'jednako je privlačan. Blaga brda prekrivena '
                               'vinogradima i maslinicima vode do utvrđenih sela poput '
                               'Motovuna i Grožnjana, dok tartufne šume i restorani s '
                               'hranom s farme čine gastronomski turizam samostalnim '
                               'razlogom za posjet.</p>',
                               '<p>Bilo da planirate tjedni obiteljski odmor ili '
                               'produženi vikend iz Trsta, Ljubljane ili Zagrebe, '
                               'Istra nudi neobičnu gustoću iskustava na kompaktnom '
                               'prostoru. Većina važnih lokacija udaljena je najviše '
                               'četrdeset pet minuta vožnje, pa su izleti jednostavni '
                               'i omogućuju spajanje kulture, prirode i aktivnog '
                               'odmora u jednom planu. Putnicima koji žele više od '
                               'sunca i mora poluotok nudi planinarske staze, cycling '
                               'rute, vinske ceste i neke od najboljih avanturističkih '
                               'objekata u Hrvatskoj — uključujući <strong>Glavani '
                               'Park</strong>, adrenalinski park kod sela Glavani '
                               'između <strong>Barbana</strong> i '
                               '<strong>Vodnjanja</strong>.</p>']},
               {'h2': 'Obalni vrhunci: Pula, Rovinj i Jadran',
                'paragraphs': ['<p><strong>Pula</strong> je najveći grad Istre i '
                               'prirodna polazna točka za istraživanje regije. Rimski '
                               'amfiteatar — jedan od najbolje očuvanih na svijetu — '
                               'dominira starim gradom, dok Nacionalni park Brijuni '
                               'nudi otočnu prirodu, otiske dinosaura i kristalno '
                               'čisto kupanje. Obitelji često jutro provode u areni '
                               'ili Aquariumu Pula, a poslijepodne traže dinamiku u '
                               'unutrašnjosti. Ako tražite <a '
                               'href="/hr/sto-raditi-kod-pule/">što raditi kod '
                               'Pule</a> izvan plaže, vožnja od trideset minuta do '
                               'Glavani Parka dodaje energičan kontrast kulturnom '
                               'jutru u gradu.</p>',
                               '<p><strong>Rovinj</strong>, s venecijanskim starim '
                               'gradom koji se uzdiže iz luke, najfotografiranija je '
                               'destinacija Istre. Popnite se na zvonik crkve sv. '
                               'Eufemije za panoramski pogled, šetajte umjetničkim '
                               'ateljima uskim ulicama i jedite svježe plodove mora na '
                               'obali. Rovinj je udaljen oko četrdeset pet minuta od '
                               'Glavani Parka, pa je kombinacija — jutro u gradu, '
                               'poslijepodne na ziplineu — potpuno izvediva tijekom '
                               'ljetne sezone.</p>',
                               '<p>Uz obalu pronaći ćete Limski kanal, dramatični '
                               'krški zaljev idealan za brodove i kajake; brdo Vrsar; '
                               'i mirne plaže istočne obale oko Rabca i Labina. Svaka '
                               'nudi drugačiji ritam, od živahnih odmarališta do uvala '
                               'u hladu borova.</p>']},
               {'h2': 'Unutrašnja Istra: gradići, vino i tartufi',
                'paragraphs': ['<p>Okrenite se prema unutrašnjosti i Istra otkriva '
                               'zeleniji, mirniji krajolik. Srednjovjekovni gradovi '
                               'stoje na brdima iznad doline rijeke Mirne: '
                               '<strong>Motovun</strong> domaćin je filmskog festivala '
                               'i lova na tartufe; <strong>Grožnjan</strong> se '
                               'pretvorio u selo umjetnika i galerija; '
                               '<strong>Hum</strong>, često navođen kao najmanji grad '
                               'na svijetu, šarmantan je zaustavljanje na Glagoljskoj '
                               'aleji.</p>',
                               '<p>Ljubitelji vina trebaju slijediti istarsku vinsku '
                               'cestu i kušati Malvaziju i Teran u obiteljskim '
                               'kletima. Rute maslinovog ulja i agroturizmi nude '
                               'degustacije istarskih delicija. Mnogi posjetitelji '
                               'zakazuju tartufni ručak u Livadeu ili Buzetu, zatim '
                               'voze prema Barbanu — poznatom po konjičkoj utrci Rasa '
                               '— prije završetka dana u Glavani Parku s potpuno '
                               'drugačijim doživljajem Istre.</p>',
                               '<p>Područje oko <strong>Barbana</strong> i '
                               '<strong>Vodnjanja</strong> manje je gušće od obale, '
                               'ali bogato autentičnošću. Crkva u Vodnjanju čuva '
                               'mumificirane svetce i jedan od najviših zvonika u '
                               'Istri, dok Barbansko srednjovjekovno jezgro i lokalne '
                               'konobe poslužuju istarska jela. Glavani Park leži na '
                               'cesti između ta dva mjesta, na adresi Glavani 10, s '
                               'besplatnim parkiranjem i radnim vremenom <strong>9–17 '
                               'h</strong> svaki dan (posljednji ulaz u <strong>15 '
                               'h</strong>).</p>']},
               {'h2': 'Aktivno što raditi u Istri na otvorenom',
                'paragraphs': ['<p>Aktivni putnici imaju bogat izbor. Biciklizam je '
                               'popularan duž Parenzane, bivše pruge koja povezuje '
                               'Trst s istarskom obalom. Planinari istražuju Park '
                               'prirode Učka na južnom rubu poluotoka, gdje označene '
                               'staze vode kroz bukove šume prema pogledima na '
                               'Kvarner. Penjači idu prema Dvigradu ili Limskom '
                               'kanalu, a kajakaši veslaju uz obalu od Pule do '
                               'Kamenjaka.</p>',
                               '<p>Za strukturiranu avanturu s profesionalnom '
                               'sigurnosnom opremom i educiranim instruktorima '
                               '<strong>Glavani Park</strong> se ističe kao jedan od '
                               'najvećih namjenskih adrenalinskih parkova u Hrvatskoj. '
                               'Na 1,5 hektara hrastove šume park nudi tri '
                               'certificirane visoke staze (žuta 2 m, plava 6 m, crna '
                               '10 m), zipline od 120 metara, ljuljačku visoku 12,5 '
                               'metara, ljudsku katapultu, Quick Jump s 20 metara i '
                               'vanjski zid za penjanje. Idealno je za obitelji, '
                               'parove i grupe koje žele pola ili cijeli dan '
                               'aktivnosti bez vlastite organizacije opreme.</p>',
                               '<p>Posjetitelji često spajaju Glavani Park s drugim '
                               'atrakcijama: jutro u parku i poslijepodne u Vodnjanu '
                               'ili Barbanu; ili obalno jutro u Puli i adrenalinsko '
                               'poslijepodne prije povratka u smještaj. Nazovite <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> '
                               'unaprijed za provjeru dostupnosti, posebno u srpnju i '
                               'kolovozu.</p>']},
               {'h2': 'Planiranje istarskog itinerara s Glavani Parkom',
                'paragraphs': ['<p>Uravnotežen itinerar mogao bi izgledati ovako: prvi '
                               'dan — rimska baština Pule i kupanje na Kamenjaku. '
                               'Drugi — stari grad Rovinj i večera na rivi. Treći — '
                               'tartufi ili degustacija vina u unutrašnjosti, zatim '
                               'Glavani Park za <a '
                               'href="/hr/avanturisticki-park-hrvatska/">obiteljske '
                               'aktivnosti</a> i zipline. Četvrti — izlet brodom na '
                               'Brijune ili opušten dan na plaži prije odlaska.</p>',
                               '<p>Glavani Park radi svaki dan od 9 do 17 sati, '
                               'posljednji ulaz u 15 sati — planirajte tri do četiri '
                               'sata za glavne atrakcije. '
                               f'{_HR_BOOKING["peak_walkin_note"]} '
                               f'{_HR_BOOKING["off_season_note"]} '
                               'Instruktori govore hrvatski i '
                               'engleski, a park je naveden na stranicama <a '
                               'href="https://www.istra.hr/hr/destinacije/barban/1531" '
                               'rel="noopener noreferrer">Turističke zajednice '
                               'Istre</a> kao preporučena vanjska atrakcija.</p>',
                               '<p>Bilo da vam je prioritet kultura, gastronomija, '
                               'obala ili adrenalin, Istra isporučuje — a Glavani Park '
                               'dodaje nezaboravnu aktivnu dimenziju svakom putovanju. '
                               'Pregledajte vodiče <a '
                               'href="/hr/zipline-hrvatska/">zipline Hrvatska</a>, <a '
                               'href="/hr/avanturisticki-park-hrvatska/">avanturistički '
                               'parkovi</a> i <a '
                               'href="/hr/sto-raditi-kod-pule/">izleti iz Pule</a> za '
                               'savršen posjet.</p>']}],
  'faqs': [{'q': 'Koje su obavezne lokacije u Istri?',
            'a': 'Vrhunci uključuju pulski amfiteatar, stari grad Rovinj, Nacionalni '
                 'park Brijuni, Motovun i Grožnjan, Limski kanal i Park prirode '
                 'Kamenjak. Aktivnim posjetiteljima Glavani Park kod Barbana nudi '
                 'zipline, visoke staze i adrenalinske vožnje na dohvat Pule i '
                 'Vodnjanja.'},
           {'q': 'Koliko dana treba za obilazak Istre?',
            'a': 'Minimum četiri do pet dana omogućuje obalu, unutrašnje gradiće i '
                 'barem jednu avanturu na otvorenom. Tjedan dana daje opušteniji tempo '
                 's degustacijama vina, danima na plaži i jutrom u Glavani Parku bez '
                 'žurbe.'},
           {'q': 'Je li Istra dobra za obitelji s djecom?',
            'a': 'Da. Istra je jedna od najobiteljskijih regija Hrvatske — sigurne '
                 'plaže, kratke udaljenosti i atrakcije za sve uzraste. Žuta staza '
                 'visine 2 m u Glavani Parku dizajnirana je za mlađu djecu, dok '
                 'tinejdžeri i roditelji mogu na više staze i zipline.'},
           {'q': 'Kada je najbolje vrijeme za posjet Istri?',
            'a': 'Od svibnja do rujna vrijeme je toplo, a park radi punim kapacitetom. '
                 'Lipanj i rujan idealni su za manje gužve. Glavani Park otvoren je '
                 '9–17 h; nazovite +385 91 896 4525 ili +385 98 224 314 za potvrdu '
                 'datuma.'}],
  'related': [{'slug': 'avanturisticki-park-hrvatska',
               'title': 'Naše aktivnosti',
               'desc': 'Devet glavnih atrakcija u Glavani Parku'},
              {'slug': 'sto-raditi-kod-pule',
               'title': 'Što raditi kod Pule',
               'desc': 'Izleti i aktivnosti na otvorenom u 30 min vožnje'},
             
              {'slug': 'zipline-hrvatska',
               'title': 'Vodič zipline Hrvatska',
               'desc': '120-metarski let kroz krošnje u Glavani Parku'}]},
 {'slug': 'obiteljske-aktivnosti-istri',
  'title': 'Obiteljske aktivnosti Istria | Avantura za djecu kod Pule',
  'h1': 'Obiteljske aktivnosti u Istri: zabava na otvorenom za sve uzraste',
  'meta_description': 'Najbolje obiteljske aktivnosti u Istri — plaže, parkovi prirode '
                      'i Glavani Park kod Pule i Barbana. Niska žuta staza za djecu, '
                      'zipline za tinejdžere. Otvoreno 9–17 h, posljednji ulaz 15 h. '
                      'Nazovite +385 98 224 314.',
  'keywords': 'obiteljske aktivnosti Istria, što raditi u Istri s djecom, obiteljski '
              'izlet Pula, aktivnosti za djecu Istria, Glavani Park obitelj, '
              'avanturistički park djeca Hrvatska',
  'hero_badge': 'Obiteljski izleti · svi uzrasti dobrodošli',
  'hero_subtitle': 'Istra je stvorena za obiteljski odmor — a Glavani Park kod Barbana '
                   'i Vodnjanja dodaje cjelodnevnu avanturu na otvorenom pod nadzorom '
                   'instruktora, sa stazama za djecu, tinejdžere i roditelje.',
  'image': '12-5m-high-swing-glavani-park-istria.webp',
  'image_alt': 'Obitelj uživa u visokoj ljuljački u Glavani Parku avanturističkom '
               'parku u Istri',
  'sections': [{'h2': 'Zašto je Istra idealna za obiteljski odmor',
                'paragraphs': ['<p>Istarski poluotok redovito se rangira među '
                               'najobiteljskijim destinacijama u Europi. Udaljenosti '
                               'su kratke, ceste uredne, u turističkim zonama se '
                               'široko govori engleski, a miks plaža, prirode i '
                               'kulture zabavlja djecu bez sati vožnje. Gradovi poput '
                               'Pule, Rovinja i Poreča nude sigurno kupanje, sladoled '
                               'na svakom koraku i povijesne znamenitosti — rimske '
                               'ruine, srednjovjekovne zidine i šetnice uz luku.</p>',
                               '<p>Izvan obale unutrašnja Istra nudi lagano '
                               'planinarenje, posjete farmama i demonstracije lova na '
                               'tartufe koje djeci približavaju ruralni život. '
                               'Smještaj ide od velikih hotela s bazenima do vila i '
                               'kampova u hladu borova. Bez obzira na budžet, regija '
                               'olakšava ravnotežu između opuštanja i aktivnosti — i '
                               'tu se savršeno uklapa <strong>Glavani '
                               'Park</strong>.</p>',
                               '<p>Istarski kalendar događanja — lokalni festivali, '
                               'koncerti u pulskoj Areni i sezonske fešte u Rovinju — '
                               'lako se uklapaju uz dan proveden u Glavani Parku. '
                               'Roditelji koji planiraju tjedni odmor često '
                               'rezerviraju jedan dan isključivo za avanturu u šumi, '
                               'dok ostatak tjedna posvećuju moru i kulturnim '
                               'znamenitostima. Takav ritam sprječava '
                               '„preplavljivanje“ djece pasivnim sadržajem i daje '
                               'svima nešto za iščekivati.</p>']},
               {'h2': 'Glavani Park: avantura prilagođena svakoj generaciji',
                'paragraphs': ['<p>Na adresi Glavani 10, između '
                               '<strong>Barbana</strong> (6 km) i '
                               '<strong>Vodnjanja</strong> (10 km), Glavani Park je '
                               'jedan od najvećih avanturističkih parkova u Hrvatskoj '
                               'na 1,5 hektara hrastove šume. Za razliku od igrališta '
                               'ili pasivnih atrakcija, park nudi stvarne fizičke '
                               'izazove pod nadzorom educiranih instruktora — jedna od '
                               'najisplativijih <strong>obiteljskih aktivnosti u '
                               'Istri</strong> za one koji žele više od plažnog '
                               'dana.</p>',
                               '<p>Središnji element za mlađe posjetitelje je '
                               '<strong>žuta visoka staza</strong> na visini od dva '
                               'metra. Uravnotežene grede, mostovi od užadi i niske '
                               'platforme grade samopouzdanje kod djece koja prvi put '
                               'pokušavaju avanturu u krošnjama. Roditelji mogu hodati '
                               'uz stazu i bodriti s tla ili se uključiti na istom '
                               'krugu. Tinejdžerima i odraslima plava staza na 6 '
                               'metara i crna na 10 metara nude veće izazove, '
                               'uključujući zipline od 113 metara u plavom krugu.</p>',
                               '<p>Samostalne atrakcije uključuju zipline od 120 '
                               'metara, ljuljačku visoku 12,5 metara, vanjski zid za '
                               'penjanje i aktivnosti na razini tla za mješovite '
                               'skupine. Ljudska katapulta i Quick Jump s 20 metara '
                               'namijenjeni su starijim tinejdžerima i odraslima s '
                               'posebnim uvjetima — osoblje savjetuje na blagajni.</p>',
                               '<p>Glavani Park surađuje s lokalnim turističkim '
                               'organizacijama i redovito prima grupe iz cijele regije '
                               '— od pulskih kampova do obiteljskih vila u Motovunu. '
                               'Recenzije na Google Maps ističu strpljivost '
                               'instruktora prema mlađoj djeci i jasne sigurnosne '
                               'upute, što je presudno kada roditelji prvi put vode '
                               'obitelj na visoke staze. Ako dolazite iz Slovenije ili '
                               'Italije cestovna povezanost preko graničnih prijelaza '
                               'u Istri jednostavna je tijekom cijele sezone.</p>']},
               {'h2': 'Cjelodnevni obiteljski dan u parku',
                'paragraphs': ['<p>Većina obitelji provede tri do četiri sata u '
                               'Glavani Parku, entuzijasti i duže. Osjenčano područje '
                               'za piknik s kavom, pićem i sladoledom omogućuje pauze '
                               'između aktivnosti bez napuštanja lokacije. Besplatno '
                               'parkiranje primjenjuju automobili, minibusevi i veći '
                               'autobusi — korisno za više obitelji ili izlete s '
                               'kampa.</p>',
                               '<p>Park radi svaki dan <strong>9–17 h</strong>, '
                               'posljednji ulaz u <strong>15 h</strong>. Dolazak prije '
                               'podneva daje najbolju šansu za više staza i atrakcija. '
                               f'{_HR_BOOKING["peak_walkin_note"]} '
                               f'{_HR_BOOKING["off_season_note"]} '
                               'Nazovite <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> '
                               '(engleski) ili <a href="tel:+38598224314">+385 98 224 '
                               '314</a> (hrvatski) ili rezervirajte online.</p>',
                               '<p>Ponesite udobnu sportsku odjeću, zatvorene cipele '
                               '(tenisice ili planinarske — bez sandala), kremu za '
                               'sunčanje i vodu. Osvježenja se prodaju u parku, ali '
                               'vlastita voda je pametna u vrućini. Vrijedne stvari '
                               'ostavite u automobilu prije opremanja harnesom.</p>',
                               '<p>Za obitelji s djecom različitih dobi preporučujemo '
                               'dolazak u manjoj grupi ili podijeljeni pristup stazama '
                               '— stariji na plavoj ruti dok mlađi završavaju žutu, '
                               'zatim zajednički zid za penjanje ili ljuljačka. '
                               'Instruktori pomažu koordinirati redoslijed kako niko '
                               'ne bi čekao predugo u ljetnoj vrućini. Na kraju dana '
                               'mnoge obitelji se vraćaju u Pulu za večeru uz more — '
                               'savršen završetak aktivnog obiteljskog izleta.</p>']},
               {'h2': 'Kombinacija Glavani Parka s drugim obiteljskim izletima',
                'paragraphs': ['<p>Glavani Park prirodno se spaja s drugim istarskim '
                               'destinacijama. Nakon jutarnjih ziplinea vožnja od '
                               'trideset minuta vodi u <strong>Pulu</strong> na '
                               'akvarij ili amfiteatar. Ili istražite srednjovjekovni '
                               '<strong>Barban</strong> i zvonik u '
                               '<strong>Vodnjanju</strong> istog dana — oba grada su '
                               'minuta vožnje od parka. Za kupanje obala oko Medulina '
                               'i Premanture udaljena je oko četrdeset minuta.</p>',
                               '<p>Obitelji iz Rovinja, Poreča ili vila u '
                               'unutrašnjosti često planiraju Glavani Park kao dan '
                               'avanture, a sljedeći dan oporavak na bazenu ili plaži. '
                               'Park preporučuje Turistička zajednica Istre, a '
                               'međunarodni posjetitelji hvalе profesionalnost '
                               'instruktora koji govore engleski.</p>',
                               '<p>Za proslave pitajte za <a '
                               'href="/hr/rodjendanske-zabave-istri/">rođendanske '
                               'pakete</a> s prioritetnim pristupom. Škole i klubovi '
                               'mogu raspitati o <a '
                               'href="/hr/skolski-izleti-istri/">edukativnim '
                               'programima</a> prilagođenim dobi.</p>']},
               {'h2': 'Smjernice po dobi i sigurnost za obitelji',
                'paragraphs': ['<p>Sigurnost je temelj svakog obiteljskog posjeta. '
                               'Svaki sudionik dobiva harnes, kacigu i obuku prije '
                               'aktivnosti. Visoke staze koriste kontinuirani osigurač '
                               'koji vas drži povezanima. Oprema je CE certificirana i '
                               'dnevno se provjerava.</p>',
                               '<p>Žuta staza dobrodošla je mlađoj djeci uz odgovornog '
                               'odraslog. Plava i crna staza namijenjene su starijoj '
                               'djeci, tinejdžerima i odraslima koji zadovoljavaju '
                               'minimalnu visinu. Zipline i visoka ljuljačka popularni '
                               'su kod tinejdžera; katapulta i Quick Jump imaju strože '
                               'uvjete. Ako niste sigurni, nazovite unaprijed — pomoći '
                               'ćemo planirati posjet.</p>',
                               '<p>Pročitajte stranicu <a '
                               'href="/hr/sigurnost/">sigurnost i oprema</a> za '
                               'certifikate i postupke. Glavani Park ugostio je tisuće '
                               'obitelji iz cijele Europe s ciljem da svaki posjet '
                               'bude uzbudljiv i siguran za roditelje.</p>']}],
  'faqs': [{'q': 'Koja je minimalna dob djece u Glavani Parku?',
            'a': 'Žuta staza visine 2 m dizajnirana je za mlađu djecu pod nadzorom '
                 'odrasle osobe. Za više atrakcije vrijede posebni uvjeti — '
                 'kontaktirajte +385 98 224 314 prije posjeta.'},
           {'q': 'Mogu li roditelji sudjelovati s djecom?',
            'a': 'Apsolutno. Roditelje potičemo na žutu i plavu stazu uz djecu. Mnoge '
                 'obitelji doživljavaju posjet kao zajedničku avanturu. Svaki sudionik '
                 'treba ulaznicu.'},
           {'q': 'Ima li park sjenice i hrane?',
            'a': 'Da. Osjenčano područje nudi kavu, bezalkoholna pića i sladoled. '
                 'Možete donijeti vlastite grickalice, ali molimo održavajte čistoću. '
                 'Nema punog restorana — obilan obrok prije ili poslije posjeta je '
                 'praktičan.'},
           {'q': 'Koliko je Glavani Park udaljen od Pule?',
            'a': 'Otprilike trideset minuta vožnje od Pule, četrdeset pet od Rovinja. '
                 'Besplatno parkiranje na Glavani 10, 52207 Barban.'}],
  'related': [{'slug': 'sto-raditi-u-istri',
               'title': 'Što raditi u Istri',
               'desc': 'Potpuni vodič poluotokom za obitelji i parove'},
              {'slug': 'sto-raditi-kod-pule',
               'title': 'Što raditi kod Pule',
               'desc': 'Izleti u 30 minuta od Pule'},
              {'slug': 'rodjendanske-zabave-istri',
               'title': 'Rođendanske zabave Istria',
               'desc': 'Proslava uz zipline i visoke staze'},
              {'slug': 'sigurnost',
               'title': 'Sigurnost i oprema',
               'desc': 'Certifikati, obuke i dnevne inspekcije'}]},
 {'slug': 'zipline-hrvatska',
  'title': 'Zipline Hrvatska | 120 m let kroz krošnje u Glavani Parku',
  'h1': 'Zipline Hrvatska: letite kroz istarsku šumsku krošnju',
  'meta_description': 'Doživite zipline u Hrvatskoj u Glavani Parku Istria — linije do '
                      '120 m i 20 m visine kod Pule i Barbana. Vođeno od instruktora, '
                      'CE certificirana oprema. Otvoreno 9–17 h. Rezervacije: +385 91 '
                      '896 4525.',
  'keywords': 'zipline Hrvatska, zipline Istria, zipline krošnje Pula, zipline kod '
              'Barbana, Glavani Park zipline, vanjski zipline Hrvatska, šumski zipline '
              'Istria',
  'hero_badge': 'Do 120 m · 20 m iznad tla',
  'hero_subtitle': 'Letite kroz hrastovu šumu na jednom od najdužih avanturističkih '
                   'ziplineova u Istri — pod nadzorom educiranih instruktora u Glavani '
                   'Parku između Barbana i Vodnjanja, trideset minuta od Pule.',
  'image': 'zipline-120m-glavani-park-istria-croatia.webp',
  'image_alt': 'Gost na ziplineu od 120 metara kroz drveće u Glavani Parku, Istria, '
               'Hrvatska',
  'sections': [{'h2': 'Zipline u Hrvatskoj: što očekivati',
                'paragraphs': ['<p>Zipline postao je jedna od najtraženijih aktivnosti '
                               'na otvorenom u Hrvatskoj, i to s razlogom. Raznoliki '
                               'krajolici — od dalmatinskog krša i šuma Plitvica do '
                               'istarskih hrastovih šuma — pružaju prirodne koridore '
                               'za let kroz krošnje. Za razliku od sezonskih '
                               'ziplineova na skijalištima, hrvatski avanturistički '
                               'parkovi rade tijekom toplih mjeseci s profesionalnim '
                               'sustavima, redundantnim linijama na mnogim '
                               'instalacijama i nadzorom instruktora na polazištu i '
                               'slijetanju.</p>',
                               '<p>Tražeći <strong>zipline Hrvatska</strong>, '
                               'kvaliteta i sigurnosni standardi variraju. Birajte '
                               'parkove s CE certificiranom opremom, kacigama i punim '
                               'harnesima, obukom prije vožnje i vidljivim rasporedom '
                               'inspekcija. Glavani Park kod <strong>Barbana</strong> '
                               'u Istri zadovoljava te kriterije i nudi neke od '
                               'najdužih i najviših linija na poluotoku — destinaciju '
                               'vrijednu planiranja odmora, a ne slučajnog '
                               'zaustavljanja uz cestu.</p>',
                               '<p>Hrvatska nudi zipline iskustva i u drugim regijama '
                               '— od primorskih parkova do planinskih lokacija — ali '
                               'rijetko koji kombiniraju dužinu linije, visinu i broj '
                               'dodatnih atrakcija unutar jedne ulaznice kao Glavani '
                               'Park. Za turiste koji već poznaju zipline iz Alpa ili '
                               'Slovenije, istarska šuma donosi drugačiju scenu: '
                               'mediteransko svjetlo kroz hrastove listove, miris '
                               'makije u pozadini i blizina mora koja omogućuje '
                               'kupanje istog dana.</p>']},
               {'h2': 'Zipline iskustva u Glavani Parku',
                'paragraphs': ['<p>Glavani Park upravlja više zipline elemenata na 1,5 '
                               'hektara. Glavna atrakcija je samostalni '
                               '<strong>zipline od 120 metara</strong> na <a '
                               'href="/hr/dolinski-zipline/">dolinskom ziplineu</a>, '
                               'koji nosi vozače do 20 metara iznad šumskog tla kroz '
                               'koridor zrelih hrastova. Instruktor prilagođava '
                               'harnes, provjerava spojeve i vodi kroz obuku prije '
                               'skoka s platforme. Let traje dovoljno dugo da osjetite '
                               'brzinu i visinu uz potpunu kontrolu od početka do '
                               'kraja.</p>',
                               '<p>Ugrađen u <strong>plavu visoku stazu</strong> na 6 '
                               'metara nalazi se zipline od 113 metara na <a '
                               'href="/hr/niski-zipline/">Stazi u krošnjama</a>, '
                               'između prve i zadnje platforme. Završetak plave staze '
                               'uključuje zračni prijelaz — idealno za one koji žele '
                               'zipline u kombinaciji s uravnoteženim preprekama. Crna '
                               'staza na 10 metara fokusirana je na zahtjevne elemente '
                               'bez zipline sekcije; mnogi gosti odaberu plavi krug i '
                               'samostalnih 120 metara u jednom posjetu.</p>',
                               '<p>Svi zipline elementi uključeni su u dnevnu '
                               'ulaznicu, a tijekom gužve osoblje upravlja redovima '
                               'kako bi sve bilo sigurno. U vrh sezone dođite prije '
                               'podneva za više vožnji.</p>',
                               '<p>Fotografiranje tijekom zipline vožnje preporučujemo '
                               'povjeriti action kamerama pričvršćenim na kacigu uz '
                               'odobrenje osoblja — ručno držanje mobitela na liniji '
                               'nije sigurno. Nakon vožnje mnogi gosti dijelimo '
                               'dojmove na terasi za piknik, uspoređujući brzinu '
                               'plavog kruga i samostalnih 120 metara. Ako planirate '
                               'više zipline lokacija u Hrvatskoj tijekom odmora, '
                               'Glavani Park ostaje referentna točka zbog opsega i '
                               'profesionalnosti tima.</p>']},
               {'h2': 'Tko može voziti zipline?',
                'paragraphs': ['<p>Zipline u Glavani Parku odgovara širokom spektru '
                               'posjetitelja — od tinejdžera na prvoj zračnoj vožnji '
                               'do odraslih u potrazi za vrhuncem istarskog odmora. '
                               'Minimalna visina i težina vrijede iz sigurnosnih '
                               'razloga — prikazane su na blagajni i objašnjavaju se '
                               'na obuci. Djeca koja ne zadovoljavaju uvjete mogu '
                               'uživati u žutoj stazi na 2 m i drugim aktivnostima dok '
                               'stariji voze zipline.</p>',
                               '<p>Potrebne su zatvorene sportske cipele i udobna '
                               'odjeća. Skinite labavi nakit, marame i nesigurne '
                               'predmete prije opremanja. Gledatelji mogu promatrati s '
                               'označenih mjesta — zajedničko iskustvo i za one koji '
                               'ostaju na tlu.</p>',
                               '<p>Ako imate zdravstvena stanja koja bi mogla utjecati '
                               'na vožnju — srce, trudnoću, nedavnu operaciju ili jaku '
                               'vertigo — razgovarajte s osobljem prije kupnje '
                               'ulaznice. Instruktori mogu preporučiti alternative '
                               'unutar parka.</p>',
                               '<p>Sezonski rad parka usklađen je s turističkom '
                               'sezonom Istre, ali proljeće i rana jesen nude manje '
                               'gužve i ugodnije temperature za nošenje harnesa. U '
                               'ljetnim vrhuncima dolazak u 9 sati omogućuje prvi '
                               'termin na ziplineu bez čekanja, nakon čega možete '
                               'mirno proći visoke staze. Za grupe i team building '
                               'pakete zipline je često centralni timski trenutak — '
                               'svi navijaju za kolege na platformi prije skoka.</p>']},
               {'h2': 'Lokacija i praktične informacije',
                'paragraphs': ['<p>Glavani Park nalazi se na Glavani 10, 52207 Barban, '
                               'na cesti između <strong>Vodnjanja</strong> (10 km) i '
                               'Barbana (6 km). S glavne ceste Pula–Labin skrenite u '
                               'Manjadvorce prema Glavani, zatim lijevo 300 metara do '
                               'ulaza. Besplatno parkiranje. GPS: 45°1′17″ N, 13°57′4″ '
                               'E.</p>',
                               '<p>Park radi <strong>9–17 h</strong>, posljednji ulaz '
                               '<strong>15 h</strong>. Planirajte najmanje tri sata za '
                               'zipline i jednu-dvije staze. '
                               f'{_HR_BOOKING["peak_walkin_note"]} '
                               f'{_HR_BOOKING["off_season_note"]} '
                               'Nazovite <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> '
                               '(engleski) ili <a href="tel:+38598224314">+385 98 224 '
                               '314</a> (hrvatski) ili rezervirajte online.</p>',
                               '<p>Iz <strong>Pule</strong> vožnja traje oko trideset '
                               'minuta — jedna od najpristupačnijih zipline '
                               'destinacija za goste na obali. Rovinj je oko četrdeset '
                               'pet minuta; Motovun oko sat vremena. Mnogi spajaju '
                               'jutro na ziplineu s poslijepodnevnim Barbandom, '
                               'Vodnjanom ili plažama južno od Pule.</p>']},
               {'h2': 'Zašto Glavani Park za zipline iskustvo u Hrvatskoj',
                'paragraphs': ['<p>Nekoliko čimbenika izdvaja Glavani Park od manjih '
                               'operatera. Površina od 1,5 ha s više atrakcija znači '
                               'cjelodnevnu aktivnost, ne petominutnu vožnju. '
                               'Bilingvalni tim, uključujući instruktore na engleskom, '
                               'dobrodošao je međunarodnim gostima. Oprema se '
                               'provjerava dnevno, a park preporučuje Turistička '
                               'zajednica Istre.</p>',
                               '<p>Bilo da ste obitelj koja tinejdžerima predstavlja '
                               'zračnu avanturu, par u potrazi za aktivnim datumom ili '
                               'korporativna grupa — ziplineovi u Glavani Parku ostaju '
                               'najjači doživljaj odmora. Pogledajte <a '
                               'href="/hr/avanturisticki-park-hrvatska/">avanturističke '
                               'parkove u Hrvatskoj</a>, <a '
                               'href="/hr/avanturisticki-park-hrvatska/">obiteljske '
                               'aktivnosti</a> i <a href="/hr/sigurnost/">sigurnosne '
                               'postupke</a> prije dolaska.</p>',
                               '<p>Planiranje zipline dana u Istri uključuje provjeru '
                               'vremenske prognoze — iako park radi u laganoj kiši, '
                               'grmljavina zaustavlja aktivnosti na visini. Pripremite '
                               'rezervne sportske cipele u automobilu i laganu jaknu '
                               'za jutarnje sate u šumi. Nakon zipline posjeta '
                               'obitelji često nastavljaju prema Vodnjanu ili Barbanu '
                               'za sladoled i kratku šetnju starim gradskim jezgrom, '
                               'što zaokružuje poludnevni izlet bez dodatnih ulaznica '
                               'ili komplicirane logistike.</p>']}],
  'faqs': [{'q': 'Koliko je dugačak zipline u Glavani Parku?',
            'a': 'Samostalni zipline dugačak je 120 metara, do 20 metara visine. Plava '
                 'staza uključuje zipline od 113 metara između platformi na 6 metara.'},
           {'q': 'Trebam li rezervaciju za zipline?',
            'a': f'{_HR_BOOKING["peak_walkin_note"]} '
                 f'{_HR_BOOKING["off_season_note"]} '
                 'Nazovite +385 98 224 314 ili rezervirajte online.'},
           {'q': 'Je li zipline siguran za početnike?',
            'a': 'Da. Svaki vozač dobiva harnes, kacigu i obuku od educiranog '
                 'instruktora. Oprema je CE certificirana i dnevno provjeravana. '
                 'Osoblje je na polazištu i slijetanju.'},
           {'q': 'Mogu li samo zipline bez visokih staza?',
            'a': 'Dnevna ulaznica uključuje sve atrakcije. Možete se fokusirati na '
                 'zipline i samostalne vožnje bez cijelih staza, iako mnogi '
                 'kombiniraju oboje.'},
           {'q': 'Koliko je visok zipline u Glavani Parku?',
            'a': 'Samostalni zipline u Glavani Parku dostiže do 20 metara iznad '
                 'šumskog tla. Zipline na plavoj stazi teče na 6 metara visine između '
                 'platformi.'},
           {'q': 'Koliko je zipline u Glavani Parku udaljen od Pule?',
            'a': 'Glavani Park je otprilike 30 minuta automobilom iz Pule — jedan od '
                 'najbližih zipline parkova istarskoj obali. Besplatno parkiranje na '
                 'Glavani 10, 52207 Barban.'},
           {'q': 'Koja je minimalna dob za zipline u Glavani Parku?',
            'a': 'Minimalna visina i dob vrijede iz sigurnosnih razloga. Mlađa djeca '
                 'mogu uživati u žutoj stazi na 2 m, dok starija djeca i tinejdžeri '
                 'voze zipline. Nazovite +385 98 224 314 prije posjeta ako niste '
                 'sigurni.'}],
  'related': [{'slug': 'avanturisticki-park-hrvatska',
               'title': 'Avanturistički parkovi u Hrvatskoj',
               'desc': 'Pregled atrakcija u Glavani Parku Istria'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Naše aktivnosti',
               'desc': 'Zipline i visoke staze za sve uzraste'},
              {'slug': 'sto-raditi-kod-pule',
               'title': 'Što raditi kod Pule',
               'desc': 'Zipline izlet iz Pule za 30 minuta'},
              {'slug': 'sigurnost',
               'title': 'Sigurnost i oprema',
               'desc': 'Standardi harnesa i dnevne inspekcije'}]},
 {'slug': 'skolski-izleti-istri',
  'title': 'Školski izleti Istria | Edukativni posjeti Glavani Parku',
  'h1': 'Školski izleti u Istri: učenje na otvorenom u Glavani Parku',
  'meta_description': 'Edukativni školski izleti u Istri u Glavani Parku — procjena '
                      'rizika, koordinacija i priroda kod Pule i Barbana. Staze '
                      'prilagođene dobi. Rezervacije grupa: +385 98 224 314.',
  'keywords': 'školski izleti Istria, edukativni posjeti Hrvatska, školski izlet Pula, '
              'obrazovanje na otvorenom Istria, Glavani Park škola, razredni izlet '
              'avantura',
  'hero_badge': 'Škole i mlade grupe · učenje povezano s kurikulumom',
  'hero_subtitle': 'Iznesite nastavu na otvorenom s programima pod vodstvom '
                   'instruktora koji podučavaju procjeni rizika, fizičkoj koordinaciji '
                   'i timskom radu u Glavani Parku između Barbana i Vodnjanja.',
  'header_call_only': True,
  'image': 'climbing-wall-outdoor-activities-istria.webp',
  'image_alt': 'Školska grupa na edukativnom posjetu Glavani Park avanturističkom '
               'parku, Istria',
  'gallery_heading': 'Galerija školskih izleta',
  'gallery': [
      {
          'image': 'visitor-gallery-school-group-7.webp',
          'en_alt': 'School group in helmets and harnesses ready for the high-ropes course at Glavani Park',
          'hr_alt': 'Školska grupa u kacigama i harnesima prije visokih staza u Glavani Parku',
      },
      {
          'image': 'visitor-gallery-group-60.webp',
          'en_alt': 'School and youth group ready for activities at Glavani Park, Istria',
          'hr_alt': 'Školska i mlada grupa spremna za aktivnosti u Glavani Parku, Istria',
      },
      {
          'image': 'visitor-gallery-group-big-58.webp',
          'en_alt': 'Large group of visitors at Glavani Park adventure park, Istria',
          'hr_alt': 'Velika grupa posjetitelja u avanturističkom parku Glavani, Istria',
      },
      {
          'image': 'visitor-gallery-group-event-10.webp',
          'en_alt': 'Group of visitors in harnesses at Glavani Park between activities',
          'hr_alt': 'Grupa posjetitelja u harnesima u Glavani Parku između aktivnosti',
      },
  ],
  'sections': [{'h2': 'Vrijednost obrazovanja na otvorenom u Istri',
                'paragraphs': ['<p>Nastava u učionici temelj je obrazovanja, ali neke '
                               'lekcije najdublje zauzimaju mjesto na otvorenom — gdje '
                               'učenici procjenjuju stvarni rizik, podržavaju kolege '
                               'pod blagim pritiskom i otkrivaju fizičke sposobnosti o '
                               'kojima nisu znali. Blaga klima i pristupačna '
                               'geografija Istre čine regiju idealnom za školske '
                               'ekskurzije, bilo da ste domaća škola ili međunarodna '
                               'razmjena.</p>',
                               '<p><strong>Glavani Park</strong> nudi strukturirano '
                               'okruženje za <strong>školski izleti u Istri</strong> '
                               'bez izazova nesuperviziranih šetnji šumom ili '
                               'neformalnih plažnih dana. Svaku aktivnost vode '
                               'educirani instruktori s CE certificiranom opremom, '
                               'stazama prilagođenim dobi i jasnim sigurnosnim obukama '
                               'prije napuštanja tla.</p>',
                               '<p>Škole iz cijele Istre — Pula, Poreč, Rovinj, Labin '
                               '— redovito koriste Glavani Park kao destinaciju za '
                               'završni razred ili sportske dane. Međunarodne škole s '
                               'kampusom u Istri cijene bilingualne instruktore i '
                               'mogućnost prilagodbe programa na engleskom. Učenici '
                               'uče da je rizik u kontroliranom okruženju nešto što se '
                               'procjenjuje i upravlja, a ne samo nešto čega treba '
                               'bojati se.</p>']},
               {'h2': 'Edukativni programi u Glavani Parku',
                'paragraphs': ['<p>Školski posjeti mogu naglasiti različite ishode '
                               'ovisno o dobi i kurikulumu. Učenici nižih razreda '
                               'koriste žutu stazu na 2 m — razvija ravnotežu, '
                               'koordinaciju i samopouzdanje uz dovoljno blizine tla '
                               'da nastavnici promatraju i bodre. Srednjoškolci '
                               'pristupaju plavoj stazi na 6 m sa ziplineom od 113 m '
                               'ili crnoj na 10 m za napredniji fizički odgoj i module '
                               'vodstva.</p>',
                               '<p>Prirodne teme uključuju procjenu rizika '
                               '(prepoznavanje opasnosti, slijede naredbi, pravilna '
                               'uporaba OZO), fiziku i inženjerstvo (kako rade harnes, '
                               'škripci i sustavi usporavanja), ekološku svijest '
                               '(ekologija hrastove šume, održivi turizam) i socijalni '
                               'razvoj (podrška vršnjacima, komunikacija pod izazovom, '
                               'inkluzivno sudjelovanje).</p>',
                               '<p>Nastavnici dobivaju informacije prije posjeta — '
                               'sigurnosni postupci, preporučeni omjeri nadzora, '
                               'odjeća i prijedlozi aktivnosti prije i poslije izleta. '
                               'Nazovite <a href="tel:+38598224314">+385 98 224 '
                               '314</a> za veličinu grupe, datume i prilagodbu '
                               'programa.</p>',
                               '<p>Integracija s kurikulumom fizike može uključivati '
                               'razgovor o silama na zipline kolici, trenju i '
                               'gravitaciji na Quick Jumpu te statičkoj opterećenosti '
                               'mostova od užadi. Biologija i geografija mogu '
                               'obuhvatiti vrste drveća u parku i održivo gospodarenje '
                               'šumom. Nastavnici dobivaju konkretne teme za domaću '
                               'zadaću odmah nakon povratka autobusom u školu.</p>']},
               {'h2': 'Sigurnost i nadzor učeničkih grupa',
                'paragraphs': ['<p>Sigurnost učenika neprihvatljiva je za kompromis. '
                               'Glavani Park provodi dnevne inspekcije opreme, '
                               'kontinuirani osigurač na visokim stazama i nadzor '
                               'instruktora na svakom polazištu. Svaki učenik dobiva '
                               'kacigu i harnes koje prilagođava osoblje te verbalnu '
                               'obuku primjerenu dobi i jeziku. Dostupne su obuke na '
                               'hrvatskom i engleskom.</p>',
                               '<p>Škole zadržavaju vlastitu dužnost brige uz '
                               'instruktore parka — tipično jedan nastavnik ili '
                               'roditelj po manjoj skupini uz osoblje parka. Minimalna '
                               'visina i zdravstveni uvjeti vrijede za određene '
                               'atrakcije; komuniciraju se pri rezervaciji kako bi '
                               'učitelji postavili realna očekivanja.</p>',
                               '<p>Detalji certifikata i operativnih standarda '
                               'objavljeni su na <a href="/hr/sigurnost/">stranici o '
                               'sigurnosti</a>. Park preporučuje Turistička zajednica '
                               'Istre i ugostio je škole iz Hrvatske i susjednih '
                               'zemalja.</p>',
                               '<p>Sigurnosni protokoli za škole uključuju jasnu točku '
                               'okupljanja, popis prisutnih učenika i koordinaciju s '
                               'vozačem autobusa oko vremena dolaska i odlaska. Za '
                               'veće škole s više razreda moguće je organizirati '
                               'rotaciju kroz staze kako bi svaki učenik imao smislenu '
                               'aktivnost bez prevelike gužve. Glavani Park ponosan je '
                               'što je dio obrazovnog krajolika Istre i svake godine '
                               'proširuje suradnju s novim školama.</p>']},
               {'h2': 'Logistika školskih ekskurzija u Istri',
                'paragraphs': ['<p>Glavani Park, Glavani 10, 52207 Barban, između '
                               '<strong>Vodnjanja</strong> (10 km) i '
                               '<strong>Barbana</strong> (6 km). Parkiranje autobusa i '
                               'minibuseva besplatno je na lokaciji. Od '
                               '<strong>Pule</strong> oko trideset minuta; od Rovinja '
                               'oko četrdeset pet. Park radi <strong>9–17 h</strong>, '
                               'posljednji ulaz <strong>15 h</strong> — većina škola '
                               'dolazi u 9:30 na posjet od 3–4 sata.</p>',
                               '<p>Učenici trebaju zatvorene sportske cipele, udobnu '
                               'odjeću i zaštitu od sunca ljeti. Užinu možete pojesti '
                               'u osjenčanom području za piknik; pića i sladoled '
                               'prodaju se u parku. Toaleti i osnovni sadržaji blizu '
                               'su blagajne.</p>',
                               '<p>Kombinirajte posjet kulturnom zaustavljanju u '
                               'Vodnjanu (zvonik, mumificirani svetci) ili Barbanu '
                               '(srednjovjekovne zidine) za cjelodnevnu ekskurziju '
                               'koja spaja aktivnost i baštinu.</p>']},
               {'h2': 'Rezervirajte školski izlet u Glavani Park',
                'paragraphs': ['<p>Najava je obavezna za školske grupe. Navedite '
                               'procijenjeni broj učenika, dob, željeni datum i '
                               'posebne zahtjeve (mješovite sposobnosti, gledatelji u '
                               'kolicima, jezične preferencije). Potvrdit ćemo '
                               'raspored instruktora, vrijeme i cijene.</p>',
                               '<p>Za omladinske klubove, skautske grupe i ljetne '
                               'kampove u istarskim kampovima vrijede slični paketi — '
                               'pogledajte <a href="/hr/partneri/">partnerski '
                               'program</a> za pružatelje smještaja. Bilo da planirate '
                               'jedan razredni izlet ili godišnju tradiciju avanture, '
                               'Glavani Park pruža edukativno iskustvo koje učenici '
                               'spominju i nakon povratka u učionicu.</p>',
                               '<p>Nastavnici izvještavaju da rasprave nakon posjeta — '
                               'crteži sustava škripaca, refleksivni eseji o '
                               'prevladavanju straha ili rasprave o riziku i nagradi — '
                               'produžuju vrijednost poludnevnog izleta daleko izvan '
                               'vožnje autobusom doma.</p>',
                               '<p>Školski izleti u Glavani Park mogu uključivati i '
                               'natjecateljski element — koji razred brže završi plavu '
                               'stazu uz poštivanje sigurnosti — što dodaje zdravu '
                               'dinamiku bez stvarnog rizika. Nastavnici fizičkog '
                               'odgoja mogu povezati posjet s ocjenjivanjem napredka u '
                               'koordinaciji i hrabrosti tijekom semestra. Za škole s '
                               'učenícima s posebnim potrebama kontaktirajte nas '
                               'unaprijed kako bismo predložili format sudjelovanja '
                               'prilagođen mogućnostima svakog učenika.</p>',
                               '<p>Škole koje ponavljaju izlet svake godine grade '
                               'tradiciju — stariji učenici pomažu mlađima na žutoj '
                               'stazi, a nastavnici koriste poznati format za bržu '
                               'organizaciju. Glavani Park pruža stabilan edukativni '
                               'partner s jasnim sigurnosnim protokolima koji se ne '
                               'mijenjaju iz sezone u sezonu, što olakšava odobrenje '
                               'stručnjaka u školi i roditelja. Kontaktirajte nas na '
                               'početku školskog polugodišta za rezervaciju proljećnih '
                               'i jesenskih termina prije nego kalendar popuni.</p>']}],
  'faqs': [{'q': 'Koje dobne skupine mogu doći na školski izlet?',
            'a': 'Dobrodošli učenici od osnovne do srednje škole. Žuta staza odgovara '
                 'mlađima; plava i crna starijima. Minimalna visina vrijedi za neke '
                 'atrakcije — razgovarajte o profilu razreda pri rezervaciji na +385 '
                 '98 224 314.'},
           {'q': 'Trebaju li nastavnici plaćati ulaz?',
            'a': 'Omjeri nadzora i cijene za nastavnike dogovaraju se pri rezervaciji. '
                 'Kontaktirajte park za trenutnu politiku besplatnih mjesta za '
                 'pratitelje.'},
           {'q': 'Postoji li minimalna veličina grupe?',
            'a': 'Paketi su dizajnirani za veličinu razreda. Manje homeschool ili '
                 'klupske grupe neka nazovu za dostupnost i cijene.'},
           {'q': 'Može li se posjet povezati s kurikulumom?',
            'a': 'Da. Materijali prije posjeta podržavaju teme rizika, fizike, '
                 'fizičkog odgoja i ekologije. Nastavnici mogu instruktorima priopćiti '
                 'specifične ciljeve učenja prije aktivnosti.'}],
  'related': [{'slug': 'team-building-istri',
               'title': 'Team building Istria',
               'desc': 'Programi za korporativne i sportske grupe'},
              {'slug': 'rodjendanske-zabave-istri',
               'title': 'Rođendanske zabave Istria',
               'desc': 'Paketi proslava za mlade'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Naše aktivnosti',
               'desc': 'Staze i atrakcije po dobi'},
              {'slug': 'sigurnost',
               'title': 'Sigurnost i oprema',
               'desc': 'Standardi nadzora učenika'}]},
 {'slug': 'sto-raditi-kod-pule',
  'title': 'Što raditi kod Pule | Izleti i Glavani Park',
  'h1': 'Što raditi kod Pule: izleti i avantura na otvorenom',
  'meta_description': 'Najbolje stvari za raditi kod Pule — rimski spomenici, plaže '
                      'Kamenjak i zipline u Glavani Parku 30 minuta dalje. Otvoreno '
                      '9–17 h, posljednji ulaz 15 h. Nazovite +385 91 896 4525.',
  'keywords': 'što raditi kod Pule, izleti iz Pule, aktivnosti na otvorenom Pula, '
              'obiteljski izlet Pula, Glavani Park Pula, avantura kod Pule Hrvatska',
  'hero_badge': '30 min od Pule · besplatno parkiranje',
  'hero_subtitle': 'Izvan amfiteatra i jadranskih plaža unutrašnja Istra nudi zipline, '
                   'visoke staze i adrenalinske vožnje u Glavani Parku — lak '
                   'poludnevni bijeg kod Barbana i Vodnjanja.',
  'location_map': True,
  'sections': [{'h2': 'Pula kao baza za istraživanje Istre',
                'paragraphs': ['<p><strong>Pula</strong> sidri južni vrh Istre s '
                               'jednim od najprometnijih aerodroma u Hrvatskoj, '
                               'dubokom rimskom baštinom i neposrednim pristupom '
                               'Jadranu. Većina posjetitelja poznaje Arenu — '
                               'amfiteatar iz prvog stoljeća koji i danas prima '
                               'koncerte — i obalni Park prirode Kamenjak sa '
                               'stjenovitim uvalama i borovim šetnicama. No boravak u '
                               'Puli stavlja vas na dohvat unutrašnjih sela, vinskog '
                               'kraja i najboljih avantura na otvorenom.</p>',
                               '<p>Kad ste obišli gradske znamenitosti i dane na '
                               'plaži, a tražite nešto aktivno, <strong>Glavani '
                               'Park</strong> spada među najbolje ocijenjene '
                               '<strong>aktivnosti kod Pule</strong> bez cjelodnevne '
                               'vožnje. Park leži trideset minuta u unutrašnjost na '
                               'Glavani 10, 52207 Barban, na cesti između Barbana i '
                               'Vodnjanja — dovoljno blizu za jutarnji izlet prije '
                               'ručka u Puli, dovoljno duboko u šumi za osjećaj '
                               'bijega.</p>',
                               '<p>Pula nudi bogat kalendar događanja — Filmski '
                               'festival, Outlook festival na Fortici, lokalne fešte '
                               'vinara — pa je planiranje „pulskog tjedna“ uključujući '
                               'Glavani Park zahtijeva samo malo koordinacije. Aktivni '
                               'putnici često biraju tri dana obale i jedan dan '
                               'unutrašnjosti; park se prirodno uklapa u četvrti dan '
                               'kada trebate promjenu ritma od ležaljki i ručaka uz '
                               'more.</p>']},
               {'h2': 'Obalne i kulturne atrakcije oko Pule',
                'paragraphs': ['<p>Prije odlaska u unutrašnjost, obalni vrhunci unutar '
                               'dvadeset minuta uključuju Aquarium Pula u bivšoj '
                               'tvrđavi — odličan za obitelji s malom djecom. '
                               'Nacionalni park Brijuni — brodom iz Fažane — spaja '
                               'arheologiju, safari životinje i kupanje. Kamenjak na '
                               'Premanturi nudi mjesta za skok s litice (za iskusne '
                               'plivače), biciklističke staze i kristalno more.</p>',
                               '<p>U gradu hram Augusta, Slavoluk Sergijevaca i '
                               'venecijanska tvrđina nagrađuju nekoliko sati hodanja. '
                               'Večeri pripadaju rivi i konobama s istarskim '
                               'tjesteninama, plodovima mora i Malvazijom. Ta iskustva '
                               'definiraju Pulu; Glavani Park ih nadopunjuje '
                               'strukturiranom fizičkom avanturom umjesto da ih '
                               'zamjenjuje.</p>',
                               '<p>Za goste bez automobila moguć je dogovor taksi '
                               'usluge ili privatnog transfera iz Pule — navedite '
                               'Glavani 10, Barban, jer lokalni vozači znaju lokaciju. '
                               'Neki pulski hoteli u partnerskom programu nude letke '
                               'ili QR kodove za brzu rezervaciju. Usporedba s drugim '
                               'aktivnostima kod Pule — delfinari, buggy ture, '
                               'jedrenje — pokazuje da park nudi jedinstvenu '
                               'kombinaciju visine, brzine i timskog doživljaja u '
                               'prirodi.</p>']},
               {'h2': 'Glavani Park: avantura u unutrašnjosti',
                'paragraphs': ['<p>Na 1,5 hektara hrastove šume Glavani Park je jedan '
                               'od najvećih namjenskih adrenalinskih parkova u '
                               'Hrvatskoj. Atrakcije uključuju tri visoke staze (žuta '
                               '2 m, plava 6 m, crna 10 m), zipline 120 m, zipline 113 '
                               'm na plavoj stazi, ljuljačku 12,5 m, ljudsku '
                               'katapultu, Quick Jump 20 m i vanjski zid za penjanje. '
                               'Instruktori na engleskom rade na svakoj stanici s CE '
                               'certificiranim harnesima i kacigama.</p>',
                               '<p>Park odgovara obiteljima, parovima i grupama u '
                               'pulskim hotelima, vilama ili kampovima koje žele pauzu '
                               'od pijeska i razgledavanja. Većina provede tri do '
                               'četiri sata. Besplatno parkiranje za automobile i veće '
                               'vozilo. Radno vrijeme <strong>9–17 h</strong>, '
                               'posljednji ulaz <strong>15 h</strong> — dođite prije '
                               'podneva za više atrakcija.</p>',
                               '<p>Rezervirajte prije polaska — '
                               f'{_HR_BOOKING["peak_walkin_note"]} '
                               f'{_HR_BOOKING["off_season_note"]} '
                               'Nazovite <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> ili '
                               'rezervirajte online.</p>',
                               '<p>Poslijepodnevni posjet parku omogućuje jutarnje '
                               'kupanje na Kamenjaku ili obilazak amfiteatra bez '
                               'žurbe, uz dolazak u park do 14 sati za solidan broj '
                               'aktivnosti prije zatvaranja. Noćenje u Puli nakon '
                               'adrenalinskog dana često uključuje opuštenu večeru u '
                               'konobi — idealan balans za odmor u Istri.</p>']},
               {'h2': 'Spajanje Pule i unutrašnje Istre u jedan dan',
                'paragraphs': ['<p>Popularan plan: rimska Pula ili plaža ujutro, '
                               'Glavani Park rano poslijepodne (posljednji ulaz u 15 '
                               'h). Ili cijelo jutro u parku, zatim '
                               '<strong>Barban</strong> ili <strong>Vodnjan</strong> — '
                               'oba su minuta vožnje od ulaza. Za duže rute dodajte '
                               'degustaciju vina u središnjoj Istri ako prihvatite '
                               'više vožnje.</p>',
                               '<p>Uže rasporede park sam ispunjava zadovoljavajućim '
                               'poludnevnim doživljajem. Širi vodič <a '
                               'href="/hr/sto-raditi-u-istri/">što raditi u Istri</a> '
                               'pomaže u planiranju višednevnog putovanja.</p>']},
               {'h2': 'Dolazak iz Pule u Glavani Park',
                'paragraphs': ['<p>Iz Pule krenite prema Labinu i skrenite u '
                               'Manjadvorce prema Glavani. Nastavite lijevo lokalnom '
                               'cestom 300 metara do ulaza. Navigacija i GPS (45°1′17″ '
                               'N, 13°57′4″ E) jednostavni su za najam automobila. '
                               'Nije potreban 4x4.</p>',
                               '<p>Javni prijevoz ograničen je; najam automobila ili '
                               'organizirani izlet praktičan je izbor. Kod rezervacije '
                               'taksi transfera navedite adresu Glavani 10, Barban. '
                               'Detalje atrakcija potražite na <a '
                               'href="/hr/zipline-hrvatska/">zipline Hrvatska</a>, <a '
                               'href="/hr/avanturisticki-park-hrvatska/">obiteljske '
                               'aktivnosti</a> i <a '
                               'href="/hr/avanturisticki-park-hrvatska/">avanturistički '
                               'park</a> prije putovanja.</p>',
                               '<p>Pula kao univerzitetski i industrijski grad ima i '
                               'residentnu populaciju koja vikendom traži izlet u '
                               'prirodu — Glavani Park odgovara i lokalnim obiteljima, '
                               'ne samo turistima. Pulski stanari često imaju prednost '
                               'fleksibilnog dolaska radnim danom kad su redovi kraći. '
                               'Kombinacija amfiteatra, Glavani Parka i večere u '
                               'Fažani ili Medulinu stvara „pulski vikend paket“ koji '
                               'možete preporučiti prijateljima koji prvi put '
                               'posjećuju Istru.</p>',
                               '<p>Glavani Park nadopunjuje tipičan „pulski“ odmor '
                               'koji uključuje amfiteatar, riblji market i večernju '
                               'šetnju uz luku. Aktivni putnici često traže upravo '
                               'jedan dan bez povijesnih spomenika i jedan dan bez '
                               'ležanja — park ispunjava taj zahtjev bez odlaska u '
                               'drugi kraj Hrvatske. Povratna vožnja prema Puli u '
                               'kasno poslijepodne omogućuje večeru u gradu uz pogled '
                               'na more, što zaokružuje savršen dan izvan gužve na '
                               'plaži.</p><p>Taxi i rideshare usluge iz Pule do '
                               'Barbana dostupne su sezonski; dogovorite povratak '
                               'unaprijed jer javni prijevoz ne pokriva Glavani '
                               'direktno. Gosti iz Medulina i Premanture imaju sličnu '
                               'udaljenost kao centar Pule — Glavani Park jednako je '
                               'logičan izbor za cijeli južni rub Istre.</p>']}],
  'faqs': [{'q': 'Koliko je Glavani Park udaljen od centra Pule?',
            'a': 'Otprilike trideset minuta automobilom, ovisno o prometu i polazištu. '
                 'Besplatno parkiranje na Glavani 10, 52207 Barban.'},
           {'q': 'Mogu li u jednom danu obići Pulu i Glavani Park?',
            'a': 'Da. Mnogi ujutro obilaze grad ili plažu, poslijepodne idu u park. '
                 'Dođite prije 15 h za posljednji ulaz; zatvaranje u 17 h.'},
           {'q': 'Je li park prikladan nakon plažnog dana?',
            'a': 'Apsolutno — potrebne su zatvorene cipele, pa se presvucite iz '
                 'japanke prije dolaska. Osjenčana šuma hladnija je od otvorene plaže '
                 'u vrućini.'},
           {'q': 'Trebam li rezervirati iz Pule ili samo doći?',
            'a': f'{_HR_BOOKING["peak_walkin_note"]} '
                 f'{_HR_BOOKING["off_season_note"]} '
                 'Nazovite +385 98 224 314 ili rezervirajte online.'}],
  'related': [{'slug': 'sto-raditi-u-istri',
               'title': 'Što raditi u Istri',
               'desc': 'Potpuni vodič destinacijom poluotoka'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Naše aktivnosti',
               'desc': 'Staze prilagođene djeci kod Pule'},
              {'slug': 'zipline-hrvatska',
               'title': 'Zipline Hrvatska',
               'desc': '120-metarski let iz baze u Puli'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Avanturistički parkovi Hrvatska',
               'desc': 'Zašto Glavani Park vodi regiju'}]},
 {'slug': 'sigurnost',
  'title': 'Sigurnost u Glavani Parku | Oprema i postupci',
  'h1': 'Sigurnost u Glavani Parku: oprema, obuka i povjerenje',
  'meta_description': 'Sigurnost Glavani Park — CE certificirani harnes, dnevne '
                      'inspekcije, educirani instruktori i kontinuirani osigurač na '
                      'visokim stazama kod Pule. Pitanja: +385 98 224 314.',
  'keywords': 'sigurnost Glavani Park, sigurnost avanturističkog parka Hrvatska, '
              'sigurnost visokih staza Istria, CE certificirani harnes Hrvatska, '
              'sigurnost zipline Pula, standardi opreme park',
  'hero_badge': 'CE certificirana oprema · dnevne inspekcije',
  'hero_subtitle': 'Svaku atrakciju u Glavani Parku vode educirani instruktori s '
                   'provjerenom, certificiranom opremom — jer je povjerenje u '
                   'sigurnost temelj svake velike avanture.',
  'banner_mod': 'safety',
  'image': 'team-building-gallery-5.webp',
  'image_alt': 'Kacige i harnesi pripreavljeni za grupnu sigurnosnu obuku u Glavani Parku, Istria',
  'sections': [{'h2': 'Naša sigurnosna filozofija',
                'paragraphs': ['<p>Adrenalin i sigurnost nisu suprotnosti — ovisni su '
                               'jedan o drugome. Posjetitelji skaču s platformi i kače '
                               'se na zipline jer vjeruju sustavima koji ih drže. U '
                               '<strong>Glavani Parku</strong> to povjerenje '
                               'zarađujemo vidljivim standardima: certificirana '
                               'oprema, ponovljene obuke, prisutnost instruktora na '
                               'svakoj stanici i kulturom u kojoj svatko može pitati '
                               'prije nego što se odluči.</p>',
                               '<p>Na Glavani 10 između <strong>Barbana</strong> i '
                               '<strong>Vodnjanja</strong> park svake sezone dočekuje '
                               'tisuće međunarodnih gostiju — mnoge prvi put na '
                               'visokim stazama ili ziplineu. Naš bilingvalni tim, '
                               'uključujući instruktore na engleskom, daje prednost '
                               'jasnoj komunikaciji jer nesporazum na visini rizik '
                               'neprihvatljiv.</p>',
                               '<p>Sigurnosna kultura u Glavani Parku uključuje i '
                               'educiranje posjetitelja — transparentne ploče s '
                               'pravilima, vidljive inspekcijske rutine ujutro i '
                               'otvorenu komunikaciju o vremenskim ograničenjima. Kada '
                               'vjetar ili grmljavina približe se parku, aktivnosti na '
                               'visini mogu se privremeno obustaviti; gosti cijene '
                               'iskrenost umjesto nastavka rada u rizičnim '
                               'uvjetima.</p>']},
               {'h2': 'Standardi opreme i certifikati',
                'paragraphs': ['<p>Sva osobna zaštitna oprema u Glavani Parku '
                               'zadovoljava europske CE zahtjeve za avanturističke '
                               'parkove. To uključuje pune harnese koje prilagođava '
                               'osoblje, kacige po mjeri, karabiner i spojnice '
                               'ocijenjene za dinamička opterećenja te sustave '
                               'usporavanja na atrakcijama poput Quick Jumpa s 20 '
                               'metara.</p>',
                               '<p>Visoke staze koriste kontinuirani osigurač koji '
                               'drži posjetitelje na sigurnosnoj liniji od trenutka '
                               'napuštanja tla do povratka na platformu. Zipline '
                               'kolica, platforme i mjesta slijetanja inspektiraju se '
                               'prije dnevnog otvaranja. Ljudska katapulta koristi '
                               'redundantne sigurnosne linije i zdravstveni pregled '
                               'prije vožnje uz standardni harnes.</p>',
                               '<p>Oprema s istrošenošću izvan granica odmah se '
                               'povlači iz uporabe — istog dana, ne na kraju sezone. '
                               'Rezervna oprema drži se na lokaciji kako rad nikad ne '
                               'bi kompromitirao kvalitetu.</p>',
                               '<p>Oprema proizvođača renomiranih brandova u adventure '
                               'industriji redovito se zamjenjuje prema planu '
                               'održavanja, ne samo kada se pokvari. Svaki incident — '
                               'čak i blagi — dokumentira se kako bi se procedura '
                               'poboljšala. Takav pristup odražava standarde koje '
                               'očekujete od vodećeg parka u regiji i razlog zašto nas '
                               'preporučuje Turistička zajednica Istre.</p>']},
               {'h2': 'Obuka instruktora i nadzor na stazi',
                'paragraphs': ['<p>Svaku atrakciju vode educirani instruktori koji '
                               'provode obuku na hrvatskom ili engleskom prema '
                               'potrebi. Obuke pokrivaju harnes, provjeru spoja, '
                               'pravila staze, signale za hitne slučajeve i upute '
                               'specifične za aktivnost — pozicioniranje na visokoj '
                               'ljuljački, polazak na ziplineu, očekivani osjećaj na '
                               'Quick Jumpu.</p>',
                               '<p>Instruktori cijeli dan prate uvjete: vrijeme, umor '
                               'sudionika, redove i funkciju opreme. Imaju ovlast '
                               'zaustaviti aktivnost ako vjetar, kiša ili zdravlje '
                               'sudionika izazovu zabrinutost. Minimalna visina, '
                               'težina, dob i zdravstvena ograničenja za ekstremne '
                               'atrakcije dosljedno se provode.</p>',
                               '<p>Grupni posjeti — <a '
                               'href="/hr/skolski-izleti-istri/">školski izleti</a>, '
                               '<a href="/hr/team-building-istri/">korporativni '
                               'događaji</a> i <a '
                               'href="/hr/rodjendanske-zabave-istri/">rođendani</a> — '
                               'dobivaju dodatnu koordinaciju kako omjeri nadzora i '
                               'odabir aktivnosti odgovaraju profilu grupe.</p>',
                               '<p>Roditelji često pitaju o razlikama između igrališta '
                               'i visoke staze — ključna je kontinuirana veza s '
                               'uredajem i profesionalni nadzor. Naš tim rado '
                               'objašnjava mehanizme prije nego djeca napuste '
                               'platformu, što smanjuje anksioznost i povećava '
                               'uživanje. Sigurnost nije marketing slogan; to je '
                               'operativni temelj svakog radnog dana u Glavani '
                               'Parku.</p>']},
               {'h2': 'Dnevni operativni postupci',
                'paragraphs': ['<p>Prije otvaranja u <strong>9 sati</strong> osoblje '
                               'završava strukturiranu inspekciju svih ruta i '
                               'samostalnih atrakcija. Spojevi, sidrišta, zipline '
                               'užad, ljuljačke, katapult sustavi i držači zida '
                               'penjanja provjeravaju se prema internom popisu. '
                               'Incidenti, skoro-nezgode i kvarovi opreme bilježe se i '
                               'analiziraju.</p>',
                               '<p>Posljednji ulaz u <strong>15 sati</strong> '
                               'osigurava dovoljno dnevnog svjetla i operativnog '
                               'vremena prije <strong>17 sati</strong> zatvaranja. '
                               'Pojedinačne atrakcije mogu ranije zatvoriti ako bi '
                               'redovi produžili rad izvan sigurnog okvira — osoblje '
                               'to komunicira na blagajni.</p>',
                               '<p>Posjetitelji doprinose sigurnosti poštivanjem '
                               'uputa, nošenjem zatvorenih cipela (tenisice ili '
                               'planinarske — bez sandala), osiguravanjem labavih '
                               'predmeta prije aktivnosti i iskrenim otkrivanjem '
                               'zdravstvenih stanja na blagajni.</p>']},
               {'h2': 'Što očekivati kao posjetitelj prvi put',
                'paragraphs': ['<p>Ako ste nervozni zbog visine ili brzine, recite '
                               'instruktoru — objasnit će svaku fazu i nikad vas neće '
                               'gurnuti s platforme. Mnogi prvi put počinju na žutoj '
                               'stazi od 2 m prije plave, crne ili ziplinea. Nema '
                               'obveze proći svaku atrakciju; promatranje s tla '
                               'dobrodošlo je prijateljima i obitelji.</p>',
                               '<p>Glavani Park preporučuje <a '
                               'href="https://www.istra.hr/hr/destinacije/barban/1531" '
                               'rel="noopener noreferrer">Turistička zajednica '
                               'Istre</a> i održava standarde vodeće regionalne '
                               'vanjske atrakcije. Pitanja prije posjeta? Nazovite <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> '
                               '(engleski) ili <a href="tel:+38598224314">+385 98 224 '
                               '314</a> (hrvatski).</p>',
                               '<p>Avantura treba biti uzbudljiva, ne neodgovorna. U '
                               'Glavani Parku kod Pule, Barbana i Vodnjanja '
                               'profesionalni sigurnosni sustavi omogućuju da se '
                               'fokusirate na pogled, brzinu i zajednički uspjeh — '
                               'znajući da detalje svakodnevno rješavaju ljudi koji '
                               'inspektiraju, educiraju i brinu.</p>',
                               '<p>Redovito educiramo osoblje o prvim pomoćima i '
                               'postupcima u hitnim slučajevima, uz suradnju s '
                               'lokalnim zdravstvenim službama u slučaju potrebe. Iako '
                               'ozbiljne nezgode rijetke su zbog preventivnih mjera, '
                               'spremnost na scenarije daje posjetiteljima dodatno '
                               'mirno. Transparentnost u sigurnosti — vidljiva oprema, '
                               'jasna pravila, dostupni instruktori — razlog je zašto '
                               'nas obitelji s malom djecom biraju umjesto neformalnih '
                               'avantura bez nadzora u istom krajoliku.</p>',
                               '<p>Posjetitelji s alergijama, asma ili drugim stanjima '
                               'trebaju informirati osoblje prije aktivnosti — tim '
                               'može preporučiti manje zahtjevne elemente ili '
                               'optimalno vrijeme posjeta. Djeca koja se boje visine '
                               'nikada se ne tjeraju na stazu; instruktori koriste '
                               'postupno izlaganje i pozitivno poticanje. Roditelji '
                               'mogu pratiti cijeli tijek s tla na žutoj stazi, što '
                               'smanjuje anksioznost i kod odraslih pratitelja koji '
                               'sami ne penju na platforme.</p>']}],
  'faqs': [{'q': 'Je li oprema u Glavani Parku certificirana?',
            'a': 'Da. Harnes, kacige, spojnice i sustavi usporavanja CE su '
                 'certificirani za avanturističke parkove i dnevno se provjeravaju '
                 'prije otvaranja u 9 sati.'},
           {'q': 'Jesu li instruktori uvijek prisutni?',
            'a': 'Svaku atrakciju nadziru educirani djelatnici koji provode obuke i '
                 'prate sudionike. Visoke staze koriste kontinuirani osigurač.'},
           {'q': 'Tko ne bi smio sudjelovati u ekstremnim atrakcijama?',
            'a': 'Trudnice, osobe sa srčanim problemima, nedavnom operacijom, jakom '
                 'vertigom ili drugim relevantnim stanjima neka se posavjetuju s '
                 'osobljem prije katapulte, Quick Jumpa ili crne staze. Alternative '
                 'mogu biti prikladne.'},
           {'q': 'Što obući radi sigurnosti?',
            'a': 'Zatvorene sportske cipele, udobna pristanka odjeća, bez labavog '
                 'nakita i marama. Dugu kosu vezati. Ljeti krema za sunčanje i voda.'}],
  'related': [{'slug': 'avanturisticki-park-hrvatska',
               'title': 'Avanturistički parkovi Hrvatska',
               'desc': 'Pregled atrakcija u Glavani Parku'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Naše aktivnosti',
               'desc': 'Smjernice po dobi i žuta staza'},
              {'slug': 'zipline-hrvatska',
               'title': 'Zipline Hrvatska',
               'desc': 'Sigurnost i obuka za zipline'},
              {'slug': 'skolski-izleti-istri',
               'title': 'Školski izleti Istria',
               'desc': 'Standardi nadzora učenika'}]},
 {'slug': 'partneri',
  'title': 'Partnerstvo s Glavani Parkom | Hoteli i travel blogovi',
  'h1': 'Partnerstvo s Glavani Parkom: hoteli, kampovi i kreatori sadržaja',
  'meta_description': 'Pridružite se partnerskom programu Glavani Park — provizija, '
                      'co-marketing i preporuke za hotele, kampove i travel blogove u '
                      'Istri. Kontakt: +385 91 896 4525.',
  'keywords': 'Glavani Park partneri, partnerski hoteli Istria, preporuke kamp '
              'Hrvatska, partnerstvo travel blog Istria, affiliate avanturistički '
              'park, turistički partner program',
  'hero_badge': 'Hoteli · kampovi · travel blogovi',
  'hero_subtitle': 'Preporučite jednu od najbolje ocijenjenih vanjskih atrakcija u '
                   'Istri gostima i čitateljima — uz strukturirano partnerstvo s '
                   'Glavani Parkom kod Pule, Barbana i Vodnjanja.',
  'banner_mod': 'swing',
  'image': 'high-swing-youtube-still.webp',
  'image_alt': 'Visoka ljuljačka 12,5 m u Glavani Parku — partnerski program za '
               'smještaj i medije u Istri',
  'sections': [{'h2': 'Zašto partnerstvo s Glavani Parkom?',
                'paragraphs': ['<p>Pružatelji smještaja i turistički mediji u Istri '
                               'često čuju pitanje: što raditi osim plaže? '
                               '<strong>Glavani Park</strong> nudi cjelodnevnu '
                               'avanturu na otvorenom — 1,5 hektara visokih staza, '
                               'ziplinea, ljudske katapulte i obiteljskih ruta '
                               'trideset minuta od <strong>Pule</strong>, minuta od '
                               '<strong>Barbana</strong> i <strong>Vodnjanja</strong>. '
                               'Partnerstvo daje vašem poslu kredibilnu, visoko '
                               'ocijenjenu aktivnost za preporuku uz referalnu '
                               'vrijednost.</p>',
                               '<p>Park je naveden kod Turističke zajednice Istre, '
                               'radi <strong>9–17 h</strong> (posljednji ulaz '
                               '<strong>15 h</strong>) i prima međunarodne '
                               'posjetitelje s instruktorima na engleskom. To olakšava '
                               'prodaju obiteljima, aktivnim parovima i korporativnim '
                               'grupama bez rizika preporuke neprovjerenih '
                               'operatora.</p>',
                               '<p>Partneri iz kampova često uključuju Glavani Park u '
                               'tjedne programe aktivnosti — ponedjeljak avantura, '
                               'utorak plaža — što povećava zadržavanje gostiju i '
                               'pozitivne recenzije na Booking.com i Google. Hoteli s '
                               'all-inclusive paketima mogu ponuditi „adventure day“ '
                               'kao premium dodatak uz standardni aranžman, uz našu '
                               'podršku u materijalima i rezervacijama.</p>']},
               {'h2': 'Kome je namijenjen partnerski program',
                'paragraphs': ['<p><strong>Hoteli i odmarališta</strong> u Puli, '
                               'Rovinju, Medulinu i unutrašnjoj Istri koriste '
                               'partnerstvo za concierge preporuke, aktivnosti za '
                               'kišne dane i diferencijaciju od konkurencije s bazenom '
                               'i plažom. Kartice na recepciji, QR kodovi i e-mail '
                               'prije dolaska lako se integriraju.</p>',
                               '<p><strong>Kampovi i holiday parkovi</strong> — brojni '
                               'u Istri — posebno profitiraju. Kamp obitelji traže '
                               'aktivne izlete; žuta staza za djecu i zipline za '
                               'tinejdžere točno odgovaraju demografiji. Za veće '
                               'kampove moguće je dogovoriti shuttle.</p>',
                               '<p><strong>Travel blogovi, influenceri i '
                               'portali</strong> o Hrvatskoj i Istri dobivaju medijske '
                               'materijale, informativne brifeve te okvire provizije '
                               'ili sponzoriranog sadržaja ovisno o publici. Cijenimo '
                               'točne recenzije iskustva, ne generičke '
                               'direktorije.</p>',
                               '<p><strong>Putničke agencije i DMC-ovi</strong> koji '
                               'grade istarske itinerare mogu uključiti Glavani Park '
                               'kao poludnevni modul između kulture Pule i gradića na '
                               'brdu — nazovite <a href="tel:+385918964525">+385 91 '
                               '896 4525</a> za grupne cijene.</p>',
                               '<p>Digitalni partneri — Instagram i TikTok kreatori, '
                               'YouTube kanali o Hrvatskoj — mogu koristiti naše '
                               'stranice Link na nas za točne URL-ove i embed kodove, '
                               'smanjujući greške u linkovima i telefonskim brojevima. '
                               'Co-marketing kampanje ljeti uključuju cross-promociju '
                               's lokalnim vinogradima ili restoranima za paket '
                               '„avantura + večera“ koji povećava vrijednost za sve '
                               'strane.</p>']},
               {'h2': 'Prednosti partnera i podrška',
                'paragraphs': ['<p>Partneri dobivaju marketinške materijale: '
                               'fotografije visoke rezolucije, odobrene opise, radno '
                               'vrijeme, upute s glavnih istarskih čvorova te '
                               'jedinstvene linkove ili promo kodove za fer '
                               'atribuciju.</p>',
                               '<p>Strukture provizije i co-marketinga dogovaraju se '
                               'individualno prema tipu i volumenu partnera. Hoteli sa '
                               'stabilnim prometom gostiju mogu imati drukčije uvjete '
                               'od nišnog adventure bloga — transparentnost i '
                               'obostrana korist vode svaki dogovor.</p>',
                               '<p>Tim odgovara na upite na hrvatskom i engleskom. '
                               'Organiziramo familiarizacijske posjete za concierge, '
                               'voditelje kampova i novinare kako preporuke dolaze iz '
                               'vlastitog iskustva — najuvjerljivija preporuka.</p>',
                               '<p>Dugoročno partnerstvo gradi povjerenje: gosti koji '
                               'dođu na preporuku partnera očekuju istu razinu usluge '
                               'koju je partner obećao — zato usklađujemo očekivanja o '
                               'radnom vremenu, potrebi za rezervacijom i odjevi. '
                               'Zadovoljan gost vraća se u hotel ili kamp, a partner '
                               'dobiva bolju recenziju. To je win-win model koji '
                               'Glavani Park njeguje sa svakim novim suradnikom u '
                               'Istri.</p>']},
               {'h2': 'Što reći gostima',
                'paragraphs': ['<p>Ključne činjenice: Glavani Park jedan je od '
                               'najvećih adrenalinskih parkova u Hrvatskoj s tri '
                               'razine visokih staza, ziplineom 120 m, ljuljačkom 12,5 '
                               'm, katapultom, Quick Jumpom i zidom za penjanje. '
                               'Adresa: Glavani 10, 52207 Barban. Besplatno '
                               'parkiranje. Otvoreno 9–17 h, posljednji ulaz 15 h. '
                               'Rezervacije: +385 91 896 4525 (engleski), +385 98 224 '
                               '314 (hrvatski).</p>',
                               '<p>Usmjerite goste na stranice: <a '
                               'href="/hr/avanturisticki-park-hrvatska/">obiteljske '
                               'aktivnosti</a>, <a href="/hr/zipline-hrvatska/">vodič '
                               'zipline</a>, <a href="/hr/team-building-istri/">team '
                               'building</a> i <a '
                               'href="/hr/sto-raditi-kod-pule/">izleti iz Pule</a>. '
                               'Naglasite najavu u vrh sezone — partneri koji to '
                               'postave smanjuju razočarenje gostiju i jačaju '
                               'povjerenje u vašu preporuku.</p>',
                               '<p>Agencije koje prodaju paket aranžmane u Istri mogu '
                               'uključiti Glavani Park kao opcionalni modul u cjeniku '
                               '— na primjer „Pula + avantura“ za obitelji s djecom '
                               'starijom od šest godina. Naš tim pomaže s '
                               'formulacijama u katalogu i odgovara na upite vaših '
                               'prodajnih agenata na engleskom ili hrvatskom, što '
                               'ubrzava zatvaranje prodaje.</p>']},
               {'h2': 'Prijavite se za partnerstvo',
                'paragraphs': ['<p>Za partnerski program javite se s nazivom tvrtke, '
                               'web stranicom, lokacijom u Istri (ako postoji), '
                               'profilom publike ili gostiju i načinom promocije '
                               'parka. E-mail <a '
                               'href="mailto:info@glavanipark.com">info@glavanipark.com</a> '
                               'ili <a href="tel:+385918964525">+385 91 896 '
                               '4525</a>.</p>',
                               '<p>Travel blogeri koji traže embed kodove i predloženi '
                               'anchor text posjetite stranicu <a '
                               'href="/hr/link-na-nas/">Link na nas</a> za HTML i SEO '
                               'smjernice. Zajedno možemo staviti više istarskih '
                               'posjetitelja na zipline — i zadovoljnijih gostiju u '
                               'vašim recenzijama.</p>',
                               '<p>Partnerski onboarding uključuje kratki vodič s '
                               'najčešćim pitanjima gostiju — radno vrijeme, dobna '
                               'ograničenja, potreba za rezervacijom, odjev — kako bi '
                               'recepcija odgovarala brzo i točno. Kvalitetna '
                               'preporuka smanjuje broj pritužbi i povećava ponovne '
                               'rezervacije smještaja kod partnera. Glavani Park mjeri '
                               'uspjeh partnerstva ne samo brojem dolazaka, već i '
                               'zadovoljstvom gostiju nakon posjeta, što se odražava u '
                               'recenzijama hotela i kampova koji nas uključe u svoje '
                               'materijale.</p>',
                               '<p>Partneri u unutrašnjoj Istri — vile, agroturizmi, '
                               'manji hoteli — jednako su dobrodošli kao veliki '
                               'resorti na obali. Glavani Park pomaže formulirati '
                               'poruku za goste koji borave dalje od mora a traže '
                               'aktivni dan bez dugih vožnji. Uključite nas u '
                               'newslettere prije sezone, QR kod na recepciji i '
                               'društvene mreže s fotografijom ziplinea — konverzija '
                               'preporuka raste kad gosti vide stvarni sadržaj, ne '
                               'samo tekst.</p>']}],
  'faqs': [{'q': 'Košta li ulazak u partnerski program?',
            'a': 'Registracija partnera besplatna je. Komercijalni uvjeti poput '
                 'provizije dogovaraju se individualno. Kontakt +385 91 896 4525 ili '
                 'info@glavanipark.com.'},
           {'q': 'Mogu li kampovi organizirati prijevoz do parka?',
            'a': 'Park ima besplatno parkiranje za autobuse i minibuseve. Shuttle s '
                 'vašeg kampa moguće je dogovoriti pri postavljanju partnerstva.'},
           {'q': 'Dobivaju li partneri familiarizacijske posjete?',
            'a': 'Da, prema rasporedu. Fam posjeti pomažu conciergeu i kreatorima '
                 'sadržaja preporučiti atrakcije točno. Pitajte pri prijavi.'},
           {'q': 'Koji marketinški materijali su dostupni?',
            'a': 'Odobreni tekstovi, fotografije, sati, upute i tracking linkovi ili '
                 'kodovi. Blogerima dostupni embed snippeti na stranici Link na nas.'}],
  'related': [{'slug': 'link-na-nas',
               'title': 'Link na nas',
               'desc': 'Embed kodovi i anchor text za backlinkove'},
              {'slug': 'sto-raditi-u-istri',
               'title': 'Što raditi u Istri',
               'desc': 'Destinacijski sadržaj za vaše goste'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Naše aktivnosti',
               'desc': 'Stranica za kamp publiku'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Avanturistički parkovi Hrvatska',
               'desc': 'Pregled za medije i agencije'}]},
 {'slug': 'link-na-nas',
  'title': 'Link na Glavani Park | Embed kodovi i anchor text',
  'h1': 'Link na nas: backlinkovi, embed kodovi i predloženi anchor text',
  'meta_description': 'Linkajte Glavani Park — HTML embed kodovi, banner snippeti i '
                      'SEO anchor text za travel blogove, hotele i istarske '
                      'direktorije. Avanturistički park kod Pule. +385 91 896 4525.',
  'keywords': 'link Glavani Park, embed kod avanturistički park, backlink turizam '
              'Istria, anchor text Glavani Park, link travel blog Hrvatska, partner '
              'HTML embed',
  'hero_badge': 'Blogeri · direktoriji · webmasteri',
  'hero_subtitle': 'Pomozite čitateljima otkriti vodeći istarski avanturistički park s '
                   'odobrenim linkovima, embed snippetima i prijedlozima anchor texta '
                   '— sve prema Glavani Parku kod Barbana i Pule.',
  'banner_mod': 'link',
  'image': 'glavani-park-adventure-istria-croatia.jpg',
  'image_alt': 'Glavani Park · Istria, Hrvatska',
  'sections': [{'h2': 'Zašto linkati Glavani Park?',
                'paragraphs': ['<p>Travel blogovi, web stranice smještaja u Istri, '
                               'turistički direktoriji i lokalni vodiči povećavaju '
                               'vrijednost za čitatelje preporukom stvarnih, '
                               'kvalitetnih atrakcija. <strong>Glavani Park</strong> '
                               'je avanturistički i adrenalinski park od 1,5 hektara '
                               'između <strong>Barbana</strong> i '
                               '<strong>Vodnjanja</strong>, trideset minuta od '
                               '<strong>Pule</strong>, otvoren <strong>9–17 h</strong> '
                               '(posljednji ulaz <strong>15 h</strong>). Link na nas '
                               'pomaže publici planirati aktivne dane uz točne '
                               'informacije na webu.</p>',
                               '<p>Dobrodošli su urednički linkovi svih koji pišu o '
                               'turizmu Istre, obiteljskim putovanjima, avanturskim '
                               'sportovima ili road tripovima Hrvatskom. Koristite '
                               'kanonske URL-ove u nastavku i izbjegavajte obmanjujuće '
                               'tvrdnje o cijenama ili certifikatima koje nisu na '
                               'našoj stranici.</p>',
                               '<p>Webmasteri koji održavaju višejezične stranice '
                               'trebaju koristiti hreflang parove između /hr/ i /en/ '
                               'URL-ova — SLUG_MAP u našem sustavu osigurava ispravno '
                               'mapiranje za SEO. Preporučujemo link na hrvatsku '
                               'verziju za domaću publiku i englesku za međunarodnu, '
                               'uz konzistentan NAP (Glavani 10, Barban, telefoni +385 '
                               '91 896 4525 i +385 98 224 314).</p>']},
               {'h2': 'Kanonski URL-ovi',
                'paragraphs': ['<p>Koristite ove primarne URL-ove pri linkanju '
                               'sadržaja Glavani Parka:</p>',
                               '<p><strong>Početna (hrvatski):</strong> '
                               '<code>https://www.glavanipark.com/hr/</code></p>',
                               '<p><strong>Što raditi u Istri:</strong> '
                               '<code>https://www.glavanipark.com/hr/sto-raditi-u-istri/</code></p>',
                               '<p><strong>Naše aktivnosti:</strong> '
                               '<code>https://www.glavanipark.com/hr/avanturisticki-park-hrvatska/</code></p>',
                               '<p><strong>Zipline Hrvatska:</strong> '
                               '<code>https://www.glavanipark.com/hr/zipline-hrvatska/</code></p>',
                               '<p><strong>Team building Istria:</strong> '
                               '<code>https://www.glavanipark.com/hr/team-building-istri/</code></p>',
                               '<p><strong>Što raditi kod Pule:</strong> '
                               '<code>https://www.glavanipark.com/hr/sto-raditi-kod-pule/</code></p>',
                               '<p><strong>Avanturistički park Hrvatska:</strong> '
                               '<code>https://www.glavanipark.com/hr/avanturisticki-park-hrvatska/</code></p>',
                               '<p><strong>Sigurnost:</strong> '
                               '<code>https://www.glavanipark.com/hr/sigurnost/</code></p>',
                               '<p><strong>Partneri:</strong> '
                               '<code>https://www.glavanipark.com/hr/partneri/</code></p>',
                               '<p>Za hreflang alternativu engleska verzija dostupna '
                               'je na odgovarajućim <code>/en/</code> URL-ovima prema '
                               'mapi slugova.</p>',
                               '<p>Structured data (Schema.org) za lokalnu firmu može '
                               'referencirati našu domenu i sliku '
                               'glavani-park-adventure-istria-croatia.jpg s točnim geo '
                               'koordinatama. Blogeri koji pišu listicle „top 10 u '
                               'Istri“ mogu koristiti kratki opis s linkom na '
                               '/hr/sto-raditi-u-istri/ za širi kontekst, a zatim '
                               'dublji link na /hr/zipline-hrvatska/ za specifičnu '
                               'aktivnost.</p>']},
               {'h2': 'Predloženi anchor text',
                'paragraphs': ['<p>Raznolik, prirodan anchor text pomaže tražilicama i '
                               'čitateljima. Odobreni primjeri:</p>',
                               '<p>• <strong>Glavani Park</strong> — brand link na '
                               'početnu<br>• <strong>avanturistički park u '
                               'Istri</strong> — početna ili stranica avanturistički '
                               'park<br>• <strong>zipline kod Pule</strong> — '
                               'zipline-hrvatska ili sto-raditi-kod-pule<br>• '
                               '<strong>obiteljske aktivnosti u Istri</strong> — '
                               'avanturisticki-park-hrvatska<br>• <strong>što raditi u '
                               'Istri s djecom</strong> — avanturisticki-park-hrvatska '
                               'ili sto-raditi-u-istri<br>• <strong>team building '
                               'Istria</strong> — team-building-istri<br>• '
                               '<strong>rođendanska lokacija Istria</strong> — '
                               'rodjendanske-zabave-istri<br>• <strong>školski izlet '
                               'avantura Hrvatska</strong> — skolski-izleti-istri<br>• '
                               '<strong>aktivnosti na otvorenom kod Barbana i '
                               'Vodnjanja</strong> — početna ili '
                               'sto-raditi-kod-pule</p>',
                               '<p>Izbjegavajte preoptimiziranu ponavljanu identičnu '
                               'anchor frazu na desecima stranica. Jedan kontekstualni '
                               'link po članku obično je dovoljan.</p>',
                               '<p>Ažuriranja sadržaja objavljujemo sezonski — sati '
                               'rada, telefonski brojevi i URL-ovi ostaju stabilni, '
                               'ali provjerite stranicu prije objave starijih članaka. '
                               'Zahvaljujemo svim web stranicama, direktorijima i '
                               'blogovima koji točno predstavljaju Glavani Park i '
                               'pomažu putnicima pronaći sigurnu avanturu u srcu '
                               'Istre.</p>']},
               {'h2': 'HTML embed kodovi',
                'paragraphs': ['<p><strong>Jednostavan tekstualni link (početna, '
                               'HR):</strong></p>',
                               '<p><code>&lt;a href="https://www.glavanipark.com/hr/" '
                               'title="Glavani Park – avanturistički park Istria, '
                               'Hrvatska"&gt;Glavani Park – avanturistički park kod '
                               'Pule, Barbana i Vodnjanja&lt;/a&gt;</code></p>',
                               '<p><strong>Tekstualni link na zipline '
                               'stranicu:</strong></p>',
                               '<p><code>&lt;a '
                               'href="https://www.glavanipark.com/hr/zipline-hrvatska/" '
                               'title="Zipline Hrvatska u Glavani Parku '
                               'Istria"&gt;120-metarski zipline u Glavani Parku '
                               'Istria&lt;/a&gt;</code></p>',
                               '<p><strong>Tekstualni link na obiteljske '
                               'aktivnosti:</strong></p>',
                               '<p><code>&lt;a '
                               'href="https://www.glavanipark.com/hr/avanturisticki-park-hrvatska/" '
                               'title="Obiteljske aktivnosti Istria"&gt;Obiteljske '
                               'aktivnosti i visoke staze kod '
                               'Pule&lt;/a&gt;</code></p>',
                               '<p><strong>Link slike s alt tekstom (zamijenite URL '
                               'slike lokalnom kopijom ili zatražite materijale putem '
                               '<a href="/hr/partneri/">partnerskog '
                               'programa</a>):</strong></p>',
                               '<p><code>&lt;a '
                               'href="https://www.glavanipark.com/hr/"&gt;&lt;img '
                               'src="https://www.glavanipark.com/images/glavani-park-adventure-istria-croatia.jpg" '
                               'alt="Glavani Park avanturistički i adrenalinski park u '
                               'Istri, Hrvatska" width="600" height="400" '
                               'loading="lazy"&gt;&lt;/a&gt;</code></p>',
                               '<p><strong>Kratki okvir preporuke (HTML):</strong></p>',
                               '<p><code>&lt;aside style="border-left:4px solid '
                               '#2d6a4f;padding:1rem '
                               '1.25rem;background:#f7faf8;"&gt;&lt;strong&gt;Glavani '
                               'Park&lt;/strong&gt; — zipline, visoke staze i ljudska '
                               'katapulta kod Pule. Otvoreno 9–17 h, posljednji ulaz '
                               '15 h. Nazovite &lt;a href="tel:+385918964525"&gt;+385 '
                               '91 896 4525&lt;/a&gt;. &lt;a '
                               'href="https://www.glavanipark.com/hr/"&gt;Planirajte '
                               'posjet →&lt;/a&gt;&lt;/aside&gt;</code></p>',
                               '<p>Za wikije putničkih destinacija i crowdsourced '
                               'vodiče molimo da ne mijenjate telefonske brojeve niti '
                               'radno vrijeme bez provjere — koristite podatke s ove '
                               'stranice ili službenog weba. Netočne informacije '
                               'stvaraju nezadovoljstvo gostiju i otežavaju naš tim na '
                               'blagajni. Kvalitetan backlink s točnim podacima '
                               'vrijedi više od desetak niskokvalitetnih '
                               'direktorijskih unosa.</p>']},
               {'h2': 'Atribucija, partneri i kontakt',
                'paragraphs': ['<p>Hoteli, kampovi i agencije s komercijalnim '
                               'volumenom preporuka neka se pridruže formalnom <a '
                               'href="/hr/partneri/">partnerskom programu</a> za '
                               'tracking kodove i proviziju. Neovisni blogeri slobodno '
                               'linkaju gornje snippete — cijenimo kratku napomenu da '
                               'je Glavani Park kod Barbana i Vodnjanja te da se '
                               'preporučuje najava na +385 91 896 4525 ili +385 98 224 '
                               '314.</p>',
                               '<p>Za fotografije visoke rezolucije, familiarizacijske '
                               'posjete ili co-branded widgete pišite <a '
                               'href="mailto:info@glavanipark.com">info@glavanipark.com</a> '
                               'ili nazovite <a href="tel:+385918964525">+385 91 896 '
                               '4525</a>. Točan NAP za citate:</p>',
                               '<p><strong>Glavani Park</strong><br>Glavani 10, 52207 '
                               'Barban, Istria, Hrvatska<br>Telefon: +385 91 896 4525 '
                               '/ +385 98 224 314<br>Web: '
                               'https://www.glavanipark.com/hr/</p>',
                               '<p>Hvala što putnicima pomažete otkriti jednu od '
                               'najboljih istarskih avantura na otvorenom. Počnite s '
                               '<a href="/hr/sto-raditi-u-istri/">što raditi u '
                               'Istri</a> i <a '
                               'href="/hr/avanturisticki-park-hrvatska/">avanturističkim '
                               'parkovima u Hrvatskoj</a> za dublje linking '
                               'mogućnosti.</p>',
                               '<p>Medijske kuće i portali koji objavljuju sezonske '
                               'vodiče trebaju ažurirati linkove svake godine — isti '
                               'URL /hr/ ostaje, ali provjerite da tekst oko linka '
                               'spominje aktualno radno vrijeme 9–17 h i oba telefona. '
                               'Uključivanje Glavani Parka u članke o obiteljskom '
                               'turizmu, aktivnom odmoru ili održivoj destinaciji '
                               'pomaže čitateljima i jača autoritet vašeg sadržaja jer '
                               'preporučujete provjerenu atrakciju s jasnim '
                               'sigurnosnim standardima, a ne generički popis bez '
                               'konteksta.</p>',
                               '<p>Ako održavate stranicu na više jezika, duplicirajte '
                               'embed kodove s odgovarajućim /hr/ ili /en/ href '
                               'atributima i prevedenim anchor tekstom — Google cijeni '
                               'konzistentnost hreflang parova. Izbjegavajte skrivene '
                               'linkove, prekomjerno optimizirane footere s desecima '
                               'linkova i automatski generirane direktorije s netočnim '
                               'satima rada. Jedan dobro napisan odlomak s linkom na '
                               'Glavani Park u relevantnom kontekstu vrijedi više od '
                               'stotina spam unosa.</p>']}],
  'faqs': [{'q': 'Smijem li koristiti fotografije Glavani Parka na blogu?',
            'a': 'Kontaktirajte info@glavanipark.com ili se pridružite partnerskom '
                 'programu za odobrene fotografije visoke rezolucije. Ne hotlinkajte '
                 'bez dopuštenja ako CMS dopušta lokalno hostanje.'},
           {'q': 'Nudite li affiliate proviziju?',
            'a': 'Komercijalni partneri u hotelima, kampovima i medijima mogu dobiti '
                 'tracking i proviziju. Prijavite se putem stranice partneri ili '
                 'nazovite +385 91 896 4525.'},
           {'q': 'Na koju stranicu linkati za obiteljski sadržaj?',
            'a': 'Koristite '
                 'https://www.glavanipark.com/hr/avanturisticki-park-hrvatska/ s '
                 "anchor textom poput 'obiteljske aktivnosti u Istri' ili 'što raditi "
                 "kod Pule s djecom'."},
           {'q': 'Mogu li prevesti link tekst na njemački ili talijanski?',
            'a': 'Da u uredničkom kontekstu, ali linkajte na /hr/ ili /en/ URL ovisno '
                 'o publici. Zadržite točne podatke (sati, telefon).'}],
  'related': [{'slug': 'partneri',
               'title': 'Partnerski program',
               'desc': 'Provizija i co-marketing za smještaj'},
              {'slug': 'sto-raditi-u-istri',
               'title': 'Što raditi u Istri',
               'desc': 'Urednički vodič destinacijom za link'},
              {'slug': 'avanturisticki-park-hrvatska',
               'title': 'Avanturistički parkovi Hrvatska',
               'desc': 'Pregled za adventure blogove'},
              {'slug': 'sto-raditi-kod-pule',
               'title': 'Što raditi kod Pule',
               'desc': 'Sadržaj fokusiran na Pulu za lokalne vodiče'}]}]

