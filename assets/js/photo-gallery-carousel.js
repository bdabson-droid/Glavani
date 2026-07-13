/**
 * Photo gallery carousel — horizontal scroll, YouTube slides, dots, and loop.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function scrollBehavior() {
    return prefersReducedMotion ? 'auto' : 'smooth';
  }

  function dotLabelPrefix() {
    var lang = (document.documentElement.lang || 'en').toLowerCase();
    return lang.indexOf('hr') === 0 ? 'Fotografija' : 'Photo';
  }

  function prepareGallery(root) {
    var viewport = root.querySelector('.photo-gallery__viewport');
    if (!viewport) {
      viewport = document.createElement('div');
      viewport.className = 'photo-gallery__viewport';
      var track = root.querySelector('[data-gallery-track]');
      var prev = root.querySelector('[data-gallery-prev]');
      var next = root.querySelector('[data-gallery-next]');
      root.insertBefore(viewport, track);
      if (prev) viewport.appendChild(prev);
      viewport.appendChild(track);
      if (next) viewport.appendChild(next);
    }

    var dots = root.querySelector('[data-gallery-dots]');
    if (!dots) {
      dots = document.createElement('div');
      dots.className = 'photo-gallery__dots';
      dots.setAttribute('data-gallery-dots', '');
      dots.setAttribute('role', 'tablist');
      viewport.appendChild(dots);
    } else if (dots.parentElement !== viewport) {
      viewport.appendChild(dots);
    }

    return { viewport: viewport, dots: dots };
  }

  function scrollToSlideInstant(track, slide) {
    if (!slide) return;
    track.scrollLeft = slide.offsetLeft;
  }

  function scrollToSlide(track, slide, behavior) {
    if (!slide) return;
    track.scrollTo({
      left: slide.offsetLeft,
      behavior: behavior || scrollBehavior(),
    });
  }

  function measureSlideHeight(slide, slideWidth) {
    var width = slideWidth || slide.offsetWidth || slide.getBoundingClientRect().width;
    var video = slide.querySelector('.photo-gallery__video');
    if (video) {
      var orientation = video.getAttribute('data-orientation') || 'portrait';
      return orientation === 'landscape' ? (width * 9) / 16 : (width * 16) / 9;
    }

    var img = slide.querySelector('img');
    if (img && img.naturalWidth > 0 && img.naturalHeight > 0) {
      return Math.round((width * img.naturalHeight) / img.naturalWidth);
    }

    return slide.offsetHeight;
  }

  function slideWidthForGallery(viewport, slides) {
    if (slides.length && slides[0].offsetWidth) return slides[0].offsetWidth;
    return viewport.clientWidth || viewport.getBoundingClientRect().width;
  }

  function cacheSlideHeights(viewport, slides) {
    var width = slideWidthForGallery(viewport, slides);
    return slides.map(function (slide) {
      return measureSlideHeight(slide, width);
    });
  }

  function heightForSlide(slide, realSlides, heights) {
    var clone = slide.getAttribute('data-clone');
    if (clone === 'first') return heights[0];
    if (clone === 'last') return heights[heights.length - 1];
    var realIndex = realSlides.indexOf(slide);
    if (realIndex >= 0) return heights[realIndex];
    return heights[0];
  }

  function activeSlideIndex(track, slides) {
    if (!slides.length) return 0;
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
    return activeIndex;
  }

  function realIndexFromAll(allSlides, index, looping) {
    if (!looping) return index;
    var slide = allSlides[index];
    var clone = slide.getAttribute('data-clone');
    if (clone === 'first') return 0;
    if (clone === 'last') return allSlides.length - 3;
    return index - 1;
  }

  function syncGalleryHeight(viewport, track, allSlides, realSlides, heights, looping) {
    if (!allSlides.length) return;
    heights = heights || cacheSlideHeights(viewport, realSlides);
    var trackRect = track.getBoundingClientRect();
    var center = trackRect.left + trackRect.width / 2;

    var activeIndex = 0;
    var activeDistance = Infinity;
    allSlides.forEach(function (slide, index) {
      var rect = slide.getBoundingClientRect();
      var slideCenter = rect.left + rect.width / 2;
      var distance = Math.abs(slideCenter - center);
      if (distance < activeDistance) {
        activeDistance = distance;
        activeIndex = index;
      }
    });

    var height = heightForSlide(allSlides[activeIndex], realSlides, heights);
    var activeSlide = allSlides[activeIndex];
    var activeRect = activeSlide.getBoundingClientRect();
    var activeCenter = activeRect.left + activeRect.width / 2;
    var neighborIndex = center < activeCenter ? activeIndex - 1 : activeIndex + 1;

    if (neighborIndex >= 0 && neighborIndex < allSlides.length) {
      var neighbor = allSlides[neighborIndex];
      var neighborRect = neighbor.getBoundingClientRect();
      var neighborCenter = neighborRect.left + neighborRect.width / 2;
      var span = Math.abs(neighborCenter - activeCenter);
      if (span > 0) {
        var progress = Math.min(1, Math.max(0, Math.abs(center - activeCenter) / span));
        var neighborHeight = heightForSlide(neighbor, realSlides, heights);
        height = height + (neighborHeight - height) * progress;
      }
    }

    viewport.style.height = Math.round(height) + 'px';
  }

  function setupInfiniteLoop(track, realSlides) {
    if (realSlides.length < 2) {
      return { allSlides: realSlides, looping: false };
    }

    var firstClone = realSlides[0].cloneNode(true);
    var lastClone = realSlides[realSlides.length - 1].cloneNode(true);
    firstClone.setAttribute('data-clone', 'first');
    lastClone.setAttribute('data-clone', 'last');
    firstClone.setAttribute('aria-hidden', 'true');
    lastClone.setAttribute('aria-hidden', 'true');

    track.insertBefore(lastClone, realSlides[0]);
    track.appendChild(firstClone);

    var allSlides = Array.from(track.querySelectorAll('.photo-gallery__slide'));
    return { allSlides: allSlides, looping: true };
  }

  function goToStart(track, allSlides, looping) {
    var startSlide = looping ? allSlides[1] : allSlides[0];
    void track.offsetWidth;
    scrollToSlideInstant(track, startSlide);
  }

  function wrapIfNeeded(track, allSlides, looping) {
    if (!looping) return;
    var index = activeSlideIndex(track, allSlides);
    var slide = allSlides[index];
    var clone = slide.getAttribute('data-clone');
    if (clone === 'first') {
      scrollToSlide(track, allSlides[1], 'auto');
    } else if (clone === 'last') {
      scrollToSlide(track, allSlides[allSlides.length - 2], 'auto');
    }
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
      if (slide.getAttribute('aria-hidden') === 'true') return;
      var wrap = slide.querySelector('[data-youtube-id]');
      if (wrap) deactivateVideo(wrap);
    });
  }

  document.querySelectorAll('[data-photo-gallery]').forEach(function (root) {
    var parts = prepareGallery(root);
    var viewport = parts.viewport;
    var dotsRoot = parts.dots;
    var track = root.querySelector('[data-gallery-track]');
    var prev = root.querySelector('[data-gallery-prev]');
    var next = root.querySelector('[data-gallery-next]');
    if (!track || !prev || !next) return;

    var realSlides = Array.from(track.querySelectorAll('.photo-gallery__slide'));
    if (!realSlides.length) return;

    var loopState = setupInfiniteLoop(track, realSlides);
    var allSlides = loopState.allSlides;
    var looping = loopState.looping;
    var heights = cacheSlideHeights(viewport, realSlides);
    var labelPrefix = dotLabelPrefix();
    var activeRealIndex = 0;

    function updateDots() {
      var dots = dotsRoot.querySelectorAll('.photo-gallery__dot');
      dots.forEach(function (dot, i) {
        var active = i === activeRealIndex;
        dot.classList.toggle('is-active', active);
        dot.setAttribute('aria-selected', active ? 'true' : 'false');
        dot.setAttribute('tabindex', active ? '0' : '-1');
      });
    }

    function refreshState(wrap) {
      if (wrap) wrapIfNeeded(track, allSlides, looping);
      activeRealIndex = realIndexFromAll(allSlides, activeSlideIndex(track, allSlides), looping);
      syncGalleryHeight(viewport, track, allSlides, realSlides, heights, looping);
      updateDots();
    }

    function remeasure(wrap) {
      heights = cacheSlideHeights(viewport, realSlides);
      refreshState(wrap);
    }

    function bindGalleryHeight() {
      var ticking = false;
      goToStart(track, allSlides, looping);
      activeRealIndex = 0;
      updateDots();
      syncGalleryHeight(viewport, track, allSlides, realSlides, heights, looping);

      realSlides.forEach(function (slide) {
        slide.querySelectorAll('img').forEach(function (img) {
          if (img.complete) return;
          img.addEventListener('load', function () {
            remeasure(false);
          }, { once: true });
        });
      });

      track.addEventListener(
        'scroll',
        function () {
          if (ticking) return;
          ticking = true;
          requestAnimationFrame(function () {
            activeRealIndex = realIndexFromAll(
              allSlides,
              activeSlideIndex(track, allSlides),
              looping
            );
            syncGalleryHeight(viewport, track, allSlides, realSlides, heights, looping);
            updateDots();
            ticking = false;
          });
        },
        { passive: true }
      );

      var settleTimer;
      function onScrollSettled() {
        clearTimeout(settleTimer);
        settleTimer = setTimeout(function () {
          stopVideosExceptSlide(root, allSlides[activeSlideIndex(track, allSlides)]);
          refreshState(true);
        }, 80);
      }

      if ('onscrollend' in window) {
        track.addEventListener('scrollend', onScrollSettled);
      } else {
        track.addEventListener('scroll', onScrollSettled, { passive: true });
      }

      window.addEventListener('resize', function () {
        var index = activeSlideIndex(track, allSlides);
        heights = cacheSlideHeights(viewport, realSlides);
        scrollToSlideInstant(track, allSlides[index]);
        activeRealIndex = realIndexFromAll(allSlides, index, looping);
        syncGalleryHeight(viewport, track, allSlides, realSlides, heights, looping);
        updateDots();
      }, { passive: true });

      requestAnimationFrame(function () {
        goToStart(track, allSlides, looping);
        activeRealIndex = 0;
        updateDots();
        syncGalleryHeight(viewport, track, allSlides, realSlides, heights, looping);
      });
    }

    dotsRoot.replaceChildren();
    if (realSlides.length > 1) {
      realSlides.forEach(function (_, i) {
        var dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'photo-gallery__dot';
        dot.setAttribute('role', 'tab');
        dot.setAttribute('aria-label', labelPrefix + ' ' + (i + 1));
        dot.addEventListener('click', function () {
          stopVideosExceptSlide(root, null);
          var target = looping ? allSlides[i + 1] : allSlides[i];
          scrollToSlide(track, target, scrollBehavior());
        });
        dotsRoot.appendChild(dot);
      });
    }

    bindGalleryHeight();

    root.addEventListener('click', function (event) {
      var button = event.target.closest('.photo-gallery__video-play');
      if (!button || !root.contains(button)) return;
      var slide = button.closest('.photo-gallery__slide');
      if (slide && slide.getAttribute('aria-hidden') === 'true') return;

      var wrap = button.closest('[data-youtube-id]');
      if (!wrap || wrap.querySelector('iframe')) return;

      stopVideosExceptSlide(root, slide);

      var videoId = wrap.getAttribute('data-youtube-id');
      var label = button.getAttribute('aria-label') || 'YouTube video';
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&rel=0&enablejsapi=1';
      iframe.title = label;
      iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
      iframe.setAttribute('allowfullscreen', '');
      iframe.setAttribute('loading', 'lazy');
      iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
      wrap.replaceChildren(iframe);
      remeasure(false);
    });

    function goBy(direction) {
      stopVideosExceptSlide(root, null);
      var index = activeSlideIndex(track, allSlides);
      var target = allSlides[index + direction];
      if (target) {
        scrollToSlide(track, target, scrollBehavior());
        return;
      }
      if (!looping) return;
      if (direction > 0) {
        scrollToSlide(track, allSlides[allSlides.length - 1], scrollBehavior());
      } else {
        scrollToSlide(track, allSlides[0], scrollBehavior());
      }
    }

    prev.addEventListener('click', function () {
      goBy(-1);
    });
    next.addEventListener('click', function () {
      goBy(1);
    });

    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        goBy(-1);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        goBy(1);
      }
    });

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.target.getAttribute('aria-hidden') === 'true') return;
            if (entry.isIntersecting && entry.intersectionRatio >= 0.55) return;
            var wrap = entry.target.querySelector('[data-youtube-id]');
            if (wrap) deactivateVideo(wrap);
          });
        },
        { root: track, threshold: [0, 0.25, 0.55, 0.75, 1] }
      );
      allSlides.forEach(function (slide) {
        observer.observe(slide);
      });
    }
  });
})();
