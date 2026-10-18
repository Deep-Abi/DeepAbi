# -*- coding: utf-8 -*-
"""
Build script for the DeepAbi static site.
Assembles each HTML page from a shared <head> SEO block, navbar, mobile menu,
floating contact launcher, and footer, plus page-specific body content and
page-specific CSS/JS includes. Run once during development; output is plain
static HTML with no runtime dependency on this script.
"""
import os as _os

ROOT = _os.path.dirname(_os.path.abspath(__file__))  # deepabi-site/ (parent of scripts/)
ROOT = _os.path.dirname(ROOT) if _os.path.basename(ROOT) == "scripts" else ROOT
SITE_URL = "https://www.deepabi.com"

# ---------------- Brand copy ----------------
MISSION = "Driving Economic Empowerment for People"
MISSION_DETAIL = "We build technology that creates real economic opportunity for the businesses and people behind it."
ABOUT_MISSION_PARAGRAPH = "DeepAbi is committed to driving economic empowerment by helping businesses, entrepreneurs and organizations establish a strong digital presence through modern, scalable and innovative technology solutions. Every website, application and digital experience we build is designed to create opportunities, improve accessibility and contribute to sustainable business growth."
VISION_HEADLINE = "Ambition Beyond Imagination"
VISION_BODY = "We envision DeepAbi becoming a globally trusted technology company delivering innovative digital experiences that transform businesses and empower communities worldwide."
VISION_DETAIL = "Becoming a globally trusted technology company delivering experiences that transform businesses worldwide."
ABOUT_VISION_PARAGRAPH = "DeepAbi envisions becoming a globally respected technology company that continuously pushes the boundaries of innovation, engineering excellence and digital transformation. Our ambition extends beyond conventional solutions, striving to create technologies that inspire growth, empower businesses and shape the future of digital experiences."
TAGLINE_PRIMARY = "Driving Economic Empowerment Through Technology"
TAGLINE_SECONDARY = "Ambition Beyond Imagination"
TAGLINE_THIRD = "Engineering Digital Excellence"

# ---------------- Contact ----------------
# Single source of truth for every contact detail rendered across the site.
#
# TWO addresses, with different jobs. Do not collapse them into one.
#   EMAIL_PRIMARY   - the public business address. Used for every general
#                     enquiry CTA, the floating contact button, the top bar,
#                     the mobile menu and the primary contact metadata.
#   EMAIL_SECONDARY - the approved technical address. Used where a technical
#                     contact is intended: the footer contact list and the
#                     Contact page's email card.
# EMAIL is kept as an alias of EMAIL_PRIMARY so existing call sites keep
# working; new code should name the address it means.
EMAIL_PRIMARY = "hello@deepabi.com"          # public / general enquiries
EMAIL_SECONDARY = "deepabi.tech@gmail.com"   # technical contact
EMAIL = EMAIL_PRIMARY
PHONE_1_DISPLAY = "+91 89460 97125"      # primary
PHONE_1_TEL = "+918946097125"
PHONE_2_DISPLAY = "+91 90255 48401"      # secondary
PHONE_2_TEL = "+919025548401"
WHATSAPP_URL = f"https://wa.me/{PHONE_1_TEL.replace('+','')}"

# ---------------- SEO keyword pool (used sparingly, naturally, across pages) ----------------
# Google ignores meta keywords for ranking; this stays only as a compact,
# honest summary of what the company does and where. Real targeting lives in
# the titles, headings, body copy and structured data.
#
# Two pools, selected by the service-visibility flags further down (see
# SEO_KEYWORDS near SERVICE_REGISTRY). The full pool is the company's long-term
# list. The website-only pool is that SAME list with every entry that advertises
# a hidden service removed - nothing reworded, nothing added. Restoring the
# services restores the full list.
SEO_KEYWORDS_ALL = (
    "software development company in Chennai, software company in Chennai, "
    "custom software development Chennai, application development company Chennai, "
    "website development company in Chennai, web application development Chennai, "
    "mobile app development Chennai, desktop application development Chennai, "
    "SaaS development Chennai, AI automation solutions Chennai, "
    "business automation Chennai, software maintenance Chennai, "
    "software development company in Mogappair, website development company in Mogappair, "
    "software company Ambattur, software company Anna Nagar, "
    "DeepAbi Innovations, DeepAbi"
)

