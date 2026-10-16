# Changelog

## v6 — Image Fixes, Contact Map, Final Cleanup (this session)

### Hero image
- **Discrepancy found and flagged**: the brief referenced an uploaded `deepabi-concept` image that does not exist anywhere in the upload. Regenerated the DEEP/ABI brand illustration (from the generator function retained since an earlier session) and saved it as `deepabi-concept.*` to fill the gap — this is an assumption, not a verified real asset; see Assumptions in the response for this session.
- Hero reverted from the per-breakpoint art-directed picture (desktop/tablet/mobile swap) to a single `deepabi-concept` image, per this brief's explicit "only replace the image, keep everything else identical" instruction.

### Built for Every Screen
- Swapped from `desktop.jpg/tablet_portrait.jpg/mobile_portrait.jpg` (differently-shaped device mockups, now freed up — still used elsewhere on the Projects page) to the larger `deepabi-desktop/tablet/mobile` marketing images.
- Redesigned the card-stack sizing for the new uniform ~3:2 landscape aspect ratio shared by all three images (previously each had a distinct device-shaped frame). Fixed a genuine CSS specificity bug in the process — the new larger frame size wouldn't have actually applied against the older per-role frame-size rules without raising the new selector's specificity to match and win on source order.

### Image quality / cropping fix
- Root-caused the "quality loss" symptom: the service-card image container's aspect ratio (1.316) didn't match the real uploaded images' native ratio (1.5–1.9), causing heavier horizontal cropping than intended via `object-fit: cover`. Widened the container to 3:2 (matching 5 of 9 real images exactly) and updated the corresponding width/height attributes — the container was resized, not the images, per the brief's explicit instruction.

### About page
- Mission and Vision images enlarged: container max-width 220px → 340px, intrinsic size 220×147 → 380×253, same aspect ratio maintained (no cropping, transparency preserved).

### Contact page
- Map placeholder replaced with a real, responsive Google Maps iframe (no API key required, `output=embed` pattern) using the exact address provided, with `loading="lazy"`, a descriptive `title`, and a responsive height across breakpoints (420px → 340px → 280px).
- Added a physical address row to the contact info card, which previously had no address at all.

### Cleanup
- Removed 9 confirmed-unused image files: duplicate OG-banner formats (PNG/WebP; only the JPG is referenced by the meta tag), an unreferenced 48px favicon size, and two unused testimonial avatars (only 4 testimonial slides exist on the site). Trimmed the corresponding calls out of `generate_images.py`'s `__main__` block so re-running the generator won't recreate them.
- Confirmed via automated scan: **zero unreferenced image files remain** in `assets/images/`.

### Known gap (not fabricated)
- No real "website development" photo/screenshot was ever uploaded (in this batch or the previous one), so that one service card still uses the earlier generated placeholder illustration. Flagged rather than invented.

---

## v5 — Hero Refinement, Services & Contact Overhaul (previous session)

### Home page
- **Hero illustration rebuilt again**, this time literally rendering the brand: large "DEEP" and "ABI" typography, connected by a glowing vertical link with a node at its midpoint, each with its full-form meaning ("Driving Economic Empowerment for People" / "Ambition Beyond Imagination") set in tracked small caps beneath. Soft blurred glow layer behind the sharp text, floating particles, subtle gradient highlights (cyan/violet/gold), and minimal corner framing — no flashy motion baked into the image itself; the existing CSS glow-pulse behind it was softened further (slower, lower-contrast pulse) to stay "very soft" per the brief.
- **Section labels overhauled**: "What We Build," "Why DeepAbi," "How We Work," "Testimonials," etc. no longer sit in a small pill badge — they're now bold, wide-tracked kicker-style labels (14px, 800 weight, 0.18em tracking) with a short accent-colored tick mark, scoped to `.section-head .eyebrow` so the pill-badge style used elsewhere (page headers, hero, cards) is untouched.

### Floating contact widget
- Changed from a repeating every-5–7-second cycle to a **single one-time auto-expand at 20 seconds** (open ~2s, then auto-collapse), per the revised brief. Manual open/close now runs fully independently and no longer cancels or resets the scheduled auto-trigger. Pulse ring softened slightly (lower peak opacity, slower, smaller scale) for a gentler feel.

