/**
 * Photo gallery carousel — horizontal scroll with optional YouTube video slides.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function scrollBehavior() {
    return prefersReducedMotion ? 'auto' : 'smooth';
  }

  function scrollToSlide(track, slide) {
    if (!slide) return;
    var trackRect = track.getBoundingClientRect();
    var slideRect = slide.getBoundingClientRect();
    track.scrollLeft += slideRect.left - trackRect.left;
  }

  function activateVideo(playButton) {
    var wrap = playButton.closest('[data-youtube-id]');
    if (!wrap || wrap.querySelector('iframe')) return;

    var videoId = wrap.getAttribute('data-youtube-id');
    var label = playButton.getAttribute('aria-label') || 'YouTube video';
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&rel=0';
    iframe.title = label;
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('loading', 'lazy');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    wrap.replaceChildren(iframe);
  }

  document.querySelectorAll('[data-photo-gallery]').forEach(function (root) {
    var track = root.querySelector('[data-gallery-track]');
    var prev = root.querySelector('[data-gallery-prev]');
    var next = root.querySelector('[data-gallery-next]');
    if (!track || !prev || !next) return;

    var slides = Array.from(track.querySelectorAll('.photo-gallery__slide'));
    if (slides.length) scrollToSlide(track, slides[0]);

    root.querySelectorAll('.photo-gallery__video-play').forEach(function (button) {
      button.addEventListener('click', function () {
        activateVideo(button);
      });
    });

    function scrollStep() {
      var slide = track.querySelector('.photo-gallery__slide');
      if (!slide) return track.clientWidth * 0.9;
      var gap = parseFloat(getComputedStyle(track).gap) || 16;
      return slide.offsetWidth + gap;
    }

    function scrollBy(direction) {
      track.scrollBy({ left: direction * scrollStep(), behavior: scrollBehavior() });
    }

    prev.addEventListener('click', function () {
      scrollBy(-1);
    });
    next.addEventListener('click', function () {
      scrollBy(1);
    });

    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        scrollBy(-1);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        scrollBy(1);
      }
    });
  });
})();
