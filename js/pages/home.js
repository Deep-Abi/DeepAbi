/**
 * Home page JS: minimal particle field in the hero background,
 * mouse parallax on the hero illustration, a subtle 3D tilt effect on the
 * service preview cards, a looping hero typing animation, an
 * auto-advancing testimonial carousel with hover-to-pause, and an
 * auto-cycling desktop/tablet/mobile device card stack.
 */
document.addEventListener('DOMContentLoaded', () => {
  initParticles();
  initTilt();
  initParallax();
  initTypingHeading();
  initTestimonialCarousel();
  initDeviceStack();
});

function initParticles() {
  const canvas = document.getElementById('particles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function resize() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  const COUNT = 46;
  const particles = Array.from({ length: COUNT }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 1.6 + 0.6,
    vx: (Math.random() - 0.5) * 0.15,
    vy: (Math.random() - 0.5) * 0.15,
  }));

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'rgba(20, 184, 255, 0.55)';
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    });
    if (!reduceMotion) requestAnimationFrame(draw);
  }
  draw();
}

/* ---------- Mouse parallax on the hero illustration ---------- */
function initParallax() {
  const hero = document.getElementById('hero');
  const visual = document.getElementById('heroParallax');
  if (!hero || !visual) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (window.matchMedia('(max-width: 768px)').matches) return; // skip on touch/small screens

  hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    const relX = (e.clientX - rect.left) / rect.width - 0.5;
    const relY = (e.clientY - rect.top) / rect.height - 0.5;
    visual.style.transform = `translate(${relX * -18}px, ${relY * -14}px)`;
  });

  hero.addEventListener('mouseleave', () => {
    visual.style.transform = '';
  });
}

function initTilt() {
  const cards = document.querySelectorAll('.service-card');
  if (!cards.length) return;

  document.addEventListener('mousemove', (e) => {
    const card = e.target.closest('.service-card');
    cards.forEach(c => { if (c !== card) c.style.transform = ''; });
    if (!card) return;
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const rx = ((y / rect.height) - 0.5) * -6;
    const ry = ((x / rect.width) - 0.5) * 6;
    card.style.transform = `perspective(700px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-4px)`;
  });
  document.addEventListener('mouseleave', () => {
    cards.forEach(c => c.style.transform = '');
  });
}

/* ---------- Hero typing animation ---------- */
function initTypingHeading() {
  const target = document.getElementById('typingTarget');
  if (!target) return;

  // The heading text is authored in the HTML, so the page reads correctly with
  // no JavaScript. Read it back from the DOM rather than repeating it here:
  // the generator stays the single source of the wording.
  const FULL_TEXT = (target.textContent || '').trim();
  if (!FULL_TEXT) return;

  const heading = target.closest('.typing-heading');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Leave the heading exactly as authored when motion is not wanted. The caret
  // stays hidden because .is-typing is never added.
  if (reduceMotion) {
    target.textContent = FULL_TEXT;
    return;
  }

  // Only now does the decorative caret appear.
  if (heading) heading.classList.add('is-typing');

  // While the text is being retyped it is a moving target, so hide it from
  // assistive technology and leave one stable, complete copy in its place.
  // Both are added here, not in the markup, so the no-JavaScript page keeps a
  // single plain heading with nothing duplicated.
  target.setAttribute('aria-hidden', 'true');
  if (heading && !heading.querySelector('.typing-sr-text')) {
    const srText = document.createElement('span');
    srText.className = 'sr-only typing-sr-text';
    srText.textContent = FULL_TEXT;
    heading.appendChild(srText);
  }

  const TYPE_SPEED = 55;      // ms per character while typing
  const DELETE_SPEED = 32;    // ms per character while deleting
  const HOLD_FULL = 2200;     // pause once fully typed
  const HOLD_EMPTY = 500;     // pause once fully deleted

  let i = 0;
  let deleting = false;

  function tick() {
    if (!deleting) {
      i++;
      target.textContent = FULL_TEXT.slice(0, i);
      if (i >= FULL_TEXT.length) {
        deleting = true;
        setTimeout(tick, HOLD_FULL);
        return;
      }
      setTimeout(tick, TYPE_SPEED);
    } else {
      i--;
      target.textContent = FULL_TEXT.slice(0, i);
      if (i <= 0) {
        deleting = false;
        setTimeout(tick, HOLD_EMPTY);
        return;
      }
      setTimeout(tick, DELETE_SPEED);
    }
  }
  tick();
}