### Services page
- **Hero rebuilt**: now a two-column layout with floating gradient blobs, a new purpose-built illustration (service modules orbiting a central hub), a brighter/richer radial-glow background, a larger heading, and two CTA buttons ("Start Your Project" + "Explore Services") — previously just an eyebrow/heading/paragraph with no visual or CTA.
- **Service cards redesigned to enterprise level**: added a colored accent strip down the left edge (cycling violet→cyan→gold→mint per card), the gradient border is now subtly visible at rest and intensifies on hover (previously hover-only), and the CTA became a dedicated "Learn More"-style button with an arrow-slide micro-interaction on hover.

### Contact page
- Removed the FAQ section entirely.
- Map moved out of the sidebar and rebuilt as its own full-width section below the form/info grid, with large rounded corners, a soft shadow, and generous padding.
- Heading changed from "Let's build something together" to "Let's Build Your Digital Future".

### Sitewide CTA copy
- Every "Get Free Consultation" button (8 occurrences across Home, About, Projects, Services, Service Detail, Technologies) replaced with "Start Your Project" for a shorter, more action-oriented, consistent CTA. The descriptive "Free Consultation" label in the Contact page's info card was left as-is since it's descriptive text, not a button.

### Footer
- Brightened body/link text (`#94A3B8` → `#B8C4D9`, contrast raised from 6.2:1 to 9.1:1 against the navy background).
- Company/Services link lists gained small chevron icons with a slide-on-hover animation; the Contact column now shows a small uppercase label ("Email," "Phone," "WhatsApp") above each value for clearer hierarchy.
- Social icons got a visible resting state (border + subtle fill, not just 6% opacity) and a stronger gradient hover treatment.
- Added a gradient accent tick under each column heading, subtle vertical separators between columns on desktop, and a divider before each legal link in the copyright bar.

See `AUDIT_REPORT.md` for the original v1→v2 audit and earlier CHANGELOG sections below for prior passes.

---

## v4 — Visual Hierarchy & Content Polish

