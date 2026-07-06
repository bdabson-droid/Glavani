/**
 * Prices page — guest stepper (1–10) and package prefill for the booking app.
 */
(function () {
  const STORAGE_KEY = 'glavani-book-prefill';
  const MAX_GUESTS = 10;
  const DEFAULT_GUESTS = 1;

  document.querySelectorAll('.price-list__item').forEach((item) => {
    const link = item.querySelector('[data-book-package]');
    const minus = item.querySelector('[data-qty-minus]');
    const plus = item.querySelector('[data-qty-plus]');
    const valueEl = item.querySelector('[data-qty-value]');
    const packageId = link?.dataset.bookPackage;
    if (!link || !minus || !plus || !valueEl || !packageId) return;

    let guests = DEFAULT_GUESTS;

    function updateQty() {
      valueEl.textContent = String(guests);
      minus.disabled = guests <= 1;
      plus.disabled = guests >= MAX_GUESTS;
    }

    minus.addEventListener('click', () => {
      if (guests > 1) {
        guests -= 1;
        updateQty();
      }
    });

    plus.addEventListener('click', () => {
      if (guests < MAX_GUESTS) {
        guests += 1;
        updateQty();
      }
    });

    link.addEventListener('click', () => {
      try {
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify({
          package: packageId,
          guests: guests,
        }));
      } catch (e) {
        /* ignore */
      }
    });

    updateQty();
  });
})();