/* ---------- Testimonial carousel: auto-advance + dots + arrows + hover-to-pause ---------- */
function initTestimonialCarousel() {
  const track = document.getElementById('testimonialTrack');
  const dotsWrap = document.getElementById('testimonialDots');
  const carousel = document.getElementById('testimonialCarousel');
  const prevBtn = document.getElementById('testimonialPrev');
  const nextBtn = document.getElementById('testimonialNext');
  if (!track || !dotsWrap || !carousel) return;

  const slides = Array.from(track.querySelectorAll('.testimonial-slide'));
  if (!slides.length) return;

  let current = 0;
  let timer = null;
  const INTERVAL = 4500;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  slides.forEach((slide, i) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('role', 'tab');
    dot.setAttribute('aria-label', `Show testimonial ${i + 1} of ${slides.length}`);
    dot.addEventListener('click', () => { goTo(i); start(); });
    dotsWrap.appendChild(dot);
  });
  const dots = Array.from(dotsWrap.children);

  function render() {
    slides.forEach((s, i) => s.classList.toggle('active', i === current));
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
  }

  function goTo(index) {
    current = (index + slides.length) % slides.length; // wraps both directions — infinite loop
    render();
  }

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  function start() {
    if (reduceMotion || slides.length < 2) return;
    stop();
    timer = setInterval(next, INTERVAL);
  }
  function stop() {
    if (timer) clearInterval(timer);
    timer = null;
  }

  render();
  start();

  if (nextBtn) nextBtn.addEventListener('click', () => { next(); start(); });
  if (prevBtn) prevBtn.addEventListener('click', () => { prev(); start(); });

  carousel.addEventListener('mouseenter', stop);
  carousel.addEventListener('mouseleave', start);
  carousel.addEventListener('focusin', stop);
  carousel.addEventListener('focusout', start);
}

/* ---------- Built for Every Screen: device card-stack cycle ---------- */
function initDeviceStack() {
  const stack = document.getElementById('deviceStack');
  if (!stack) return;

  const cards = Array.from(stack.querySelectorAll('.device-stack-card'));
  if (cards.length < 3) return;

  const order = ['desktop', 'tablet', 'mobile']; // cycle order: desktop -> tablet -> mobile -> loop
  const byRole = Object.fromEntries(cards.map(c => [c.dataset.role, c]));
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const INTERVAL = 3200;
  let frontIndex = 0;
  let timer = null;

  function render() {
    const stateClass = ['stack-front', 'stack-mid', 'stack-back'];
    order.forEach((role, i) => {
      const card = byRole[role];
      const rel = (i - frontIndex + order.length) % order.length; // 0=front,1=mid,2=back
      card.classList.remove('stack-front', 'stack-mid', 'stack-back');
      card.classList.add(stateClass[rel]);
    });
  }

  function next() {
    frontIndex = (frontIndex + 1) % order.length;
    render();
  }

  function start() {
    if (reduceMotion) return;
    stop();
    timer = setInterval(next, INTERVAL);
  }
  function stop() {
    if (timer) clearInterval(timer);
    timer = null;
  }

  render();
  start();

  stack.addEventListener('mouseenter', () => { stack.classList.add('paused'); stop(); });
  stack.addEventListener('mouseleave', () => { stack.classList.remove('paused'); start(); });
  stack.addEventListener('focusin', stop);
  stack.addEventListener('focusout', start);
}
