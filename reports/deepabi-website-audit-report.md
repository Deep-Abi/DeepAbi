# DeepAbi Innovations — Website Cleanup, Consistency, Responsiveness & Performance Report

**Prepared:** 9 September 2026
**Scope:** local working copy at `C:\work-station\DeepAbi-Innovations\DeepAbi`
**Deployment status:** nothing was deployed or published. All changes are on disk only.

---

## 1. Executive summary

The site was audited page by page in a real browser engine (headless Chromium),
at six viewport widths, with before-and-after measurements taken under identical
conditions. Seventeen public pages were covered, including all eight dedicated
service pages, Projects, Contact and the legal pages.

**The four findings that mattered**

1. **Content was invisible without JavaScript.** Every `[data-reveal]` block —
   which is most of the page body — started at `opacity: 0` and only became
   visible when a scroll observer fired. Measured on the home page: **0 of 29
   content blocks visible** with scripting unavailable. The same failure mode
   applied if `common.js` failed to load or threw. Now **29 of 29** are visible.
2. **Two blocks on the Projects page stayed blank inside the first screen**
   even with JavaScript working, because the observer had not fired for them by
   the time the page finished loading. Now zero.
3. **Images were shipped at three to four times the size they are displayed at.**
   `website-development-workspace.avif` alone was 644 KB, drawn at 453×302 from a
   2048×1143 source. Across five representative pages the first-party payload was
   **6,459 KB; it is now 2,347 KB — 64% smaller**, with no visible quality change.
4. **The contact form displayed "Message sent successfully!" and sent nothing.**
   That message is gone. The form now composes the enquiry in the visitor's own
   email client and says exactly that.

Alongside these, the company name, both email addresses and both phone numbers
were verified across every surface, the heading hierarchy was corrected on all
17 pages, the smallest touch targets were enlarged, and the page generators were
brought back into line with the approved pages so that a rebuild can no longer
revert content.

**Principal remaining limitation:** the contact form still has no backend. It
composes an email rather than delivering one, and the page now says so. Adding
real delivery is a decision for DeepAbi. See §10.

---

## 2. Audit scope and method

### Pages inspected (17)

`index` · `services` · `service-website-development` · `service-web-applications` ·
`service-mobile-applications` · `service-desktop-applications` ·
`service-custom-software` · `service-saas-products` · `service-ai-automation` ·
`service-software-maintenance` · `service-detail` (redirect stub) · `projects` ·
`technologies` · `about` · `contact` · `privacy` · `terms`

### Viewports

| Label | Width × height | Represents |
|---|---|---|
| mobile-360 | 360 × 780 | small Android phones |
| mobile-390 | 390 × 844 | iPhone-class phones |
| tablet-768 | 768 × 1024 | portrait tablet |
| laptop-1024 | 1024 × 768 | landscape tablet / small laptop |
| desktop-1366 | 1366 × 900 | common laptop |
| desktop-1440 | 1440 × 900 | larger desktop |

**107 page × viewport runs** per pass (17 pages × 6 viewports, plus a
JavaScript-disabled pass over five pages), run identically before and after.

### Tools and conditions

- **Headless Chromium via Playwright**, running in an isolated Linux container.
- Structural checks over `file://`; payload and timing measurements over a local
  HTTP server so that resource sizes are reported accurately.
- Automated checks per run: document scroll width vs viewport width (with the
  offending elements identified), interactive-element hit-box sizes, image
  natural size vs displayed size and aspect-ratio distortion, count of
  `[data-reveal]` blocks still transparent after load, console errors, failed
  requests, HTTP status codes, request counts, encoded transfer sizes, paint and
  load timings.
- Static checks over the whole tree: internal links, section anchors, CSS/JS/image
  references, `mailto:`/`tel:`/WhatsApp destinations, canonical URLs, robots
  directives, JSON-LD parse validity, sitemap coverage, heading hierarchy.

### Conditions that limit these numbers

- **Local lab measurements, not production.** Everything was measured against a
  local HTTP server in a container. These figures show the *relative* effect of
  the changes; they are not real-user performance and should not be quoted as
  such.
- **Third-party resources were unreachable** from the audit container
  (Google Fonts, the Font Awesome CDN, the Google Maps embed). They were aborted
  deliberately and identically in both the before and after runs, so the
  comparison is fair, but every payload figure is **first-party only** and
  excludes those three.
