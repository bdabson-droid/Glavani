/**
 * Photo gallery carousel — horizontal scroll for event page galleries.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function scrollBehavior() {
    return prefersReducedMotion ? 'auto' : 'smooth';
  }

  function scrollToSlide(track, slide) {
    if (!slide) return;
    const trackRect = track.getBoundingClientRect();
    const slideRect = slide.getBoundingClientRect();
    track.scrollLeft += slideRect.left - trackRect.left;
  }

  document.querySelectorAll('[data-photo-gallery]').forEach((root) => {
    const track = root.querySelector('[data-gallery-track]');
    const prev = root.querySelector('[data-gallery-prev]');
    const next = root.querySelector('[data-gallery-next]');
    if (!track || !prev || !next) return;

    const slides = Array.from(track.querySelectorAll('.photo-gallery__slide'));
    if (slides.length) scrollToSlide(track, slides[0]);

    function scrollStep() {
      const slide = track.querySelector('.photo-gallery__slide');
      if (!slide) return track.clientWidth * 0.9;
      const gap = parseFloat(getComputedStyle(track).gap) || 16;
      return slide.offsetWidth + gap;
    }

    function scrollBy(direction) {
      track.scrollBy({ left: direction * scrollStep(), behavior: scrollBehavior() });
    }

    prev.addEventListener('click', () => scrollBy(-1));
    next.addEventListener('click', () => scrollBy(1));

    track.addEventListener('keydown', (e) => {
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
