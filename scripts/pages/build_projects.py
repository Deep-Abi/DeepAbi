"""Projects page.

Two halves, treated very differently.

1. PROTECTED — the page header, the Featured Success Story (Commercial
   Hardware & Industrial Supply) and the device-preview strip are reproduced
   here byte-for-byte from the deployed page. That featured story is real
   client work and must not be edited, restyled or re-worded. It had been
   hand-edited directly in projects.html and this generator had drifted away
   from it; the markup below is the deployed version, brought back in so a
   rebuild can no longer overwrite it.

2. REGENERATED — the "What We Build" area below the device strip. It is now a
   demo library organised around DeepAbi's eight primary services, built from
   the CATEGORIES and DEMOS lists at the top of this file.

Truthfulness rules baked into the data
--------------------------------------
* Nothing here is presented as completed client work. The one piece of real
  client work on this page is the protected featured story.
* No demo carries a testimonial, a client name, a project count or a
  performance claim. The old dummy quotes and the "case studies coming soon"
  line are gone.
* A demo is only shown with an action button when `url` holds a real, verified
  destination. At the time of writing NO deployment URLs exist anywhere in this
  project, so every demo renders as a clearly labelled "Planned Demo" with no
  button and no href. Publishing one later is a one-field edit: set `url` on
  that demo and the button appears with the `action` label already chosen.
* Urban Spice is deliberately absent: no project, image or reference for it
  exists in this repository, so listing it would be an invention.

TEMPORARY IMAGERY
-----------------
Every demo image is an existing local asset re-used as a stand-in, named by the
`img` (name, folder) pair. Replacing one with a real screenshot later means
changing that pair and the alt text, nothing else. No image was generated or
downloaded. Only names that have a .jpg fallback on disk are used, so the
<img> inside each <picture> always resolves.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture, PUBLIC_SERVICE_SLUGS

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.deepabi.com/"},
    {"@type": "ListItem", "position": 2, "name": "Projects", "item": "https://www.deepabi.com/projects.html"}
  ]
}
</script>'''


# ---------------------------------------------------------------------------
# The eight service categories. `label` is the filter button, `intro` is the
# one-line explanation shown under the bar when that category is selected.
# ---------------------------------------------------------------------------
# (key, Font Awesome icon, filter-button label, one-line intro)
CATEGORIES = [
    ("all", "fa-solid fa-border-all", "All Demos",
     "Demonstration projects across all eight DeepAbi services, built to show what each service produces. These are our own builds and concepts &mdash; the one piece of client work on this page is the featured story above."),
    ("website-development", "fa-solid fa-window-maximize", "Website Development",
     "Public-facing sites &mdash; business, restaurant, corporate and portfolio &mdash; built to explain what an organisation does and make contact straightforward."),
    ("web-applications", "fa-solid fa-table-columns", "Web Applications",
     "Browser-based systems people log into and work inside: bookings, dashboards, stock control and customer portals."),
    ("mobile-applications", "fa-solid fa-mobile-screen", "Mobile Applications",
     "Apps on a phone &mdash; for customers ordering and booking, and for staff working away from a desk."),
    ("desktop-applications", "fa-solid fa-desktop", "Desktop Applications",
     "Software installed on a specific machine: counter and billing tools, offline capture, and bulk file work."),
    ("custom-software", "fa-solid fa-code", "Custom Software",
     "Tools built around one particular business task, where no standard product fits the way the work actually runs."),
    ("saas-products", "fa-solid fa-cloud", "SaaS Products",
     "Subscription products with sign-up, separate customer workspaces, plans and an administration side for the product owner."),
    ("ai-automation", "fa-solid fa-robot", "AI &amp; Automation",
     "Repeated work handled automatically &mdash; routing enquiries, reading documents, preparing the same report every week."),
    ("software-maintenance", "fa-solid fa-screwdriver-wrench", "Software Maintenance",
     "Improvements to software that already exists: a documented fix, a compatibility update, a performance change. Not new builds."),
]

# Categories and demos are filtered by the SERVICE_REGISTRY. Hidden
# services keep every demo entry, image mapping and future deployment URL
# in the lists above - they are simply not rendered while hidden.
# ---------------------------------------------------------------------------
# Website Development sub-categories.
#
# These are the filters shown while Website Development is the only public
# service - they are subdivisions of ONE service, not the eight primary
# services, which stay governed by SERVICE_REGISTRY. A category only appears
# if at least one visible demo carries its slug in `subcat`, so the bar can
# never show an empty filter.
# ---------------------------------------------------------------------------
WEBSITE_CATEGORIES = [
    ("all", "All",
     "Every website demo we have built so far \u2014 business, corporate, landing page and portfolio work."),
    ("landing-pages", "Landing Pages",
     "Single-purpose pages built around one campaign goal, with nothing on them that does not serve it."),
    ("business-websites", "Business Websites",
     "A credible presence for service businesses: what you do, who you do it for, and how to get in touch."),
    ("corporate-websites", "Corporate Websites",
     "Structured sites for organisations with several departments, divisions or regions to represent."),
    ("portfolio-websites", "Portfolio Websites",
     "Image-forward sites for studios and individual professionals, where the work stays the focus."),
]

VISIBLE_CATEGORIES = [c for c in CATEGORIES
                      if c[0] == "all" or c[0] in PUBLIC_SERVICE_SLUGS]
CAT_LABEL = {k: label for k, _ic, label, _i in CATEGORIES}
DEMO_COUNT = {}  # filled once DEMOS is defined


# ---------------------------------------------------------------------------
# Demos. One entry = one distinct project.
#
#   url    : None until a real deployment exists. Set it and the card gains a
#            working button labelled with `action`.
#   action : which button label applies once `url` is set. One of
#            "View Live Demo", "View App Preview", "View Desktop Preview",
#            "View Automation Demo", "View Improvements".
#   img    : (asset name, folder) — temporary stand-in, see module docstring.
# ---------------------------------------------------------------------------
DEMOS = [
    # ----- Website Development -------------------------------------------
    # `subcat` places the demo in one of the WEBSITE_CATEGORIES filters above.
    # Entries marked "restored from git" were in the Projects page before the
    # service restructure (commit 02d4510); their title, description, image and
    # alt text are carried over verbatim. Their dummy client testimonials were
    # NOT restored - they were never real.
    dict(cat="website-development", subcat="business-websites",
         name="Local Business Website",
         desc="A single-location service business: what it does, the areas it covers, and a contact route that does not make the visitor hunt.",
         features=["Service and area pages", "Enquiry form and click-to-call", "Built for local search"],
         img=("local_services_website", "assets/images/projects"),
         alt="Design concept for a local services business website",
         action="View Live Demo", url=None),
    # restored from git (was "Professional Services Site")
    dict(cat="website-development", subcat="business-websites",
         name="Professional Services Site",
         desc="A polished small business website concept for a consulting practice.",
         features=["Practice and expertise pages", "Team and credentials section", "Enquiry-led contact route"],
         img=("professional_services_site", "assets/images/projects"),
         alt="Screenshot of a professional services website built by DeepAbi",
         action="View Live Demo", url=None),
    dict(cat="website-development", subcat="business-websites",
         name="Restaurant &amp; Caf&eacute; Website",
         desc="Menu, timings, location and a table enquiry, arranged so a hungry visitor on a phone finds all four in seconds.",
         features=["Menu with sections and pricing", "Table enquiry and map", "Photo-led mobile layout"],
         img=("business_websites", "assets/images/services"),
         alt="Design concept for a restaurant and cafe website",
         action="View Live Demo", url=None),
    dict(cat="website-development", subcat="corporate-websites",
         name="Corporate Website",
         desc="A multi-department organisation with several product lines, structured so each division has a home without fragmenting the brand.",
         features=["Department and division sections", "Careers and press areas", "Consistent brand system"],
         img=("corporate_website_design", "assets/images/projects"),
         alt="Design concept for a multi-department corporate website",
         action="View Live Demo", url=None),
    # restored from git (was "Enterprise Website Framework")
    dict(cat="website-development", subcat="corporate-websites",
         name="Enterprise Website Framework",
         desc="A scalable enterprise website framework designed for multi-region content.",
         features=["Multi-region content structure", "Shared component library", "Role-based content editing"],
         img=("enterprise_website_framework", "assets/images/projects"),
         alt="Screenshot of an enterprise website framework built by DeepAbi",
         action="View Live Demo", url=None),
    # restored from git (was "Landing Page Development")
    dict(cat="website-development", subcat="landing-pages",
         name="Landing Page Development",
         desc="High-conversion landing page development built for a single campaign goal.",
         features=["One goal, one call to action", "Fast mobile load", "Lead capture form"],
         img=("landing_page_development", "assets/images/projects"),
         alt="Screenshot of a product launch landing page built by DeepAbi",
         action="View Live Demo", url=None),
    dict(cat="website-development", subcat="portfolio-websites",
         name="Creative Portfolio Website",
         desc="An image-forward site for a studio or individual professional, where the work loads fast and stays the focus.",
         features=["Filterable work grid", "Case-study page template", "Optimised image delivery"],
         img=("portfolio_websites", "assets/images/services"),
         alt="Design concept for a creative portfolio website",
         action="View Live Demo", url=None),

    # ----- Web Applications ----------------------------------------------
    dict(cat="web-applications", name="Appointment Booking System",
         desc="Customers pick a slot from real availability; staff see the day's schedule and reschedule without a phone call.",
         features=["Live availability calendar", "Automatic confirmations", "Staff day and week views"],
         img=("professional_services_site", "assets/images/projects"),
         alt="Concept interface for a browser-based appointment booking system",
         action="View Live Demo", url=None),
    dict(cat="web-applications", name="Inventory &amp; Stock Dashboard",
         desc="Stock levels across locations on one screen, with low-stock alerts and a movement history behind every number.",
         features=["Multi-location stock view", "Low-stock alerting", "Movement audit trail"],
         img=("enterprise_website_framework", "assets/images/projects"),
         alt="Concept interface for an inventory and stock management dashboard",
         action="View Live Demo", url=None),
    dict(cat="web-applications", name="Customer Self-Service Portal",
         desc="A logged-in area where clients check their own orders, invoices and job status instead of emailing to ask.",
         features=["Per-customer login", "Order and invoice history", "Live job status"],
         img=("web_application_development", "assets/images/projects"),
         alt="Concept interface for a customer self-service portal",
         action="View Live Demo", url=None),

    # ----- Mobile Applications -------------------------------------------
    dict(cat="mobile-applications", name="Customer Ordering App",
         desc="Browse, order, pay and track — the repeat-purchase journey for a business whose customers come back weekly.",
         features=["Saved addresses and reorder", "Order tracking", "Push notifications"],
         img=("deepabi-mobile", "assets/images/home"),
         alt="Concept screens for a customer ordering mobile app",
         action="View App Preview", url=None),
    dict(cat="mobile-applications", name="Field Service Job App",
         desc="Today's jobs for an engineer on the road: directions, checklist, photos and a signature captured at the door.",
         features=["Job list and directions", "Photo and signature capture", "Works offline, syncs later"],
         img=("mobile_portrait", "assets/images/projects"),
         alt="Concept screens for a field service job mobile app",
         action="View App Preview", url=None),
    dict(cat="mobile-applications", name="Class &amp; Membership App",
         desc="A studio or club timetable in the member's pocket — book a place, see what is booked, get reminded.",
         features=["Timetable and booking", "Membership and credits", "Reminder notifications"],
         img=("deepabi-tablet", "assets/images/home"),
         alt="Concept screens for a class booking and membership mobile app",
         action="View App Preview", url=None),

    # ----- Desktop Applications ------------------------------------------
    dict(cat="desktop-applications", name="Counter Billing &amp; Receipt Tool",
         desc="Keyboard-first billing for a busy counter: scan or type, total, print, next customer — without waiting on a browser.",
         features=["Keyboard-driven entry", "Receipt printer support", "Day-end totals"],
         img=("desktop", "assets/images/projects"),
         alt="Concept interface for a desktop counter billing and receipt tool",
         action="View Desktop Preview", url=None),
    dict(cat="desktop-applications", name="Offline Data Collection Utility",
         desc="Records captured on a machine with no reliable connection, validated on entry and synced once the network returns.",
         features=["Validation before saving", "Local storage while offline", "Sync and conflict reporting"],
         img=("deepabi-desktop", "assets/images/home"),
         alt="Concept interface for an offline desktop data collection utility",
         action="View Desktop Preview", url=None),
    dict(cat="desktop-applications", name="Bulk Document Processor",
         desc="A folder of files in, a tidy set out: renamed, converted, merged or extracted in one pass instead of one at a time.",
         features=["Folder-level batch runs", "Rename, convert and merge", "Run log of what changed"],
         img=("performance_optimization", "assets/images/services"),
         alt="Concept interface for a desktop bulk document processing utility",
         action="View Desktop Preview", url=None),

    # ----- Custom Software -----------------------------------------------
    dict(cat="custom-software", name="Quotation &amp; Estimation Tool",
         desc="Priced from your own rate card and rules rather than a spreadsheet everyone keeps a private copy of.",
         features=["Rate card and margin rules", "Versioned quotes", "PDF output for the customer"],
         img=("team-collaboration", "assets/images/about"),
         alt="Concept interface for a quotation and estimation tool",
         action="View Live Demo", url=None),
    dict(cat="custom-software", name="Job Tracking System",
         desc="Every job from enquiry to completion, with an owner at each stage and an answer to &ldquo;where is it now?&rdquo; that does not require asking.",
         features=["Stage-by-stage ownership", "Deadline and overdue views", "History on every job"],
         img=("tablet_portrait", "assets/images/projects"),
         alt="Concept interface for a job tracking system",
         action="View Live Demo", url=None),
    dict(cat="custom-software", name="Multi-Stage Approval Workflow",
         desc="A request that needs three sign-offs in the right order, with approval limits applied by the system rather than remembered.",
         features=["Sequential and parallel approvals", "Value-based approval limits", "Full decision audit trail"],
         img=("corporate_websites", "assets/images/services"),
         alt="Concept interface for a multi-stage approval workflow tool",
         action="View Live Demo", url=None),

    # ----- SaaS Products --------------------------------------------------
    dict(cat="saas-products", name="Subscription Product Starter",
         desc="The parts a product needs before its first paying customer: sign-up, plan selection, payment and plan changes.",
         features=["Self-serve onboarding", "Plans, upgrades and cancellation", "Billing gateway integration"],
         img=("website-development-workspace", "assets/images/services"),
         alt="Concept interface for a subscription product sign-up and billing flow",
         action="View Live Demo", url=None),
    dict(cat="saas-products", name="Team Workspace &amp; Admin Console",
         desc="Each customer organisation gets its own workspace and members; the product owner gets a console to support them.",
         features=["Separate workspace per customer", "Invitations, roles and permissions", "Owner console for support"],
         img=("deepabi-concept", "assets/images/home"),
         alt="Concept interface for a multi-workspace SaaS administration console",
         action="View Live Demo", url=None),

    # ----- AI & Automation ------------------------------------------------
    dict(cat="ai-automation", name="Enquiry Routing Automation",
         desc="An enquiry arrives, gets logged and categorised, reaches the right person and is acknowledged — with nobody watching an inbox.",
         features=["Multi-channel intake", "Category and owner assignment", "Automatic acknowledgement"],
         img=("technology-stack-network", "assets/images/technology"),
         alt="Concept diagram of an automated enquiry routing workflow",
         action="View Automation Demo", url=None),
    dict(cat="ai-automation", name="Invoice &amp; Document Extraction",
         desc="Supplier invoices read automatically, the fields that matter pulled out, and anything uncertain flagged for a person.",
         features=["Field extraction from PDFs", "Confidence flagging", "Human review before commit"],
         img=("landing_page", "assets/images/services"),
         alt="Concept interface for automated invoice and document data extraction",
         action="View Automation Demo", url=None),
    dict(cat="ai-automation", name="Scheduled Report Automation",
         desc="The Monday figures currently assembled by hand from three systems, compiled on schedule and sent out.",
         features=["Pulls from multiple sources", "Runs on a fixed schedule", "Alerts when a source fails"],
         img=("seo", "assets/images/services"),
         alt="Concept interface for a scheduled reporting automation",
         action="View Automation Demo", url=None),

    # ----- Software Maintenance -------------------------------------------
    # These are examples of improving something that already exists, not new
    # builds. Each is framed as a documented change, not as a product.
    dict(cat="software-maintenance", name="Booking Site: Compatibility Update",
         desc="A worked example of bringing an ageing booking site back into line with current browsers and a supported library set.",
         features=["Dependency upgrade path", "Cross-browser retest", "Change log of what moved"],
         img=("website_maintenance", "assets/images/services"),
         alt="Concept illustration of a compatibility update to an existing booking website",
         action="View Improvements", url=None),
    dict(cat="software-maintenance", name="Dashboard: Performance Improvement",
         desc="A worked example of a reporting screen that slowed as data grew, traced to its queries and indexes rather than re-built.",
         features=["Query and index profiling", "Before and after timings recorded", "No feature change required"],
         img=("web_application_development", "assets/images/projects"),
         alt="Concept illustration of a performance improvement to an existing reporting dashboard",
         action="View Improvements", url=None),
    dict(cat="software-maintenance", name="Enquiry Form: Documented Bug Fix",
         desc="A worked example of a fault reported, reproduced, traced to its cause and fixed — with the reasoning written down.",
         features=["Reproduction steps recorded", "Root cause, not a workaround", "Regression test added"],
         img=("landing_page_development", "assets/images/projects"),
         alt="Concept illustration of a documented bug fix to an existing enquiry form",
         action="View Improvements", url=None),
]


WEBSITE_CAT_LABEL = {k: label for k, label, _i in WEBSITE_CATEGORIES}


def _card_cat(d):
    """What the filter buttons match against. While Website Development is the
    only public service the filters are its sub-categories, so cards are keyed
    by `subcat`; otherwise they are keyed by the primary service."""
    if SUBCATEGORY_MODE and d.get("subcat"):
        return d["subcat"]
    return d["cat"]


def _card_tag(d):
    """The label printed on the card. The sub-category is the more useful of
    the two when every card belongs to the same service."""
    if SUBCATEGORY_MODE and d.get("subcat"):
        return WEBSITE_CAT_LABEL[d["subcat"]]
    return CAT_LABEL[d["cat"]]


def demo_card(d):
    """One demo. Reuses the page's existing .project-card / .mock-browser
    components; only the body below the image is new."""
    name, folder = d["img"]
    feats = "".join(f"<li>{f}</li>" for f in d.get("features", []))
    feats_html = f'\n            <ul class="pf-feats">{feats}</ul>' if feats else ""

    if d.get("url"):
        badge = '<span class="launch-badge">Live</span>'
        action = (f'\n            <a class="btn btn-secondary pf-action" href="{d["url"]}"'
                  f' target="_blank" rel="noopener noreferrer">{d["action"]}'
                  f' <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a>')
    else:
        # No verified destination exists, so there is no button and no href.
        badge = '<span class="coming-soon-badge">Planned Demo</span>'
        action = ('\n            <p class="pf-status"><i class="fa-solid fa-clock" aria-hidden="true"></i>'
                  ' Planned demo &mdash; not yet built or published.</p>')

    return f'''
        <article class="project-card pf-card" data-cat="{_card_cat(d)}">
          <div class="mock-wrap">{badge}
            <div class="mock-browser"><div class="mock-browser-bar"><span></span><span></span><span></span></div>
            {picture(name, d["alt"], 1100, 620, folder, css_class="mock-browser-body-img")}
            </div>
          </div>
          <div class="project-card-body">
            <span class="tag">{_card_tag(d)}</span>
            <h3 class="pf-card-title">{d["name"]}</h3>
            <p class="pf-card-desc">{d["desc"]}</p>{feats_html}{action}
          </div>
        </article>'''


VISIBLE_DEMOS = [d for d in DEMOS if d["cat"] in PUBLIC_SERVICE_SLUGS]

for _d in VISIBLE_DEMOS:
    DEMO_COUNT[_d["cat"]] = DEMO_COUNT.get(_d["cat"], 0) + 1


def category_card(key, icon, label, intro):
    """One of the eight service cards shown in the All Demos view.

    Deliberately the SAME component as a demo card — the .project-card frame,
    the mock-browser image, the tag and the body — so the index reads as part
    of this page rather than borrowing the home page's icon-tile style. The
    only difference is the footer line, which counts the demos inside instead
    of showing a demo status.

    It is a <button>, not a link: it switches the filter to that service in
    place, so it is reachable by keyboard and touch with no extra wiring and
    does not create a destination that would 404 without JavaScript. The
    preview image is the first demo listed under that service, so it is always
    an image already used on this page and never a new asset.
    """
    first = next(d for d in VISIBLE_DEMOS if d["cat"] == key)
    name, folder = first["img"]
    n = DEMO_COUNT.get(key, 0)
    plural = "demo" if n == 1 else "demos"
    return f'''
        <button type="button" class="project-card pf-card pf-cat-card" data-goto="{key}">
          <span class="mock-wrap"><span class="coming-soon-badge">{n} {plural}</span>
            <span class="mock-browser"><span class="mock-browser-bar"><span></span><span></span><span></span></span>
            {picture(name, "", 1100, 620, folder, css_class="mock-browser-body-img")}
            </span>
          </span>
          <span class="project-card-body">
            <span class="tag"><i class="{icon}" aria-hidden="true"></i> Service</span>
            <span class="pf-card-title pf-cat-name">{label}</span>
            <span class="pf-card-desc pf-cat-text">{intro}</span>
            <span class="pf-cat-foot">Browse {label} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span>
          </span>
        </button>'''


filter_buttons = "\n".join(
    f'          <button type="button" class="filter-btn pf-btn{" active" if k == "all" else ""}"'
    f' data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}"'
    f' data-intro="{intro}">{label}</button>'
    for k, _icon, label, intro in VISIBLE_CATEGORIES)

all_intro = VISIBLE_CATEGORIES[0][3]
category_cards = "\n".join(category_card(k, ic, lb, it) for k, ic, lb, it in VISIBLE_CATEGORIES[1:])
# Sub-categories that actually have a visible demo behind them. No empty
# filter is ever rendered, and no demo is duplicated to populate one.
_present = {d.get("subcat") for d in VISIBLE_DEMOS if d.get("subcat")}
VISIBLE_WEBSITE_CATEGORIES = [c for c in WEBSITE_CATEGORIES
                              if c[0] == "all" or c[0] in _present]

website_filter_buttons = "\n".join(
    '          <button type="button" class="filter-btn pf-btn%s"'
    ' data-filter="%s" aria-pressed="%s" data-intro="%s">%s</button>'
    % (" active" if k == "all" else "", k, "true" if k == "all" else "false", intro, label)
    for k, label, intro in VISIBLE_WEBSITE_CATEGORIES)

website_all_intro = VISIBLE_WEBSITE_CATEGORIES[0][2]

# One primary service left means the primary filter bar and the service index
# would each be a control with a single choice, so neither is emitted. The
# Website Development sub-categories take their place instead.
SINGLE_CATEGORY = len(VISIBLE_CATEGORIES) <= 2
SUBCATEGORY_MODE = SINGLE_CATEGORY and VISIBLE_CATEGORIES[-1][0] == "website-development"

# Built last: demo_card() reads SUBCATEGORY_MODE to decide a card's filter key.
demo_cards = "\n".join(demo_card(d) for d in VISIBLE_DEMOS)


if SINGLE_CATEGORY:
    seo_title = "Website Development Projects & Demos | DeepAbi Innovations"
    seo_desc = ("DeepAbi Innovations website projects and demos \u2014 business, corporate, "
                "landing page and portfolio websites, with maintenance, SEO and performance work.")
else:
    seo_title = "Software Development Demo Projects | DeepAbi Innovations"
    seo_desc = ("DeepAbi Innovations demo projects by service \u2014 websites, web and mobile "
                "applications, desktop tools, custom software, SaaS products, AI automation and "
                "software maintenance.")

if SINGLE_CATEGORY:
    library_lede = ("Demonstration website projects &mdash; business, corporate, landing page "
                    "and portfolio builds.")
    if SUBCATEGORY_MODE and len(VISIBLE_WEBSITE_CATEGORIES) > 1:
        # Same markup, classes and JavaScript as the primary filter bar, so the
        # styling, the mobile scroll behaviour and the keyboard handling are
        # shared rather than duplicated.
        browse_controls = (
            '\n      <nav class="pf-filter" aria-label="Filter demos by website type" data-reveal>\n'
            '        <div class="pf-filter-scroll" id="pfFilter">\n'
            + website_filter_buttons + '\n'
            '        </div>\n'
            '      </nav>\n\n'
            '      <p class="pf-intro" id="pfIntro" aria-live="polite" data-reveal>'
            + website_all_intro + '</p>\n')
        empty_state = (
            '\n      <p class="pf-empty" id="pfEmpty" hidden>No demos are listed under this '
            'website type yet. Choose another, or <a href="contact.html">tell us what you '
            'need</a>.</p>')
    else:
        browse_controls = ""
        empty_state = ""
else:
    library_lede = ("Demonstration projects organised by service &mdash; websites, web and "
                    "mobile applications, desktop tools, custom software, SaaS products, "
                    "automation and maintenance work.")
    browse_controls = (
        '\n      <nav class="pf-filter" aria-label="Filter demos by service" data-reveal>\n'
        '        <div class="pf-filter-scroll" id="pfFilter">\n'
        + filter_buttons + '\n'
        '        </div>\n'
        '      </nav>\n\n'
        '      <p class="pf-intro" id="pfIntro" aria-live="polite" data-reveal>'
        + all_intro + '</p>\n\n'
        '      <!-- All Demos view: the public services as introduction cards.\n'
        '           Choosing one swaps this index for that service\'s demo cards. -->\n'
        '      <div class="grid-3 pf-cats pf-grid" id="pfCats" data-reveal>\n'
        + category_cards + '\n      </div>\n')
    empty_state = (
        '\n      <p class="pf-empty" id="pfEmpty" hidden>No demos are listed under this '
        'service yet. Choose another service, or <a href="contact.html">tell us what you '
        'need</a>.</p>')

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Our Work</span>
      <h1>Projects &amp; Success Stories</h1>
      <p>We're a young, senior-led website development company building our public case-study library one launch at a time. Here's our featured success story and current project types &mdash; from small business website builds to custom web application development.</p>
    </div>
  </div>

  <!-- FEATURED CASE STUDY -->
  <!-- PROTECTED: real client work, reproduced verbatim from the deployed
       page. Do not edit the content, imagery, layout or links below. -->
  <div class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="featured-case" data-reveal>
        <div class="featured-case-visual">
          <span class="launch-badge"><i class="fa-solid fa-rocket" aria-hidden="true"></i> Launched 2025</span>
          {picture("featured-cardsession-platform", "Abstract mockup illustration of a commercial hardware and industrial supply website", 700, 475, "assets/images/projects")}
        </div>
        <div class="featured-case-copy">
          <span class="eyebrow mint">Featured Success Story</span>
          <h2 style="font-size:30px; margin-bottom:14px;">Commercial Hardware &amp; Industrial Supply</h2>
          <p style="margin-bottom:14px;">Developed a modern commercial website for a company specializing in electrical products, hardware supplies, electronics components and industrial tools. The website was designed to improve credibility, showcase product categories, simplify customer enquiries and provide a responsive browsing experience across all devices.</p>
          <p style="margin-bottom:22px;">The project goal was to create a professional digital presence for a commercial electrical, hardware, electronics and industrial tools supplier while improving customer engagement and showcasing products effectively.</p>
          <ul class="featured-list" style="margin:0 0 22px;">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Website Design</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> UI/UX Design</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Responsive Development</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Product Showcase</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Business Information Architecture</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Contact Integration</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Performance Optimization</li>
          </ul>
          <div class="case-meta">
            <div><span>Industry</span><strong>Commercial Hardware &amp; Industrial Supply</strong></div>
            <div><span>Project Type</span><strong>Corporate Commercial Website</strong></div>
            <div><span>Duration</span><strong>4 Weeks</strong></div>
            <div><span>Platform</span><strong>Responsive Web Development</strong></div>
            <div><span>Website Type</span><strong>Commercial Business Website</strong></div>
            <div><span>Status</span><strong>Successfully Launched (2025)</strong></div>
          </div>
          <div class="mini-review" style="margin-top:22px;">
            <i class="fa-solid fa-quote-left" aria-hidden="true"></i> "Our new website finally reflects the scale of our business. Customers can browse our product categories and reach us directly, and enquiries have grown noticeably since launch." <span>&mdash; Business Owner, Commercial Hardware &amp; Industrial Supply Client</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- END PROTECTED -->

  <!-- DEVICE PREVIEW -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow">Responsive Website Design</span> -->
        <h2>Every build is tested across devices</h2>
      </div>
      <div class="device-row" data-reveal>
        <div class="device-frame desktop">
          {picture("desktop", "Desktop screenshot preview of a DeepAbi website build", 480, 300, "assets/images/projects")}
          <span class="device-label"><i class="fa-solid fa-desktop" aria-hidden="true"></i> Desktop</span>
        </div>
        <div class="device-frame tablet">
          {picture("tablet_portrait", "Tablet portrait screenshot preview of a DeepAbi website build", 260, 340, "assets/images/projects")}
          <span class="device-label"><i class="fa-solid fa-tablet-screen-button" aria-hidden="true"></i> Tablet</span>
        </div>
        <div class="device-frame mobile">
          {picture("mobile_portrait", "Mobile portrait screenshot preview of a DeepAbi website build", 150, 320, "assets/images/projects")}
          <span class="device-label"><i class="fa-solid fa-mobile-screen" aria-hidden="true"></i> Mobile</span>
        </div>
      </div>
    </div>
  </div>

  <!-- DEMO LIBRARY -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <h2>What We Build</h2>
        <p style="margin:0 auto;">{library_lede}</p>
      </div>
{browse_controls}
      <div class="grid-3 pf-grid" id="projectsGrid" data-reveal>
{demo_cards}
      </div>
{empty_state}
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Want to be our next success story?</h2>
        <p>Tell us about your project and let's talk about what we'd build.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="projects.html",
    active="projects",
    title=seo_title,
    description=seo_desc,
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/projects.css">',
    extra_js='<script src="js/pages/projects.js"></script>',
    schema=SCHEMA,
    extra_keywords="software development demo projects, web application demo, mobile app demo, business software examples Chennai",
)