- **No Lighthouse scores, no Core Web Vitals field data and no real-device
  testing** were produced. None are claimed anywhere in this report.
- Cumulative Layout Shift was instrumented but is not reported: with
  third-party fonts blocked, the font-swap shift that a real visitor would
  experience does not occur, so the local figure would be misleading.

---

## 3. Company and contact consistency

### Final values

| Field | Value | Where it is used |
|---|---|---|
| Company name | **DeepAbi Innovations** | Footer copyright, structured data, page titles and descriptions. "DeepAbi" remains in use as the short brand name (logo alt text, `og:site_name`, body copy) — that is intentional and was left alone. |
| **Primary email** | **hello@deepabi.com** | Top contact bar, desktop and mobile navigation, floating contact button, footer "Email" row, Contact page email card (first line), all enquiry CTAs, Organization structured data, the contact form's compose target. |
| **Secondary email** | **deepabi.tech@gmail.com** | Footer "Technical" row and the Contact page email card (second line, labelled *Technical*). Restored — see the correction note below. |
| Phone 1 (primary) | **+91 89460 97125** — `tel:+918946097125` | Top bar, mobile menu, footer, Contact page, floating button, structured data. Also the WhatsApp number. |
| Phone 2 (secondary) | **+91 90255 48401** — `tel:+919025548401` | Footer, Contact page, structured data. |
| WhatsApp | `https://wa.me/918946097125` | Top bar, mobile menu, footer, Contact page, floating button. |

### Correction: the secondary email had been removed

A previous instruction in this project was to consolidate to a single address,
and `deepabi.tech@gmail.com` was removed site-wide as a result. That instruction
has since been superseded: `hello@deepabi.com` is the **new primary**, not the
only address. The secondary address has been **restored** to its original two
locations, with its original wording:

- the footer contact list, as a **Technical** row beneath the Email row;
- the Contact page email card, as a second line labelled **Technical**.

It is now defined as `EMAIL_SECONDARY` in `scripts/build_site.py` alongside
`EMAIL_PRIMARY`, with a comment stating that the two must not be collapsed.
No other DeepAbi address was altered, and no customer or example address
anywhere on the site was touched.

### Verification counts across all 17 pages

| Token | Occurrences |
|---|---|
| `DeepAbi Innovations` | 249 |
| `DeepAbi Technologies` (obsolete) | **0** |
| `hello@deepabi.com` | 121 |
| `deepabi.tech@gmail.com` | 34 |
| `tel:+918946097125` | 65 |
| `tel:+919025548401` | 33 |
| `wa.me/918946097125` | 49 |

Surfaces individually confirmed: top contact bar · desktop navigation ·
Services mega-menu · mobile navigation and services accordion · footer contact
list · footer service links · Contact page form and info card · floating contact
button · all eight service pages · Projects · Privacy · Terms · accessible
labels (`aria-label` on the floating buttons and social links) · `mailto:`,
`tel:` and WhatsApp hrefs · page titles, meta descriptions, Open Graph and
Twitter metadata · JSON-LD `Organization` block · the generator constants.

`tel:` and WhatsApp destinations are in international format
(`+918946097125`); readable spacing is preserved separately for display.

### Image-embedded branding

The logo and icon assets under `assets/images/logos/` and
`assets/images/logos_icons/` are image files. Their contents were **not**
inspected character by character and no text replacement can affect them. If any
of them contains an older company name or an old contact detail rendered into
the artwork, that is **not** corrected by this work and needs a new asset. This
is stated as a limitation, not as a finding — no such problem was observed, but
none was ruled out either.

---

## 4. Project structure

### Before

```
/  (deployable root)
   17 × *.html                    generated pages
   README.md  DEPLOYMENT.md  CHANGELOG.md
   AUDIT_REPORT.md  SERVICE_PAGES_IMPLEMENTATION.md    <- dev docs in the web root
   LICENSE  robots.txt  sitemap.xml  site.webmanifest
   assets/images/<group>/<format>/     27.0 MB
   css/common.css + css/pages/*.css    (service.css unused)
   js/common.js  + js/pages/*.js       (services.js unused)
   scripts/build_site.py, scripts/generate_images.py
   scripts/pages/build_*.py            (service_data.py unused)
```

