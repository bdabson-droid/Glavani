/**
 * Horizontal reviews carousel — shuffle on each visit, scroll left/right.
 */
(function () {
  function shuffleCards(track) {
    const cards = Array.from(track.querySelectorAll('.review-card'));
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    cards.forEach((card) => track.appendChild(card));
    return cards;
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

    const cards = shuffleCards(track);
    const start = cards[Math.floor(Math.random() * cards.length)];
    scrollToCard(track, start);

    function scrollStep() {
      const card = track.querySelector('.review-card');
      if (!card) return track.clientWidth * 0.85;
      const gap = parseFloat(getComputedStyle(track).gap) || 16;
      return card.offsetWidth + gap;
    }

    function scrollBy(direction) {
      track.scrollBy({ left: direction * scrollStep(), behavior: 'smooth' });
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
