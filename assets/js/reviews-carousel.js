/**
 * Reviews carousel — show all TripAdvisor reviews, newest first, horizontal scroll.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function scrollBehavior() {
    return prefersReducedMotion ? 'auto' : 'smooth';
  }

  function scrollToCard(track, card) {
    if (!card) return;
    const trackRect = track.getBoundingClientRect();
    const cardRect = card.getBoundingClientRect();
    track.scrollLeft += cardRect.left - trackRect.left;
  }

  document.querySelectorAll('[data-reviews-carousel]').forEach((root) => {
    const track = root.querySelector('[data-reviews-track]');
    const prev = root.querySelector('[data-reviews-prev]');
    const next = root.querySelector('[data-reviews-next]');
    if (!track || !prev || !next) return;

    const cards = Array.from(track.querySelectorAll('.review-card'));
    cards.sort((a, b) => (b.dataset.reviewDate || '').localeCompare(a.dataset.reviewDate || ''));
    cards.forEach((card) => track.appendChild(card));
    scrollToCard(track, cards[0]);

    function scrollStep() {
      const card = track.querySelector('.review-card');
      if (!card) return track.clientWidth * 0.85;
      const gap = parseFloat(getComputedStyle(track).gap) || 16;
      return card.offsetWidth + gap;
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
