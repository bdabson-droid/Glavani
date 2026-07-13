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

  function trackPadding(track) {
    var styles = getComputedStyle(track);
    return (parseFloat(styles.paddingTop) || 0) + (parseFloat(styles.paddingBottom) || 0);
  }

  function measureSlideHeight(slide) {
    var video = slide.querySelector('.photo-gallery__video');
    if (video) {
      var width = slide.offsetWidth || slide.getBoundingClientRect().width;
      var orientation = video.getAttribute('data-orientation') || 'portrait';
      return orientation === 'landscape' ? (width * 9) / 16 : (width * 16) / 9;
    }

    var img = slide.querySelector('img');
    var width = slide.offsetWidth || slide.getBoundingClientRect().width;
    if (img && img.naturalWidth > 0 && img.naturalHeight > 0) {
      return Math.round((width * img.naturalHeight) / img.naturalWidth);
    }

    return slide.offsetHeight;
  }

  function cacheSlideHeights(slides) {
    return slides.map(measureSlideHeight);
  }

  function syncTrackHeight(track, slides, heights) {
    if (!slides.length) return;
    heights = heights || cacheSlideHeights(slides);
    var padding = trackPadding(track);
    var trackRect = track.getBoundingClientRect();
    var center = trackRect.left + trackRect.width / 2;

    var activeIndex = 0;
    var activeDistance = Infinity;
    slides.forEach(function (slide, index) {
      var rect = slide.getBoundingClientRect();
      var slideCenter = rect.left + rect.width / 2;
      var distance = Math.abs(slideCenter - center);
      if (distance < activeDistance) {
        activeDistance = distance;
        activeIndex = index;
      }
    });

    var height = heights[activeIndex];
    var activeSlide = slides[activeIndex];
    var activeRect = activeSlide.getBoundingClientRect();
    var activeCenter = activeRect.left + activeRect.width / 2;
    var neighborIndex = center < activeCenter ? activeIndex - 1 : activeIndex + 1;

    if (neighborIndex >= 0 && neighborIndex < slides.length) {
      var neighbor = slides[neighborIndex];
      var neighborRect = neighbor.getBoundingClientRect();
      var neighborCenter = neighborRect.left + neighborRect.width / 2;
      var span = Math.abs(neighborCenter - activeCenter);
      if (span > 0) {
        var progress = Math.min(1, Math.max(0, Math.abs(center - activeCenter) / span));
        height = heights[activeIndex] + (heights[neighborIndex] - heights[activeIndex]) * progress;
      }
    }

    track.style.height = Math.round(height + padding) + 'px';
  }

  function bindTrackHeight(track, slides) {
    var heights = cacheSlideHeights(slides);
    var sync = function () {
      syncTrackHeight(track, slides, heights);
    };
    var ticking = false;

    function remeasure() {
      heights = cacheSlideHeights(slides);
      sync();
    }

    sync();
    slides.forEach(function (slide) {
      slide.querySelectorAll('img').forEach(function (img) {
        if (img.complete) return;
        img.addEventListener('load', remeasure, { once: true });
      });
    });

    track.addEventListener(
      'scroll',
      function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
          syncTrackHeight(track, slides, heights);
          ticking = false;
        });
      },
      { passive: true }
    );

    window.addEventListener('resize', remeasure, { passive: true });
    return sync;
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
    var track = wrap.closest('[data-gallery-track]');
    if (track) {
      var slides = Array.from(track.querySelectorAll('.photo-gallery__slide'));
      syncTrackHeight(track, slides, cacheSlideHeights(slides));
    }
  }

  document.querySelectorAll('[data-photo-gallery]').forEach(function (root) {
    var track = root.querySelector('[data-gallery-track]');
    var prev = root.querySelector('[data-gallery-prev]');
    var next = root.querySelector('[data-gallery-next]');
    if (!track || !prev || !next) return;

    var slides = Array.from(track.querySelectorAll('.photo-gallery__slide'));
    var syncHeight = bindTrackHeight(track, slides);
    if (slides.length) {
      scrollToSlide(track, slides[0]);
      syncHeight();
    }

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