### After

```
/  (deployable root)
   17 × *.html                    generated pages
   README.md                      rewritten: what this is, how to build, where things live
   LICENSE  robots.txt  sitemap.xml  site.webmanifest
   assets/images/<group>/<format>/     14.4 MB   (47% smaller, same images)
   css/  js/  scripts/            unchanged layout
   docs/                          NEW — developer documentation
        BUILD.md                  NEW — authoritative files, build steps, safety rules
        DEPLOYMENT.md             moved from the root
        CHANGELOG.md              moved from the root
        AUDIT_REPORT.md           moved from the root (historical)
        SERVICE_PAGES_IMPLEMENTATION.md   moved from the root (historical)
   reports/                       NEW — this report; not deployed
```

The existing architecture was kept deliberately: shared styles and scripts stay
separated from page-specific ones (`css/common.css` vs `css/pages/<page>.css`,
`js/common.js` vs `js/pages/<page>.js`), assets stay grouped by purpose then
format, and generators stay in `scripts/pages/`. No public page URL changed, no
file was renamed, and no framework was introduced.

### Obsolete files — confirmed unused, awaiting deletion

Each was checked for references across HTML, CSS, JavaScript, the generators and
the documentation before being listed. **They are still present**: this session
can write files to the machine but cannot delete them, and no delete-permission
tool was available. They are listed here for manual removal.

| File | Evidence | Recommendation |
|---|---|---|
| `css/pages/service.css` | 0 references anywhere. Superseded by `css/pages/services.css`. | Delete |
| `js/pages/services.js` | 0 code references. A comment-only stub left by a reverted change. | Delete |
| `scripts/pages/service_data.py` | 0 imports. A data module from an abandoned generator approach. | Delete |
| `AUDIT_REPORT.md`, `CHANGELOG.md`, `DEPLOYMENT.md`, `SERVICE_PAGES_IMPLEMENTATION.md` (root copies) | Now duplicated in `docs/`. | Delete the root copies once `docs/` is confirmed |
| `scripts/__pycache__/` | Python bytecode cache. | Delete and add to `.gitignore` |

### Deliberately kept

- **`service-detail.html`** — a retired public URL. It is a 1 KB stub carrying
  `noindex, follow`, a canonical pointing at `service-website-development.html`,
  a meta refresh and a visible fallback link. It is **not** unused: it is a
  compatibility redirect for anything still linking to the old address. It is
  correctly excluded from `sitemap.xml`.
- **`scripts/generate_images.py`** — not part of the page build, and not run
  during this work. It is retained as the original image-derivative tool, but
  **it can overwrite the optimised assets**, so `docs/BUILD.md` now warns
  against running it as part of a normal edit.
- **All original image masters** — every image was resized in place to a 1200px
  longest side; the higher-resolution originals remain in git history and can be
  recovered from there if a larger source is ever needed.

---

## 5. Source and generation workflow

**Authoritative:** `scripts/build_site.py` (shared head, navigation, mega-menu,
footer, floating contact launcher, contact constants, the `picture()` helper),
`scripts/pages/build_*.py` (one per page or page family), all CSS, all
JavaScript, all images, and `docs/`.

**Generated output, not authoritative:** every `*.html` in the project root,
plus `sitemap.xml`, `robots.txt` and `site.webmanifest`.

### The defect this workflow had

Several generated pages had been edited by hand and the edits were never mirrored
back into the generators. Running a generator therefore silently reverted
approved content. This was **reproduced and measured** during the audit: a full
rebuild reverted, on the home page alone, the featured success story (from the
approved *Commercial Hardware & Industrial Supply* story back to a retired
*Card Session* one), the "Built & Tested Across All Devices" section heading and
copy, the launch year, the featured capability list, the approved hero image
dimensions, and five eyebrow labels the design had deliberately commented out.
The About and Technologies pages lost six more eyebrow labels between them, and
four pages regained meta keywords that had been removed.

### What was done about it

Every one of those differences was carried back into the generator that produces
the page — including the commented-out eyebrow labels, each of which now sits
behind a comment in the generator source saying it is intentional and must not
be uncommented. All ten generators were then run and every page diffed against
the approved version. The result: **the only differences are the intended ones**
listed in §9. A rebuild is now safe and repeatable.

### How to edit safely from now on