### Home page
- **Section heading hierarchy swapped sitewide**: "What We Build," "Built for Every Screen," "Why DeepAbi," "How We Work," and "Testimonials" are now the large `<h2>` titles themselves (bigger, heavier, with the decorative gradient underline), with the previous descriptive sentence demoted to a small supporting subtitle underneath. Applied via a single shared `.section-head h2` upgrade (larger `clamp()` range, 800 weight, tighter letter-spacing) so every section on every page benefits consistently, not just the ones named in the brief.
- **"Built for Every Screen" rebuilt**: replaced the small floating-icon-frame graphic with a new, large, purpose-built multi-device mockup illustration (generated at showcase scale, matching the Projects page's featured-image size), given a slight continuous float animation, deep shadow, and large border radius. "Responsive Website Design" now sits as a dedicated `<h3>` content heading below the image, above a redesigned 4-item feature grid (icon chip + heading + description per item, hover lift, more padding, better vertical rhythm) replacing the old plain checklist.
- **New hero illustration**: replaced the abstract placeholder with a purpose-built conceptual piece — a glowing "innovation core" (Deep) orbited by connected nodes (Abi/ambition), an ascending growth-bar-and-arrow motif (business growth), soft layered glows, and scattered floating particles. Added a pulsing glow behind the image itself.
- **Testimonial carousel upgraded**: added manual prev/next arrow controls (in addition to the existing dots and auto-advance/pause-on-hover from v3), a glass-effect card (backdrop blur), hover elevation, a fourth dummy review, and tightened the auto-advance interval to ~4.5s.
- **"Why DeepAbi" cards**: new `.why-card` modifier (bigger icon chip, stronger hover lift + scale, icon rotate/gradient-fill on hover) layered on top of the shared `.card` component so the enhancement is scoped to this section without changing `.card` usage elsewhere on the site.
- **"How We Work" timeline**: increased spacing between steps, added a second connecting-line layer that animates its width from 0→100% (gradient fill) in sync with the existing staggered step reveal, larger dots, bolder step typography.
- **What We Build cards**: added a "Learn more →" micro-interaction that fades/slides in on hover.

### Services page
- Fixed a real navbar bug: the page's dark gradient header wasn't paired with `body.hero-dark`, so the navbar rendered with dark text over a dark background before scrolling (invisible/inconsistent with Home). Added the missing body class.
- "See It In Detail" CTA enlarged (`.btn-lg`) with a new `.btn-glow` hover treatment (outer glow ring + lift).

### Projects page
- "More Project Types" → "What We Build" (eyebrow demoted to "Our Work" to avoid duplicating the new H2 text).
- Reduced project card thumbnail height (170px → 140px) so more cards are visible per scroll.

### Technologies page
- "Filter by Category" → "Stacks We Use"; "Browse the stack" → "Explore Our Technology Stack".
- Added GoDaddy and Hostinger to the Deployment category.
- Removed the "Frontend Stack (This Site)" section entirely — the page now covers only technologies used for client projects.

### About page
- Mission and Vision rebuilt as identical-layout premium cards: logo mark → small-caps heading ("Mission"/"Vision") → large catchline (no trailing period, per brief) → professional paragraph. Gradient border reveals on hover, matching the card treatment used elsewhere on the site.
- New catchlines: "Driving Economic Empowerment for People" / "Ambition Beyond Imagination" (both punctuation-free per brief). These are now the shared `MISSION`/`VISION_HEADLINE` constants in `build_site.py`, so the footer's mission banner and the home hero's Mission/Vision cards stay in sync automatically.
- New long-form paragraphs (`ABOUT_MISSION_PARAGRAPH`/`ABOUT_VISION_PARAGRAPH`) written for this page specifically, separate from the shorter hero-card copy.

### Floating contact widget
- Now auto-expands on its own every 5–7 seconds, stays open ~2 seconds, and auto-collapses — while still fully manually togglable. Once a user manually interacts with it, the auto-cycle stops (so it doesn't keep popping open against an already-engaged visitor). Respects `prefers-reduced-motion` (no auto-cycle).

### Global
- Spacing scale tightened further (`--sp-9`/`--sp-10` 88px → 72–76px, `--sp-6`/`--sp-7`/`--sp-8` trimmed similarly) to reduce excess vertical whitespace while keeping section breathing room.

See `AUDIT_REPORT.md` for the original v1→v2 audit and earlier CHANGELOG sections below for prior passes.

---

## v3 — Premium Polish Pass

Continuation on the v2 enterprise redesign. The uploaded project already had the palette, spacing, and most section shells from this brief in place; this pass focused on **finishing the functional gaps** (markup that existed with no CSS/JS behind it) and the remaining explicit removals.

### Fixed: markup with no styling/behavior behind it
- **Hero typing animation**: the `#typingTarget`/`.typing-cursor` markup existed but had zero JS — added a looping type/delete/pause cycle (`initTypingHeading` in `home.js`) and a blinking-cursor CSS animation. Respects `prefers-reduced-motion` (shows full text, no animation). An `.sr-only` fallback span (also newly added) carries the real heading text for screen readers.
- **Hero Mission/Vision glass cards**: `.hero-mv-grid`/`.hero-mv-card` had no CSS at all — added full glassmorphism treatment (blur, soft glow on hover, icon, border, small description) side-by-side inside the hero, replacing the old `.hero-banner` component.
- **"What We Build" cards**: `.wwb-grid`/`.wwb-card` had no CSS — added icon, gradient-border-on-hover, and micro-interaction (icon scale + rotate) for all 8 cards (Business/Corporate/Landing/Maintenance/SEO/Performance/Modern UI/Scalable Architecture).
- **Responsive Website Design showcase**: `.responsive-showcase`/`.responsive-float-frame` had no CSS — added floating device frames with staggered animation, a pulsing glow, and a gradient border on the mobile frame.
- **Testimonial carousel**: markup (`.testimonial-track`, `.testimonial-dots`) existed with no JS — added `initTestimonialCarousel` (auto-advance every 5.5s, dot navigation, pause on hover/focus, respects reduced-motion) plus full crossfade CSS, larger avatars, and a large quotation mark.

### Removed (per brief)
- Breadcrumbs sitewide (`Home > Services` etc.) — removed from all 7 page generators and the now-dead `.breadcrumb` CSS.
- The entire Pricing section from `service-detail.html`, including the "View Pricing" hero button (now "View FAQs") and the now-dead `.pricing-card` CSS. Removed lingering "pricing" mentions from copy/meta description/keywords.
- Stale "Trusted by ambitious startups…" line — confirmed already absent from the generator source; a rebuild flushed it out of the shipped `index.html`.

### Services page
- Hero now uses a colored gradient background (`.page-header-gradient`, reusing the hero/CTA-only gradient token) instead of plain surface.
- Each service block is now a bordered, shadowed card with a gradient border on hover, a large floating icon badge over the image, and its own "Get Started" CTA — previously a plain two-column row with a bottom divider.

### Cleanup
- Removed dead CSS left behind by the above removals (`.breadcrumb`, `.pricing-card`).

See `AUDIT_REPORT.md` for the v1→v2 baseline audit and `CHANGELOG.md`'s v2 section (below) for the previous pass.

---

## v2 — Enterprise Redesign

Full audit-driven refresh on top of the original static-site architecture. See `AUDIT_REPORT.md` for the baseline scores and findings this pass addresses. Nothing below removed existing functionality — it's additive/corrective on the same architecture.

### Brand
- Replaced the entire color system: Deep Royal Navy `#071D49`, Crystal Cyan `#14B8FF`, Royal Violet `#6D28D9`, Emerald Green `#00C27A`, Premium Gold `#FFB703`.
- Added AA-safe "ink" variants (`--cyan-ink`, `--violet-ink`, `--mint-ink`, `--gold-ink`) for text-on-light use, since the full-saturation accents fail WCAG AA as body text (documented with exact contrast ratios in the audit).
- Restricted gradients to hero backgrounds and CTA sections; every button, badge, and icon chip elsewhere now uses a solid brand color.
- New mission ("Driving Economic Empowerment for People through Innovative Digital Solutions.") and vision ("Beyond Imagination. …") copy, threaded through the hero, About page, and a new footer mission banner.
- Three taglines (primary/secondary/third) introduced and used in the hero eyebrow, top bar, and About intro.

### Navbar
- Fixed the real contrast bug flagged in the audit (nav text at 3.86:1 against the dark hero, below AA for normal text): navbar now switches to light text automatically on dark-hero pages via `body.hero-dark`, and goes fully solid/dark-text once scrolled or on any light-hero inner page.
- Added a slim top bar (phone, WhatsApp, email, tagline) above the main nav, hidden on mobile.
- Larger CTA button (`.btn-lg`), animated gold active-page underline, `aria-current="page"` on the active link, elegant blur+shadow on scroll.

### Contact
- Replaced all contact info sitewide with `deepabi.tech@gmail.com`, `+91 89460 97125`, `+91 89252 79380`.
- Added a floating action button (bottom-right, every page) that expands into WhatsApp / Call / Email with scale+fade animation, keyboard-dismissible (`Escape`) and click-outside-to-close.
- Contact page now lists both phone numbers and a WhatsApp link alongside email.

### Navigation / IA
- Renamed "Portfolio" to "Projects" everywhere: nav, footer, breadcrumbs, page title (now "Projects & Success Stories"), `sitemap.xml`, internal links, JSON-LD, and the CSS/JS filenames (`projects.css`/`projects.js`).
- Fixed the fluid-sizing gap on the Projects page's device-preview frames (previously fixed-pixel widths that could overflow under 360px; now `clamp()`-based).

### Hero
- Added mouse parallax on the hero illustration, a scroll indicator, and mission/vision banner cards, on top of the existing gradient mesh, floating blobs, particle field, and animated counters.

### Technologies
- Rebuilt as a filterable grid (Frontend / Backend / Database / Cloud / Deployment / Tools) with per-technology descriptions and a hover animation, replacing the previous static grouped-by-heading layout. Added a "Deployment" category (Docker, GitHub Actions, Vercel/Netlify) that didn't exist before.

### Assets
- Reorganized every image out of a single flat `images/` folder into `assets/images/{home,services,about,projects,technology,testimonials}/{jpg,png,webp}/`, plus flat `logos/`, `backgrounds/`, and reserved `icons/`/`illustrations/` folders.
- Renamed every file from generic names (`hero-illustration`, `service-seo`, `avatar-1`…) to descriptive, real-photo-style names (`hero-digital-network`, `seo-analytics-dashboard`, `client-avatar-1`…) so a real photograph can drop into the same path later with zero markup changes.

### SEO
- Expanded meta keywords and page copy to naturally cover the full target term list (custom website development, corporate website design, small business website, enterprise website, web application development, SEO services, technical SEO, website redesign, e-commerce website, etc.) via a per-page `extra_keywords` mechanism plus a shared base keyword set.
- Updated `sitemap.xml` for the Portfolio → Projects rename; added SRI hash to the third-party Font Awesome stylesheet.

### Accessibility
- `aria-hidden="true"` added to all decorative icons sitewide; interactive-only icons kept accessible labels.
- FAQ accordion (`<details>`) styles consolidated into `common.css` (previously only loaded on the service-detail page, so it rendered unstyled on the Contact page — a genuine bug found during the audit and fixed here) with an explicit focus ring added.
- `aria-current="page"` added to the active nav link.

### Code quality (per the audit's own findings)
- Moved `.faq-item`/`.faq-list` from a page-specific stylesheet into `common.css` since two pages use it (was previously duplicated risk / actually a rendering bug on Contact).
- Renamed `.portfolio-card`/`.portfolio-card-body` to `.project-card`/`.project-card-body` in `common.css` to match the new IA.
