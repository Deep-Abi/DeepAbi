import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import (page, picture, PUBLIC_SERVICE_SLUGS, WEBSITE_ONLY_MODE,
                        WEBSITE_SUBSERVICES)
from build_site import MISSION, MISSION_DETAIL, VISION_HEADLINE, VISION_DETAIL, TAGLINE_PRIMARY

# Structured data lists only what is publicly offered, so the markup and the
# visible page agree.
import json as _json
if WEBSITE_ONLY_MODE:
    _knows = ["Website Development", "Business Websites", "Corporate Websites",
              "Landing Page Development", "Portfolio Websites", "Website Maintenance",
              "Search Engine Optimization", "Website Performance Optimization"]
else:
    _knows = ["Website Development", "Web Application Development",
              "Mobile Application Development", "Desktop Application Development",
              "Custom Software Development", "SaaS Product Development",
              "AI and Business Automation", "Software Maintenance and Support"]
# Indented to sit cleanly inside the surrounding JSON-LD block.
KNOWS_ABOUT = _json.dumps(_knows, indent=2).replace('\n', '\n  ')

# Organization.description has to agree with what is actually public, the same
# way knowsAbout already does. While only Website Development is switched on it
# must not advertise the seven hidden services. Both strings are JSON string
# contents, so they carry no quotes or backslashes. Restoring the services
# restores the full description.
if WEBSITE_ONLY_MODE:
    ORG_DESCRIPTION = ("DeepAbi Innovations is a website development company in Chennai "
                       "building business, corporate, landing page and portfolio websites, "
                       "with website maintenance, SEO and performance optimisation.")