1. Change the **generator**, never the generated `.html`.
2. Run the generator, then read `git diff` for that page in full.
3. If the diff contains anything you did not intend, the generator has drifted
   from the approved page — fix the generator rather than re-editing the HTML.
4. Contact details are changed in exactly one place: the constants at the top of
   `scripts/build_site.py`.

Full details in **`docs/BUILD.md`**.

---

## 6. Responsive findings and fixes

### Horizontal overflow

**None found, before or after.** Across all 107 page × viewport runs, at 360,
390, 768, 1024, 1366 and 1440 pixels, the document scroll width never exceeded
the viewport width. The check identified offending elements by tag and class
where overflow occurred, and it never fired. The Projects filter strip, which
runs edge-to-edge on mobile using negative margins, was specifically confirmed
not to widen the page: its −16px margins cancel the container's 16px padding
exactly at that breakpoint, and it scrolls inside its own container.

### Issues found and fixed

| # | Issue | Where | Fix |
|---|---|---|---|
| R1 | Two content blocks inside the first screen stayed blank after load — the section heading and the device-preview row | `projects.html`, 390px | The scroll-reveal script now reveals anything already inside the viewport on the next animation frame, rather than waiting for the observer |
| R2 | Carousel dots were **9 × 9 px** — the smallest controls on the site, below the 24 × 24 minimum and awkward to hit on a phone | `index.html` testimonials | Each button is now a 24 × 24 target with the dot drawn as a pseudo-element inside it. The visual appearance is unchanged |
| R3 | "Learn more" links on the What We Build cards are `opacity: 0` until the card is hovered — on a touch screen the hover never happens, so the link was invisible but tappable | `index.html` | Shown by default under `@media (hover: none)`; also given a 24px minimum height |
| R4 | Heading levels skipped a rank in 16 of 17 pages (h2 → h4 in every process track, h2 → h5 in every footer, h1 → h3 in the home hero cards, and more) | site-wide | Corrected to a continuous hierarchy. Each affected heading kept its exact visual size by moving the styling from the tag selector to a class — **no visual change** |
| R5 | Carousel dots had no visible focus ring | `index.html` | Focus-visible outline added |

### Verified after the fixes

- 0 horizontal overflow across 107 runs.
- 0 heading-level skips across all 17 pages; exactly one `<h1>` per page.
- No control smaller than 24 × 24 px remains except text links whose hit box is
  exactly 24 px tall, which meets the AA minimum.
- No image is distorted: displayed aspect ratio matches natural aspect ratio
  everywhere, so no crop or squash was introduced.
- 0 console errors on any page at any viewport (excluding the blocked
  third-party requests described in §2).

### The Projects featured success story

The *Commercial Hardware & Industrial Supply* story was treated as protected. Its
content, imagery, layout, links and behaviour are **byte-for-byte identical** to
the approved version — verified programmatically after every rebuild, alongside
the navbar and footer. No responsive defect was found in it, so no styling change
was needed. Its image file was resized in common with every other asset; the
composition, crop and aspect ratio are unchanged, and the rendered result is the
same picture.

One cosmetic issue in that section is **reported rather than fixed**: its
`.featured-list` bullet list is styled in `css/pages/home.css`, which
`projects.html` does not load, so the list renders unstyled on that page. Fixing
it would change the section's appearance, which was out of bounds. It is a
two-line CSS addition whenever you want it.

### Screenshots

Captured at 390 px, 768 px and 1366 px for Home, Services, a detail service page,
Projects and Contact — 15 images, included in the appendix of the PDF.

---

## 7. Loading and performance findings

### Diagnosed causes

| Cause | Evidence |
|---|---|
| **Scroll-reveal blanking** — `[data-reveal]{opacity:0}` applied unconditionally; content only appeared when an IntersectionObserver fired | With scripting unavailable: home 0/29 blocks visible, Services 0/10, Projects 0/9, About 0/11, Contact 0/3. With scripting working, 2 blocks inside the first screen on Projects were still transparent after load |
| **Images three to four times their display size** | `website-development-workspace.avif` 644 KB, drawn 453×302 from 2048×1143. `services-hero-illustration.avif` 248 KB at 497×355 from 1484×1060. `technology-stack-network.avif` 333 KB. Pattern repeated across the asset tree |
| **Home hero offered in a format larger than its fallback** | `deepabi-concept.avif` is 166 KB against 73 KB for the JPEG, so offering AVIF made the largest paint *heavier* |
| **Render-blocking third-party CSS** | Google Fonts and the Font Awesome CDN are two blocking stylesheets in `<head>` on every page |
| **No reduced-motion handling for entrance animations** | `prefers-reduced-motion` was respected by some scripts but not by the site-wide reveal animation |

