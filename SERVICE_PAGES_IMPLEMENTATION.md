# Service architecture consolidation — implementation summary

Date: 2026-09-09
Scope: local working copy at `C:\work-station\DeepAbi-Innovations\DeepAbi`. **Nothing was deployed or published.**

---

## 1. Naming and contact consolidation

- `DeepAbi Technologies` → **`DeepAbi Innovations`** everywhere it appeared (footer copyright on all 15 content pages). 0 occurrences remain.
- Single public email: **`hello@deepabi.com`**. `deepabi.tech@gmail.com` removed from:
  - the duplicate "Technical" row in the footer contact list (all pages),
  - the second address line in the Contact page's Email card.
  - 0 occurrences of `gmail` remain in any HTML file.
- Source of truth is now `scripts/build_site.py` → `EMAIL_PRIMARY`. The `EMAIL_SECONDARY` alias was deleted rather than left pointing at the same address.

## 2. Website Development page consolidated

`service-website-development.html` is now the single destination for this service.

- **Removed:** the "See It In Detail" section and its `View Full Service Detail` button.
- **Migrated in** from the old `service-detail.html`, verbatim copy and markup, with the eyebrow labels (`Benefits` / `Process` / `Related Services`) stripped:
  - `What you get with a DeepAbi build` — 4-card grid
  - `How a website development project runs` — 7-step process track
  - `Often paired with Website Development` — 3 cards
- The legacy FAQ / "Common questions" section was **not** migrated, and its `FAQPage` structured data is gone with it.
- The three related-service cards now link to the in-page anchors `#website-maintenance`, `#seo`, `#performance-optimization`, which exist on this page.
- All eight original sub-service blocks and the pill quick-nav are unchanged.

### `service-detail.html` retired

Overwritten with a minimal stub: `robots: noindex, follow`, `canonical` → `service-website-development.html`, a meta refresh, a JS `location.replace`, and a visible fallback link. It carries no nav, footer, CSS or JS. It is also removed from `sitemap.xml`.

**Manual step for you:** the file can be deleted outright from the repo/server once you're satisfied nothing external links to it. I can't delete files on your machine from here, so I overwrote it instead.

## 3. Seven dedicated service pages built

Replacing the 478-byte redirect stubs:

| Page | Title length | Meta desc length |
|---|---|---|
| `service-web-applications.html` | 60 | 166 |
| `service-mobile-applications.html` | 55 | 166 |
| `service-desktop-applications.html` | 64 | 160 |
| `service-custom-software.html` | 60 | 155 |
| `service-saas-products.html` | 57 | 151 |
| `service-ai-automation.html` | 61 | 160 |
| `service-software-maintenance.html` | 67 | 161 |

Each page uses the same component family as the Website Development page — gradient hero with breadcrumb, alternating `.service-block` rows, a `.grid-4` deliverables set, a `.process-track`, a `.grid-3` related-services set, and a closing CTA. **No new CSS or JS was written**; every class already existed in `css/common.css`, `css/pages/services.css` and `css/pages/service-detail.css`.

What differs per page: H1, lede, three content blocks, four deliverables, seven process steps, three related services, CTA wording, hero image, title, description and keywords. Titles and descriptions are unique across all 17 pages (checked programmatically — 0 duplicates).

**Content honesty:** copy describes what *can* be built and the business problem it addresses. No completed products, client names, results, metrics, testimonials, certifications, team size or years of experience are claimed on any page.

## 4. Service journey connected

Every entry point now lands on a real dedicated page instead of a fragment:

- **Navbar mega-menu** (desktop) — 8 items → `service-<slug>.html`
- **Mobile services accordion** — 8 items → `service-<slug>.html`
- **Home → What We Build** — 8 "Learn more" links → `service-<slug>.html`
- **Services page** — all 8 block CTAs → `service-<slug>.html`
- **Footer services column** — Website Development / Web Applications / Mobile Applications / Custom Software → dedicated pages; "All Services" still → `services.html`
- The eight `#slug` anchors on `services.html` are retained, so any old bookmark still resolves.

`sitemap.xml`: now 16 URLs — the 8 service pages added at priority 0.8/0.9, `service-detail.html` removed.

## 5. Imagery — all temporary, all existing assets

No image was generated or downloaded. Every service page reuses an existing project asset as a stand-in:

