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

  openBtn.addEventListener('click', () => {
    menu.classList.add('open');
    document.body.style.overflow = 'hidden';
  });
  const close = () => {
    menu.classList.remove('open');
    document.body.style.overflow = '';
  };
  if (closeBtn) closeBtn.addEventListener('click', close);
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', close));
}

/* ---------- Scroll reveal ---------- */
function initReveal() {
  const targets = document.querySelectorAll('[data-reveal]');
  if (!targets.length) return;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  targets.forEach(el => observer.observe(el));
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

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setOpen(open) {
    fab.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-hidden', String(!open));
  }

  // Auto-expand exactly once, 20 seconds after the page loads, and remain
  // open for ~2 seconds before collapsing. This runs on its own schedule —
  // manual opens/closes by the user don't cancel or reset it.
  if (!reduceMotion) {
    setTimeout(() => {
      setOpen(true);
      setTimeout(() => setOpen(false), 2000);
    }, 20000);
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
