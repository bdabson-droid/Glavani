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

  function buildPlayButton(wrap) {
    var videoId = wrap.getAttribute('data-youtube-id');
    var title = wrap.getAttribute('data-video-title') || 'YouTube video';
    var label = wrap.getAttribute('data-play-label') || ('Play video: ' + title);
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'photo-gallery__video-play';
    button.setAttribute('aria-label', label);
    var img = document.createElement('img');
    img.src = 'https://i.ytimg.com/vi/' + videoId + '/hqdefault.jpg';
    img.alt = title;
    img.width = 800;
    img.height = 450;
    img.loading = 'lazy';
    var icon = document.createElement('span');
    icon.className = 'photo-gallery__video-icon';
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = '▶';
    button.appendChild(img);
    button.appendChild(icon);
    return button;
  }

  function deactivateVideo(wrap) {
    if (!wrap || !wrap.querySelector('iframe')) return;
    wrap.replaceChildren(buildPlayButton(wrap));
  }

  function stopVideosExceptSlide(root, activeSlide) {
    root.querySelectorAll('.photo-gallery__slide--video').forEach(function (slide) {
      if (slide === activeSlide) return;
      var wrap = slide.querySelector('[data-youtube-id]');
      if (wrap) deactivateVideo(wrap);
    });
  }

  function activateVideo(playButton) {
    var wrap = playButton.closest('[data-youtube-id]');
    if (!wrap || wrap.querySelector('iframe')) return;

    var root = wrap.closest('[data-photo-gallery]');
    var slide = wrap.closest('.photo-gallery__slide');
    if (root) stopVideosExceptSlide(root, slide);

    var videoId = wrap.getAttribute('data-youtube-id');
    var label = playButton.getAttribute('aria-label') || 'YouTube video';
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&rel=0&enablejsapi=1';
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

    root.addEventListener('click', function (event) {
      var button = event.target.closest('.photo-gallery__video-play');
      if (button && root.contains(button)) activateVideo(button);
    });

    function scrollStep() {
      var slide = track.querySelector('.photo-gallery__slide');
      if (!slide) return track.clientWidth * 0.9;
      var gap = parseFloat(getComputedStyle(track).gap) || 16;
      return slide.offsetWidth + gap;
    }

    function scrollBy(direction) {
      stopVideosExceptSlide(root, null);
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

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting && entry.intersectionRatio >= 0.55) return;
            var wrap = entry.target.querySelector('[data-youtube-id]');
            if (wrap) deactivateVideo(wrap);
          });
        },
        { root: track, threshold: [0, 0.25, 0.55, 0.75, 1] }
      );
      slides.forEach(function (slide) {
        observer.observe(slide);
      });
    } else {
      var scrollTimer;
      track.addEventListener(
        'scroll',
        function () {
          clearTimeout(scrollTimer);
          scrollTimer = setTimeout(function () {
            stopVideosExceptSlide(root, null);
          }, 150);
        },
        { passive: true }
      );
    }
  });
})();