### Changes made

1. **Reveal content is only hidden when scripting is actually available.** An
   inline script in `<head>` swaps `html.no-js` for `html.js`, and the
   `opacity: 0` rule is scoped to `.js [data-reveal]`. If the script never runs,
   nothing is hidden.
2. **Three-layer failsafe in `js/common.js`.** Anything already inside the
   viewport is revealed on the next animation frame; anything still hidden 2.5
   seconds after `load` is revealed outright; and browsers without
   IntersectionObserver get everything immediately.
3. **`prefers-reduced-motion: reduce` now disables the entrance animation
   entirely**, in both CSS and JavaScript — content is simply present.
4. **Every image capped at a 1200 px longest side**, re-encoded in place at high
   quality (AVIF q62, WebP q82, JPEG q84), aspect ratios preserved exactly. The
   largest display size anywhere on the site is about 560 CSS pixels, so 1200 px
   still covers a 2× screen with room to spare. 86 files changed.
5. **AVIF suppressed for the home hero only**, via a new `skip_formats` argument
   to `picture()`, because its AVIF encode is larger than its JPEG.
6. **Broken image reference fixed**: `services.html` pointed at
   `services/jpg/services-hero-illustration.jpg`, which does not exist. The
   generator correctly falls back to PNG; the stale HTML did not. Regenerated.

Not done, deliberately: no preloading was added, no dependency was introduced,
no image quality was noticeably reduced, and the third-party font/icon CSS was
left in place rather than deferred, which would have caused icons to pop in late.

### Measured results

Five representative pages, local HTTP, third-party blocked identically in both
runs, full-page scroll so that lazy images actually load. **First-party payload
only.**

| Page | Before | After | Change | Requests |
|---|---:|---:|---:|---:|
| index.html | 896 KB | 502 KB | **−44%** | 18 → 18 |
| services.html | 2,318 KB | 680 KB | **−71%** | 17 → 17 |
| service-web-applications.html | 649 KB | 310 KB | **−52%** | 13 → 13 |
| projects.html | 2,499 KB | 755 KB | **−70%** | 20 → 20 |
| contact.html | 97 KB | 101 KB | +4% | 9 → 9 |
| **Total (5 pages)** | **6,459 KB** | **2,347 KB** | **−64%** | — |

Contact grew by 4 KB: it has almost no imagery, and the added text is the honest
explanation of what the form does.

Home page payload by type: AVIF 508 → 193 KB, WebP 258 → 176 KB, CSS 68 → 70 KB,
JS 16 → 17 KB.

Whole asset tree: **27.0 MB → 14.4 MB (−47%)**.

Content visibility, home page, scripting unavailable:
**0 of 29 blocks visible → 29 of 29.**

Above-the-fold blocks still transparent after load, Projects at 390 px:
**2 → 0.**

Load timings were recorded but are not presented as a result: on a local server
with third-party requests blocked they sit between 90 ms and 210 ms both before
and after, which says more about the container than about the site. The payload
reduction is the real, transferable finding.

### Not verified

Server-side caching and compression could not be tested. The site is served as
static files and the audit ran against a plain local HTTP server with no
compression. Enabling gzip or Brotli and long-lived cache headers on the real
host would compound the payload reduction above; whether they are currently
enabled was not established.

---

## 8. Functional and SEO verification

