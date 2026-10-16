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

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "DeepAbi Innovations",
  "alternateName": "DeepAbi",
  "url": "https://www.deepabi.com",
  "logo": "https://www.deepabi.com/assets/images/logos/favicon-512.png",
  "description": "DeepAbi Innovations is a software development company in Chennai building websites, web and mobile applications, desktop and custom software, SaaS products, AI automation and software maintenance.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Mogappair, Chennai",
    "addressRegion": "Tamil Nadu",
    "addressCountry": "IN"
  },
  "areaServed": [
    { "@type": "Place", "name": "Mogappair, Chennai" },
    { "@type": "Place", "name": "Ambattur, Chennai" },
    { "@type": "Place", "name": "Anna Nagar, Chennai" },
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

# The home hero is the largest paint on the site. Its AVIF encode is 166KB
# against 73KB for the JPEG, so AVIF is deliberately not offered for this one
# image - serving it would make the hero heavier, not lighter.
HERO_SKIP = ("avif",)

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


TESTIMONIALS = [
    ("client-avatar-1", "Portrait placeholder for Aarav Rao", "DeepAbi rebuilt our site in under six weeks and it finally loads fast on mobile. Our contact form submissions doubled within the first month.", "Aarav Rao", "Founder, Northline Consulting"),
    ("client-avatar-2", "Portrait placeholder for Priya Kapoor", "What stood out was the communication. We always knew exactly what stage the project was in, and nothing shipped without our sign-off.", "Priya Kapoor", "Marketing Lead, Verdant Foods Co."),
    ("client-avatar-3", "Portrait placeholder for Samuel Ntuli", "They handled our SEO migration without losing a single ranking position, which is more than I can say for the last two agencies we worked with.", "Samuel Ntuli", "Operations Director, Harborview Logistics"),
    ("client-avatar-4", "Portrait placeholder for Meera Joshi", "Our new landing page converts noticeably better and the DeepAbi team kept us updated every single week without us having to chase them.", "Meera Joshi", "Growth Lead, Fieldstone Analytics"),
]

testimonial_slides_html = "\n          ".join(
    testimonial_slide(i == 0, *t) for i, t in enumerate(TESTIMONIALS)
)

# Visible hero copy and the meta description describe what is actually on
# offer. Both revert with the registry flags.
if WEBSITE_ONLY_MODE:
    hero_sub = ("We build modern, scalable websites &mdash; from a single landing page to a "
                "complete corporate site &mdash; designed to load fast, read well on a phone "
                "and bring you enquiries.")
    seo_desc = ("DeepAbi Innovations builds professional business, corporate, landing page and "
                "portfolio websites for businesses in Mogappair and across Chennai, with "
                "maintenance, SEO and performance support.")
else:
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
      <div class="hero-content" data-reveal>
        <span class="eyebrow gold"><i class="fa-solid fa-sparkles" aria-hidden="true"></i> {TAGLINE_PRIMARY}</span>
        <h1 class="typing-heading">
          <span id="typingTarget" class="grad-text" aria-hidden="true"></span><span class="typing-cursor" aria-hidden="true">|</span>
          <span class="sr-only">Building Intelligent Digital Solutions</span>
        </h1>
        <p class="hero-sub">{hero_sub}</p>

        <div class="hero-actions">
          <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          <a href="services.html" class="btn btn-secondary">Explore Services</a>
        </div>
      </div>

      <div class="hero-visual" id="heroParallax" data-reveal="scale">
        <div class="hero-visual-glow" aria-hidden="true"></div>
        {picture(
            "deepabi-concept",
            "Premium illustration of the DeepAbi brand concept, symbolizing economic empowerment and ambition through connected innovation and growth",
            1024, 1536, "assets/images/home", css_class="hero-illustration-img", eager=True,
            skip_formats=HERO_SKIP
        )}
      </div>
    </div>

    <div class="container">
      <div class="hero-mv-grid" data-reveal>
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

    <div class="container">
      <div class="stat-strip hero-stats" data-reveal>
        <div class="stat-item"><div class="num"><span class="counter" data-target="12">0</span><span class="grad-text">+</span></div><div class="label">Projects Delivered</div></div>
        <div class="stat-item"><div class="num"><span class="counter" data-target="2">0</span><span class="grad-text">+</span></div><div class="label">Years Building</div></div>
        <div class="stat-item"><div class="num"><span class="counter" data-target="24">0</span><span class="grad-text">/7</span></div><div class="label">Support &amp; Monitoring</div></div>
        <div class="stat-item"><div class="num"><span class="counter" data-target="15">0</span><span class="grad-text">+</span></div><div class="label">Technologies Mastered</div></div>
      </div>
    </div>

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
          {picture("featured-cardsession-platform", "Abstract mockup illustration of a commercial hardware and industrial supply website", 640, 434, "assets/images/projects")}
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

  <!-- ============ CTA ============ -->
  <section class="section" style="padding-top:0;">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Ready to build your next digital experience?</h2>
        <p>Tell us about your project and we'll get back to you within one business day with next steps.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </section>
'''

page(
    filename="index.html",
    active="home",
    title="DeepAbi Innovations | Software Development Company in Chennai",
    description=seo_desc,
    body=body,
    canonical_path="",
    extra_css='<link rel="stylesheet" href="css/pages/home.css">',
    extra_js='<script src="js/pages/home.js"></script>',
    schema=SCHEMA,
    body_class="hero-dark",
)
