/**
 * GitHub Pages preview — keep booking links on the preview host.
 * www.glavanipark.com/en/book/ still hits the old IIS site (poruka.asp).
 */
(function () {
  var meta = document.querySelector('meta[name="glavani-preview-base"]');
  if (!meta) return;

  var previewBase = meta.content.replace(/\/$/, '');
  var enBook = previewBase + '/en/book/';
  var hrBook = previewBase + '/hr/rezervacija/';
  var prodHost = 'glavanipark.com';

  function isBookingControl(el) {
    return (
      el.classList.contains('btn-book-now') ||
      el.classList.contains('btn-book-tickets') ||
      el.classList.contains('site-nav__cta') ||
      el.classList.contains('price-list__book-btn') ||
      el.classList.contains('btn-primary--large') ||
      el.hasAttribute('data-book-package')
    );
  }

  function bookingTarget(el, href) {
    var h = (href || '').toLowerCase();
    if (h.indexOf('/hr/') !== -1 || h.indexOf('rezervacija') !== -1) return hrBook;
    if (location.pathname.indexOf('/hr/') !== -1 && h.indexOf('/en/') === -1) return hrBook;
    return enBook;
  }

  function isBrokenBookingHref(href) {
    if (!href) return false;
    var h = href.trim();
    if (h.indexOf(prodHost) !== -1) return true;
    if (h === 'book/' || h === '../book/' || h === './book/') return true;
    if (h === 'rezervacija/' || h === '../rezervacija/' || h === './rezervacija/') return true;
    if (/^\/?en\/book\/?(\?|#|$)/.test(h)) return h.indexOf('github.io') === -1;
    if (/^\/?hr\/rezervacija\/?(\?|#|$)/.test(h)) return h.indexOf('github.io') === -1;
    if (/^\/?en\/upit\/?(\?|#|$)/.test(h)) return true;
    if (/^\/?hr\/upit\/?(\?|#|$)/.test(h)) return true;
    return false;
  }

  function shouldFix(el, href) {
    if (!isBrokenBookingHref(href)) return false;
    if (isBookingControl(el)) return true;
    return /book|rezervacija|upit/i.test(href);
  }

  function fixLinks() {
    document.querySelectorAll('a[href]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!shouldFix(a, href)) return;
      a.setAttribute('href', bookingTarget(a, href));
    });
  }

  document.addEventListener(
    'click',
    function (e) {
      var a = e.target.closest('a');
      if (!a) return;
      var href = a.getAttribute('href') || '';
      if (!shouldFix(a, href)) return;
      e.preventDefault();
      location.href = bookingTarget(a, href);
    },
    true
  );

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fixLinks);
  } else {
    fixLinks();
  }
})();