# Entries kept verbatim from the list above. The removed ones named services
# that are not public: custom software, application / web / mobile / desktop
# development, SaaS, AI and business automation, software maintenance, and the
# two generic "software development/company" descriptors. "software company
# Ambattur" and "software company Anna Nagar" went with them because their
# service wording advertised software development; they were deliberately NOT
# reworded to say "website", since that would be retargeting rather than
# aligning. Locality signal is unaffected - it lives in areaServed, the footer
# and the meta descriptions.
SEO_KEYWORDS_WEBSITE_ONLY = (
    "website development company in Chennai, "
    "website development company in Mogappair, "
    "DeepAbi Innovations, DeepAbi"
)


NAV_ITEMS = [
    ("home", "index.html", "Home"),
    ("services", "services.html", "Services"),
    ("projects", "projects.html", "Projects"),
    ("technologies", "technologies.html", "Technologies"),
    ("about", "about.html", "About"),
    ("contact", "contact.html", "Contact"),
]

# ===========================================================================
# SERVICE REGISTRY  —  the single source of truth for service visibility
# ===========================================================================
# Every service DeepAbi has built content for lives here. `public` decides
# whether it appears anywhere on the public website: navigation, the Services
# page, the home "What We Build" grid, the Projects demo categories, the
# Contact form's service selector, related-service links, structured data and
# the sitemap all derive from this list. Nothing is deleted when a service is
# hidden — its generator, its dedicated page, its demos and its assets stay in
# the project exactly as they are, and its page keeps working at its URL.
#
# TO RESTORE A SERVICE: set its "public" to True and rebuild every page
# (see docs/BUILD.md). To restore all eight, set them all to True.
#
#   slug        the service identifier, used as the page anchor, the demo
#               category key and the dedicated page filename suffix
#   label       display name (may contain HTML entities, e.g. &amp;)
#   icon        Font Awesome class
#   menu_blurb  one-line description used in the navbar mega menu
#   page        the dedicated page for this service
#   contact     the label shown in the Contact form's service selector
#   public      whether the service is currently offered publicly
# ---------------------------------------------------------------------------
SERVICE_REGISTRY = [
    {"slug": "website-development", "label": "Website Development",
     "icon": "fa-solid fa-window-maximize",
     "menu_blurb": "Business, corporate and portfolio sites",
     "page": "service-website-development.html",
     "footer": True,
     "contact": "Website Development", "public": True},

    {"slug": "web-applications", "label": "Web Applications",
     "icon": "fa-solid fa-table-columns",
     "menu_blurb": "Dashboards, portals and business systems",
     "page": "service-web-applications.html",
     "footer": True,
     "contact": "Web Applications", "public": False},

    {"slug": "mobile-applications", "label": "Mobile Applications",
     "icon": "fa-solid fa-mobile-screen",
     "menu_blurb": "Apps built around your services",
     "page": "service-mobile-applications.html",
     "footer": True,
     "contact": "Mobile Applications", "public": False},

    {"slug": "desktop-applications", "label": "Desktop Applications",
     "icon": "fa-solid fa-desktop",
     "menu_blurb": "Internal tools and desktop software",
     "page": "service-desktop-applications.html",
     "contact": "Desktop Applications", "public": False},

    {"slug": "custom-software", "label": "Custom Software",
     "icon": "fa-solid fa-code",
     "menu_blurb": "Built around your exact process",
     "page": "service-custom-software.html",
     "footer": True,
     "contact": "Custom Software", "public": False},

    {"slug": "saas-products", "label": "SaaS Products",
     "icon": "fa-solid fa-cloud",
     "menu_blurb": "Cloud platforms with user accounts",
     "page": "service-saas-products.html",
     "contact": "SaaS Products", "public": False},

    {"slug": "ai-automation", "label": "AI &amp; Automation",
     "icon": "fa-solid fa-robot",
     "menu_blurb": "Less repetitive work, smarter workflows",
     "page": "service-ai-automation.html",
     "contact": "AI &amp; Automation", "public": False},

    {"slug": "software-maintenance", "label": "Software Maintenance",
     "icon": "fa-solid fa-screwdriver-wrench",
     "menu_blurb": "Support, updates and improvements",
     "page": "service-software-maintenance.html",
     "contact": "Software Maintenance", "public": False},
]