| Check | Result |
|---|---|
| Internal page links | **0 broken** across all 17 pages |
| Section anchors (`#id`) | **0 broken**, including every mega-menu and quick-nav target |
| CSS / JS / image references | **1 broken before** (`services-hero-illustration.jpg`), **0 after** |
| Console errors | **0** on every page at every viewport (excluding blocked third-party hosts) |
| Failed requests / HTTP ≥ 400 | **0 first-party** |
| Canonical URLs | Correct on all 16 indexable pages; `service-detail.html` correctly canonicalises to `service-website-development.html` |
| Robots directives | 16 pages `index, follow`; `service-detail.html` `noindex, follow` — correct |
| `sitemap.xml` | 16 entries, all resolve to files on disk; the retired redirect is correctly excluded |
| `robots.txt` | Valid, allows all, points at the sitemap |
| JSON-LD | **All blocks parse as valid JSON.** Types in use: `Organization`, `WebSite`, `BreadcrumbList`, `Service`. Content agrees with the visible page — company name, both phone numbers and the primary email match what is rendered |
| Titles and descriptions | Unique on all 17 pages; titles 24–67 characters, descriptions 104–166 |
| Heading hierarchy | Exactly one `<h1>` per page; **0 level skips** (was 26 skips across 16 pages) |
| Demo destinations, Projects | All 24 demo cards are labelled **Planned Demo** with no button and no `href="#"`. No deployment URL exists anywhere in the project, so none is claimed |
| Contact actions | `mailto:` for both addresses, `tel:` for both numbers and the WhatsApp link were each verified present and correctly formatted on every surface |

### The contact form

**Before:** submitting displayed *"Message sent successfully! We'll be in touch
within one business day."* and reset the form. No network request was made. The
enquiry went nowhere and the visitor was told it had arrived.

**After:** the misleading behaviour is removed. Submitting now validates the
fields and opens the visitor's own email client with a pre-filled message
addressed to `hello@deepabi.com`, containing their name, email, phone, selected
service and message. The confirmation says: *"Your email app should now open with
this enquiry ready to send. If nothing opened, email hello@deepabi.com
directly."* The button reads **Compose Enquiry Email**, and the note beneath it
explains that nothing is sent until they send it, and points to the email, phone
and WhatsApp details alongside. The form is deliberately **not** reset, so if the
handoff fails the visitor's text is still on screen.

No external form service was added and no delivery is claimed. If a backend is
added later, `js/pages/contact.js` carries a comment saying to replace the
handoff with the real request and update the wording — and not to restore a
success message that no delivery backs.

### Preserved

The eight-service architecture, all existing SEO intent, the Services mega-menu
and mobile accordion, and the Projects featured success story. No FAQ,
testimonial, statistic, claim or marketing tool was added.

---

## 9. Change inventory

**37 files changed or added, 86 image files re-encoded.**

### Contact and company consistency
`scripts/build_site.py` — `EMAIL_SECONDARY` restored and documented; footer
Technical row restored · `scripts/pages/build_contact.py` — technical address
restored to the email card · `css/pages/contact.css` — role label styling

### Loading and performance
`css/common.css` — reveal scoped to `html.js`, reduced-motion rule ·
`js/common.js` — reveal failsafes, reduced-motion, viewport-first reveal ·
`scripts/build_site.py` — `html.no-js` + inline class swap; `picture()` gained
`skip_formats` · `scripts/pages/build_home.py` — hero AVIF suppressed ·
**86 image files** under `assets/images/` re-encoded at ≤1200 px

### Responsiveness and accessibility
`css/pages/home.css` — 24×24 carousel dots, focus ring, touch-visible card links,
heading class · `css/common.css`, `css/pages/about.css`, `css/pages/contact.css`,
`css/pages/service.css` — heading selectors moved from tag to class ·
`scripts/pages/build_home.py`, `build_about.py`, `build_contact.py`,
`build_website_development.py`, `build_service_pages.py` — heading levels

### Contact form honesty
`js/pages/contact.js` — rewritten · `scripts/pages/build_contact.py` — button
label and explanatory notes

### Generator/output alignment
`scripts/pages/build_home.py` — featured story, section copy, launch year,
capability list, hero dimensions, eyebrow labels, keywords ·
`scripts/pages/build_about.py`, `build_technologies.py` — eyebrow labels,
keywords · `scripts/pages/build_contact.py` — keywords

### Structure and documentation
`README.md` rewritten · `docs/BUILD.md` new · `docs/DEPLOYMENT.md`,
`docs/CHANGELOG.md`, `docs/AUDIT_REPORT.md`,
`docs/SERVICE_PAGES_IMPLEMENTATION.md` copied from the root ·
`reports/` created with this report

### Regenerated pages (16)
`index` · `about` · `contact` · `projects` · `technologies` · `services` ·
`service-website-development` · the seven other `service-*` pages · `privacy` ·
`terms`. `service-detail.html` is unchanged.

