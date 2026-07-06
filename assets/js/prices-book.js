/**
 * Prices page — store selected package before navigating to the booking app.
 */
(function () {
  const STORAGE_KEY = 'glavani-book-prefill';

  document.querySelectorAll('[data-book-package]').forEach((link) => {
    link.addEventListener('click', () => {
      const packageId = link.dataset.bookPackage;
      if (!packageId) return;
      try {
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify({ package: packageId }));
      } catch (e) {
        /* ignore */
      }
    });
  });
})();