ALL_SERVICE_SLUGS = [s["slug"] for s in SERVICE_REGISTRY]
PUBLIC_SERVICES = [s for s in SERVICE_REGISTRY if s["public"]]
PUBLIC_SERVICE_SLUGS = [s["slug"] for s in PUBLIC_SERVICES]
HIDDEN_SERVICE_SLUGS = [s["slug"] for s in SERVICE_REGISTRY if not s["public"]]

# True when Website Development is the only public service. This is DERIVED,
# not a separate switch: make any other service public and the site returns to
# its multi-service presentation automatically.
WEBSITE_ONLY_MODE = PUBLIC_SERVICE_SLUGS == ["website-development"]

# What the shared footer says the company builds. It has to agree with what is
# actually public: while only Website Development is switched on, the footer
# must not advertise applications or custom software. This derives from the
# same flags as the navigation and the sitemap, so restoring a service restores
# the wording with it. The locality wording is deliberately left untouched here
# - geographic targeting is a separate decision.
if WEBSITE_ONLY_MODE:
    FOOTER_BUILDS = "builds professional websites"
else:
    FOOTER_BUILDS = "builds websites, applications and custom software"

# Meta keywords follow the same flags. Google ignores this tag for ranking, so
# this is a consistency correction, not an optimisation.
SEO_KEYWORDS = SEO_KEYWORDS_WEBSITE_ONLY if WEBSITE_ONLY_MODE else SEO_KEYWORDS_ALL


def is_service_public(slug):
    """Used by the service-page generator to decide noindex, and by any
    generator that needs to filter its own content by service."""
    return slug in PUBLIC_SERVICE_SLUGS


def service_page(slug):
    for s in SERVICE_REGISTRY:
        if s["slug"] == slug:
            return s["page"]
    raise KeyError(slug)


# ---------------- Website sub-services ----------------
# The offerings that live INSIDE Website Development, as sections of
# service-website-development.html. In website-only mode these replace the
# eight top-level services in the navigation and on the home page, so the
# menus stay full and useful instead of collapsing to a single item. Each
# anchor matches a section id on that page.
WEBSITE_SUBSERVICES = [
    ("fa-solid fa-window-maximize", "Website Development", "Complete websites for businesses and brands", "service-website-development.html"),
    ("fa-solid fa-rocket", "Landing Pages", "Single-purpose pages built around one goal", "service-website-development.html#landing-pages"),
    ("fa-solid fa-building", "Corporate Websites", "Structured sites for multi-department organizations", "service-website-development.html#corporate-websites"),
    ("fa-solid fa-store", "Business Websites", "A credible presence for service businesses", "service-website-development.html#business-websites"),
    ("fa-solid fa-images", "Portfolio Websites", "Image-forward sites for studios and professionals", "service-website-development.html#portfolio-websites"),
    ("fa-solid fa-screwdriver-wrench", "Website Maintenance", "Updates, security and monitoring after launch", "service-website-development.html#website-maintenance"),
    ("fa-solid fa-magnifying-glass-chart", "SEO", "Technical and on-page groundwork to be found", "service-website-development.html#seo"),
    ("fa-solid fa-gauge-high", "Performance Optimization", "Core Web Vitals and faster page loads", "service-website-development.html#performance-optimization"),
]


