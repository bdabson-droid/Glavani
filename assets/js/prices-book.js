/**
 * Prices & activities pages — guest stepper (1–10) and booking prefill.
 */
(function () {
  const STORAGE_KEY = 'glavani-book-prefill';
  const MAX_GUESTS = 10;
  const DEFAULT_GUESTS = 1;

  function getItem(el) {
    return el.closest('.price-list__item');
  }

  function readGuests(item) {
    const n = parseInt(item.dataset.guests || String(DEFAULT_GUESTS), 10);
    if (Number.isNaN(n)) return DEFAULT_GUESTS;
    return Math.min(MAX_GUESTS, Math.max(1, n));
  }

  function writeGuests(item, guests) {
    const count = Math.min(MAX_GUESTS, Math.max(1, guests));
    item.dataset.guests = String(count);
    const valueEl = item.querySelector('[data-qty-value]');
    const minus = item.querySelector('[data-qty-minus]');
    const plus = item.querySelector('[data-qty-plus]');
    if (valueEl) valueEl.textContent = String(count);
    if (minus) minus.disabled = count <= 1;
    if (plus) plus.disabled = count >= MAX_GUESTS;
    return count;
  }

  function initItems() {
    document.querySelectorAll('.price-list__item').forEach((item) => {
      if (!item.querySelector('[data-book-package]')) return;
      writeGuests(item, readGuests(item));
    });
  }

  document.addEventListener('click', (e) => {
    const minus = e.target.closest('[data-qty-minus]');
    if (minus) {
      e.preventDefault();
      const item = getItem(minus);
      if (item) writeGuests(item, readGuests(item) - 1);
      return;
    }

    const plus = e.target.closest('[data-qty-plus]');
    if (plus) {
      e.preventDefault();
      const item = getItem(plus);
      if (item) writeGuests(item, readGuests(item) + 1);
      return;
    }

    const book = e.target.closest('[data-book-package]');
    if (!book) return;

    const packageId = book.dataset.bookPackage;
    const item = getItem(book);
    if (!packageId || !item) return;

    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify({
        package: packageId,
        guests: readGuests(item),
      }));
    } catch (err) {
      /* ignore */
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initItems);
  } else {
    initItems();
  }
})();