else:
    ORG_DESCRIPTION = ("DeepAbi Innovations is a software development company in Chennai "
                       "building websites, web and mobile applications, desktop and custom "
                       "software, SaaS products, AI automation and software maintenance.")

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "DeepAbi Innovations",
  "alternateName": "DeepAbi",
  "url": "https://www.deepabi.com",
  "logo": "https://www.deepabi.com/assets/images/logos/favicon-512.png",
  "description": "__ORG_DESCRIPTION__",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Mogappair, Chennai",
    "addressRegion": "Tamil Nadu",
    "addressCountry": "IN"
  },
  "areaServed": [
    { "@type": "Place", "name": "Mogappair, Chennai" },
    { "@type": "Place", "name": "Mogappair East, Chennai" },
    { "@type": "Place", "name": "Mogappair West, Chennai" },
    { "@type": "Place", "name": "Nolambur, Chennai" },
    { "@type": "Place", "name": "Ambattur, Chennai" },
    { "@type": "Place", "name": "Anna Nagar, Chennai" },
    { "@type": "Place", "name": "Anna Nagar East, Chennai" },
    { "@type": "Place", "name": "Anna Nagar West, Chennai" },
    { "@type": "Place", "name": "Anna Nagar West Extension, Chennai" },
    { "@type": "City", "name": "Chennai" }
  ],
  "knowsAbout": __KNOWS_ABOUT__,
  "email": "hello@deepabi.com",
  "telephone": ["+918946097125", "+919025548401"],
  "sameAs": [
    "https://www.instagram.com/deepabi_innovations/",
    "https://www.facebook.com/profile.php?id=61593491164948"
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "DeepAbi",
  "url": "https://www.deepabi.com"
}
</script>'''

SCHEMA = SCHEMA.replace('__KNOWS_ABOUT__', KNOWS_ABOUT)
SCHEMA = SCHEMA.replace('__ORG_DESCRIPTION__', ORG_DESCRIPTION)

# The home hero is the largest paint on the site.
#
# AVIF used to be skipped here on the grounds that its encode was 166KB against
# 73KB for the JPEG. That is no longer true of the files on disk: the AVIF was
# regenerated at some point and now measures 64.6KB against 168.7KB for the
# WebP, at the same 800x1200 size and with the same transparent canvas (73.2%
# of the canvas transparent in both; opaque content occupies the same rows).
# It decodes cleanly in Chromium and renders at an identical size, so AVIF is
# now offered first and the hero's largest image drops by ~104KB.
#
# "jpg" stays skipped, so the <img> falls back to the PNG. The three
# derivatives are not interchangeable for this image: the WebP and the PNG are
# both 800x1200 (2:3) with a transparent background, while the JPEG is
# 1200x1100 - a different crop, a different aspect ratio and an opaque blue
# background. Any browser that fell through to the JPEG would have rendered a
# differently shaped, opaque picture inside a box reserved at 2:3, and the
# hero's stacked layout further assumes the transparent canvas. The PNG matches
# the WebP exactly, so the fallback is consistent with what modern browsers
# actually load. Replace the JPEG with a matching 2:3 export to re-enable it.
#
# Order served: AVIF (64.6KB) -> WebP (168.7KB) -> PNG fallback (677KB).
HERO_SKIP = ("jpg",)

# ---------------------------------------------------------------------------
# Device showcase: visibility follows the service configuration.
#
# The three screenshots inside this showcase are mock-ups of the DeepAbi
# homepage, and the mock-up text is baked into the artwork. It still reads
# "Building Intelligent Digital Solutions" - the heading this site replaced -
# and "modern, scalable and high-performance websites and applications", which
# offers applications the site deliberately does not sell while only Website
# Development is public. Neither line can be corrected without regenerating the
# artwork.
#
# So the showcase is hidden in website-only mode. Nothing is deleted: all three
# assets keep every format on disk, the markup below is preserved verbatim, and
# the showcase returns on its own as soon as more than one service is public.
# The flag is derived from SERVICE_REGISTRY, not hand-set, so it cannot drift.
#
# The section around it is unaffected - its heading, lede and the Responsive
# Website Design block below are all independent of the showcase, so removing
# the element removes its box and its margins with it and leaves no gap.
SHOW_DEVICE_SHOWCASE = not WEBSITE_ONLY_MODE

DEVICE_SHOWCASE = f'''      <!-- Declared 640x427 is correct here: the assets are 1200x800 (desktop)
           and 1200x801 (tablet, mobile), so the declared ratio 1.4988 matches
           the real 1.5 to within 0.08%. The frames also set their own width and
           height in CSS with object-fit:cover, so these attributes have no
           layout effect either way. Left as they are. -->
      <div class="device-stack device-stack-large" id="deviceStack" data-reveal="scale" role="group" aria-label="Showcase cycling through desktop, tablet, and mobile presentations of the DeepAbi brand" aria-live="off">
        <div class="device-stack-card" data-role="desktop">
          <div class="device-stack-frame">
            {picture("deepabi-desktop", "DeepAbi website showcased on a desktop display", 640, 427, "assets/images/home")}
          </div>
          <span class="device-stack-label"><i class="fa-solid fa-desktop" aria-hidden="true"></i> Desktop</span>
        </div>
        <div class="device-stack-card" data-role="tablet">
          <div class="device-stack-frame">
            {picture("deepabi-tablet", "DeepAbi website showcased on a tablet display", 640, 427, "assets/images/home")}
          </div>
          <span class="device-stack-label"><i class="fa-solid fa-tablet-screen-button" aria-hidden="true"></i> Tablet</span>
        </div>
        <div class="device-stack-card" data-role="mobile">
          <div class="device-stack-frame">
            {picture("deepabi-mobile", "DeepAbi website showcased on a mobile display", 640, 427, "assets/images/home")}
          </div>
          <span class="device-stack-label"><i class="fa-solid fa-mobile-screen" aria-hidden="true"></i> Mobile</span>
        </div>
      </div>
