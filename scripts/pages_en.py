"""
English landing page content for Glavani Park SEO site.
Each page targets 800–1200 words of substantive Istria tourism and park content.
"""

from booking_policy import BOOKING_POLICY

_EN_BOOKING = BOOKING_POLICY["en"]

HOME = {
    "title": "Glavani Park | Croatia's Number 1 Adventure Park · Istria",
    "meta_description": (
        "Glavani Park is Croatia's number 1 adventure park in Istria — ziplines, high ropes, human catapult "
        "and outdoor activities near Pula, Barban & Vodnjan. Open daily 9 AM–5 PM, last entry 3 PM. "
        "Call +385 91 896 4525 or book online for up to 10 people."
    ),
    "keywords": (
        "Croatia number 1 adventure park, adventure park Istria, adventure park Croatia, zipline park Istria, "
        "zipline park Croatia, adrenaline park Istria, outdoor activities Istria Croatia, high ropes course Croatia, "
        "family activities Istria, things to do near Pula, Glavani Park"
    ),
    "h1": "Glavani Park – Croatia's Number 1 Adventure Park",
    "hero_badge": "Croatia's Number 1 Adventure Park",
    "hero_subtitle": (
        "We're a family-run adventure park in the Istrian countryside — friendly, qualified staff, "
        "forest ziplines, and memories you'll talk about for years. Drop in for a chat before you clip in."
    ),
    "image": "glavani-park-adventure-istria-croatia.jpg",
    "image_alt": "Aerial view of Glavani Park, Croatia's number 1 adventure park in Istria",
}


