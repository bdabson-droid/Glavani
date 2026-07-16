"""
Old CMS URL → new static site redirects for glavanipark.com migration.

Used to generate:
- Client-side redirect script in 404.html (GitHub Pages fallback)
- _redirects for Cloudflare Pages / Netlify (true HTTP 301 at cutover)
"""

from __future__ import annotations

# Exact pathname matches (no trailing slash). Checked before prefix rules.
EXACT_REDIRECTS: dict[str, str] = {
    "/": "/hr/",
    "/hr": "/hr/",
    "/en": "/en/",
    "/de": "/en/",
    "/it": "/en/",
    "/ru": "/en/",
    "/nl": "/en/",
    "/hr/avantura/2": "/hr/avanturisticki-park-hrvatska/",
    "/hr/adventure/2": "/hr/avanturisticki-park-hrvatska/",
    "/hr/aktivnosti/3": "/hr/avanturisticki-park-hrvatska/",
    "/en/adventure/2": "/en/adventure-park-croatia/",
    "/en/activities/3": "/en/adventure-park-croatia/",
    "/hr/cjenik/13": "/hr/cijene/",
    "/en/prices/13": "/en/prices/",
    "/hr/lokacija/5": "/hr/sto-raditi-kod-pule/#location-map",
    "/en/location/5": "/en/things-to-do-near-pula/#location-map",
    "/hr/o_nama/6": "/hr/",
    "/en/about_us/6": "/en/",
    "/hr/partneri/64/12": "/hr/partneri/",
    "/en/partners/64/12": "/en/partners/",
    "/hr/poklon_bon/4": "/hr/cijene/",
    "/hr/gift_card/4": "/hr/cijene/",
    "/en/gift_card/4": "/en/prices/",
    "/en/gift_voucher/4": "/en/prices/",
    "/hr/upit": "/hr/rezervacija/",
    "/en/upit": "/en/reservation/",
    "/en/book": "/en/reservation/",
    "/hr/blog/7": "/hr/",
    "/en/blog/7": "/en/",
    "/hr/galerija": "/hr/avanturisticki-park-hrvatska/",
    "/en/galerija": "/en/adventure-park-croatia/",
    "/hr/naslovna/10": "/hr/",
    "/en/naslovna/10": "/en/",
    "/hr/glavani_park_tim/9": "/hr/partneri/",
    "/en/the_glavani_crew/9": "/en/partners/",
    "/hr/osoblje/9/10": "/hr/partneri/",
    "/en/staff/9/10": "/en/partners/",
    "/hr/izjava_o_privatnosti/5/8": "/hr/pravila-privatnosti/",
    "/hr/izvaja_o_privatnosti/5/8": "/hr/pravila-privatnosti/",
    "/en/izjava_o_privatnosti/5/8": "/en/privacy-policy/",
    "/en/izvaja_o_privatnosti/5/8": "/en/privacy-policy/",
    "/hr/opci_uvjeti_koristenja/6/8": "/hr/uvjeti-koristenja/",
    "/en/opci_uvjeti_koristenja/6/8": "/en/terms-of-use/",
    "/hr/reklamacije_i_povrati/7/8": "/hr/cesta-pitanja/",
    "/en/reklamacije_i_povrati/7/8": "/en/faq/",
    "/hr/jedinstveno_okruzenje_u_centru_istre/11/10": "/hr/avanturisticki-park-hrvatska/",
    "/en/ready_to_feel_some_adrenaline/11/10": "/en/adventure-park-croatia/",
    "/hr/staze_za_sve_uzraste/1/3": "/hr/trening-ruta/",
    "/en/routes_for_all_ages/1/3": "/en/training-route/",
    "/hr/team_building_program/57/3": "/hr/team-building-istri/",
    "/en/team_building_program/57/3": "/en/team-building-istria/",
    "/hr/rodendani_u_glavani_parku/47/2": "/hr/rodjendanske-zabave-istri/",
    "/hr/rodendani_u_glavani_parku/44/3": "/hr/rodjendanske-zabave-istri/",
    "/en/birthdays_in_glavani_park/47/2": "/en/birthday-parties-istria/",
    "/en/birthdays_in_glavani_park/44/3": "/en/birthday-parties-istria/",
}