'''

device_showcase = DEVICE_SHOWCASE if SHOW_DEVICE_SHOWCASE else ""

WHAT_WE_BUILD = [
    ("fa-solid fa-window-maximize", "Website Development", "Professional websites for businesses, companies and brands — from landing pages and portfolios to complete corporate websites.", "website-development"),
    ("fa-solid fa-table-columns", "Web Applications", "Interactive web-based applications, dashboards, portals and business systems built around real operational needs.", "web-applications"),
    ("fa-solid fa-mobile-screen", "Mobile Applications", "Custom mobile applications designed around business requirements, user experiences and digital services.", "mobile-applications"),
    ("fa-solid fa-desktop", "Desktop Applications", "Purpose-built desktop software and internal tools for business operations, productivity and specialized workflows.", "desktop-applications"),
    ("fa-solid fa-code", "Custom Software", "Tailored software solutions designed around unique business processes, requirements and operational challenges.", "custom-software"),
    ("fa-solid fa-cloud", "SaaS Products", "Cloud-based software products and platforms designed for accessible, scalable and ongoing digital services.", "saas-products"),
    ("fa-solid fa-robot", "AI &amp; Automation", "AI-powered solutions and workflow automation designed to reduce repetitive work and improve business efficiency.", "ai-automation"),
    ("fa-solid fa-screwdriver-wrench", "Software Maintenance", "Ongoing software support, improvements, optimization and maintenance to keep digital products reliable and evolving.", "software-maintenance"),
]


def build_card(icon, title, desc, anchor, href=None):
    """`anchor` is the service slug; each card links to that service's own
    dedicated page. anchor=None falls back to the Services overview."""
    if href is None:
        href = f"service-{anchor}.html" if anchor else "services.html"
    return f'''<div class="wwb-card" data-reveal>
        <div class="wwb-icon"><i class="{icon}" aria-hidden="true"></i></div>
        <h3>{title}</h3>
        <p>{desc}</p>
        <a href="{href}" class="wwb-more">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>'''


# Only services marked public in the SERVICE_REGISTRY reach the grid. In
# website-only mode the eight website sub-offerings take their place, so the
# grid stays full instead of collapsing to a single card and leaving a gap.
if WEBSITE_ONLY_MODE:
    _cards = [(icon, label, blurb + ".", href)
              for icon, label, blurb, href in WEBSITE_SUBSERVICES]
    wwb_cards_html = "\n      ".join(
        build_card(icon, title, desc, None, href=href) for icon, title, desc, href in _cards)
    wwb_lede = ("Professional websites for businesses, brands and organizations &mdash; built to "
                "load fast, read well on a phone and make getting in touch obvious.")
else:
    _visible = [c for c in WHAT_WE_BUILD if c[3] in PUBLIC_SERVICE_SLUGS]
    wwb_cards_html = "\n      ".join(build_card(*c) for c in _visible)
    wwb_lede = ("From professional websites to custom software, DeepAbi builds digital solutions "
                "designed around real business needs.")

RESPONSIVE_FEATURES = [
    ("fa-solid fa-mobile-screen-button", "Mobile-First Layouts", "Designed for the smallest screen first, then scaled up with intention."),
    ("fa-solid fa-text-height", "Fluid Typography", "Type scales smoothly across breakpoints instead of jumping at fixed sizes."),
    ("fa-solid fa-hand-pointer", "Touch-Friendly UI", "Tap targets, spacing, and gestures built for real fingers, not just a mouse."),
    ("fa-solid fa-display", "Cross-Device QA", "Every build is checked on real desktop, tablet, and mobile viewports before launch."),
]


def responsive_feature(icon, title, desc):
    return f'''<div class="rf-item">
        <div class="rf-icon"><i class="{icon}" aria-hidden="true"></i></div>
        <div class="rf-text"><h3>{title}</h3><p>{desc}</p></div>
      </div>'''


rf_html = "\n        ".join(responsive_feature(*f) for f in RESPONSIVE_FEATURES)


def testimonial_slide(active, avatar, alt, quote, name, role):
    active_cls = " active" if active else ""
    return f'''<div class="testimonial-slide{active_cls}">
            <div class="testimonial-card">
              <i class="fa-solid fa-quote-left testimonial-quote-mark" aria-hidden="true"></i>
              <div class="testimonial-stars"><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i></div>
              <p class="quote">"{quote}"</p>
              <div class="testimonial-person">
                {picture(avatar, alt, 56, 56, "assets/images/testimonials", css_class="avatar-img")}
                <div><h3>{name}</h3><span>{role}</span></div>
              </div>
            </div>
          </div>'''


# Verified client testimonials only.
#
# This list is EMPTY on purpose. It previously held four entries attributed to
# named people at named companies (Aarav Rao / Northline Consulting, Priya
# Kapoor / Verdant Foods Co., Samuel Ntuli / Harborview Logistics, Meera Joshi
# / Fieldstone Analytics), including a measurable claim that contact form
# submissions doubled. None of them was real, so all four were removed.
#
# Add a tuple here ONLY for a testimonial a real client has actually given and
# approved for publication:
#
#     (avatar_name, avatar_alt, quote, person_name, person_role)
#
# The whole visible section below is generated from this list. With the list
# empty, no heading, carousel, arrows, dots or spacing are emitted at all, so
# the page has no placeholder and no gap. Adding the first verified entry
# brings the section back with no other change needed.
TESTIMONIALS = []

testimonial_slides_html = "\n          ".join(
    testimonial_slide(i == 0, *t) for i, t in enumerate(TESTIMONIALS)
)

# The testimonials section exists only when there is something verified to put
# in it. No entries means no section at all - not an empty heading or carousel.
if TESTIMONIALS:
    testimonials_section = f'''

  <!-- ============ TESTIMONIALS (carousel) ============ -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow">Client Feedback</span> -->
        <h2>Testimonials</h2>
        <p style="margin:0 auto;">What clients say about working with us.</p>
      </div>
      <div class="testimonial-carousel" data-reveal id="testimonialCarousel">
        <button type="button" class="testimonial-arrow prev" id="testimonialPrev" aria-label="Previous testimonial"><i class="fa-solid fa-chevron-left" aria-hidden="true"></i></button>
        <div class="testimonial-track" id="testimonialTrack">
          {testimonial_slides_html}
        </div>
        <button type="button" class="testimonial-arrow next" id="testimonialNext" aria-label="Next testimonial"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i></button>
        <div class="testimonial-dots" id="testimonialDots" role="tablist" aria-label="Testimonial navigation"></div>
      </div>
    </div>
  </section>
