/**
 * DeepAbi — Common JS
 * Shared across every page: navbar scroll behavior (hide on scroll down,
 * show on scroll up, solid after scroll), mobile menu, scroll-reveal,
 * animated counters, and footer year. Page-specific behavior lives in
 * js/pages/*.js and is loaded after this file.
 */

document.addEventListener('DOMContentLoaded', () => {
  setFooterYear();
  initNavbar();
  initMobileMenu();
  initReveal();
  initCounters();
  initContactFab();
  initServicesMenu();
  initMobileServices();
});

function setFooterYear() {
  const el = document.getElementById('year');
  if (el) el.textContent = new Date().getFullYear();
}

/* ---------- Navbar: solid after scroll, hide on scroll down / show on scroll up ---------- */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  let lastY = window.scrollY;
  let ticking = false;

  function onScroll() {
    const y = window.scrollY;
    navbar.classList.toggle('scrolled', y > 20);

    if (y > lastY && y > 140) {
      navbar.classList.add('nav-hidden');
    } else {
      navbar.classList.remove('nav-hidden');
    }
    lastY = y;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(onScroll);
      ticking = true;
    }
  });
}

/* ---------- Mobile menu ---------- */
function initMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  const openBtn = document.getElementById('menuToggle');
  const closeBtn = document.getElementById('menuClose');
  if (!menu || !openBtn) return;

  // The panel is hidden with visibility:hidden while closed (see common.css),
  // which already keeps its controls out of the tab order and the
  // accessibility tree. What follows is the state and focus handling that
  // belongs with it: the button has always been marked aria-expanded="false"
  // in the markup and nothing ever changed it, so assistive technology was
  // told the menu was shut even while it was open.
  const setOpen = (open) => {
    menu.classList.toggle('open', open);
    openBtn.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';

    if (open) {
      // Move focus into the panel so the next Tab continues inside it rather
      // than behind the overlay. The close button is the natural first stop.
      (closeBtn || menu.querySelector('a, button'))?.focus();
    } else if (menu.contains(document.activeElement)) {
      // Only pull focus back when it is still inside the panel we just hid -
      // following a menu link navigates away and must not be interrupted.
      openBtn.focus();
    }
  };

  openBtn.addEventListener('click', () => setOpen(true));
  if (closeBtn) closeBtn.addEventListener('click', () => setOpen(false));
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));

  // Escape closes the panel, matching the floating contact menu's behaviour.
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('open')) setOpen(false);
  });
}

/* ---------- Scroll reveal ---------- */
function initReveal() {
  const targets = document.querySelectorAll('[data-reveal]');
  if (!targets.length) return;

  const revealAll = () => targets.forEach(el => el.classList.add('in'));

  // Anyone who asked for reduced motion, or any browser without
  // IntersectionObserver, gets the content immediately rather than an
  // animation they did not want or a page that never reveals itself.
  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealAll();
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px 10% 0px' });
  targets.forEach(el => observer.observe(el));

  // Failsafe: whatever happens, nothing stays invisible for long. Anything
  // already inside the viewport is revealed on the next frame (so above-the-
  // fold content never waits on the observer), and anything still hidden a
  // few seconds after load is revealed outright.
  requestAnimationFrame(() => {
    targets.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) { el.classList.add('in'); observer.unobserve(el); }
    });
  });
  window.addEventListener('load', () => setTimeout(revealAll, 2500));
}

/* ---------- Animated counters ---------- */
function initCounters() {
  const counters = document.querySelectorAll('.counter');
  if (!counters.length) return;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const step = Math.max(1, Math.ceil(target / 44));
      let cur = 0;
      (function tick() {
        cur += step;
        if (cur >= target) { el.textContent = target; return; }
        el.textContent = cur;
        requestAnimationFrame(tick);
      })();
      observer.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(c => observer.observe(c));
}

/* ---------- Floating contact button (WhatsApp / Call / Email) ---------- */
function initContactFab() {
  const fab = document.getElementById('contactFab');
  const toggle = document.getElementById('fabToggle');
  const menu = document.getElementById('fabMenu');
  if (!fab || !toggle || !menu) return;

  // The menu opens ONLY when the visitor activates the button.
  //
  // It used to expand by itself 20 seconds after load and collapse 2 seconds
  // later. That has been removed entirely: nothing here runs on a timer, so the
  // menu never appears unprompted, never covers content the visitor is reading,
  // and never reopens after they have closed it. Position, appearance and the
  // open/close animation are unchanged - only the automatic trigger is gone.

  function setOpen(open) {
    const wasOpen = fab.classList.contains('open');
    fab.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-hidden', String(!open));

    // Closing gives the menu visibility:hidden, which drops its links out of
    // the tab order. If one of them held focus at that moment, focus would fall
    // back to <body> and keyboard users would lose their place in the page.
    // Hand it back to the button that controls the menu.
    if (wasOpen && !open && menu.contains(document.activeElement)) {
      toggle.focus();
    }
  }

  toggle.addEventListener('click', () => {
    setOpen(!fab.classList.contains('open'));
  });

  document.addEventListener('click', (e) => {
    if (!fab.contains(e.target)) setOpen(false);
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') setOpen(false);
  });
}