# Prefix matches (pathname lowercased, no trailing slash). Longest prefixes first.
# Only use prefixes that cannot match new-site slugs (underscore CMS paths).
PREFIX_REDIRECTS: list[tuple[str, str]] = [
    ("/hr/ljudski_katapult", "/hr/ljudska-katapulta/"),
    ("/en/human_catapult", "/en/human-catapult/"),
    ("/hr/12_", "/hr/visoka-ljuljacka/"),
    ("/en/giant_swing", "/en/high-swing/"),
    ("/hr/zuta_staza", "/hr/trening-ruta/"),
    ("/en/yellow_route", "/en/training-route/"),
    ("/hr/quick_jump", "/hr/pad-s-20m/"),
    ("/en/quick_jump", "/en/20m-drop/"),
    ("/hr/stijena_za_penjanje", "/hr/penjacki-zid/"),
    ("/en/climbing_wall", "/en/climbing-wall/"),
    ("/hr/most_s_monociklom", "/hr/most-s-monociklom/"),
    ("/en/devils_causeway", "/en/devils-causeway/"),
    ("/hr/nevenko_bulic", "/hr/partneri/"),
    ("/hr/nigel_simpson", "/hr/partneri/"),
    ("/en/nevenko_bulic", "/en/partners/"),
    ("/en/nigel_simpson", "/en/partners/"),
    ("/hr/g/nevenko_bulic", "/hr/partneri/"),
    ("/en/g/nevenko_bulic", "/en/partners/"),
    ("/hr/rodendani", "/hr/rodjendanske-zabave-istri/"),
    ("/en/birthdays_in_glavani", "/en/birthday-parties-istria/"),
    ("/hr/team_building", "/hr/team-building-istri/"),
    ("/en/team_building", "/en/team-building-istria/"),
    ("/hr/cjenik", "/hr/cijene/"),
    ("/hr/lokacija", "/hr/sto-raditi-kod-pule/#location-map"),
    ("/en/location", "/en/things-to-do-near-pula/#location-map"),
    ("/hr/o_nama", "/hr/"),
    ("/en/about_us", "/en/"),
    ("/hr/poklon_bon", "/hr/cijene/"),
    ("/hr/gift_card", "/hr/cijene/"),
    ("/en/gift_card", "/en/prices/"),
    ("/en/gift_voucher", "/en/prices/"),
    ("/de/", "/en/"),
    ("/it/", "/en/"),
    ("/ru/", "/en/"),
    ("/nl/", "/en/"),
]


def render_redirect_script() -> str:
    """Inline script for 404.html — runs before paint to redirect legacy URLs."""
    exact_items = ",\n    ".join(f'"{k}": "{v}"' for k, v in sorted(EXACT_REDIRECTS.items()))
    prefix_items = ",\n    ".join(f'"{k}": "{v}"' for k, v in PREFIX_REDIRECTS)
    return f"""<script>
(function () {{
  var exact = {{
    {exact_items}
  }};
  var prefixes = [
{chr(10).join(f'    ["{k}", "{v}"],' for k, v in PREFIX_REDIRECTS)}
  ];
  var path = location.pathname.replace(/\\/+$/,'') || '/';
  path = path.toLowerCase();
  var target = exact[path];
  if (!target) {{
    for (var i = 0; i < prefixes.length; i++) {{
      if (path === prefixes[i][0] || path.indexOf(prefixes[i][0]) === 0) {{
        target = prefixes[i][1];
        break;
      }}
    }}
  }}
  if (target) {{
    location.replace(target);
  }}
}})();
</script>"""


def render_redirects_file() -> str:
    """Cloudflare Pages / Netlify _redirects (HTTP 301 at edge)."""
    import re

    lines = [
        "# Glavani Park CMS → static site migration redirects",
        "# Deploy with Cloudflare Pages or Netlify for true 301 responses.",
        "# GitHub Pages alone uses the 404.html client-side fallback.",
        "",
    ]
    lang_roots = {"/en", "/hr", "/de", "/it", "/ru", "/nl"}
    for old, new in sorted(EXACT_REDIRECTS.items()):
        if old == "/":
            lines.append(f"/  {new}  301")
            continue
        lines.append(f"{old}  {new}  301")
        if old not in lang_roots and re.search(r"/\d+", old):
            lines.append(f"{old}/*  {new}  301")
    seen_prefixes: set[str] = set()
    for prefix, target in PREFIX_REDIRECTS:
        if prefix in seen_prefixes:
            continue
        seen_prefixes.add(prefix)
        wildcard = prefix if prefix.endswith("/") else f"{prefix}*"
        lines.append(f"{wildcard}  {target}  301")
    return "\n".join(lines) + "\n"