'''
else:
    testimonials_section = ""

# Visible hero copy, the H1 and the meta description describe what is actually
# on offer. All three revert with the registry flags.
if WEBSITE_ONLY_MODE:
    hero_heading = "Websites Built Around Your Business"
    hero_sub = ("We build modern, scalable websites &mdash; from a single landing page to a "
                "complete corporate site &mdash; designed to load fast, read well on a phone "
                "and bring you enquiries.")
    seo_desc = ("DeepAbi Innovations builds business, corporate, landing page and portfolio "
                "websites for businesses in Mogappair and across Chennai, with maintenance, "
                "SEO and performance support.")
    seo_title = "DeepAbi Innovations | Website Development Company in Chennai"
else:
    hero_heading = "Building Intelligent Digital Solutions"
    seo_title = "DeepAbi Innovations | Software Development Company in Chennai"
    hero_sub = ("We build modern, scalable and intelligent digital products &mdash; from custom "
                "website development to enterprise web applications &mdash; that help businesses "
                "grow faster.")
    seo_desc = ("DeepAbi Innovations builds websites, web and mobile apps, custom software, SaaS "
                "and automation solutions for businesses in Mogappair and across Chennai.")

body = f'''
  <!-- ============ HERO ============ -->
  <section class="hero" id="hero">
    <div class="hero-bg" aria-hidden="true">
      <canvas id="particles"></canvas>
      <div class="mesh-blob blob-1"></div>
      <div class="mesh-blob blob-2"></div>
      <div class="mesh-blob blob-3"></div>
    </div>

    <div class="container hero-grid">
      <!-- The three hero blocks deliberately carry no data-reveal. The entrance
           animation hides its target with opacity:0 until JavaScript marks it
           visible, which for above-the-fold content delays the largest paint by
           roughly a second (measured: LCP 3096ms -> 2536ms at 375px and 3908ms
           -> 2904ms at 1440px on a throttled connection). Below the fold the
           reveal costs nothing and is left exactly as it was. -->
      <div class="hero-content">
        <span class="eyebrow gold"><i class="fa-solid fa-sparkles" aria-hidden="true"></i> {TAGLINE_PRIMARY}</span>
        <!-- The heading text ships in the markup, so it is complete and readable
             with no JavaScript and under reduced motion. js/pages/home.js reads
             it from the DOM and retypes it, so the two can never drift apart.
             The caret is an empty span drawn entirely in CSS: it holds no text
             node and no generated content, so it stays out of the accessible
             heading name and out of the page's text. -->
        <h1 class="typing-heading">
          <!-- Space reserver. Holds the complete heading so the <h1> always occupies
               the height of the finished line-wrap, whatever the typing animation is
               showing at that instant. It is a real text node, so it re-wraps with the
               viewport, with the font once it loads, and with browser zoom - there is no
               fixed height anywhere and nothing can be clipped. It is hidden with
               visibility, which keeps it out of the rendered page, out of the
               accessibility tree and out of the page's text, so the heading a visitor or
               a screen reader gets is still a single complete one. The inline
               visibility is a safety net: if css/pages/home.css ever fails to load, the
               reserver stays hidden instead of printing the heading twice. -->
          <span class="typing-reserve" aria-hidden="true" style="visibility:hidden">{hero_heading}</span>
          <span class="typing-live"><span id="typingTarget" class="grad-text">{hero_heading}</span><span class="typing-cursor" aria-hidden="true"></span></span>
        </h1>
        <p class="hero-sub">{hero_sub}</p>

        <div class="hero-actions">
          <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          <a href="services.html" class="btn btn-secondary">Explore Services</a>
        </div>
      </div>

      <div class="hero-visual" id="heroParallax">
        <div class="hero-visual-glow" aria-hidden="true"></div>
        {picture(
            "deepabi-concept",
            "Premium illustration of the DeepAbi brand concept, symbolizing economic empowerment and ambition through connected innovation and growth",
            800, 1200, "assets/images/home", css_class="hero-illustration-img", eager=True,
            skip_formats=HERO_SKIP
        )}
      </div>
    </div>

    <div class="container">
      <div class="hero-mv-grid">
        <div class="hero-mv-card">
          <div class="hero-mv-icon"><i class="fa-solid fa-bullseye" aria-hidden="true"></i></div>
          <span class="hero-mv-label">Mission</span>
          <h2 class="hero-mv-title">{MISSION}</h2>
          <p>{MISSION_DETAIL}</p>
        </div>
        <div class="hero-mv-card">
          <div class="hero-mv-icon"><i class="fa-solid fa-star" aria-hidden="true"></i></div>
          <span class="hero-mv-label">Vision</span>
          <h2 class="hero-mv-title">{VISION_HEADLINE}</h2>
          <p>{VISION_DETAIL}</p>
        </div>
      </div>
    </div>

    <!-- The hero statistics strip was removed here. It animated four counters -
         12+ Projects Delivered, 2+ Years Building, 24/7 Support & Monitoring and
         15+ Technologies Mastered - none of which was evidenced, and the 24/7
         figure was a service-level promise rather than a statistic. No
         replacement numbers have been invented. If verified figures are ever
         available, the strip was a `.stat-strip.hero-stats` grid of
         `.stat-item` blocks, each holding a `span.counter[data-target]`
         animated by initCounters() in js/common.js. -->

    <a href="#what-we-build" class="scroll-indicator" aria-label="Scroll to explore">
      <span>Scroll</span>
      <span class="mouse"></span>
    </a>
  </section>

  <!-- ============ WHAT WE BUILD ============ -->
  <section class="section" id="what-we-build">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow cyan">What We Do</span> -->
        <h2>What We Build</h2>
        <p style="margin:0 auto;">{wwb_lede}</p>
      </div>
      <div class="wwb-grid">
      {wwb_cards_html}
      </div>
    </div>
  </section>

  <!-- ============ RESPONSIVE DESIGN SHOWCASE ("Built & Tested Across All Devices") ============ -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow gold">Built &amp; Tested Across All Devices</span> -->
        <h2>Built &amp; Tested Across All Devices</h2>
        <p style="margin:0 auto;">Our websites are carefully designed, tested and optimized across desktop, laptop, tablet and mobile devices to deliver a seamless user experience on every screen.</p>
      </div>

