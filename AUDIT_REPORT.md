# DeepAbi — Project Audit Report
**Scope:** Full static site (9 HTML pages, shared CSS/JS architecture, generated imagery)
**Method:** Automated structural analysis (link/tag integrity, selector cross-referencing, WCAG contrast math on the actual hex values) + manual review of every HTML/CSS/JS file.
**Date:** Pre-refresh baseline, prior to the enterprise redesign requested in this session.

---

## 1. Scores

| Category | Score /10 | Basis |
|---|---|---|
| Project Structure | 8.0 | Clean `common` + `pages` split for CSS/JS; no includes/templating, so navbar markup is duplicated across all 9 pages (see §4) |
| UI | 7.0 | Consistent components, but palette reads as a fairly conventional blue/violet SaaS theme — matches the new brief's own critique |
| UX | 7.5 | Clear nav, consistent CTAs, working filters/forms; no quick-contact channel (phone/WhatsApp) surfaced anywhere |
| Accessibility | 7.5 | Skip link, focus-visible states, full alt text, single-H1 per page; **one real contrast bug** — nav text is under-contrasted against the dark hero before scroll (measured below) |
| SEO | 7.0 | Full meta/OG/Twitter/JSON-LD scaffolding present on every page, but keyword coverage is narrow relative to the 25-term target list in this brief |
| Performance | 7.5 | WebP-first `<picture>` everywhere, reasonable source dimensions (0.06–1.5MP); **no responsive `srcset` variants** — every viewport downloads the same full-size image |
| Animation | 7.0 | Scroll-reveal, count-up, tilt, mesh blobs, hide/show navbar all present and smooth; no parallax, no scroll indicator, no per-section animation variety requested in this brief |
| Code Quality | 7.5 | Valid HTML/CSS/JS (checked programmatically), but 71 inline `style=""` attributes and 4 instances of a page CSS file silently overriding a `common.css` selector |
| Responsive Design | 8.0 | Full breakpoint coverage at 1024px/768px/600px; portfolio device-preview frames use fixed pixel widths that could be more fluid |
| Maintainability | 7.0 | Python generator scripts document how pages were assembled and are portable/re-runnable, but the *shipped* artifact is plain static HTML, so a copy change to the navbar still means touching 9 files (or re-running the generator) |
| Modern Design | 6.5 | Competent, but not distinctive — generic blue-led SaaS palette rather than a "luxury enterprise" identity |
| Enterprise Readiness | 6.0 | No phone/WhatsApp channel, single email placeholder, imagery is abstract/illustrative rather than photographic, no dedicated case-study depth beyond one featured project |

**Estimated overall rating: 7.3 / 10** — a solid, clean, accessible foundation that is functionally complete but visually and content-wise reads as "competent startup" rather than "premium enterprise," which is exactly the gap this brief asks to close.

---

## 2. Accessibility findings

- ✅ Skip-to-content link, `:focus-visible` outlines, semantic landmarks, single `<h1>` per page, descriptive `alt` text on every image, native form validation with associated `<label>`s.
- 🔴 **Contrast bug (confirmed by calculation):** `--text-secondary` (`#64748B`) on the dark hero background (`#0B132B`) measures **3.86:1**, which passes WCAG AA only for large text/UI components, not body-sized nav links — this is the "poor navbar visibility" issue named in the new brief, and it's real, not just a subjective impression.
- ⚠️ The requested new **Gold** (`#FFB703`), **Crystal Cyan** (`#14B8FF`), and **Emerald Green** (`#00C27A`) all **fail AA as text-on-white** (1.75:1, 2.25:1, 2.33:1 respectively) — they're excellent as accents, icon color, buttons-with-white-text, or on the dark navy surface (7.3–9.4:1 there), but must **not** be used as body/label text directly on white. This needs a deliberate "ink" variant of each for text use, the same pattern already used for the old `.eyebrow.cyan` label.
- ⚠️ No `aria-current="page"` on the active nav link (a CSS `.active` class is visual-only; screen reader users get no equivalent signal).
- ⚠️ `<details>` FAQ accordions are keyboard-operable natively (good), but have no visible focus ring distinct from the default browser style on some platforms — worth an explicit rule.

---

## 3. SEO findings

- Every page already ships unique `<title>`, meta description, canonical, OG/Twitter tags, and page-appropriate JSON-LD (`Organization`/`WebSite` on home, `BreadcrumbList` on inner pages, `Service`+`FAQPage` on the service detail page).
- **Gap:** the target keyword list in this brief (25 terms — "business website development," "e-commerce website," "enterprise website," "web application development," etc.) is only partially represented in current copy. Meta descriptions and H2s should be expanded to cover these naturally without keyword-stuffing.
- **Gap:** `sitemap.xml` does not yet reflect a "Projects" URL rename, and internal anchor text ("Portfolio") will need updating sitewide once renamed.
- **Gap:** no `Product`/`Service`-level structured data on the Services overview page (only present on the single detail template).

---

## 4. Code quality / duplication findings

