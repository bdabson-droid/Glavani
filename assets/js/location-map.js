(function () {
  var PARK = { lat: 45.021389, lng: 13.951111, en: "Glavani Park", hr: "Glavani Park" };

  // Used only to frame southern Istria (no markers shown for these towns).
  var VIEW_BOUNDS = [
    [45.0475, 14.0147],
    [44.9597, 13.8492],
    [44.8666, 13.8496],
    [45.0812, 13.6387],
    [PARK.lat, PARK.lng],
  ];

  function init() {
    var container = document.getElementById("istria-map");
    if (!container || typeof L === "undefined") return;

    var lang = container.getAttribute("data-lang") || "en";
    var label = PARK[lang] || PARK.en;
    var map = L.map(container, {
      scrollWheelZoom: true,
      tap: true,
      zoomControl: true,
    });

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 18,
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);

    var pinIcon = L.divIcon({
      className: "istria-map__pin",
      html: '<span aria-hidden="true">📍</span>',
      iconSize: [36, 36],
      iconAnchor: [18, 34],
      popupAnchor: [0, -30],
    });

    L.marker([PARK.lat, PARK.lng], { icon: pinIcon })
      .addTo(map)
      .bindPopup("<strong>" + label + "</strong>");

    map.fitBounds(VIEW_BOUNDS, { padding: [36, 36], maxZoom: 10 });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