def services_menu_items():
    """(icon, label, blurb, href) for every navigation surface.

    Website-only mode shows the website sub-services; otherwise it shows one
    entry per public top-level service. Both the desktop mega menu, the mobile
    accordion and the footer services column read from this one function, so
    they can never drift apart.
    """
    if WEBSITE_ONLY_MODE:
        return list(WEBSITE_SUBSERVICES)
    return [(s["icon"], s["label"], s["menu_blurb"], s["page"]) for s in PUBLIC_SERVICES]


# Menu wording follows what is actually on offer.
if WEBSITE_ONLY_MODE:
    SERVICES_MENU_TITLE = "Website Development"
    SERVICES_MENU_SUBTITLE = "Professional websites for businesses, brands and organizations."
    SERVICES_MENU_FOOT = "Looking for a website built around your business?"
    SERVICES_MENU_CTA = "Explore Website Services"
else:
    SERVICES_MENU_TITLE = "Software Solutions"
    SERVICES_MENU_SUBTITLE = "From digital experiences to intelligent software systems."
    SERVICES_MENU_FOOT = "Need something built around your business?"
    SERVICES_MENU_CTA = "Explore All Services"

# Kept as a module-level name because existing call sites import it.
SERVICES_MENU = services_menu_items()


def head(title, description, canonical_path, og_image="assets/images/backgrounds/og-social-banner.jpg",
         extra_css="", schema="", extra_keywords="", noindex=False):
    canonical = f"{SITE_URL}/{canonical_path}" if canonical_path else SITE_URL
    keywords = SEO_KEYWORDS + (f", {extra_keywords}" if extra_keywords else "")
    # "follow" is kept so crawlers still traverse the page's links, and the
    # page is never blocked in robots.txt - a blocked page can't be read, so
    # its noindex would never be seen.
    robots = "noindex, follow" if noindex else "index, follow"
    return f'''<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="keywords" content="{keywords}" />
<meta name="author" content="DeepAbi" />
<link rel="canonical" href="{canonical}" />
<meta name="robots" content="{robots}" />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{SITE_URL}/{og_image}" />
<meta property="og:site_name" content="DeepAbi" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{SITE_URL}/{og_image}" />

<!-- Favicons -->
<link rel="icon" type="image/x-icon" href="assets/images/logos/favicon.ico" />
<link rel="icon" type="image/png" sizes="48x48" href="assets/images/logos/favicon-48.png" />
<link rel="icon" type="image/png" sizes="32x32" href="assets/images/logos/favicon-32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="assets/images/logos/favicon-16.png" />
<link rel="apple-touch-icon" sizes="180x180" href="assets/images/logos/favicon-180.png" />
<link rel="manifest" href="site.webmanifest" />
<meta name="theme-color" content="#081F4D" />

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
      integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
      crossorigin="anonymous" referrerpolicy="no-referrer" />

<!-- Styles -->
<link rel="stylesheet" href="css/common.css">
{extra_css}
{schema}'''


def _services_mega(active):
    """Services navbar entry: a real link to services.html plus the mega panel."""
    cls = ' class="nav-mega-trigger active" aria-current="page"' if active else ' class="nav-mega-trigger"'
    items = "\n".join(
        f'''          <a href="{href}" class="mega-item">
            <span class="mega-ico"><i class="{icon}" aria-hidden="true"></i></span>
            <span class="mega-item-body">
              <span class="mega-item-title">{title} <i class="fa-solid fa-arrow-right mega-arrow" aria-hidden="true"></i></span>
              <span class="mega-item-desc">{desc}</span>
            </span>
          </a>''' for icon, title, desc, href in SERVICES_MENU)
    return f'''      <div class="nav-mega" id="servicesNav">
        <a href="services.html"{cls} id="servicesTrigger" aria-haspopup="true" aria-expanded="false" aria-controls="servicesMega">Services <i class="fa-solid fa-chevron-down mega-chev" aria-hidden="true"></i></a>
        <div class="mega" id="servicesMega" role="group" aria-label="Services">
          <div class="mega-head">
            <h2>{SERVICES_MENU_TITLE}</h2>
            <p>{SERVICES_MENU_SUBTITLE}</p>
          </div>
          <div class="mega-grid">
{items}
          </div>
          <div class="mega-foot">
            <p>{SERVICES_MENU_FOOT}</p>
            <a href="services.html" class="mega-foot-cta">{SERVICES_MENU_CTA} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          </div>
        </div>
      </div>'''