- **Duplicated markup:** the `<header id="navbar">…</header>` block is present in all 9 files; content is identical except for which nav link carries `class="active"` (7 distinct hashes across 9 files, purely from that one class difference). The `<footer>` block is **byte-identical across all 9 pages** (1 unique hash) — good discipline, but still hand-synced rather than templated. This is an inherent tradeoff of the "no build step, plain static HTML" requirement from the original brief and is called out here rather than silently left as a surprise.
- **Inline styles:** 71 occurrences of `style="…"` across pages (mostly one-off margin/text-align tweaks), concentrated in `portfolio.html` and `services.html` (20 each). These should become utility classes to reduce drift.
- **Selector overlap between `common.css` and page CSS** (page file overrides a common rule for the same selector): `.tech-chip` (technologies.css), `.card` (service-detail.css), `.card-icon` (about.css), `.grad-text`/`.num`/`.label` (home.css). None are bugs, but they're worth consolidating so a future common.css change doesn't silently get shadowed.
- **Unused utility classes** defined in `common.css` but not referenced by any page today: `.badge-cyan`, `.btn-on-dark`, `.container-wide`, `.grid-12`, `.mt-0`, `.text-lg`, `.text-sm`. Safe to keep as an intentional utility layer, but flagged as dead weight if the goal is a lean stylesheet.
- No genuinely dead JavaScript functions were found — two flagged by static analysis (`onScroll`, `tick`) are false positives (used via `requestAnimationFrame` reference and self-recursion, not a direct call the regex could see).

## 5. Performance findings

- Images already ship as WebP-first `<picture>` with PNG/JPEG fallback, explicit `width`/`height` (no layout shift), and `loading="lazy"` on everything except the eager-loaded hero image — this part is solid.
- **Gap:** every image is a single fixed resolution. A phone on a 375px-wide viewport downloads the same 1400×1100 hero source as a 1440px desktop. Adding a second, smaller-resolution `srcset` entry per image would meaningfully cut mobile payload.
- **Gap:** Font Awesome is loaded in full from cdnjs on every page for a fairly small set of icons actually used — an icon subset or inline-SVG approach would be lighter, though this is a minor cost relative to the images.
- No render-blocking issues found; CSS/JS are appropriately deferred by placement (JS at end of body).

## 6. Responsive design findings

- Breakpoints at 1024px/768px/600px are applied consistently and cover the documented grid/nav/card collapses.
- The portfolio page's device-preview frames (`.device-frame.desktop/tablet/mobile`) use fixed pixel widths (480px/260px/150px) rather than `clamp()`-based fluid sizing, so on very narrow phones (<360px) the "desktop" preview can slightly overflow before its own breakpoint kicks in.

## 7. Security recommendations

- The contact form currently validates client-side only and has no backend wired up (documented in the README as an intentional stub) — when connected to a real endpoint, add server-side validation/sanitization, not just the native HTML5 `required` attributes.
- The Font Awesome stylesheet is loaded from `cdnjs.cloudflare.com` without a Subresource Integrity (`integrity`) attribute — recommend adding SRI hashes for any third-party CDN asset.
- Placeholder social links currently point to `#`; once replaced with real external URLs, add `rel="noopener noreferrer"` alongside `target="_blank"` if they're set to open in a new tab.
- Recommend a `Content-Security-Policy` header at the hosting layer once a real domain is live, given the site pulls fonts/icons from two external origins.

## 8. Recommended folder structure (target state for this pass)

```
assets/
  images/
    home/{jpg,png,webp}
    services/{jpg,png,webp}
    about/{jpg,png,webp}
    projects/{jpg,png,webp}
    technology/{jpg,png,webp}
    testimonials/{jpg,png,webp}
    logos/          (favicons, wordmark exports)
    backgrounds/    (OG/social banner)
    icons/          (reserved — UI icons currently via Font Awesome CDN)
    illustrations/  (reserved — future custom SVG/illustration assets)
```
Each page-scoped folder is seeded with a clearly-named file occupying the "real photo" slot (e.g. `assets/images/about/jpg/team-collaboration.jpg`) so a real photograph can later replace it in place, same filename, same dimensions, zero markup changes.

## 9. Recommended component structure

No change to the "plain static HTML + shared CSS/JS" architecture is proposed — the brief explicitly asks to preserve compatibility. Within that constraint, the improvement is disciplined **utility-class consolidation** (replacing the 71 inline styles with a small set of spacing/alignment utilities already partially defined in `common.css`) and a **new shared component**, the floating contact launcher (`#contact-fab`), added once to `common.js`/`common.css` so it appears identically on every page without per-page duplication.

---

## 10. What this pass will change

1. Full palette replacement (Deep Royal Navy / Crystal Cyan / Royal Violet / Emerald Green / Premium Gold), with accessible "ink" text variants for the accent colors.
2. Navbar contrast fix (dynamic light/dark mode depending on hero darkness + scroll state), larger CTA, animated active-page underline, `aria-current`.
3. New mission/vision copy and three taglines, threaded through hero, About, footer, and a dedicated mission section.
4. Image reorganization into the folder hierarchy above, with descriptive real-photo-style filenames.
5. Contact info replaced everywhere (email + two phone numbers), surfaced in navbar, footer, Contact page, and a new floating WhatsApp/Call/Email popup.
6. "Portfolio" renamed to "Projects" sitewide (nav, links, breadcrumbs, footer, SEO, sitemap).
7. Hero upgraded with mouse parallax and a scroll indicator, on top of the existing mesh/particles/counters.
8. Technologies page gets category filtering (Frontend/Backend/Database/Cloud/Deployment/Tools) to match the existing Projects-filter pattern.
9. SEO expansion using the target keyword list, added naturally to meta descriptions, H2s, and structured data — not stuffed.
10. Accessibility fixes: `aria-current="page"`, ink-safe accent colors, explicit focus rings on `<details>`.

Everything below this line in the delivered project reflects those changes already applied.
