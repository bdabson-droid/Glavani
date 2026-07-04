(function () {
  var TOWNS = [
    { lat: 45.021389, lng: 13.951111, en: "Glavani Park", hr: "Glavani Park", primary: true },
    { lat: 45.0475, lng: 14.0147, en: "Barban", hr: "Barban" },
    { lat: 44.9597, lng: 13.8492, en: "Vodnjan", hr: "Vodnjan" },
    { lat: 44.8666, lng: 13.8496, en: "Pula", hr: "Pula" },
    { lat: 45.0812, lng: 13.6387, en: "Rovinj", hr: "Rovinj" },
  ];

  function init() {
    var container = document.getElementById("istria-map");
    if (!container || typeof L === "undefined") return;

    var lang = container.getAttribute("data-lang") || "en";
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

    var bounds = [];
    TOWNS.forEach(function (town) {
      var label = town[lang] || town.en;
      var marker;
      if (town.primary) {
        marker = L.circleMarker([town.lat, town.lng], {
          radius: 11,
          color: "#b91c1c",
          fillColor: "#dc2626",
          fillOpacity: 1,
          weight: 3,
        });
      } else {
        marker = L.circleMarker([town.lat, town.lng], {
          radius: 7,
          color: "#1a3d2e",
          fillColor: "#fbbf24",
          fillOpacity: 1,
          weight: 2,
        });
      }
      marker.addTo(map).bindPopup("<strong>" + label + "</strong>");
      bounds.push([town.lat, town.lng]);
    });

    map.fitBounds(bounds, { padding: [36, 36], maxZoom: 10 });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