def _services_accordion():
    """Mobile equivalent: the same items as an expandable accordion."""
    items = "\n".join(
        f'''        <a href="{href}"><span class="m-acc-ico"><i class="{icon}" aria-hidden="true"></i></span>{title}</a>'''
        for icon, title, desc, href in SERVICES_MENU)
    return f'''    <div class="m-acc">
      <button type="button" class="m-acc-trigger" id="mServicesTrigger" aria-expanded="false" aria-controls="mServicesPanel">Services <i class="fa-solid fa-chevron-down m-acc-chev" aria-hidden="true"></i></button>
      <div class="m-acc-panel" id="mServicesPanel">
{items}
        <a href="services.html" class="m-acc-all">{SERVICES_MENU_CTA} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>'''


def navbar(active):
    main_links = []
    for key, href, label in NAV_ITEMS:
        if key == "services":
            main_links.append(_services_mega(active == "services"))
        elif key == active:
            main_links.append(f'      <a href="{href}" class="active" aria-current="page">{label}</a>')
        else:
            main_links.append(f'      <a href="{href}">{label}</a>')
    main_links_html = "\n".join(main_links)

    mobile_links = "\n".join(
        _services_accordion() if key == "services" else f'    <a href="{href}">{label}</a>'
        for key, href, label in NAV_ITEMS
    )

    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header id="navbar">
  <div class="navbar-topbar">
    <div class="container topbar-inner">
      <div class="topbar-contact">
        <a href="tel:{PHONE_1_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {PHONE_1_DISPLAY}</a>
        <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
        <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i> {EMAIL}</a>
      </div>
      <div class="topbar-tagline">{TAGLINE_THIRD}</div>
    </div>
  </div>
  <div class="container nav-inner">
    <a href="index.html" class="logo" aria-label="DeepAbi Innovations — home">
      <picture class="logo-full">
        <source srcset="assets/images/logos_icons/web/logo.avif" type="image/avif">
        <source srcset="assets/images/logos_icons/web/logo.webp" type="image/webp">
        <img src="assets/images/logos_icons/web/logo.png" alt="DeepAbi Innovations" width="324" height="132">
      </picture>
      <picture class="logo-plate">
        <source srcset="assets/images/logos_icons/web/logo-plate.avif" type="image/avif">
        <source srcset="assets/images/logos_icons/web/logo-plate.webp" type="image/webp">
        <img src="assets/images/logos_icons/web/logo-plate.png" alt="DeepAbi Innovations" width="288" height="132">
      </picture>
    </a>
    <nav class="nav-links" aria-label="Primary">
{main_links_html}
    </nav>
    <div class="nav-right">
      <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><i class="fa-solid fa-bars" aria-hidden="true"></i></button>
    </div>
  </div>
</header>

<div id="mobile-menu">
  <div class="mobile-menu-head">
    <a href="index.html" class="logo" aria-label="DeepAbi Innovations — home">
      <picture class="logo-full">
        <source srcset="assets/images/logos_icons/web/logo.avif" type="image/avif">
        <source srcset="assets/images/logos_icons/web/logo.webp" type="image/webp">
        <img src="assets/images/logos_icons/web/logo.png" alt="DeepAbi Innovations" width="324" height="132">
      </picture>
    </a>
    <button class="menu-toggle" id="menuClose" aria-label="Close menu"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
  </div>
  <nav aria-label="Mobile">
{mobile_links}
  </nav>
  <div class="mobile-contact">
    <a href="tel:{PHONE_1_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {PHONE_1_DISPLAY}</a>
    <a href="tel:{PHONE_2_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {PHONE_2_DISPLAY}</a>
    <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i> {EMAIL}</a>
  </div>