/* ---------- Services mega menu (desktop) + Services accordion (mobile) ----------
 * No dependencies, no markup generation — it only toggles classes and ARIA on
 * elements already present in the navbar. Both parts exit quietly if their
 * markup is absent, so the file stays safe on any page.
 */
function initServicesMenu() {
  const wrap = document.getElementById('servicesNav');
  const trigger = document.getElementById('servicesTrigger');
  const panel = document.getElementById('servicesMega');
  if (!wrap || !trigger || !panel) return;

  // Matches the CSS breakpoint where .mega is display:none and the mobile
  // menu takes over — below it the trigger is just a plain link.
  const desktop = window.matchMedia('(min-width: 769px)');
  const hoverable = window.matchMedia('(hover: hover) and (pointer: fine)');
  let closeTimer = null;

  function setOpen(open) {
    if (open && !desktop.matches) return;
    clearTimeout(closeTimer);
    wrap.classList.toggle('open', open);
    trigger.setAttribute('aria-expanded', String(open));
  }
  const isOpen = () => wrap.classList.contains('open');

  // Hover, with a small close delay so the pointer can travel from the
  // trigger down into the panel without it snapping shut.
  wrap.addEventListener('mouseenter', () => { if (hoverable.matches) setOpen(true); });
  wrap.addEventListener('mouseleave', () => {
    if (!hoverable.matches) return;
    closeTimer = setTimeout(() => setOpen(false), 160);
  });

  // Click: on touch/no-hover devices the first tap opens the panel instead of
  // navigating (a second tap on the trigger then follows the link). Where
  // hover works, the click just navigates to the Services page as before.
  trigger.addEventListener('click', (e) => {
    if (!desktop.matches || hoverable.matches) return;
    if (!isOpen()) { e.preventDefault(); setOpen(true); }
  });

  // Keyboard: focus opens, Escape closes and returns focus, Arrow Down enters
  // the panel. Tabbing past the last item closes it via focusout.
  wrap.addEventListener('focusin', () => setOpen(true));
  wrap.addEventListener('focusout', () => {
    setTimeout(() => { if (!wrap.contains(document.activeElement)) setOpen(false); }, 0);
  });
  wrap.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen()) {
      e.preventDefault();
      setOpen(false);
      trigger.focus();
    }
    if (e.key === 'ArrowDown' && document.activeElement === trigger) {
      e.preventDefault();
      setOpen(true);
      const first = panel.querySelector('a');
      if (first) first.focus();
    }
  });

  document.addEventListener('click', (e) => { if (!wrap.contains(e.target)) setOpen(false); });
  // The navbar hides itself on scroll-down; an open panel should go with it.
  window.addEventListener('scroll', () => { if (isOpen()) setOpen(false); }, { passive: true });
  desktop.addEventListener('change', () => setOpen(false));
}

/* ---------- Mobile Services accordion ---------- */
function initMobileServices() {
  const trigger = document.getElementById('mServicesTrigger');
  const panel = document.getElementById('mServicesPanel');
  if (!trigger || !panel) return;

  function setOpen(open) {
    trigger.setAttribute('aria-expanded', String(open));
    // Measured height keeps the transition exact at any font size and stops
    // long labels from being clipped.
    panel.style.maxHeight = open ? panel.scrollHeight + 'px' : '0px';
  }

  trigger.addEventListener('click', () => {
    setOpen(trigger.getAttribute('aria-expanded') !== 'true');
  });

  // Collapse whenever the mobile menu closes, so it reopens in a known state.
  const menu = document.getElementById('mobile-menu');
  if (menu) {
    new MutationObserver(() => {
      if (!menu.classList.contains('open')) setOpen(false);
    }).observe(menu, { attributes: true, attributeFilter: ['class'] });
  }
  window.addEventListener('resize', () => {
    if (trigger.getAttribute('aria-expanded') === 'true') {
      panel.style.maxHeight = panel.scrollHeight + 'px';
    }
  });
}
