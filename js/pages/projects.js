/**
 * Projects page: filters the demo library by service.
 *
 * No dependencies and no framework. Three jobs:
 *   1. show only the cards for the chosen service (or all of them);
 *   2. keep the chosen button marked both visually (.active) and
 *      programmatically (aria-pressed), and swap in that service's intro;
 *   3. show an empty-state message if a service has no demos listed.
 *
 * Buttons are real <button> elements, so keyboard and touch work without any
 * extra handling; the intro paragraph is aria-live so a screen reader hears
 * the change.
 */
document.addEventListener('DOMContentLoaded', () => {
  const bar = document.getElementById('pfFilter');
  const grid = document.getElementById('projectsGrid');
  if (!bar || !grid) return;

  const buttons = Array.from(bar.querySelectorAll('.filter-btn'));
  const cards = Array.from(grid.querySelectorAll('.project-card'));
  const intro = document.getElementById('pfIntro');
  const cats = document.getElementById('pfCats');
  const empty = document.getElementById('pfEmpty');
  if (!buttons.length || !cards.length) return;

  // Show or hide a block. Site-wide reveal animation starts at opacity:0 and
  // only adds .in when the element scrolls into view — an element that was
  // display:none at load never gets observed, so mark it revealed on show.
  function reveal(el, show) {
    el.classList.toggle('pf-hidden', !show);
    if (show && el.hasAttribute('data-reveal')) el.classList.add('in');
  }

  function apply(btn) {
    const filter = btn.dataset.filter;

    buttons.forEach(b => {
      const on = b === btn;
      b.classList.toggle('active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });

    // "All" shows the eight service introduction cards instead of every demo
    // at once; a specific service shows its own demos.
    const isAll = filter === 'all';
    // With a service index present, "All" shows that index and a specific
    // choice shows the demo grid. Without one - which is the case when the
    // filters are Website Development sub-categories - the grid is always the
    // view, and "All" simply stops filtering it.
    if (cats) {
      reveal(cats, isAll);
      reveal(grid, !isAll);
    } else {
      reveal(grid, true);
    }

    let shown = 0;
    cards.forEach(card => {
      const show = filter === 'all' || card.dataset.cat === filter;
      card.classList.toggle('pf-hidden', !show);
      if (show) shown++;
    });

    if (intro && btn.dataset.intro) intro.innerHTML = btn.dataset.intro;
    if (empty) empty.hidden = shown !== 0;

    // Keep the chosen button in view when the bar scrolls sideways on mobile.
    if (bar.scrollWidth > bar.clientWidth && typeof btn.scrollIntoView === 'function') {
      btn.scrollIntoView({ block: 'nearest', inline: 'center',
        behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    }
  }

  buttons.forEach(btn => btn.addEventListener('click', () => apply(btn)));

  // The service cards in the All view drive the same filter.
  if (cats) {
    cats.querySelectorAll('[data-goto]').forEach(card => {
      card.addEventListener('click', () => {
        const target = buttons.find(b => b.dataset.filter === card.dataset.goto);
        if (target) apply(target);
      });
    });
  }

  // Set the initial view (hides the demo grid behind the service index).
  apply(buttons.find(b => b.classList.contains('active')) || buttons[0]);
});
