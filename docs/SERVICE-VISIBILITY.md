# Service visibility — temporary website-only mode

**Current state: Website Development only.** The other seven services are
hidden from the public website. Nothing has been deleted: every generator,
dedicated page, demo entry, image and piece of copy for them is still in the
project and still builds.

---

## The one place visibility is decided

`scripts/build_site.py` → **`SERVICE_REGISTRY`**

```python
SERVICE_REGISTRY = [
    {"slug": "website-development",  ... "public": True},
    {"slug": "web-applications",     ... "public": False},
    {"slug": "mobile-applications",  ... "public": False},
    {"slug": "desktop-applications", ... "public": False},
    {"slug": "custom-software",      ... "public": False},
    {"slug": "saas-products",        ... "public": False},
    {"slug": "ai-automation",        ... "public": False},
    {"slug": "software-maintenance", ... "public": False},
]
```

`public` is the only switch. Everything below is derived from it, so a service
can never be half-hidden — advertised in one place and missing from another.

`WEBSITE_ONLY_MODE` is **derived, not set**: it is simply
`PUBLIC_SERVICE_SLUGS == ["website-development"]`. Make any second service
public and the site returns to its multi-service presentation on its own.

---

## To restore all eight services

1. Open `scripts/build_site.py`.
2. Set `"public": True` on all eight entries in `SERVICE_REGISTRY`.
3. Rebuild every page:

```
cd scripts/pages
python3 build_home.py
python3 build_about.py
python3 build_contact.py
python3 build_projects.py
python3 build_technologies.py
python3 build_services.py
python3 build_website_development.py
python3 build_service_pages.py
python3 build_service_detail.py
python3 build_legal_and_seo.py
```

4. Check `git diff` — the eight services should return to navigation, the
   Services page, the home grid, Projects, the Contact selector, the sitemap
   and the structured data, and the `noindex` should disappear from the seven
   service pages.

That is the whole procedure. No content needs rewriting and no file needs
restoring from anywhere.

## To restore one service at a time

Set `"public": True` on just that service and rebuild. It reappears in every
surface by itself. This is the expected path as DeepAbi's delivery capability
grows — bring a service back the week you can actually deliver it.

---

## What each flag controls

| Surface | How it is filtered |
|---|---|
| Desktop Services mega menu | `services_menu_items()` in `build_site.py` |
| Mobile Services accordion | the same function |
| Footer services column | `_footer_service_links()`, same function |
| Mega-menu heading, subtitle and CTA wording | `SERVICES_MENU_TITLE` / `_SUBTITLE` / `_FOOT` / `_CTA` |
| Services page sections and quick-nav | `VISIBLE` in `build_services.py` |
| Services page hero, CTA and metadata | `WEBSITE_ONLY_MODE` branch in `build_services.py` |
| Home "What We Build" cards | `build_home.py` |
| Home hero sub-headline and meta description | `WEBSITE_ONLY_MODE` branch in `build_home.py` |
| Home `knowsAbout` structured data | `KNOWS_ABOUT` in `build_home.py` |
| About studio intro sentence | `studio_intro` in `build_about.py` |
| Projects demo categories, demo cards, filter bar, service index | `VISIBLE_CATEGORIES` / `VISIBLE_DEMOS` / `SINGLE_CATEGORY` in `build_projects.py` |
| Projects page metadata | `SINGLE_CATEGORY` branch in `build_projects.py` |
| Contact service selector | `build_contact.py` |
| `noindex` on hidden service pages | `is_service_public()` via `page(noindex=...)` |
| Sitemap entries | `build_legal_and_seo.py` |

---

## In website-only mode, menus show website sub-services

Collapsing an eight-item menu to one item would look broken. While Website
Development is the only public service, the navigation, the home grid and the
Services page overview show the eight offerings **inside** it instead, defined
in `WEBSITE_SUBSERVICES` (`build_site.py`):

Website Development · Landing Pages · Corporate Websites · Business Websites ·
Portfolio Websites · Website Maintenance · SEO · Performance Optimization

The first links to `service-website-development.html`; the rest link to their
sections on that page. These are real sections that already existed — nothing
was invented to fill the menu.

---

## How the hidden pages behave

- They **still exist** and still build: `service-web-applications.html` and the
  other six are regenerated on every build, with all their content.
- They are **reachable at their URLs**. This is deliberate: the task was to
  remove them from the public journey, not to add access control.
- They carry **`<meta name="robots" content="noindex, follow">`** — reversible,
  and `follow` is kept so crawlers still traverse their links.
- They are **absent from `sitemap.xml`**.
- **`robots.txt` is deliberately unchanged** and still allows everything. A
  page blocked in robots.txt can never be fetched, so its `noindex` would never
  be read and it could linger in search results. Do not add a `Disallow` for
  these pages.
- Their own related-service cards still point at each other. They are off the
  public journey and noindexed, and keeping those links intact means the set
  restores as a coherent whole.

---

## Rules when editing in this mode

- **Never hide a service with CSS.** Hidden services are filtered out during
  generation, so no markup for them reaches the page. A CSS-hidden link stays
  in the tab order and is still announced by screen readers, and would offer
  visitors something DeepAbi cannot currently deliver.
- **Never hard-code a service list in a page generator.** Read it from
  `SERVICE_REGISTRY` so the next visibility change does not need a hunt.
- **Keep visible copy honest.** If a sentence promises a hidden service, branch
  it on `WEBSITE_ONLY_MODE` rather than editing it permanently — that way it
  comes back with the service.
- **Leave the About journey timeline alone.** Its "Next: AI & Automation" and
  "Future Vision: Enterprise Software" entries describe DeepAbi's direction,
  not a current offer, and are explicitly labelled as future stages.
