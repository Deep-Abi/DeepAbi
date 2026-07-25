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