### Not changed
Every image's composition and crop · the Projects featured success story ·
the navbar, Services mega-menu and footer structure · all public page URLs ·
`robots.txt`, `site.webmanifest`, `LICENSE`, `.git` and its configuration ·
`scripts/generate_images.py`

---

## 10. Remaining items

### Unresolved defects

| Item | Detail |
|---|---|
| **Contact form has no delivery backend** | The form composes an email in the visitor's client; DeepAbi receives nothing unless the visitor sends it. This is now stated honestly on the page, but it is not a working server-side enquiry pipeline. Fixing it needs a decision: a serverless function, a hosting provider's form handler, or accepting the mailto approach |
| **Obsolete files still on disk** | The three unused files and four duplicated root docs in §4 could not be deleted from this session. They are harmless but should be removed |
| **`.featured-list` unstyled on Projects** | The Projects featured story's bullet list is styled only in `home.css`, which that page does not load. Left alone to avoid altering the protected section |

### External limitations

- **No production measurement.** Everything is local-lab. Real-user performance,
  Lighthouse scores and Core Web Vitals remain unmeasured.
- **Third-party resources untested.** Google Fonts, the Font Awesome CDN and the
  Google Maps embed could not be reached from the audit container. Their real
  effect on first paint is unmeasured, and the Maps embed on the Contact page was
  never rendered.
- **Server configuration unverified.** Compression and cache headers on the live
  host could not be checked.
- **Logo and icon artwork not inspected for embedded text** (§3).

### Optional future improvements

1. **Serve responsive image sizes.** Images are now capped at 1200 px, but a card
   thumbnail drawn at 330 px still downloads a 1200 px file. Adding `srcset` with
   two or three widths would cut the remaining image weight substantially — the
   audit still flags 383 instances of an image being more than 2.6× its display
   size.
2. **Self-host the icon font and web fonts,** removing two render-blocking
   third-party stylesheets from every page.
3. **Publish real demos.** Every Projects card is currently a Planned Demo. Each
   entry has a `url` field: filling it in turns the card into a live one with the
   correct button label automatically.
4. **Replace the temporary demo imagery** — the Projects and service-page images
   are existing assets re-used as stand-ins, documented in the generators.
5. **Add `.gitignore` for `__pycache__`.**

---

## 11. Maintenance guidance

**Changing a contact detail.** Edit the constant in `scripts/build_site.py`
(`EMAIL_PRIMARY`, `EMAIL_SECONDARY`, `PHONE_1_*`, `PHONE_2_*`), then rebuild every
page. Never hard-code an address or number in a page generator. Keep the
`*_DISPLAY` and `*_TEL` values in step: display carries readable spacing, `_TEL`
carries the international format used by `tel:` and WhatsApp links. The two email
addresses have different jobs — do not collapse them.

**Adding a page.** Copy the nearest generator in `scripts/pages/`, give it a
unique title, description and canonical path, add it to the `pages` list in
`build_legal_and_seo.py` so it reaches the sitemap, and add a page stylesheet
under `css/pages/` only if it needs one.

**Adding an image.** Put it in `assets/images/<group>/<format>/<name>.<ext>` and
reference it by name — `picture()` finds every format present. Keep the longest
side at or below 1200 px. Do not run `scripts/generate_images.py` casually: it
can overwrite optimised assets.

**Never edit a root `.html` file by hand.** It is generated output. A hand-edit
survives until the next build and then vanishes — which is exactly how the home
page came to have a retired featured story waiting to reappear.

**Before publishing, re-run these checks.** Regenerate everything and read
`git diff` in full; confirm every internal link, anchor and asset path resolves;
load the site with JavaScript disabled and confirm all content is visible; check
360 px, 768 px and 1366 px for horizontal overflow; confirm the contact form
still claims only what is true.

**Do not reintroduce these.** Unconditional `opacity: 0` on content that a script
must reveal. A success message the site cannot back with a delivery. Images
shipped at three times their display size. Hand-edits to generated HTML.

---

*Prepared from measurements taken in a headless Chromium container against a
local copy of the site. Local lab measurements do not establish real-user
production performance. No Lighthouse score, Core Web Vitals result or
real-device test appears in this report because none was performed.*