</div>'''


def contact_fab():
    return f'''<div class="contact-fab" id="contactFab">
  <div class="fab-menu" id="fabMenu" role="menu" aria-hidden="true">
    <a role="menuitem" class="fab-item" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" aria-label="Chat with DeepAbi on WhatsApp">
      <span class="fab-icon fab-whatsapp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></span><span class="fab-label">WhatsApp</span>
    </a>
    <a role="menuitem" class="fab-item" href="tel:{PHONE_1_TEL}" aria-label="Call DeepAbi at {PHONE_1_DISPLAY}">
      <span class="fab-icon fab-call"><i class="fa-solid fa-phone" aria-hidden="true"></i></span><span class="fab-label">Call Us</span>
    </a>
    <a role="menuitem" class="fab-item" href="mailto:{EMAIL}" aria-label="Email DeepAbi">
      <span class="fab-icon fab-email"><i class="fa-solid fa-envelope" aria-hidden="true"></i></span><span class="fab-label">Email</span>
    </a>
  </div>
  <button class="fab-main" id="fabToggle" aria-expanded="false" aria-controls="fabMenu" aria-label="Open contact options">
    <i class="fa-solid fa-comment-dots" id="fabIconOpen" aria-hidden="true"></i>
    <i class="fa-solid fa-xmark" id="fabIconClose" aria-hidden="true"></i>
  </button>
</div>'''


def _footer_service_links(limit=4):
    """The footer services column.

    Normally the services flagged `footer` in the registry, which preserves the
    approved four-link column exactly. In website-only mode there is only one
    such service, so the first few website sub-offerings are listed instead and
    an All Services row is added - otherwise the column would be a single link.
    Either way it is derived from the registry, so the footer can never
    advertise a service the navigation has hidden."""
    if WEBSITE_ONLY_MODE:
        entries = services_menu_items()[:limit]
        add_all = True
    else:
        entries = [(x["icon"], x["label"], x["menu_blurb"], x["page"])
                   for x in PUBLIC_SERVICES if x.get("footer")][:limit]
        add_all = False
    rows = [
        f'          <li><a href="{href}"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> {label}</a></li>'
        for _icon, label, _blurb, href in entries
    ]
    if add_all:
        rows.append('          <li><a href="services.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> All Services</a></li>')
    return "\n".join(rows)


def footer():
    footer_services = _footer_service_links()
    return f'''<footer>
  <div class="footer-mission">
    <div class="container">
      <span class="footer-mission-label">Our Mission</span>
      <p>&ldquo;{MISSION}&rdquo;</p>
    </div>
  </div>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <picture class="footer-logo-img">
            <source srcset="assets/images/logos_icons/web/logo-plate.avif" type="image/avif">
            <source srcset="assets/images/logos_icons/web/logo-plate.webp" type="image/webp">
            <img src="assets/images/logos_icons/web/logo-plate.png" alt="DeepAbi Innovations" width="288" height="132">
          </picture>
        </div>
        <p>{TAGLINE_PRIMARY}. Based in Mogappair, DeepAbi Innovations {FOOTER_BUILDS} for businesses across Ambattur, Anna Nagar and Chennai.</p>
        <div class="footer-social">
          <a href="https://www.instagram.com/deepabi_innovations/" target="_blank" rel="noopener noreferrer" aria-label="DeepAbi Innovations on Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
          <a href="https://www.facebook.com/profile.php?id=61593491164948" target="_blank" rel="noopener noreferrer" aria-label="DeepAbi Innovations on Facebook"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a>
        </div>
      </div>
      <div class="footer-col">
        <h3 class="footer-col-title">Company</h3>
        <ul>
          <li><a href="index.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Home</a></li>
          <li><a href="about.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> About</a></li>
          <li><a href="projects.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Projects</a></li>
          <li><a href="technologies.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Technologies</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3 class="footer-col-title">Services</h3>
        <ul>
{footer_services}
        </ul>
      </div>
      <div class="footer-col footer-col-contact">
        <h3 class="footer-col-title">Contact</h3>
        <ul>
          <li><a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i><span><em>Email</em>{EMAIL}</span></a></li>
          <li><a href="mailto:{EMAIL_SECONDARY}"><i class="fa-solid fa-envelope" aria-hidden="true"></i><span><em>Technical</em>{EMAIL_SECONDARY}</span></a></li>
          <li><a href="tel:{PHONE_1_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i><span><em>Phone</em>{PHONE_1_DISPLAY}</span></a></li>
          <li><a href="tel:{PHONE_2_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i><span><em>Phone</em>{PHONE_2_DISPLAY}</span></a></li>
          <li><a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i><span><em>WhatsApp</em>Chat with us</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year"></span> DeepAbi Innovations. All rights reserved.</span>
      <span class="legal"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></span>
    </div>
  </div>