{device_showcase}
      <div class="responsive-content" data-reveal>
        <h3 class="responsive-heading">Responsive Website Design</h3>
        <p class="responsive-lede">Whether a visitor lands on a 27-inch monitor or a five-inch phone, the experience is built once and tested everywhere — not bolted on after the fact.</p>
        <div class="rf-grid">
        {rf_html}
        </div>
      </div>
    </div>
  </section>

  <!-- ============ WHY DEEPABI ============ -->
  <section class="section" id="why-deepabi">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow">Why Choose Us</span> -->
        <h2>Why DeepAbi</h2>
        <p style="margin:0 auto;">DeepAbi is a professional website development and software company built around reliability, transparency, and measurable results.</p>
      </div>
      <div class="grid-3">
        <div class="card why-card" data-reveal><div class="card-icon"><i class="fa-solid fa-bolt" aria-hidden="true"></i></div><h3>Fast, Disciplined Delivery</h3><p>Clear timelines and structured sprints mean your custom website development project ships on schedule.</p></div>
        <div class="card why-card" data-reveal><div class="card-icon"><i class="fa-solid fa-shield-halved" aria-hidden="true"></i></div><h3>Secure by Design</h3><p>Security and best practices are built in from the first commit, not bolted on afterward.</p></div>
        <div class="card why-card" data-reveal><div class="card-icon"><i class="fa-solid fa-diagram-project" aria-hidden="true"></i></div><h3>Scalable Architecture</h3><p>From small business website to enterprise website, systems are designed to grow without a rebuild.</p></div>
        <div class="card why-card" data-reveal><div class="card-icon"><i class="fa-solid fa-magnifying-glass-chart" aria-hidden="true"></i></div><h3>SEO-First Foundations</h3><p>Every build follows technical SEO best practices from day one, so search engines can find you.</p></div>
        <div class="card why-card" data-reveal><div class="card-icon"><i class="fa-solid fa-headset" aria-hidden="true"></i></div><h3>Long-Term Partnership</h3><p>We stay involved after launch with website maintenance, monitoring, and a direct line to our team.</p></div>
        <div class="card why-card" data-reveal><div class="card-icon"><i class="fa-solid fa-gauge-high" aria-hidden="true"></i></div><h3>Performance Obsessed</h3><p>Core Web Vitals and load-time budgets are tracked on every performance optimization project we ship.</p></div>
      </div>
    </div>
  </section>

  <!-- ============ PROCESS ============ -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow">Our Process</span> -->
        <h2>How We Work</h2>
        <p style="margin:0 auto;">Seven stages take your project from first conversation to a fully supported, live product.</p>
      </div>
      <div class="process-track" data-reveal>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i><span class="process-num">01</span></div><h3>Discover</h3><p>Goals &amp; audience</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-chart-line" aria-hidden="true"></i><span class="process-num">02</span></div><h3>Research</h3><p>Market analysis</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-pen-ruler" aria-hidden="true"></i><span class="process-num">03</span></div><h3>Design</h3><p>Wireframes &amp; UI</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-code" aria-hidden="true"></i><span class="process-num">04</span></div><h3>Development</h3><p>Scalable build</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-vial" aria-hidden="true"></i><span class="process-num">05</span></div><h4>Testing</h4><p>Cross-device QA</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-rocket" aria-hidden="true"></i><span class="process-num">06</span></div><h3>Deployment</h3><p>Production launch</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-screwdriver-wrench" aria-hidden="true"></i><span class="process-num">07</span></div><h3>Maintenance</h3><p>Ongoing support</p></div>
      </div>
    </div>
  </section>

  <!-- ============ FEATURED PROJECT ============ -->
  <section class="section">
    <div class="container">
      <div class="featured-project" data-reveal>
        <div class="featured-visual">
          {picture("featured-cardsession-platform", "Abstract mockup illustration of a commercial hardware and industrial supply website", 640, 446, "assets/images/projects")}
        </div>
        <div class="featured-copy">
          <span class="badge badge-mint"><i class="fa-solid fa-circle-check" aria-hidden="true"></i> Launched 2025</span>
          <h2 style="margin:14px 0;">Featured Success Story: Commercial Hardware &amp; Industrial Supply</h2>
          <p>A corporate commercial website built end-to-end for a hardware, electrical, electronics and industrial tools supplier &mdash; from business information architecture through a production launch in 4 weeks.</p>
          <ul class="featured-list">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Responsive commercial website design</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Product &amp; category showcase</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Business information architecture</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Contact &amp; enquiry integration</li>
          </ul>
          <a href="projects.html" class="btn btn-primary">View Our Work <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
  </section>
{testimonials_section}
  <!-- ============ CTA ============ -->
  <section class="section" style="padding-top:0;">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Ready to build your next digital experience?</h2>
        <p>Tell us about your website project and the support you need. We build websites for businesses in Mogappair, Nolambur and Anna Nagar.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </section>
'''

page(
    filename="index.html",
    active="home",
    title=seo_title,
    description=seo_desc,
    body=body,
    canonical_path="",
    extra_css='<link rel="stylesheet" href="css/pages/home.css">',
    extra_js='<script src="js/pages/home.js"></script>',
    schema=SCHEMA,
    body_class="hero-dark",
)