| Page | Image | Folder |
|---|---|---|
| Web Applications | `web_application_development` | `assets/images/projects` |
| Mobile Applications | `mobile_portrait` | `assets/images/projects` |
| Desktop Applications | `desktop` | `assets/images/projects` |
| Custom Software | `mission` | `assets/images/about` |
| SaaS Products | `enterprise_website_framework` | `assets/images/projects` |
| AI & Automation | `technology-stack-network` | `assets/images/technology` |
| Software Maintenance | `website_maintenance` | `assets/images/services` |
| Website Development (hero) | `corporate_website_design` | `assets/images/projects` |

Each mapping lives as a single `(name, folder)` pair in `scripts/pages/build_service_pages.py`. Swapping in a real photo later means changing that pair and its alt text — nothing else.

## 6. SEO

Per page: unique title, unique meta description, canonical, OG tags, page-specific keyword additions on top of the shared local set (Chennai / Mogappair / Ambattur / Anna Nagar), and JSON-LD `Service` + `BreadcrumbList` with `areaServed`. No fabricated business information was added. **No tracking pixels, analytics, advertising scripts, cookie tools or new dependencies were installed** — Font Awesome 6.5.1, already present, is the only external resource.

## 7. Generators updated with the output

Both sides are in sync. Changed:

- `scripts/build_site.py` — name, single email, footer contact row, mega-menu + footer service hrefs
- `scripts/pages/build_home.py` — What We Build hrefs
- `scripts/pages/build_services.py` — 8 block CTAs
- `scripts/pages/build_website_development.py` — section removed, three sections migrated
- `scripts/pages/build_service_pages.py` — the seven pages (new)
- `scripts/pages/build_service_detail.py` — now emits the redirect stub
- `scripts/pages/build_legal_and_seo.py` — sitemap list
- `scripts/pages/build_contact.py` — single email in the contact card

Where a deployed page had hand-edits the generator no longer reproduces (`index`, `about`, `contact`, `projects`, `technologies`, `privacy`, `terms`), I patched the deployed HTML surgically rather than regenerating it, and mirrored the same change into the generator. Verified: those files differ from their previous versions **only** in the link, name and email lines listed above — no design, layout, copy or spacing changes.

`services.html` and `service-website-development.html` were safe to regenerate: the generator reproduced the deployed files byte-for-byte before my edits, so their diffs contain only intended changes.

## 8. Verification — what was and was not done

**Done (static, programmatic):**

- Link audit across all 17 pages: **0 broken page links, 0 broken anchors.** Every `service-*.html` is reachable from both the home page and the Services page.
- Asset audit: every referenced CSS, JS and image path resolves against the real files in your folder, with one pre-existing exception noted below.
- Structure/accessibility: exactly one `<h1>` per page; `lang="en"`; `width=device-width` viewport; **every `<img>` has an `alt` and explicit `width`/`height`** (so no layout shift); hero images `loading="eager"`, all below-fold images `loading="lazy"`; AVIF → WebP → JPEG `<picture>` sources preserved.
- Heading order: the new pages contain one `h2 → h4` step (the process track), which is the same pattern the existing home and services pages already use. Not introduced by this work, but worth tidying site-wide at some point.

**Not done — stated plainly:**

- **No browser rendering was performed.** I could not open the pages in a browser from this session, so I have **not** visually verified responsive behaviour at any breakpoint, and I have **no** Lighthouse, PageSpeed or contrast-ratio measurements. Any number I gave you would be invented. The new pages reuse only existing, already-responsive components, which is a good reason to expect them to behave — not evidence that they do. Please open the seven new pages at ~375px, ~768px and ~1200px before publishing.
- **The contact form still does not send anything.** `js/pages/contact.js` calls `preventDefault()`, checks validity, shows a success toast and resets the form. There is no network request. A visitor who submits it sees "sent" and you receive nothing. No claim about enquiry delivery is made on any page, and I did not add a form provider. This needs a decision from you.
- Pre-existing: `services.html` references `assets/images/services/jpg/services-hero-illustration.jpg` as the `<img>` fallback, and only `.png`, `.webp` and `.avif` exist. Modern browsers take the AVIF/WebP `<source>` so it is invisible in practice, but the fallback is dead. Not changed — it predates this task.
- `js/pages/services.js` is an orphaned comment-only stub from an earlier reverted change. Nothing loads it; safe to delete.

## 9. Files changed

**Written to your folder (26):** `index`, `about`, `contact`, `projects`, `technologies`, `privacy`, `terms`, `services`, `service-website-development`, `service-detail`, and the 7 new `service-*` pages; `sitemap.xml`; 8 generator scripts under `scripts/`.

**Not touched:** any CSS, any JS, any image, `robots.txt`, `site.webmanifest`, `.git`, `.gitignore`, GitHub configuration, deployment configuration, package dependencies, developer tooling, README.