</footer>

<!-- The toast has exactly one consumer: the contact form, which does not
     send anything - it hands the enquiry to the visitor's own mail client.
     So the shipped default must not claim a delivery. It previously read
     "Message sent successfully!" with a green tick, which would have been
     a false statement in any state that showed the toast before
     js/pages/contact.js had rewritten it. The default is now the honest
     hand-off wording and the icon is an envelope, not a success tick.
     role="status" lets assistive technology announce it when it appears. -->
<div class="toast" id="toast" role="status" aria-live="polite"><i class="fa-solid fa-envelope-open-text" aria-hidden="true"></i><span id="toastMsg">Your email app should open with this enquiry ready to send.</span></div>'''


def picture(name, alt, w, h, folder, css_class="", loading="lazy", eager=False, skip_formats=()):
    """Build a <picture> element with automatic format detection and a strict
    priority order: AVIF > WebP > PNG > JPG/JPEG. Only <source> tags for
    formats that actually exist on disk for this image are emitted, so an
    image that only ships as AVIF+JPG (no WebP/PNG) still produces valid,
    minimal markup. `folder` is the page-scoped asset directory, e.g.
    "assets/images/home". Explicit width/height prevents layout shift;
    `eager=True` marks the hero-priority image (eager load + fetchpriority high),
    everything else lazy-loads with async decoding.

    Pass loading="eager" (leaving eager=False) for an image that is inside the
    first viewport but is not the page's priority hero: it loads in the normal
    batch instead of being deferred, without claiming high fetch priority.

    `skip_formats` omits formats that exist on disk but are not wanted for a
    particular image. It is used for the home hero, where the JPEG is a different
    crop and aspect ratio from the other derivatives and would render wrongly if a
    browser fell through to it."""
    loading_attr = "eager" if eager else loading
    fetchpriority = ' fetchpriority="high"' if eager else ''
    cls = f' class="{css_class}"' if css_class else ''

    FORMAT_PRIORITY = [
        ("avif", "image/avif"),
        ("webp", "image/webp"),
        ("png", "image/png"),
    ]
    found = {}
    for ext, _ in FORMAT_PRIORITY:
        if ext in skip_formats:
            continue
        path = _os.path.join(ROOT, folder, ext, f"{name}.{ext}")
        if _os.path.exists(path):
            found[ext] = True
    # fallback <img> src: prefer jpg, then jpeg, then png, then whatever's found.
    # `skip_formats` applies here too, so an image whose JPEG derivative does not
    # match the other formats can opt out of it and fall back to PNG instead.
    img_src = None
    for ext in ("jpg", "jpeg"):
        if ext in skip_formats:
            continue
        path = _os.path.join(ROOT, folder, ext, f"{name}.{ext}")
        if _os.path.exists(path):
            img_src = f"{folder}/{ext}/{name}.{ext}"
            break
    if img_src is None and "png" in found:
        img_src = f"{folder}/png/{name}.png"
    if img_src is None:
        # last resort: use the highest-priority format found as the <img> src too
        for ext, _ in FORMAT_PRIORITY:
            if ext in found:
                img_src = f"{folder}/{ext}/{name}.{ext}"
                break
    if img_src is None:
        raise FileNotFoundError(f"No image file found for '{name}' in '{folder}' (checked avif/webp/png/jpg/jpeg)")

    sources = "\n        ".join(
        f'<source srcset="{folder}/{ext}/{name}.{ext}" type="{mime}">'
        for ext, mime in FORMAT_PRIORITY if ext in found
    )

    return f'''<picture{cls}>
        {sources}
        <img src="{img_src}" alt="{alt}" width="{w}" height="{h}" loading="{loading_attr}"{fetchpriority} decoding="async">
      </picture>'''


def art_directed_picture(breakpoints, alt, w, h, folder, css_class="", eager=False):
    """Build a <picture> element that swaps to a DIFFERENT image per
    breakpoint (art direction), not just a different format of the same
    image. `breakpoints` is an ordered list of (media_query_or_None, name)
    tuples, most-specific first, ending with (None, default_name) for the
    default/desktop case. Each name still gets the full AVIF > WebP > PNG
    format-priority treatment, auto-detected from disk. Desktop images are
    NEVER downscaled for smaller screens — each breakpoint loads its own
    dedicated source image."""
    FORMAT_PRIORITY = [
        ("avif", "image/avif"),
        ("webp", "image/webp"),
        ("png", "image/png"),
    ]
    loading_attr = "eager" if eager else "lazy"
    fetchpriority = ' fetchpriority="high"' if eager else ''
    cls = f' class="{css_class}"' if css_class else ''

    def found_formats(name):
        found = {}
        for ext, _ in FORMAT_PRIORITY:
            if _os.path.exists(_os.path.join(ROOT, folder, ext, f"{name}.{ext}")):
                found[ext] = True
        return found

    sources = []
    default_name = breakpoints[-1][1]
    for media, name in breakpoints:
        found = found_formats(name)
        media_attr = f' media="{media}"' if media else ''
        for ext, mime in FORMAT_PRIORITY:
            if ext in found:
                sources.append(f'<source{media_attr} srcset="{folder}/{ext}/{name}.{ext}" type="{mime}">')

    img_src = None
    for ext in ("jpg", "jpeg"):
        path = _os.path.join(ROOT, folder, ext, f"{default_name}.{ext}")
        if _os.path.exists(path):
            img_src = f"{folder}/{ext}/{default_name}.{ext}"
            break
    if img_src is None:
        img_src = f"{folder}/png/{default_name}.png"

    sources_html = "\n        ".join(sources)
    return f'''<picture{cls}>
        {sources_html}
        <img src="{img_src}" alt="{alt}" width="{w}" height="{h}" loading="{loading_attr}"{fetchpriority} decoding="async">
      </picture>'''


def page(filename, active, title, description, body, canonical_path=None,
         extra_css="", extra_js="", og_image="assets/images/backgrounds/og-social-banner.jpg",
         schema="", body_class="", extra_keywords="", noindex=False):
    canonical_path = canonical_path if canonical_path is not None else filename
    body_attr = f' class="{body_class}"' if body_class else ''
    html = f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<script>document.documentElement.className=document.documentElement.className.replace('no-js','js');</script>
{head(title, description, canonical_path, og_image, extra_css, schema, extra_keywords, noindex)}
</head>
<body{body_attr}>

{navbar(active)}

<main id="main">
{body}
</main>

{footer()}

{contact_fab()}

<script src="js/common.js"></script>
{extra_js}
</body>
</html>
'''
    with open(_os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {filename} ({len(html)} bytes)")