PAGES = [{'slug': 'things-to-do-in-istria',
  'title': 'Things to Do in Istria | Family Guide & Glavani Park',
  'h1': 'Things to Do in Istria: The Complete Visitor Guide',
  'meta_description': 'Discover the best things to do in Istria — beaches, hill towns, '
                      'food trails, and outdoor adventures. Plan your trip with '
                      'Glavani Park near Pula, Barban & Vodnjan. Open daily 9–5, last '
                      'entry 3 PM.',
  'keywords': 'things to do in Istria, Istria attractions, Istria with kids, family '
              'holiday Istria, outdoor activities Istria, Glavani Park, adventure park '
              'Istria, day trips Istria Croatia',
  'hero_badge': 'Istria Travel Guide · Outdoor Adventures',
  'hero_subtitle': 'From Roman Pula and truffle country to forest ziplines and '
                   'medieval hill towns — Istria rewards curious travellers. Add '
                   'Glavani Park to your itinerary for a full day of adrenaline '
                   'between Barban and Vodnjan.',
  'image': 'glavani-park-adventure-istria-croatia.jpg',
  'image_alt': 'Glavani Park adventure park set in the Istrian countryside near Barban '
               'and Pula',
  'sections': [{'h2': "Why Istria Is One of Croatia's Most Versatile Destinations",
                'paragraphs': ['<p>Istria occupies a triangular peninsula at the '
                               'northern edge of the Adriatic, where Italian, Slavic, '
                               'and Central European influences blend into something '
                               'uniquely its own. Visitors come for the coastline — '
                               "Rovinj's pastel harbour, the rocky coves around Pula, "
                               'and family-friendly beaches at Medulin and Premantura '
                               '— but the inland landscape is equally compelling. '
                               'Rolling hills covered in vineyards and olive groves '
                               'lead to fortified villages like Motovun and Grožnjan, '
                               'while truffle forests and farm-to-table restaurants '
                               'make food tourism a reason to visit in its own '
                               'right.</p>',
                               '<p>Whether you are planning a week-long family holiday '
                               'or a long weekend from Trieste, Ljubljana, or Zagreb, '
                               'Istria packs an unusual density of experiences into a '
                               'compact area. Most major sights lie within a 45-minute '
                               'drive of one another, which makes day trips effortless '
                               'and allows you to combine culture, nature, and active '
                               'adventure in a single itinerary. For travellers who '
                               'want more than sun and sea, the peninsula offers '
                               'hiking trails, cycling routes, wine roads, and some of '
                               'the best outdoor adventure facilities in Croatia — '
                               'including <strong>Glavani Park</strong>, an adrenaline '
                               'park near the village of Glavani between '
                               '<strong>Barban</strong> and '
                               '<strong>Vodnjan</strong>.</p>']},
               {'h2': 'Coastal Highlights: Pula, Rovinj, and the Adriatic',
                'paragraphs': ["<p><strong>Pula</strong> is Istria's largest city and "
                               'a natural starting point for exploring the region. Its '
                               'Roman amphitheatre — one of the best preserved in the '
                               'world — dominates the old town, while nearby Brijuni '
                               'National Park offers island wildlife, dinosaur '
                               'footprints, and clear swimming waters. Families often '
                               'spend a morning at the arena or the Aquarium Pula '
                               'before heading inland for an afternoon activity. If '
                               'you are searching for <a '
                               'href="/en/things-to-do-near-pula/">things to do near '
                               'Pula</a> beyond the beach, the 30-minute drive to '
                               'Glavani Park adds a high-energy counterpoint to a '
                               'cultural morning in the city.</p>',
                               '<p><strong>Rovinj</strong>, with its Venetian-style '
                               "old town rising from the harbour, is Istria's most "
                               'photographed destination. Climb the bell tower of St '
                               "Euphemia's Church for panoramic views, wander the "
                               "artists' studios in the cobbled lanes, and eat fresh "
                               'seafood at waterfront trattorias. Rovinj sits roughly '
                               '45 minutes from Glavani Park by car, making a combined '
                               'day — morning in town, afternoon on the ziplines — '
                               'entirely feasible during the summer season.</p>',
                               '<p>Along the coast you will also find the Lim Fjord, a '
                               'dramatic karst inlet ideal for boat trips and '
                               'kayaking; the hilltop village of Vrsar; and the quiet '
                               'beaches of the east coast around Rabac and Labin. Each '
                               'offers a different pace, from bustling resort towns to '
                               "secluded coves where pine trees shade the water's "
                               'edge.</p>']},
               {'h2': 'Inland Istria: Hill Towns, Wine, and Truffles',
                'paragraphs': ['<p>Turn inland from the coast and Istria reveals a '
                               'softer, greener landscape. Medieval towns perch on '
                               'hilltops above the Mirna River valley: '
                               '<strong>Motovun</strong> hosts an international film '
                               'festival and truffle-hunting experiences; '
                               '<strong>Grožnjan</strong> has reinvented itself as a '
                               'village of artists and galleries; and '
                               "<strong>Hum</strong>, often cited as the world's "
                               'smallest town, offers a charming stop on the '
                               'Glagolitic Alley cultural trail.</p>',
                               '<p>Wine lovers should follow the Istrian wine road, '
                               'sampling Malvazija whites and Teran reds at family-run '
                               'cellars. Olive oil routes and agritourism farms '
                               "provide tastings of Istria's other flagship products. "
                               'Many visitors schedule a truffle lunch in Livade or '
                               'Buzet, then drive south to Barban and Glavani Park for '
                               'an active afternoon in the forest.</p>',
                               '<p>The area around <strong>Barban</strong> and '
                               '<strong>Vodnjan</strong> is less crowded than the '
                               "coast but rich in authenticity. Vodnjan's parish "
                               'church houses mummified saints and one of the tallest '
                               "bell towers in Istria, while Barban's medieval walls "
                               'and local konobas serve hearty Istrian fare. Glavani '
                               'Park sits on the road between these two communities at '
                               'Glavani 10, with free parking and opening hours from '
                               '<strong>9 AM to 5 PM</strong> daily (last entry at '
                               '<strong>3 PM</strong>).</p>']},
               {'h2': 'Outdoor and Active Things to Do in Istria',
                'paragraphs': ['<p>Active travellers have no shortage of options. '
                               'Cycling is popular along the Parenzana trail, a '
                               'converted railway line linking Trieste with coastal '
                               'Istria. Hikers explore Učka Nature Park at the '
                               "peninsula's southern edge, where marked paths climb "
                               'through beech forest to viewpoints over Kvarner Bay. '
                               'Rock climbers head to Dvigrad or Lim Bay, while '
                               'kayakers paddle the coast from Pula to Kamenjak Nature '
                               'Park.</p>',
                               '<p>For structured adventure with professional safety '
                               'equipment and trained instructors, <strong>Glavani '
                               'Park</strong> stands out as one of the largest '
                               'dedicated adrenaline parks in Croatia. Spread across '
                               '1.5 hectares of oak forest, the park features three '
                               'certified high-ropes routes (yellow at 2 m, blue at 6 '
                               'm, and black at 10 m), a 120-metre zipline, a '
                               '12.5-metre high swing, a human catapult, a 20-metre '
                               'Quick Jump, and an outdoor climbing wall. It is ideal '
                               'for families, couples, and groups who want a '
                               'guaranteed half-day or full-day of activity without '
                               'organising equipment themselves.</p>',
                               '<p>Visitors often pair Glavani Park with other '
                               'regional highlights: a morning at the park followed by '
                               'an afternoon in Vodnjan or Barban; or a coastal '
                               'morning in Pula and an adrenaline afternoon before '
                               'returning to their accommodation. Call <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> in '
                               'advance to check availability, especially during July '
                               'and August.</p>']},
               {'h2': 'Planning Your Istria Itinerary with Glavani Park',
                'paragraphs': ['<p>A well-balanced Istria itinerary might look like '
                               "this: Day one — explore Pula's Roman heritage and swim "
                               'at Kamenjak. Day two — Rovinj old town and a sunset '
                               'dinner on the harbour. Day three — truffle experience '
                               'or wine tasting inland, then Glavani Park for <a '
                               'href="/en/adventure-park-croatia/">family '
                               'activities</a> and ziplines. Day four — Brijuni boat '
                               'trip or a lazy beach day before departure.</p>',
                               '<p>Glavani Park is open daily from 9 AM to 5 PM with '
                               'last entry at 3 PM — allow three to four hours to '
                               'enjoy the main attractions comfortably. '
                               f'{_EN_BOOKING["off_season_note"]} '
                               f'{_EN_BOOKING["peak_walkin_note"]} '
                               'English-speaking staff are on hand '
                               'throughout the season, and the park is listed by the '
                               "Istria Tourist Board as one of the region's "
                               'recommended outdoor attractions.</p>',
                               '<p>Whether your priority is culture, cuisine, '
                               'coastline, or adrenaline, Istria delivers — and '
                               'Glavani Park adds an unforgettable active dimension to '
                               'any trip. Browse our dedicated guides on <a '
                               'href="/en/zipline-croatia/">ziplines in Croatia</a>, '
                               '<a href="/en/adventure-park-croatia/">adventure '
                               'parks</a>, and <a '
                               'href="/en/things-to-do-near-pula/">day trips from '
                               'Pula</a> to plan the perfect visit.</p>']}],
  'faqs': [{'q': 'What are the must-see places in Istria?',
            'a': "Top Istria highlights include Pula's Roman amphitheatre, Rovinj old "
                 'town, Brijuni National Park, Motovun and Grožnjan hill towns, the '
                 'Lim Fjord, and Kamenjak Nature Park. For active visitors, Glavani '
                 'Park near Barban offers ziplines, high ropes, and adrenaline rides '
                 'within easy reach of Pula and Vodnjan.'},
           {'q': 'How many days do you need in Istria?',
            'a': 'A minimum of four to five days lets you explore the coast, inland '
                 'hill towns, and at least one outdoor adventure. A week allows a more '
                 'relaxed pace with wine tastings, beach days, and activities like a '
                 'full morning at Glavani Park without rushing.'},
           {'q': 'Is Istria good for families with children?',
            'a': "Yes. Istria is one of Croatia's most family-friendly regions, with "
                 'safe beaches, short driving distances, and attractions for all ages. '
                 "Glavani Park's 2-metre yellow high-ropes route is designed "
                 'specifically for younger children, while teens and parents can '
                 'tackle taller courses and ziplines.'},
           {'q': 'When is the best time to visit Istria?',
            'a': 'May through September offers warm weather and full park opening '
                 'hours. June and September are ideal for fewer crowds. Glavani Park '
                 'is open daily 9 AM–5 PM during the season; call +385 91 896 4525 to '
                 'confirm dates and availability before travelling.'}],
  'related': [{'slug': 'adventure-park-croatia',
               'title': 'Our Activities',
               'desc': 'Nine signature attractions at Glavani Park'},
              {'slug': 'things-to-do-near-pula',
               'title': 'Things to Do Near Pula',
               'desc': 'Day trips and outdoor activities within 30 minutes of Pula'},
             
              {'slug': 'zipline-croatia',
               'title': 'Zipline Croatia Guide',
               'desc': '120-metre treetop flights at Glavani Park Istria'}]},
 {'slug': 'family-activities-istria',
  'title': 'Family Activities Istria | Kids Adventures Near Pula',
  'h1': 'Family Activities in Istria: Outdoor Fun for All Ages',
  'meta_description': 'Best family activities in Istria — beaches, nature parks, and '
                      'Glavani Park near Pula & Barban. Yellow high-ropes for kids, '
                      'ziplines for teens. Open 9–5, last entry 3 PM. Call +385 91 896 '
                      '4525.',
  'keywords': 'family activities Istria, things to do Istria with kids, family day '
              'trip Pula, outdoor activities children Istria, Glavani Park family, '
              'adventure park kids Croatia',
  'hero_badge': 'Family Day Trips · All Ages Welcome',
  'hero_subtitle': 'Istria is built for family holidays — and Glavani Park near Barban '
                   'and Vodnjan adds a full day of supervised outdoor adventure with '
                   'routes designed for children, teens, and parents alike.',
  'image': '12-5m-high-swing-glavani-park-istria.webp',
  'image_alt': 'Family enjoying the high swing at Glavani Park adventure park in '
               'Istria, Croatia',
  'sections': [{'h2': 'Why Istria Is Ideal for Family Holidays',
                'paragraphs': ["<p>Croatia's Istrian peninsula consistently ranks "
                               'among the most family-friendly destinations in Europe. '
                               'Distances are short, roads are well maintained, '
                               'English is widely spoken in tourist areas, and the mix '
                               'of beaches, nature, and culture keeps children engaged '
                               'without endless hours in the car. Towns like Pula, '
                               'Rovinj, and Poreč offer safe swimming, ice cream on '
                               'every corner, and historical sights that capture young '
                               'imaginations — Roman ruins, medieval walls, and '
                               'harbour-side promenades.</p>',
                               '<p>Beyond the coast, inland Istria provides gentle '
                               'hiking, farm visits, and truffle-hunting '
                               'demonstrations that introduce children to rural life. '
                               'Accommodation ranges from large resort hotels with '
                               "pools and kids' clubs to private villas and campsite "
                               'pitches shaded by pine trees. Whatever your budget and '
                               'style, the region makes it easy to balance relaxation '
                               'with activity — and that is where <strong>Glavani '
                               'Park</strong> fits perfectly into a family '
                               'itinerary.</p>']},
               {'h2': 'Glavani Park: Adventure Designed for Every Generation',
                'paragraphs': ['<p>Located at Glavani 10, between '
                               '<strong>Barban</strong> (6 km) and '
                               '<strong>Vodnjan</strong> (10 km), Glavani Park is one '
                               'of the largest dedicated adventure parks in Croatia, '
                               'covering 1.5 hectares of oak forest. Unlike generic '
                               'playgrounds or passive attractions, the park offers '
                               'real physical challenges under the supervision of '
                               'trained instructors — making it one of the most '
                               'rewarding <strong>family activities in Istria</strong> '
                               'for visitors who want more than a beach day.</p>',
                               '<p>The centrepiece for younger visitors is the '
                               '<strong>yellow high-ropes route</strong>, suspended '
                               'just 2 metres above the ground. Balance beams, rope '
                               'bridges, and low platforms build confidence in '
                               'children who may never have tried aerial adventure '
                               'before. Parents can walk alongside and encourage from '
                               'below, or join in on the same course. For teenagers '
                               'and adults, the blue route at 6 metres and the black '
                               'route at 10 metres provide progressively greater '
                               'challenges, including a 113-metre zipline integrated '
                               'into the blue course.</p>',
                               '<p>Standalone attractions include a 120-metre zipline '
                               'through the treetops, a 12.5-metre high swing, an '
                               'outdoor climbing wall with routes for different skill '
                               'levels, and ground-level activities suitable for '
                               'mixed-age groups. The Human Catapult and 20-metre '
                               'Quick Jump are aimed at older teens and adults with '
                               'specific height and health requirements — staff advise '
                               'on suitability at the ticket desk.</p>']},
               {'h2': 'A Full Family Day at the Park',
                'paragraphs': ['<p>Most families spend three to four hours at Glavani '
                               'Park, though enthusiastic groups often stay longer. '
                               'The shaded picnic area with coffee, drinks, and ice '
                               'cream means you can take breaks between activities '
                               'without leaving the site. Free on-site parking '
                               'accommodates cars, minibuses, and larger vehicles — '
                               'useful for multi-family trips or campsite '
                               'excursions.</p>',
                               '<p>The park is open daily from <strong>9 AM to 5 '
                               'PM</strong>, with last entry at <strong>3 PM</strong>. '
                               'Arriving before midday gives you the best chance to '
                               'complete multiple routes and attractions before '
                               'closing. From the end of September until the start of July, all visits require advance '
                               'booking. Call <a href="tel:+385918964525">+385 91 896 '
                               '4525</a> or use the online booking form to secure your '
                               'date.</p>',
                               '<p>What to bring: comfortable athletic clothing, '
                               'closed-toe sports shoes (trainers or hiking shoes — no '
                               'sandals), sunscreen, and water bottles. The park sells '
                               'refreshments on site, but having your own water is '
                               'wise on hot summer days. Lockers or leaving valuables '
                               'in the car are recommended before harnessing up.</p>']},
               {'h2': 'Combining Glavani Park with Other Family Days Out',
                'paragraphs': ['<p>Glavani Park pairs naturally with other Istrian '
                               'family destinations. After a morning on the ziplines, '
                               'drive 30 minutes to <strong>Pula</strong> for the '
                               'aquarium or amphitheatre. Alternatively, explore '
                               'medieval <strong>Barban</strong> or climb the bell '
                               'tower in <strong>Vodnjan</strong> on the same day — '
                               'both towns are minutes from the park. For beach time, '
                               'the coast around Medulin and Premantura lies within a '
                               '40-minute drive.</p>',
                               '<p>Many families staying in Rovinj, Poreč, or central '
                               'Istria villas treat Glavani Park as a dedicated '
                               'adventure day, then recover with a pool or beach day '
                               'afterwards. The park is featured by the Istria Tourist '
                               'Board and regularly receives positive reviews from '
                               'international visitors praising the professionalism of '
                               'the English-speaking instructor team.</p>',
                               '<p>For group celebrations, ask about <a '
                               'href="/en/birthday-parties-istria/">birthday party '
                               'packages</a> with priority access and a dedicated '
                               'celebration area. Schools and youth groups can enquire '
                               'about <a href="/en/school-trips-istria/">educational '
                               'outdoor programmes</a> tailored to age and '
                               'ability.</p>']},
               {'h2': 'Age Guidance and Safety for Families',
                'paragraphs': ['<p>Safety is central to everything at Glavani Park. '
                               'Every participant receives a harness, helmet, and '
                               'briefing before each activity. High-ropes routes use '
                               'continuous belay systems that keep visitors connected '
                               'at all times. Equipment is CE-certified and inspected '
                               'daily by staff.</p>',
                               '<p>The yellow route welcomes young children '
                               'accompanied by a responsible adult. Blue and black '
                               'routes suit older children, teenagers, and adults who '
                               'meet minimum height requirements. Standalone ziplines '
                               'and the high swing are popular with teens; the Human '
                               'Catapult and Quick Jump have stricter age and health '
                               'criteria. If you are unsure which activities suit your '
                               'children, call ahead — our team will help you plan a '
                               "visit that matches your family's ages and confidence "
                               'levels.</p>',
                               '<p>Read our full <a href="/en/safety/">safety and '
                               'equipment page</a> for detailed information on '
                               'certifications, procedures, and what to expect on '
                               'arrival. Glavani Park has welcomed thousands of '
                               'families from across Europe and aims to make every '
                               'visit both thrilling and reassuring for '
                               'parents.</p>']}],
  'faqs': [{'q': 'What is the minimum age for children at Glavani Park?',
            'a': 'The 2-metre yellow high-ropes route is designed for younger children '
                 'with adult supervision. Specific age and height limits apply to '
                 'taller attractions like the Human Catapult and Quick Jump. Contact '
                 '+385 91 896 4525 before visiting if you have questions about '
                 'suitability for your children.'},
           {'q': 'Can parents participate with their children?',
            'a': 'Absolutely. Parents are encouraged to join the yellow and blue '
                 'routes alongside their children. Many families treat it as a shared '
                 'experience rather than a drop-off activity. Separate tickets apply '
                 'for each participant.'},
           {'q': 'Is there food and shade at the park?',
            'a': 'Yes. A shaded picnic area offers coffee, soft drinks, and ice cream. '
                 'You are welcome to bring your own snacks, but please take litter '
                 'with you or use the bins provided. There is no full restaurant on '
                 'site, so a substantial meal before or after your visit works best.'},
           {'q': 'How far is Glavani Park from Pula?',
            'a': 'Glavani Park is approximately 30 minutes by car from Pula, 45 '
                 'minutes from Rovinj, and 10 minutes from Vodnjan. Free parking is '
                 'available on site at Glavani 10, 52207 Barban.'}],
  'related': [{'slug': 'things-to-do-in-istria',
               'title': 'Things to Do in Istria',
               'desc': 'Complete peninsula guide for families and couples'},
              {'slug': 'things-to-do-near-pula',
               'title': 'Things to Do Near Pula',
               'desc': 'Day trips within 30 minutes of Pula'},
              {'slug': 'birthday-parties-istria',
               'title': 'Birthday Parties Istria',
               'desc': 'Celebrate with ziplines and high ropes'},
              {'slug': 'safety',
               'title': 'Safety & Equipment',
               'desc': 'Certifications, briefings, and daily inspections'}]},
 {'slug': 'zipline-croatia',
  'title': 'Zipline Park Istria | Zipline Croatia at Glavani Park',
  'h1': "Zipline Croatia: Fly Through Istria's Forest Canopy",
  'meta_description': "Glavani Park is Istria's top zipline park — 120 m forest "
                      'ziplines up to 20 m high near Pula & Barban. Instructor-led '
                      'outdoor activities in Croatia. Open 9–5, last entry 3 PM. Book: '
                      '+385 91 896 4525.',
  'keywords': 'zipline park Istria, zipline park Croatia, zipline Croatia, zipline '
              'Istria, treetop zipline Pula, Glavani Park zipline, outdoor activities '
              'Istria Croatia, forest zipline Istria',
  'hero_badge': 'Zipline Park Istria · Up to 120 m · 20 m Above Ground',
  'hero_subtitle': 'Soar through oak forest at Glavani Park — a zipline park and '
                   'adventure destination in Istria with supervised flights between '
                   'Barban and Vodnjan, 30 minutes from Pula.',
  'image': 'zipline-120m-glavani-park-istria-croatia.webp',
  'image_alt': 'Guest riding the 120 metre zipline through the trees at Glavani Park, '
               'Istria, Croatia',
  'sections': [{'h2': 'Ziplining in Croatia: What to Expect',
                'paragraphs': ['<p>Ziplining has become one of the most sought-after '
                               'outdoor activities in Croatia, and for good reason. '
                               "The country's diverse landscapes — from Dalmatian "
                               'karst and Plitvice forests to Istrian oak woodland — '
                               'provide natural corridors for treetop flight. Unlike '
                               'ski-resort ziplines that operate seasonally on snow, '
                               'Croatian adventure parks run throughout the warm '
                               'months with professional harness systems, dual-line '
                               'redundancy on many installations, and instructor '
                               'supervision at launch and landing platforms.</p>',
                               '<p>When searching for <strong>zipline Croatia</strong> '
                               'experiences, quality and safety standards vary. Look '
                               'for parks that use CE-certified equipment, provide '
                               'helmets and full-body harnesses, conduct pre-ride '
                               'briefings, and maintain visible inspection schedules. '
                               'Glavani Park near <strong>Barban</strong> in Istria '
                               'meets these criteria and offers some of the longest '
                               'and highest lines on the peninsula — making it a '
                               'destination worth planning into your Croatian holiday '
                               'rather than a casual roadside stop.</p>']},
               {'h2': 'Glavani Park Zipline Experiences',
                'paragraphs': ['<p>Glavani Park operates multiple zipline elements '
                               'across its 1.5-hectare site. The headline attraction '
                               'is the standalone <strong>120-metre zipline</strong> '
                               'on the <a href="/en/valley-zipline/">Valley Zip Line '
                               'Course</a>, which carries riders up to 20 metres above '
                               'the forest floor through a corridor of mature oak '
                               'trees. An instructor fits your harness, checks '
                               'connections, and guides you through a launch briefing '
                               'before you step off the platform. The flight lasts '
                               'long enough to savour the sensation of speed and '
                               'height while remaining fully controlled from start to '
                               'finish.</p>',
                               '<p>Integrated into the <strong>blue high-ropes '
                               'route</strong> at 6 metres is a 113-metre zipline on '
                               'the <a href="/en/low-zipline/">Treetop Course</a>, '
                               'connecting the first and last platforms of the course. '
                               'Completing the blue route therefore includes an aerial '
                               'traverse as part of a longer challenge — ideal for '
                               'visitors who want ziplining combined with balance '
                               'obstacles and rope bridges. The black route at 10 '
                               'metres focuses on demanding aerial elements without a '
                               'zipline section, so many guests choose to experience '
                               'both the blue course and the standalone 120-metre line '
                               'in a single visit.</p>',
                               '<p>All zipline activities at Glavani Park are included '
                               'in standard day admission rather than sold as separate '
                               'upsells, though time on each element may be managed by '
                               'staff during busy periods to keep queues moving. '
                               'Arrive before midday during peak season to maximise '
                               'your opportunities on the lines.</p>']},
               {'h2': 'Who Can Ride the Zipline?',
                'paragraphs': ['<p>Ziplining at Glavani Park suits a broad range of '
                               'visitors, from teenagers experiencing their first '
                               'aerial ride to adults seeking an adrenaline highlight '
                               'during an Istria road trip. Minimum height and weight '
                               'limits apply for safety reasons — these are displayed '
                               'at the ticket area and explained during the briefing. '
                               'Children who do not meet the minimum requirements can '
                               'still enjoy the 2-metre yellow high-ropes route and '
                               'other ground-level activities while older family '
                               'members ride the ziplines.</p>',
                               '<p>Participants should wear closed-toe sports shoes '
                               'and comfortable clothing that allows freedom of '
                               'movement. Loose jewellery, scarves, and unsecured '
                               'items should be removed or stored before harnessing '
                               'up. Spectators can watch from designated areas near '
                               'the launch and landing platforms, making ziplining a '
                               'shared experience even for those who prefer to stay on '
                               'the ground.</p>',
                               '<p>If you have health conditions that might affect '
                               'your ability to ride — heart conditions, pregnancy, '
                               'recent surgery, or severe vertigo — discuss them with '
                               'staff before purchasing tickets. Instructors may '
                               'advise against certain attractions while recommending '
                               'alternatives within the park.</p>']},
               {'h2': 'Location and Practical Information',
                'paragraphs': ['<p>Glavani Park is located at Glavani 10, 52207 '
                               'Barban, on the road between <strong>Vodnjan</strong> '
                               '(10 km) and Barban (6 km). From the Pula–Labin main '
                               'road, turn at Manjadvorci toward Glavani, then left on '
                               'the local road for 300 metres. Free parking is '
                               'available on site. GPS coordinates: 45°1′17″ N, '
                               '13°57′4″ E.</p>',
                               '<p>The park is open daily from <strong>9 AM to 5 '
                               'PM</strong> with last entry at <strong>3 PM</strong>. '
                               'Allow at least three hours if you plan to ride the '
                               'ziplines plus one or two high-ropes routes. '
                               f'{_EN_BOOKING["off_season_note"]} '
                               f'{_EN_BOOKING["peak_walkin_note"]} '
                               'Call <a '
                               'href="tel:+385918964525">+385 91 896 4525</a> '
                               '(English) or book online before travelling.</p>',
                               '<p>From <strong>Pula</strong>, the drive takes '
                               'approximately 30 minutes — making Glavani Park one of '
                               'the most accessible zipline destinations for visitors '
                               'based on the coast. Rovinj is roughly 45 minutes away; '
                               'central Istria hill towns like Motovun are about an '
                               'hour. Many guests combine a zipline morning with an '
                               'afternoon exploring Barban, Vodnjan, or the beaches '
                               'south of Pula.</p>']},
               {'h2': 'Why Choose Glavani Park for Your Zipline Croatia Experience',
                'paragraphs': ['<p>Several factors distinguish Glavani Park from '
                               'smaller or seasonal zipline operators elsewhere in '
                               "Croatia. The park's scale — 1.5 hectares with multiple "
                               'attractions beyond ziplines — means a full day of '
                               'activity rather than a five-minute ride. The bilingual '
                               'instructor team, including English-speaking guides, '
                               'welcomes international visitors throughout the season. '
                               'Equipment is inspected daily, and the park is '
                               'recommended by the Istria Tourist Board.</p>',
                               '<p>Whether you are a family introducing teens to '
                               'aerial adventure, a couple seeking an active date away '
                               'from the beach, or a corporate group building '
                               'confidence through shared challenges, the ziplines at '
                               'Glavani Park deliver a memorable highlight. Explore '
                               'related pages on <a '
                               'href="/en/adventure-park-croatia/">adventure parks in '
                               'Croatia</a>, <a '
                               'href="/en/adventure-park-croatia/">family activities '
                               'in Istria</a>, and <a href="/en/safety/">safety '
                               'procedures</a> to plan your visit with '
                               'confidence.</p>']}],
  'faqs': [{'q': 'How long is the zipline at Glavani Park?',
            'a': 'The standalone zipline is 120 metres long, reaching up to 20 metres '
                 'above the ground. The blue high-ropes route also includes a '
                 '113-metre zipline between platforms at 6 metres height.'},
           {'q': 'Do I need a reservation for the zipline?',
            'a': f'{_EN_BOOKING["off_season_note"]} '
                 f'{_EN_BOOKING["peak_walkin_note"]} '
                 'Call +385 91 896 4525 or book online.'},
           {'q': 'Is ziplining safe for first-timers?',
            'a': 'Yes. Every rider receives a full harness, helmet, and pre-flight '
                 'briefing from a trained instructor. Equipment is CE-certified and '
                 'checked daily. Staff remain at launch and landing points throughout '
                 'operation.'},
           {'q': 'Can I do the zipline without the high-ropes courses?',
            'a': 'Day admission includes access to all attractions. You can focus on '
                 'the ziplines and standalone rides without completing the high-ropes '
                 'routes, though many visitors enjoy combining both during a single '
                 'visit.'},
           {'q': 'How high is the zipline at Glavani Park?',
            'a': 'The standalone zipline at Glavani Park reaches up to 20 metres above '
                 'the forest floor. The zipline on the blue high-ropes route runs at 6 '
                 'metres height between platforms.'},
           {'q': 'How far is the Glavani Park zipline from Pula?',
            'a': 'Glavani Park is about 30 minutes by car from Pula, making it one of '
                 "the closest zipline parks to Croatia's Istrian coast. Free parking "
                 'is available on site at Glavani 10, 52207 Barban.'},
           {'q': 'What is the minimum age for the zipline at Glavani Park?',
            'a': 'Minimum height and age limits apply for safety. Younger children can '
                 'enjoy the 2-metre yellow route while older children and teens ride '
                 'the ziplines. Call +385 91 896 4525 before visiting if you are '
                 'unsure about suitability.'}],
  'related': [{'slug': 'adventure-park-croatia',
               'title': 'Adventure Parks in Croatia',
               'desc': 'Full attraction overview at Glavani Park Istria'},
              {'slug': 'adventure-park-croatia',
               'title': 'Our Activities',
               'desc': 'Ziplines and high ropes for all ages'},
              {'slug': 'things-to-do-near-pula',
               'title': 'Things to Do Near Pula',
               'desc': 'Zipline day trip from Pula in 30 minutes'},
              {'slug': 'safety',
               'title': 'Safety & Equipment',
               'desc': 'Harness standards and daily inspections'}]},
 {'slug': 'school-trips-istria',
  'title': 'School Trips Istria | Educational Visits to Glavani Park',
  'h1': 'School Trips in Istria: Outdoor Learning at Glavani Park',
  'meta_description': 'Educational school trips in Istria at Glavani Park — risk '
                      'awareness, coordination & nature near Pula & Barban. '
                      'Age-appropriate routes. Book groups: +385 91 896 4525.',
  'keywords': 'school trips Istria, educational visits Croatia, school outing Pula, '
              'outdoor education Istria, Glavani Park school trip, class trip '
              'adventure park',
  'hero_badge': 'Schools & Youth Groups · Curriculum-Linked Learning',
  'hero_subtitle': 'Take learning outdoors with instructor-led programmes that teach '
                   'risk assessment, physical coordination, and teamwork at Glavani '
                   'Park between Barban and Vodnjan.',
  'image': 'climbing-wall-outdoor-activities-istria.webp',
  'image_alt': 'School group on an educational visit to Glavani Park outdoor adventure '
               'park, Istria',
  'sections': [{'h2': 'The Value of Outdoor Education in Istria',
                'paragraphs': ['<p>Classroom learning forms the foundation of '
                               'education, but some lessons land most powerfully '
                               'outdoors — where students assess real risk, support '
                               'classmates under mild pressure, and discover physical '
                               'capabilities they did not know they possessed. '
                               "Istria's mild climate and accessible geography make it "
                               'an ideal region for school excursions, whether you are '
                               'a local Croatian school or an international group '
                               'visiting on a cultural exchange.</p>',
                               '<p><strong>Glavani Park</strong> offers a structured '
                               'environment for <strong>school trips in '
                               'Istria</strong> without the open-ended management '
                               'challenges of unsupervised forest hikes or informal '
                               'beach days. Every activity is staffed by trained '
                               'instructors using CE-certified equipment, with '
                               'age-appropriate routes and clear safety briefings '
                               'before participants leave the ground.</p>']},
               {'h2': 'Educational Programmes at Glavani Park',
                'paragraphs': ['<p>School visits can emphasise different learning '
                               'outcomes depending on age group and curriculum goals. '
                               'Primary pupils benefit from the 2-metre yellow '
                               'high-ropes route, which develops balance, '
                               'coordination, and confidence while remaining close '
                               'enough to the ground for teachers to observe and '
                               'encourage. Secondary students tackle the blue route at '
                               '6 metres — including a 113-metre zipline — or the '
                               'black route at 10 metres for advanced physical '
                               'education and leadership modules.</p>',
                               '<p>Educational themes naturally embedded in the visit '
                               'include risk assessment (identifying hazards, '
                               'following instructions, using PPE correctly), physics '
                               'and engineering (how harnesses, pulleys, and descender '
                               'systems work), environmental awareness (oak forest '
                               'ecology, sustainable tourism), and social development '
                               '(peer support, communication under challenge, '
                               'inclusive participation).</p>',
                               '<p>Teachers receive a pre-visit information pack '
                               'outlining safety procedures, recommended '
                               'student-to-supervisor ratios, clothing requirements, '
                               'and suggested pre- and post-visit classroom '
                               'activities. Call <a href="tel:+385918964525">+385 91 '
                               '896 4525</a> to discuss group size, dates, and '
                               'programme customisation.</p>']},
               {'h2': 'Safety and Supervision for Student Groups',
                'paragraphs': ['<p>Student safety is non-negotiable. Glavani Park '
                               'operates with daily equipment inspections, continuous '
                               'belay systems on high-ropes routes, and instructor '
                               'supervision at every launch point. Each student '
                               'receives a helmet and harness fitted by staff, plus a '
                               'verbal briefing appropriate to their age and language '
                               'level. English and Croatian instruction are '
                               'available.</p>',
                               '<p>Schools should maintain their own duty-of-care '
                               'supervision alongside park instructors — typically one '
                               'teacher or parent helper per small group in addition '
                               'to park staff. Minimum height and health requirements '
                               'apply to certain attractions; these are communicated '
                               'during booking so teachers can set accurate '
                               'expectations before the trip.</p>',
                               '<p>Full details of certifications and operational '
                               'standards are published on our <a '
                               'href="/en/safety/">safety page</a>. The park is '
                               'recommended by the Istria Tourist Board and has hosted '
                               'school groups from across Croatia and neighbouring '
                               'countries.</p>']},
               {'h2': 'Logistics for Istria School Excursions',
                'paragraphs': ['<p>Glavani Park is located at Glavani 10, 52207 '
                               'Barban, between <strong>Vodnjan</strong> (10 km) and '
                               '<strong>Barban</strong> (6 km). Coach and minibus '
                               'parking is free on site. From <strong>Pula</strong>, '
                               'allow approximately 30 minutes; from Rovinj, 45 '
                               'minutes. The park is open daily <strong>9 AM–5 '
                               'PM</strong> with last entry at <strong>3 PM</strong> — '
                               'most school groups schedule 9:30 AM arrival for a 3–4 '
                               'hour visit.</p>',
                               '<p>Students should wear closed-toe sports shoes, '
                               'comfortable clothing, and sunscreen in summer. Packed '
                               'lunches can be eaten in the shaded picnic area; soft '
                               'drinks and ice cream are sold on site. Toilets and '
                               'basic facilities are available near the ticket '
                               'area.</p>',
                               '<p>Combine the visit with a cultural stop in Vodnjan '
                               '(bell tower, mummy saints) or Barban (medieval walls) '
                               'to create a full-day Istria excursion that balances '
                               'physical activity with local heritage.</p>']},
               {'h2': 'Book a School Trip to Glavani Park',
                'paragraphs': ['<p>Advance booking is essential for school groups. '
                               'Provide estimated student numbers, age range, '
                               'preferred date, and any special requirements (mixed '
                               'abilities, wheelchair users who may spectate, language '
                               'preferences). We will confirm instructor allocation, '
                               'timing, and pricing.</p>',
                               '<p>For youth clubs, scout groups, and summer camps '
                               'based at Istrian campsites, similar packages apply — '
                               'see our <a href="/en/partners/">partner programme</a> '
                               'for accommodation providers interested in recommending '
                               'Glavani Park to guests. Whether you are planning a '
                               'single class outing or an annual adventure tradition, '
                               'Glavani Park delivers an educational experience '
                               'students reference long after returning to the '
                               'classroom.</p>',
                               '<p>Teachers report that post-visit classroom '
                               'discussions — drawing diagrams of pulley systems, '
                               'writing reflective essays about overcoming fear, or '
                               'debating risk versus reward — extend the value of a '
                               'half-day excursion well beyond the bus ride home. That '
                               'makes Glavani Park not merely a reward trip but a '
                               'legitimate supplement to PE, science, and '
                               'personal-development curricula.</p>']}],
  'faqs': [{'q': 'What age groups can visit on a school trip?',
            'a': 'Primary through secondary ages are welcome. The yellow route suits '
                 'younger pupils; blue and black routes suit older students. Minimum '
                 'height limits apply to some attractions — discuss your class profile '
                 'when booking on +385 91 896 4525.'},
           {'q': 'Do teachers need to pay?',
            'a': 'Teacher and supervisor ratios are agreed during booking. Contact the '
                 'park for current policy on complimentary supervisor places and '
                 'pricing for students.'},
           {'q': 'Is there a minimum group size?',
            'a': 'School packages are designed for class-sized groups. Smaller '
                 'homeschool or club groups should call to discuss availability and '
                 'pricing.'},
           {'q': 'Can the visit link to curriculum topics?',
            'a': 'Yes. Pre-visit materials support discussions on risk, physics, PE, '
                 'and environmental science. Teachers are welcome to brief instructors '
                 'on specific learning objectives before activities begin.'}],
  'related': [{'slug': 'team-building-istria',
               'title': 'Team Building Istria',
               'desc': 'Corporate and sports group programmes'},
              {'slug': 'birthday-parties-istria',
               'title': 'Birthday Parties Istria',
               'desc': 'Youth celebration packages'},
              {'slug': 'adventure-park-croatia',
               'title': 'Our Activities',
               'desc': 'Age-appropriate routes and attractions'},
              {'slug': 'safety',
               'title': 'Safety & Equipment',
               'desc': 'Standards for supervised student visits'}]},
 {'slug': 'things-to-do-near-pula',
  'title': 'Things to Do Near Pula | Day Trips & Glavani Park',
  'h1': 'Things to Do Near Pula: Day Trips and Outdoor Adventures',
  'meta_description': 'Best things to do near Pula — Roman sights, Kamenjak beaches & '
                      'Glavani Park ziplines 30 min away. Open daily 9–5, last entry 3 '
                      'PM. Call +385 91 896 4525.',
  'keywords': 'things to do near Pula, day trips from Pula, outdoor activities Pula, '
              'family day trip Pula, Glavani Park Pula, adventure near Pula Croatia',
  'hero_badge': '30 Min from Pula · Free Parking',
  'hero_subtitle': 'Beyond the amphitheatre and Adriatic beaches, inland Istria offers '
                   'ziplines, high ropes, and adrenaline rides at Glavani Park — an '
                   'easy half-day escape near Barban and Vodnjan.',
  'image': 'visitor-gallery-zipline-trio-16.webp',
  'image_alt': 'Three visitors on a suspended log high above the forest on the zipline course at Glavani Park, Istria',
  'location_map': True,
  'sections': [{'h2': 'Pula as Your Istria Base Camp',
                'paragraphs': ['<p><strong>Pula</strong> anchors the southern tip of '
                               "Istria with one of Croatia's busiest airports, a "
                               'deep-rooted Roman heritage, and immediate access to '
                               'the Adriatic. Most visitors know the Arena — a '
                               'first-century amphitheatre still hosting concerts and '
                               'film festivals — and the nearby coastal nature park at '
                               'Kamenjak, where rocky coves and pine-shaded paths '
                               'define the classic Istrian summer. But staying in Pula '
                               'also puts you within easy reach of inland villages, '
                               "wine country, and some of the region's best outdoor "
                               'adventures.</p>',
                               '<p>If you have covered the city sights and beach days '
                               'and want something active, <strong>Glavani '
                               'Park</strong> is among the top-rated <strong>things to '
                               'do near Pula</strong> that does not require a full-day '
                               'drive. The park sits 30 minutes inland at Glavani 10, '
                               '52207 Barban, on the road between Barban and Vodnjan — '
                               'close enough for a morning outing before lunch back in '
                               'Pula, yet far enough to feel immersed in Istrian '
                               'forest countryside.</p>']},
               {'h2': 'Coastal and Cultural Attractions Around Pula',
                'paragraphs': ['<p>Before heading inland, note the coastal highlights '
                               'within 20 minutes of Pula centre. The Aquarium Pula '
                               'occupies a former Austro-Hungarian fort and appeals to '
                               'families with young children. Brijuni National Park — '
                               'reached by boat from Fažana — combines archaeology, '
                               'safari animals, and swimming. Kamenjak Nature Park at '
                               'Premantura offers cliff jumping spots (for confident '
                               "swimmers), cycling trails, and some of Istria's "
                               'clearest water.</p>',
                               '<p>In town, the Temple of Augustus, Arch of the '
                               'Sergii, and hilltop Venetian fortress reward a few '
                               'hours of walking. Evenings belong to the harbour '
                               'promenade and konobas serving Istrian pasta, seafood, '
                               'and local Malvazija wine. These experiences define '
                               'Pula; Glavani Park complements them with structured '
                               'physical adventure rather than replacing them.</p>']},
               {'h2': 'Glavani Park: The Inland Adventure Option',
                'paragraphs': ['<p>Spread across 1.5 hectares of oak forest, Glavani '
                               "Park is one of Croatia's largest dedicated adrenaline "
                               'parks. Attractions include three high-ropes routes '
                               '(yellow 2 m, blue 6 m, black 10 m), a 120-metre '
                               'zipline, a 113-metre zipline on the blue course, a '
                               '12.5-metre high swing, Human Catapult, 20-metre Quick '
                               'Jump, and an outdoor climbing wall. English-speaking '
                               'instructors operate every station with CE-certified '
                               'harnesses and helmets.</p>',
                               '<p>The park suits families, couples, and groups based '
                               'in Pula hotels, villas, or campsites who want a break '
                               'from sand and sightseeing. Most visitors spend three '
                               'to four hours on site. Free parking accommodates cars '
                               'and larger vehicles. Opening hours are daily <strong>9 '
                               'AM–5 PM</strong> with last entry at <strong>3 '
                               'PM</strong> — plan to arrive before midday if you want '
                               'to experience multiple attractions.</p>',
                               '<p>Book before you drive out — '
                               f'{_EN_BOOKING["off_season_note"]} '
                               f'{_EN_BOOKING["peak_walkin_note"]} '
                               'Call <a href="tel:+385918964525">+385 '
                               '91 896 4525</a> or book online.</p>']},
               {'h2': 'Combining Pula and Inland Istria in One Day',
                'paragraphs': ['<p>A popular itinerary: Roman Pula or Kamenjak beach '
                               'in the morning, then drive to Glavani Park for an '
                               'early-afternoon adrenaline session (remember last '
                               'entry is 3 PM). Alternatively, dedicate a full morning '
                               'to the park and explore <strong>Barban</strong> or '
                               "<strong>Vodnjan</strong> afterward — Barban's medieval "
                               "core and Vodnjan's towering church bell are both "
                               'minutes from the park entrance.</p>',
                               '<p>Another option pairs Glavani Park with a wine '
                               'tasting or truffle lunch in central Istria if you are '
                               'willing to extend the drive. For tighter schedules, '
                               'the park alone fills a satisfying half-day without '
                               'rushing. See our broader guide to <a '
                               'href="/en/things-to-do-in-istria/">things to do in '
                               'Istria</a> for multi-day planning.</p>']},
               {'h2': 'Getting from Pula to Glavani Park',
                'paragraphs': ['<p>From Pula, take the road toward Labin and turn at '
                               'Manjadvorci toward Glavani. Continue left on the local '
                               'road for 300 metres to the park entrance. Signage and '
                               'GPS (45°1′17″ N, 13°57′4″ E) make navigation '
                               'straightforward for rental-car visitors. No 4x4 or '
                               'special vehicle is required.</p>',
                               '<p>Public transport options are limited; a rental car '
                               'or organised excursion is the practical choice. Taxi '
                               'and private transfer services from Pula can be '
                               'arranged — provide the address Glavani 10, Barban, '
                               'when booking. For detailed attraction information, '
                               'visit <a href="/en/zipline-croatia/">zipline '
                               'Croatia</a>, <a '
                               'href="/en/adventure-park-croatia/">family '
                               'activities</a>, and <a '
                               'href="/en/adventure-park-croatia/">adventure park</a> '
                               'pages before you travel.</p>',
                               '<p>Repeat visitors from Pula often discover that '
                               'inland adventure balances a beach-heavy holiday: after '
                               'two or three days of swimming at Stinjan or Verudela, '
                               'a forest zipline morning restores energy and gives '
                               'teenagers a story to tell back at school. Glavani '
                               "Park's shaded oak canopy also offers welcome relief "
                               'when the coastal pavement radiates midday heat in July '
                               'and August.</p>']}],
  'faqs': [{'q': 'How far is Glavani Park from Pula city centre?',
            'a': 'Approximately 30 minutes by car, depending on traffic and your '
                 'starting point in Pula. Free parking is available on site at Glavani '
                 '10, 52207 Barban.'},
           {'q': 'Can I visit Glavani Park and Pula sights in one day?',
            'a': 'Yes. Many visitors do the amphitheatre or beach in the morning and '
                 'Glavani Park in the afternoon. Arrive before 3 PM for last entry; '
                 'the park closes at 5 PM.'},
           {'q': 'Is Glavani Park suitable after a beach day?',
            'a': 'Absolutely — closed-toe shoes are required, so change out of '
                 'flip-flops before arrival. The shaded forest environment is cooler '
                 'than open beach in peak summer heat.'},
           {'q': 'Do I need to book from Pula or can I just drive there?',
            'a': f'{_EN_BOOKING["off_season_note"]} '
                 f'{_EN_BOOKING["peak_walkin_note"]} '
                 'Call +385 91 896 4525 or book online.'}],
  'related': [{'slug': 'things-to-do-in-istria',
               'title': 'Things to Do in Istria',
               'desc': 'Full peninsula destination guide'},
              {'slug': 'adventure-park-croatia',
               'title': 'Our Activities',
               'desc': 'Kid-friendly routes near Pula'},
              {'slug': 'zipline-croatia',
               'title': 'Zipline Croatia',
               'desc': '120-metre treetop flights from Pula base'},
              {'slug': 'adventure-park-croatia',
               'title': 'Adventure Parks in Croatia',
               'desc': 'Why Glavani Park leads the region'}]},
 {'slug': 'safety',
  'title': 'Safety at Glavani Park | Equipment & Procedures',
  'h1': 'Safety at Glavani Park: Equipment, Training, and Trust',
  'meta_description': 'Glavani Park safety — CE-certified harnesses, daily '
                      'inspections, trained instructors & continuous belay on high '
                      'ropes near Pula. Open 9–5. Questions: +385 91 896 4525.',
  'keywords': 'Glavani Park safety, adventure park safety Croatia, high ropes safety '
              'Istria, CE certified harness Croatia, zipline safety Pula, adventure '
              'park equipment standards',
  'hero_badge': 'CE-Certified Equipment · Daily Inspections',
  'hero_subtitle': 'Every attraction at Glavani Park is operated by trained '
                   'instructors using inspected, certified equipment — because '
                   'confidence in safety is the foundation of every great adventure.',
  'image': 'quick-jump-20m-free-fall-istria.webp',
  'image_alt': 'Instructor briefing a visitor before the Quick Jump at Glavani Park, '
               'Istria',
  'sections': [{'h2': 'Our Safety Philosophy',
                'paragraphs': ['<p>Adrenaline and safety are not opposites — they '
                               'depend on each other. Visitors step off platforms and '
                               'clip onto ziplines because they trust the systems '
                               'holding them. At <strong>Glavani Park</strong>, that '
                               'trust is earned through visible standards: certified '
                               'equipment, repeated briefings, instructor presence at '
                               'every station, and a culture where any participant can '
                               'ask questions before committing to an activity.</p>',
                               '<p>Located at Glavani 10 between '
                               '<strong>Barban</strong> and <strong>Vodnjan</strong>, '
                               'the park welcomes thousands of international guests '
                               'each season — many trying high ropes or ziplines for '
                               'the first time. Our bilingual team, including '
                               'English-speaking instructors, prioritises clear '
                               'communication because misunderstanding at height is a '
                               'risk we refuse to accept.</p>']},
               {'h2': 'Equipment Standards and Certifications',
                'paragraphs': ['<p>All personal protective equipment at Glavani Park '
                               'meets European CE certification requirements for '
                               'adventure park use. This includes full-body harnesses '
                               'sized and fitted by staff, helmets adjusted for each '
                               'participant, carabiners and connectors rated for '
                               'dynamic loads, and descender systems on attractions '
                               'such as the 20-metre Quick Jump.</p>',
                               '<p>High-ropes courses use continuous belay systems '
                               'that keep visitors connected to safety lines from the '
                               'moment they leave the ground until they return to the '
                               'platform. Zipline trollies, launch platforms, and '
                               'landing areas are inspected before daily opening. The '
                               'Human Catapult employs redundant safety lines and '
                               'pre-ride health screening in addition to standard '
                               'harness protocols.</p>',
                               '<p>Equipment that shows wear beyond acceptable limits '
                               'is removed from service immediately — not at end of '
                               'season, not after the next delivery, but the same day. '
                               'Replacement stock is maintained on site so operations '
                               'never compromise on gear quality.</p>']},
               {'h2': 'Instructor Training and On-Course Supervision',
                'paragraphs': ['<p>Every attraction is staffed by trained instructors '
                               'who conduct pre-activity briefings in English or '
                               'Croatian as required. Briefings cover harness fitting, '
                               'connection checks, course rules, emergency signals, '
                               'and activity-specific instructions — how to position '
                               'on the high swing, how to launch on the zipline, what '
                               'to expect on the Quick Jump descent.</p>',
                               '<p>Instructors monitor conditions throughout the day: '
                               'weather, participant fatigue, queue management, and '
                               'equipment function. They have authority to pause or '
                               'stop an activity if wind, rain, or participant health '
                               'raises concern. Minimum height, weight, age, and '
                               'health restrictions exist for extreme attractions; '
                               'these are enforced consistently, not waived under '
                               'pressure.</p>',
                               '<p>Group visits — <a '
                               'href="/en/school-trips-istria/">school trips</a>, <a '
                               'href="/en/team-building-istria/">corporate events</a>, '
                               'and <a href="/en/birthday-parties-istria/">birthday '
                               'parties</a> — receive additional coordination so '
                               'supervisor ratios and activity selection match the '
                               "group's profile.</p>"]},
               {'h2': 'Daily Operational Procedures',
                'paragraphs': ['<p>Before the park opens at <strong>9 AM</strong>, '
                               'staff complete a structured inspection routine across '
                               'all routes and standalone attractions. Connections, '
                               'anchor points, zipline lines, swing cables, catapult '
                               'systems, and climbing wall holds are checked according '
                               'to an internal checklist. Incidents, near-misses, and '
                               'equipment defects are logged and reviewed.</p>',
                               '<p>Last entry at <strong>3 PM</strong> ensures '
                               'participants have adequate daylight and operational '
                               'time to complete activities before the <strong>5 '
                               'PM</strong> closing. Attractions may close '
                               'individually earlier if queues would extend beyond '
                               'safe operating hours — staff communicate this at the '
                               'ticket desk rather than leaving visitors stranded '
                               'mid-visit.</p>',
                               '<p>Visitors contribute to safety by following '
                               'instructions, wearing appropriate footwear (closed-toe '
                               'sports shoes only — no sandals or flip-flops), '
                               'securing loose items before activities, and disclosing '
                               'relevant health conditions honestly at the ticket '
                               'area.</p>']},
               {'h2': 'What to Expect as a First-Time Visitor',
                'paragraphs': ['<p>If you are nervous about height or speed, tell your '
                               'instructor — they will explain each phase of the '
                               'activity and never rush you off a platform. Many '
                               'first-time visitors start on the 2-metre yellow route '
                               'before progressing to blue, black, or standalone '
                               'ziplines. There is no obligation to complete every '
                               'attraction; watching from ground level is welcome for '
                               'friends and family who prefer to stay below the '
                               'canopy.</p>',
                               '<p>Glavani Park is featured by the <a '
                               'href="https://www.istra.hr/en/destinations/barban/1531" '
                               'rel="noopener noreferrer">Istria Tourist Board</a> and '
                               'maintains the operational standards expected of a '
                               'leading regional outdoor attraction. Questions before '
                               'your visit? Call <a href="tel:+385918964525">+385 91 '
                               '896 4525</a> (English) and speak directly with our '
                               'team.</p>',
                               '<p>Adventure should feel exhilarating, not reckless. '
                               'At Glavani Park near Pula, Barban, and Vodnjan, '
                               'professional safety systems let you focus on the view, '
                               'the speed, and the shared achievement — knowing the '
                               'details are handled by people who inspect, train, and '
                               'care every single day.</p>',
                               '<p>Parents often ask whether younger children can '
                               'watch while older siblings ride the ziplines — the '
                               'answer is yes. Designated spectator areas keep '
                               'families together without pressuring every member onto '
                               'every attraction. That inclusive approach, combined '
                               'with transparent briefing procedures, is why Glavani '
                               'Park remains a trusted choice for first-time adventure '
                               'visitors across Istria.</p>']}],
  'faqs': [{'q': 'Is the equipment at Glavani Park certified?',
            'a': 'Yes. Harnesses, helmets, connectors, and descender systems are '
                 'CE-certified for adventure park use and inspected daily before '
                 'opening at 9 AM.'},
           {'q': 'Are instructors always present?',
            'a': 'Every attraction is supervised by trained staff who conduct '
                 'briefings and monitor participants throughout operation. High-ropes '
                 'routes use continuous belay systems.'},
           {'q': 'Who should not participate in extreme attractions?',
            'a': 'Pregnant women, people with heart conditions, recent surgery, severe '
                 'vertigo, or other relevant health issues should consult staff before '
                 'riding the Human Catapult, Quick Jump, or high black route. '
                 'Alternative activities may still be suitable.'},
           {'q': 'What should I wear for safety?',
            'a': 'Closed-toe sports shoes (trainers or hiking shoes), comfortable '
                 'fitted clothing, no loose jewellery or scarves. Long hair should be '
                 'tied back. Sunscreen and water are recommended in summer.'}],
  'related': [{'slug': 'adventure-park-croatia',
               'title': 'Adventure Parks in Croatia',
               'desc': 'Full attraction overview at Glavani Park'},
              {'slug': 'adventure-park-croatia',
               'title': 'Our Activities',
               'desc': 'Age guidance and yellow route for children'},
              {'slug': 'zipline-croatia',
               'title': 'Zipline Croatia',
               'desc': 'Zipline-specific safety and briefing info'},
              {'slug': 'school-trips-istria',
               'title': 'School Trips Istria',
               'desc': 'Supervision standards for student groups'}]},
 {'slug': 'partners',
  'title': 'Partner With Glavani Park | Hotels & Travel Blogs',
  'h1': 'Partner With Glavani Park: Hotels, Campsites, and Travel Creators',
  'meta_description': 'Join the Glavani Park partner programme — commission, '
                      'co-marketing & guest referrals for hotels, campsites & travel '
                      'blogs in Istria. Contact: +385 91 896 4525.',
  'keywords': 'Glavani Park partners, Istria hotel partners, campsite referral '
              'Croatia, travel blog partnership Istria, affiliate adventure park '
              'Croatia, tourism partner programme',
  'hero_badge': 'Hotels · Campsites · Travel Blogs',
  'hero_subtitle': "Recommend one of Istria's top-rated outdoor attractions to your "
                   'guests and readers — and benefit from a structured partnership '
                   'with Glavani Park near Pula, Barban, and Vodnjan.',
  'image': 'glavani-park-adventure-istria-croatia.jpg',
  'image_alt': 'Glavani Park partnership programme for Istria accommodation and travel '
               'media',
  'sections': [{'h2': 'Why Partner With Glavani Park?',
                'paragraphs': ['<p>Istria accommodation providers and travel '
                               'publishers face a recurring guest question: what '
                               'should we do besides the beach? <strong>Glavani '
                               'Park</strong> answers that question with a full-day '
                               'outdoor adventure — 1.5 hectares of high ropes, '
                               'ziplines, Human Catapult, and family-friendly routes '
                               'just 30 minutes from <strong>Pula</strong>, minutes '
                               'from <strong>Barban</strong> and '
                               '<strong>Vodnjan</strong>. Partnering with us gives '
                               'your business a credible, high-review activity to '
                               'recommend while generating referral value for your '
                               'organisation.</p>',
                               '<p>The park is listed by the Istria Tourist Board, '
                               'operates daily <strong>9 AM–5 PM</strong> (last entry '
                               '<strong>3 PM</strong>), and welcomes international '
                               'visitors with English-speaking instructors. These '
                               'attributes make Glavani Park an easy sell to families, '
                               'active couples, and corporate groups staying in your '
                               'hotel, campsite, or villa — without the reputational '
                               'risk of recommending unvetted operators.</p>']},
               {'h2': 'Who Our Partner Programme Serves',
                'paragraphs': ['<p><strong>Hotels and resorts</strong> in Pula, '
                               'Rovinj, Medulin, and inland Istria use our partnership '
                               'to enhance concierge recommendations, fill activity '
                               'gaps on rainy days, and differentiate from competitors '
                               'offering only beach and pool options. Front-desk '
                               'cards, QR codes, and pre-arrival email suggestions '
                               'integrate seamlessly with guest communication.</p>',
                               '<p><strong>Campsites and holiday parks</strong> — '
                               'abundant across Istria — benefit especially. Camping '
                               "families seek active day trips; Glavani Park's yellow "
                               'route for children and teen-friendly ziplines match '
                               'that demographic precisely. Group shuttle coordination '
                               'can be discussed for larger sites.</p>',
                               '<p><strong>Travel blogs, influencers, and tourism '
                               'portals</strong> covering Croatia and Istria gain '
                               'access to media assets, factual briefings, and '
                               'commission or sponsored-content frameworks depending '
                               'on audience size and alignment. We value accurate, '
                               'experience-based coverage over generic directory '
                               'listings.</p>',
                               '<p><strong>Travel agencies and DMCs</strong> building '
                               'Istria itineraries can slot Glavani Park as a half-day '
                               'module between cultural Pula and hill-town excursions '
                               '— call <a href="tel:+385918964525">+385 91 896 '
                               '4525</a> for group rates and availability '
                               'windows.</p>']},
               {'h2': 'Partner Benefits and Support',
                'paragraphs': ['<p>Partners receive marketing materials including '
                               'high-resolution photography, approved descriptions, '
                               'opening-hour facts, and directions from major Istria '
                               'hubs. We provide printable A4 sheets for reception '
                               'desks, digital banners where appropriate, and unique '
                               'tracking links or promo codes to attribute referrals '
                               'fairly.</p>',
                               '<p>Commission structures and co-marketing terms are '
                               'agreed individually based on partner type and volume. '
                               'Hotels sending steady guest traffic may receive '
                               'different arrangements than a niche adventure travel '
                               'blog — transparency and mutual benefit guide every '
                               'agreement.</p>',
                               '<p>We also welcome cross-promotion with complementary '
                               'Istria businesses — wineries, e-bike rental shops, and '
                               'cultural guides — whose guests benefit from a balanced '
                               'itinerary mixing food, heritage, and outdoor sport. '
                               'Introduce your partners to us when building package '
                               'offers; collaborative bundles strengthen every '
                               "participant's visibility across the peninsula.</p>",
                               '<p>Our team responds to partner enquiries in English '
                               'and Croatian. We can arrange familiarisation visits '
                               'for concierges, camp managers, and journalists so '
                               'recommendations come from firsthand experience — the '
                               'most convincing referral of all.</p>']},
               {'h2': 'What to Tell Your Guests',
                'paragraphs': ['<p>Key facts partners share consistently: Glavani Park '
                               "is one of Croatia's largest adrenaline parks with "
                               'three high-ropes levels, 120-metre zipline, 12.5-metre '
                               'swing, Human Catapult, Quick Jump, and climbing wall. '
                               'Address: Glavani 10, 52207 Barban. Free parking. Open '
                               'daily 9–5, last entry 3 PM. Booking phone: +385 91 896 '
                               '4525 (English).</p>',
                               '<p>Direct guests to our activity pages for depth: <a '
                               'href="/en/adventure-park-croatia/">family '
                               'activities</a>, <a href="/en/zipline-croatia/">zipline '
                               'guide</a>, <a href="/en/team-building-istria/">team '
                               'building</a>, and <a '
                               'href="/en/things-to-do-near-pula/">day trips from '
                               'Pula</a>. Emphasise calling ahead in peak season — '
                               'partners who set that expectation reduce guest '
                               'disappointment and strengthen trust in your '
                               'recommendation.</p>']},
               {'h2': 'Apply to Become a Partner',
                'paragraphs': ['<p>To join the Glavani Park partner programme, contact '
                               'us with your business name, website, location in '
                               'Istria (if applicable), audience or guest profile, and '
                               'how you plan to promote the park. Email <a '
                               'href="mailto:info@glavanipark.com">info@glavanipark.com</a> '
                               'or call <a href="tel:+385918964525">+385 91 896 '
                               '4525</a>.</p>',
                               '<p>Travel bloggers seeking embed codes and suggested '
                               'anchor text should visit our <a '
                               'href="/en/link-to-us/">Link to Us</a> page for '
                               'ready-to-use HTML and SEO guidance. Together we can '
                               'put more Istria visitors on ziplines — and more '
                               'satisfied guests back in your reviews.</p>',
                               '<p>Seasonal demand peaks from June through August, so '
                               'partners who promote early-summer and September slots '
                               'help spread visitor flow while giving guests better '
                               'on-site experiences. We reciprocate with accurate '
                               'availability guidance and prompt responses to guest '
                               'enquiries referred through your front desk or blog '
                               'comments section.</p>',
                               '<p>New partners typically receive onboarding within a '
                               'few business days: approved copy blocks, map '
                               'directions from Pula and Rovinj, and answers to the '
                               'guest questions your reception team hears most often — '
                               'parking, age limits, and whether to book ahead on +385 '
                               '91 896 4525.</p>']}],
  'faqs': [{'q': 'Is there a cost to join the partner programme?',
            'a': 'Partnership registration is free. Commercial terms such as '
                 'commission or co-marketing are agreed individually. Contact +385 91 '
                 '896 4525 or info@glavanipark.com to discuss.'},
           {'q': 'Can campsites arrange group transport to Glavani Park?',
            'a': 'The park has free coach and minibus parking. Shuttle coordination '
                 'from your site can be discussed during partnership setup — many camp '
                 'guests travel by rental car.'},
           {'q': 'Do partners receive familiarisation visits?',
            'a': 'Yes, subject to scheduling. Fam visits help concierges and content '
                 'creators recommend attractions accurately. Enquire when applying.'},
           {'q': 'What marketing assets are available?',
            'a': 'Partners receive approved copy, photography, hours, directions, and '
                 'tracking links or codes. Bloggers also access embed snippets on our '
                 'Link to Us page.'}],
  'related': [{'slug': 'link-to-us',
               'title': 'Link to Us',
               'desc': 'Embed codes and anchor text for backlinks'},
              {'slug': 'things-to-do-in-istria',
               'title': 'Things to Do in Istria',
               'desc': 'Destination content for your guests'},
              {'slug': 'adventure-park-croatia',
               'title': 'Our Activities',
               'desc': 'Family-focused page for campsite audiences'},
              {'slug': 'adventure-park-croatia',
               'title': 'Adventure Parks in Croatia',
               'desc': 'Overview for travel media and agencies'}]},
 {'slug': 'link-to-us',
  'title': 'Link to Glavani Park | Embed Codes & Anchor Text',
  'h1': 'Link to Us: Backlinks, Embed Codes, and Suggested Anchor Text',
  'meta_description': 'Link to Glavani Park — HTML embed codes, banner snippets & SEO '
                      'anchor text for travel blogs, hotels & Istria directories. '
                      'Adventure park near Pula. +385 91 896 4525.',
  'keywords': 'link to Glavani Park, embed code adventure park, backlink Istria '
              'tourism, anchor text Glavani Park, travel blog link Croatia, partner '
              'embed HTML',
  'hero_badge': 'Bloggers · Directories · Webmasters',
  'hero_subtitle': "Help your readers discover Istria's leading adventure park with "
                   'approved links, embed snippets, and anchor-text suggestions — all '
                   'pointing to Glavani Park near Barban and Pula.',
  'image': 'glavani-park-adventure-istria-croatia.jpg',
  'image_alt': 'Link to Glavani Park — embed and backlink resources for travel '
               'websites',
  'sections': [{'h2': 'Why Link to Glavani Park?',
                'paragraphs': ['<p>Travel blogs, Istria accommodation websites, '
                               'tourism directories, and local business guides improve '
                               'reader value when they recommend genuine, high-quality '
                               'attractions. <strong>Glavani Park</strong> is a '
                               '1.5-hectare adventure and adrenaline park between '
                               '<strong>Barban</strong> and <strong>Vodnjan</strong>, '
                               '30 minutes from <strong>Pula</strong>, open daily '
                               '<strong>9 AM–5 PM</strong> (last entry <strong>3 '
                               'PM</strong>). Linking to us helps your audience plan '
                               'active days while supporting accurate information '
                               'across the web.</p>',
                               '<p>We welcome editorial links from anyone covering '
                               'Istria tourism, family travel, adventure sports, or '
                               'Croatia road trips. Please use the canonical English '
                               'URLs below and avoid misleading claims about pricing '
                               'or safety credentials not stated on our site.</p>']},
               {'h2': 'Canonical URLs',
                'paragraphs': ['<p>Use these primary URLs when linking to Glavani Park '
                               'content:</p>',
                               '<p><strong>Homepage (English):</strong> '
                               '<code>https://www.glavanipark.com/en/</code></p>',
                               '<p><strong>Things to Do in Istria:</strong> '
                               '<code>https://www.glavanipark.com/en/things-to-do-in-istria/</code></p>',
                               '<p><strong>Our Activities:</strong> '
                               '<code>https://www.glavanipark.com/en/adventure-park-croatia/</code></p>',
                               '<p><strong>Zipline Croatia:</strong> '
                               '<code>https://www.glavanipark.com/en/zipline-croatia/</code></p>',
                               '<p><strong>Team Building Istria:</strong> '
                               '<code>https://www.glavanipark.com/en/team-building-istria/</code></p>',
                               '<p><strong>Things to Do Near Pula:</strong> '
                               '<code>https://www.glavanipark.com/en/things-to-do-near-pula/</code></p>',
                               '<p><strong>Adventure Park Croatia:</strong> '
                               '<code>https://www.glavanipark.com/en/adventure-park-croatia/</code></p>',
                               '<p><strong>Safety:</strong> '
                               '<code>https://www.glavanipark.com/en/safety/</code></p>',
                               '<p><strong>Partners:</strong> '
                               '<code>https://www.glavanipark.com/en/partners/</code></p>']},
               {'h2': 'Suggested Anchor Text',
                'paragraphs': ['<p>Varied, natural anchor text helps search engines '
                               'and readers alike. Approved examples you may use:</p>',
                               '<p>• <strong>Glavani Park</strong> — brand link to '
                               'homepage<br>• <strong>adventure park in '
                               'Istria</strong> — homepage or adventure-park-croatia '
                               'page<br>• <strong>zipline near Pula</strong> — '
                               'zipline-croatia or things-to-do-near-pula<br>• '
                               '<strong>family activities in Istria</strong> — '
                               'adventure-park-croatia<br>• <strong>things to do in '
                               'Istria with kids</strong> — adventure-park-croatia or '
                               'things-to-do-in-istria<br>• <strong>team building '
                               'Istria</strong> — team-building-istria<br>• '
                               '<strong>birthday party venue Istria</strong> — '
                               'birthday-parties-istria<br>• <strong>school trip '
                               'adventure Croatia</strong> — school-trips-istria<br>• '
                               '<strong>outdoor activities near Barban and '
                               'Vodnjan</strong> — homepage or '
                               'things-to-do-near-pula</p>',
                               '<p>Avoid over-optimised repetition of identical anchor '
                               'text across dozens of pages. One contextual link per '
                               'article is usually sufficient.</p>']},
               {'h2': 'HTML Embed Codes',
                'paragraphs': ['<p><strong>Simple text link (homepage):</strong></p>',
                               '<p><code>&lt;a href="https://www.glavanipark.com/en/" '
                               'title="Glavani Park – Adventure Park Istria, '
                               'Croatia"&gt;Glavani Park – adventure park near Pula, '
                               'Barban &amp; Vodnjan&lt;/a&gt;</code></p>',
                               '<p><strong>Text link to zipline page:</strong></p>',
                               '<p><code>&lt;a '
                               'href="https://www.glavanipark.com/en/zipline-croatia/" '
                               'title="Zipline Croatia at Glavani Park '
                               'Istria"&gt;120-metre zipline at Glavani Park '
                               'Istria&lt;/a&gt;</code></p>',
                               '<p><strong>Text link to family '
                               'activities:</strong></p>',
                               '<p><code>&lt;a '
                               'href="https://www.glavanipark.com/en/adventure-park-croatia/" '
                               'title="Family activities Istria"&gt;Family activities '
                               'and high ropes near Pula&lt;/a&gt;</code></p>',
                               '<p><strong>Image link with alt text (replace image URL '
                               'with your hosted copy or request assets via <a '
                               'href="/en/partners/">partner '
                               'programme</a>):</strong></p>',
                               '<p><code>&lt;a '
                               'href="https://www.glavanipark.com/en/"&gt;&lt;img '
                               'src="https://www.glavanipark.com/images/glavani-park-adventure-istria-croatia.jpg" '
                               'alt="Glavani Park adventure and adrenaline park in '
                               'Istria, Croatia" width="600" height="400" '
                               'loading="lazy"&gt;&lt;/a&gt;</code></p>',
                               '<p><strong>Short recommendation box (copy into HTML '
                               'view):</strong></p>',
                               '<p><code>&lt;aside style="border-left:4px solid '
                               '#2d6a4f;padding:1rem '
                               '1.25rem;background:#f7faf8;"&gt;&lt;strong&gt;Glavani '
                               'Park&lt;/strong&gt; — ziplines, high ropes &amp; Human '
                               'Catapult near Pula. Open daily 9 AM–5 PM, last entry 3 '
                               'PM. Call &lt;a href="tel:+385918964525"&gt;+385 91 896 '
                               '4525&lt;/a&gt;. &lt;a '
                               'href="https://www.glavanipark.com/en/"&gt;Plan your '
                               'visit →&lt;/a&gt;&lt;/aside&gt;</code></p>']},
               {'h2': 'Attribution, Partners, and Contact',
                'paragraphs': ['<p>Hotels, campsites, and travel agencies with '
                               'commercial referral volume should join our formal <a '
                               'href="/en/partners/">partner programme</a> for '
                               'tracking codes and commission terms. Independent '
                               'bloggers may link freely using the snippets above — we '
                               'appreciate a brief mention that Glavani Park is near '
                               'Barban and Vodnjan with booking recommended on +385 91 '
                               '896 4525.</p>',
                               '<p>For high-resolution images, familiarisation visits, '
                               'or custom co-branded widgets, email <a '
                               'href="mailto:info@glavanipark.com">info@glavanipark.com</a> '
                               'or call <a href="tel:+385918964525">+385 91 896 '
                               '4525</a>. Correct NAP (name, address, phone) for '
                               'citations:</p>',
                               '<p><strong>Glavani Park</strong><br>Glavani 10, 52207 '
                               'Barban, Istria, Croatia<br>Phone: +385 91 896 '
                               '4525<br>Web: https://www.glavanipark.com/en/</p>',
                               '<p>Thank you for helping travellers discover one of '
                               "Istria's best outdoor adventures. Explore our content "
                               'hub starting with <a '
                               'href="/en/things-to-do-in-istria/">things to do in '
                               'Istria</a> and <a '
                               'href="/en/adventure-park-croatia/">adventure parks in '
                               'Croatia</a> for deeper linking opportunities.</p>',
                               '<p><strong>Structured citation block for directories '
                               '(plain text):</strong></p>',
                               '<p>Glavani Park — Adventure &amp; adrenaline park in '
                               'Istria, Croatia. Activities: high ropes (2 m / 6 m / '
                               '10 m), 120 m zipline, 12.5 m swing, Human Catapult, '
                               'Quick Jump, climbing wall. Address: Glavani 10, 52207 '
                               'Barban. Near Pula (30 min), Vodnjan (10 km), Barban (6 '
                               'km). Hours: daily 9 AM–5 PM, last entry 3 PM. Phone: '
                               '+385 91 896 4525. Website: '
                               'https://www.glavanipark.com/en/</p>',
                               '<p>When publishing listicles such as "Top 10 things to '
                               'do in Istria" or "Best day trips from Pula", a single '
                               'well-placed Glavani Park link with factual hours and '
                               'phone details adds genuine utility for readers '
                               'planning active family holidays — and signals to '
                               'search engines that your Istria content is '
                               'comprehensive and locally accurate.</p>',
                               '<p>If you maintain a Croatian-language site, link to '
                               '<code>https://www.glavanipark.com/hr/</code> for '
                               'domestic audiences while keeping English canonical '
                               'URLs for international travel guides. Either way, '
                               'preserving accurate opening hours (9 AM–5 PM, last '
                               'entry 3 PM) and the booking line +385 91 896 4525 '
                               'helps readers and supports fair representation of '
                               'Glavani Park across the web.</p>']}],
  'faqs': [{'q': 'May I use Glavani Park photos on my blog?',
            'a': 'Contact info@glavanipark.com or join the partner programme for '
                 'approved high-resolution images. Do not hotlink without permission '
                 'if your CMS allows local hosting instead.'},
           {'q': 'Do you offer affiliate commission?',
            'a': 'Commercial partners in hotels, campsites, and travel media may '
                 'receive referral tracking and commission. Apply via the partners '
                 'page or call +385 91 896 4525.'},
           {'q': 'Which page should I link for family travel content?',
            'a': 'Use https://www.glavanipark.com/en/adventure-park-croatia/ with '
                 "anchor text such as 'family activities in Istria' or 'things to do "
                 "near Pula with kids'."},
           {'q': 'Can I translate your link text into German or Italian?',
            'a': 'Yes for editorial context, but link to the English /en/ URLs unless '
                 'Croatian /hr/ pages are more appropriate for your audience. Keep '
                 'factual details (hours, phone) accurate.'}],
  'related': [{'slug': 'partners',
               'title': 'Partner Programme',
               'desc': 'Commission and co-marketing for accommodation'},
              {'slug': 'things-to-do-in-istria',
               'title': 'Things to Do in Istria',
               'desc': 'Editorial destination guide to link'},
              {'slug': 'adventure-park-croatia',
               'title': 'Adventure Parks in Croatia',
               'desc': 'Overview page for adventure travel blogs'},
              {'slug': 'things-to-do-near-pula',
               'title': 'Things to Do Near Pula',
               'desc': 'Pula-focused content for local guides'}]}]

