"""Generates the eight dedicated service pages from service_data.SERVICES.

Every page shares one information architecture so the section order is
predictable for visitors and for search engines:

  1. Hero (breadcrumb, name, value line, CTAs)
  2. What is this service?          - plain language, no jargon
  3. What we can build              - solution categories
  4. Real business use cases        - written as possibilities, never as
                                      completed DeepAbi projects
  5. Who is it for?
  6. Capabilities
  7. How we approach it             - shared 7-step process
  8. Related services               - cross-links
  9. CTA

Website Development additionally carries the detailed sub-service blocks and
the FAQ that already existed on the old services.html / service-detail.html,
rather than replacing that material with new copy.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture, SITE_URL
from service_data import SERVICES, BY_SLUG, page_file

EXTRA_CSS = ('<link rel="stylesheet" href="css/pages/services.css">\n'
             '<link rel="stylesheet" href="css/pages/service.css">')

# Shared, deliberately simple. Every page shows the same seven steps so the
# process reads as one company method rather than nine different ones.
PROCESS = [
    ("fa-solid fa-comments", "Understand", "Your goals &amp; problem"),
    ("fa-solid fa-clipboard-list", "Plan", "Scope &amp; priorities"),
    ("fa-solid fa-pen-ruler", "Design", "Structure &amp; screens"),
    ("fa-solid fa-code", "Develop", "Build in stages"),
    ("fa-solid fa-vial", "Test", "Check on real devices"),
    ("fa-solid fa-rocket", "Deploy", "Go live"),
    ("fa-solid fa-screwdriver-wrench", "Maintain", "Support &amp; improve"),
]


def breadcrumb(name):
    return f'''<nav class="svc-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
        <a href="services.html">Services</a>
        <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
        <span aria-current="page">{name}</span>
      </nav>'''


def process_track():
    steps = "\n".join(
        f'        <div class="process-step"><div class="process-dot"><i class="{icon}" aria-hidden="true"></i>'
        f'<span class="process-num">0{i}</span></div><h4>{title}</h4><p>{sub}</p></div>'
        for i, (icon, title, sub) in enumerate(PROCESS, start=1)
    )
    return f'<div class="process-track" data-reveal>\n{steps}\n      </div>'


def build_cards(items):
    cards = "\n".join(
        f'''        <div class="svc-card" data-reveal>
          <div class="svc-icon"><i class="{icon}" aria-hidden="true"></i></div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>''' for icon, title, desc in items
    )
    return f'<div class="svc-grid">\n{cards}\n      </div>'


def usecases(items):
    blocks = "\n".join(
        f'''        <div class="svc-usecase" data-reveal>
          <h4>{label}</h4>
          <p>{text}</p>
        </div>''' for label, text in items
    )
    return f'<div class="svc-usecases">\n{blocks}\n      </div>'


def capability_list(items):
    rows = "\n".join(
        f'          <div class="service-list-item"><i class="fa-solid fa-check" aria-hidden="true"></i>{i}</div>'
        for i in items
    )
    return f'<div class="service-list" data-reveal>\n{rows}\n        </div>'


def related(slugs):
    cards = "\n".join(
        f'''        <a href="{page_file(s)}" class="svc-card" data-reveal>
          <div class="svc-icon"><i class="{BY_SLUG[s]['icon']}" aria-hidden="true"></i></div>
          <h3>{BY_SLUG[s]['name']}</h3>
          <p>{BY_SLUG[s]['card']}</p>
          <span class="svc-card-link">Explore service <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span>
        </a>''' for s in slugs
    )
    return f'<div class="svc-grid svc-grid-3">\n{cards}\n      </div>'


def schema_for(svc):
    """Service + BreadcrumbList. No ratings, reviews or counts — none exist."""
    plain_name = svc["name"].replace("&amp;", "and")
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{plain_name}",
  "name": "{plain_name}",
  "description": "{svc['seo_desc'].replace('&amp;', 'and')}",
  "provider": {{
    "@type": "Organization",
    "name": "DeepAbi Innovations",
    "url": "{SITE_URL}"
  }},
  "areaServed": [
    {{"@type": "Place", "name": "Mogappair, Chennai"}},
    {{"@type": "Place", "name": "Ambattur, Chennai"}},
    {{"@type": "Place", "name": "Anna Nagar, Chennai"}},
    {{"@type": "City", "name": "Chennai"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE_URL}/"}},
    {{"@type": "ListItem", "position": 2, "name": "Services", "item": "{SITE_URL}/services.html"}},
    {{"@type": "ListItem", "position": 3, "name": "{plain_name}", "item": "{SITE_URL}/{page_file(svc['slug'])}"}}
  ]
}}
</script>'''


# ---------------------------------------------------------------------------
# Website Development only: the sub-service blocks and FAQ that already
# existed on services.html / service-detail.html, moved here rather than
# rewritten. Same markup, same images, same anchors, so old deep links such as
# services.html#business-websites still land on the right content.
# ---------------------------------------------------------------------------
def service_block(anchor, eyebrow, title, desc, items, image_name, image_alt, icon, reverse=False):
    order_class = " reverse" if reverse else ""
    items_html = "\n".join(
        f'            <div class="service-list-item"><i class="fa-solid fa-check" aria-hidden="true"></i>{i}</div>'
        for i in items)
    return f'''
      <div class="service-block{order_class}" id="{anchor}" data-reveal>
        <div class="service-visual-wrap">
          <div class="service-visual">
            {picture(image_name, image_alt, 560, 373, "assets/images/services")}
          </div>
          <div class="service-big-icon"><i class="{icon}" aria-hidden="true"></i></div>
        </div>
        <div>
          <span class="eyebrow">{eyebrow}</span>
          <h2 style="font-size:30px; margin-bottom:14px;">{title}</h2>
          <p style="margin-bottom:22px;">{desc}</p>
          <div class="service-list">
{items_html}
          </div>
          <a href="contact.html" class="service-learn-more">Discuss This <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>'''


WEBDEV_BLOCKS = f'''
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Website Types</span>
        <h2>The kinds of websites we build</h2>
        <p style="margin:0 auto;">Different businesses need different things from a website. These are the shapes most projects take.</p>
      </div>
      {service_block(
        "business-websites", "Establish", "Business Websites",
        "A clean, conversion-aware presence for service-based and local businesses that need to look credible quickly and make contact easy.",
        ["Service &amp; Pricing Pages", "Local SEO Foundations", "Booking / Contact Integration",
         "Testimonials &amp; Case Studies", "Mobile-First Layouts", "Fast, Low-Maintenance CMS"],
        "business_websites", "Example of a business website layout", "fa-solid fa-store"
      )}
      {service_block(
        "corporate-websites", "Represent", "Corporate Websites",
        "Structured, trust-building sites for organisations with multiple departments, offices or product lines.",
        ["Multi-Department Structure", "Investor &amp; Press Sections", "Careers &amp; Culture Pages",
         "Multi-Region Content Support", "Brand System Implementation", "Governance-Ready CMS Roles"],
        "corporate_websites", "Example of a corporate website layout", "fa-solid fa-building", reverse=True
      )}
      {service_block(
        "landing-pages", "Convert", "Landing Pages",
        "Single-purpose pages engineered around one campaign goal — built to load fast and convert visitors without distraction.",
        ["Conversion-Focused Layouts", "A/B Test-Ready Structure", "Fast Mobile Load Times",
         "Lead Capture Integration", "Analytics Event Tracking", "Copy Written for the Funnel"],
        "landing_page", "Example of a landing page layout", "fa-solid fa-rocket"
      )}
      {service_block(
        "portfolio-websites", "Showcase", "Portfolio Websites",
        "Image-forward, fast-loading portfolio sites for studios, agencies and individual professionals.",
        ["Project Case Study Templates", "Optimized Image Galleries", "Filterable Work Grids",
         "Personal Brand Styling", "Contact &amp; Enquiry Forms", "Simple Content Updates"],
        "portfolio_websites", "Example of a portfolio website layout", "fa-solid fa-images", reverse=True
      )}
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow gold">Built In, Not Bolted On</span>
        <h2>Search visibility and speed</h2>
        <p style="margin:0 auto;">Two things that decide whether a website actually works. We handle them during the build rather than selling them back afterwards.</p>
      </div>
      {service_block(
        "seo", "Get Found", "SEO-Ready Development",
        "A website only works if people can find it. Technical foundations, clean page structure and proper analytics are set up as part of the build.",
        ["Technical SEO Foundations", "On-Page Structure", "Semantic, Crawlable Markup",
         "Search Console Setup", "Analytics Implementation", "Local SEO Groundwork"],
        "seo", "Illustration of search performance analytics", "fa-solid fa-magnifying-glass-chart"
      )}
      {service_block(
        "performance-optimization", "Stay Fast", "Performance Optimization",
        "Speed is a feature. Every layer is tuned so pages load quickly on ordinary phones and ordinary connections, not just on a fast office network.",
        ["Core Web Vitals", "Image Optimization", "Caching Strategy",
         "Code-Level Optimization", "CDN &amp; Edge Configuration", "Ongoing Performance Checks"],
        "performance_optimization", "Illustration of website performance metrics", "fa-solid fa-gauge-high", reverse=True
      )}
    </div>
  </div>

  <div class="section section-alt" id="faq">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">FAQs</span>
        <h2>Common questions</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="faq-item" open>
          <summary>How long does a typical website development project take?</summary>
          <p>Most business and corporate websites take four to eight weeks from kickoff to launch, depending on scope, content readiness and the number of review rounds. Custom web applications generally take longer and are scoped individually.</p>
        </details>
        <details class="faq-item">
          <summary>Do you write the content, or do we provide it?</summary>
          <p>Either. We can work from content you provide, or draft professional copy for your review as part of the engagement. Most projects use a mix of both.</p>
        </details>
        <details class="faq-item">
          <summary>What happens after the site launches?</summary>
          <p>Every build includes a 30-day post-launch support window at no extra cost. After that, most clients move to an ongoing <a href="service-software-maintenance.html">maintenance plan</a> covering updates, monitoring and backups.</p>
        </details>
        <details class="faq-item">
          <summary>Can you work with our existing design or brand guidelines?</summary>
          <p>Yes. If you have an existing design system or brand guide, we build within it. If not, we can establish one as part of the design phase.</p>
        </details>
      </div>
    </div>
  </div>
'''

WEBDEV_FAQ_SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a typical website development project take?",
      "acceptedAnswer": {"@type": "Answer", "text": "Most business and corporate websites take four to eight weeks from kickoff to launch, depending on scope, content readiness and the number of review rounds. Custom web applications generally take longer and are scoped individually."}
    },
    {
      "@type": "Question",
      "name": "Do you write the content, or do we provide it?",
      "acceptedAnswer": {"@type": "Answer", "text": "Either. We can work from content you provide, or draft professional copy for your review as part of the engagement. Most projects use a mix of both."}
    },
    {
      "@type": "Question",
      "name": "What happens after the site launches?",
      "acceptedAnswer": {"@type": "Answer", "text": "Every build includes a 30-day post-launch support window at no extra cost. After that, most clients move to an ongoing maintenance plan covering updates, monitoring and backups."}
    },
    {
      "@type": "Question",
      "name": "Can you work with our existing design or brand guidelines?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes. If you have an existing design system or brand guide, we build within it. If not, we can establish one as part of the design phase."}
    }
  ]
}
</script>'''


def build(svc):
    slug = svc["slug"]
    img_name, img_folder = svc["image"]
    what_is = "\n        ".join(f"<p>{p}</p>" for p in svc["what_is"])
    extra = WEBDEV_BLOCKS if slug == "website-development" else ""
    schema = schema_for(svc) + ("\n" + WEBDEV_FAQ_SCHEMA if slug == "website-development" else "")

    body = f'''
  <div class="page-header page-header-gradient services-hero">
    <div class="hero-bg" aria-hidden="true">
      <div class="mesh-blob blob-1"></div>
      <div class="mesh-blob blob-2"></div>
    </div>
    <div class="container">
      {breadcrumb(svc["name"])}
      <span class="eyebrow gold">{svc["name"]}</span>
      <h1>{svc["hero_line"]}</h1>
      <p>{svc["card"]}</p>
      <div class="services-hero-actions">
        <a href="contact.html" class="btn btn-accent btn-lg">Discuss Your Requirement <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        <a href="#what-we-can-build" class="btn btn-secondary btn-lg services-hero-btn-outline">What We Can Build</a>
      </div>
    </div>
  </div>

  <!-- WHAT IS THIS SERVICE -->
  <div class="section">
    <div class="container">
      <div class="svc-split" data-reveal>
        <div>
          <span class="eyebrow">In Plain Terms</span>
          <h2 style="font-size:28px; margin-bottom:16px;">What is {svc["name"].lower()}?</h2>
          {what_is}
        </div>
        <div class="svc-split-media">
          {picture(img_name, svc["image_alt"], 560, 373, img_folder)}
        </div>
      </div>
    </div>
  </div>

  <!-- WHAT WE CAN BUILD -->
  <div class="section section-alt" id="what-we-can-build">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">What We Can Build</span>
        <h2>Solutions in this area</h2>
        <p style="margin:0 auto;">Each of these is developed around your requirements rather than sold as a fixed package.</p>
      </div>
      {build_cards(svc["build"])}
    </div>
  </div>

  <!-- USE CASES -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow gold">In Practice</span>
        <h2>How a business could use this</h2>
        <p style="margin:0 auto;">Examples of what this service can solve. These illustrate what we can develop for you, not completed client projects.</p>
      </div>
      {usecases(svc["use_cases"])}
    </div>
  </div>
{extra}
  <!-- WHO IS IT FOR + CAPABILITIES -->
  <div class="section {'' if slug == 'website-development' else 'section-alt'}">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Who It's For</span>
        <h2>This usually suits</h2>
      </div>
      <div class="svc-audience" data-reveal>
        {"".join(f"<span>{a}</span>" for a in svc["audience"])}
      </div>

      <div class="section-head center" data-reveal style="margin-top:64px;">
        <span class="eyebrow cyan">Capabilities</span>
        <h2>What's included</h2>
      </div>
      {capability_list(svc["capabilities"])}
    </div>
  </div>

  <!-- PROCESS -->
  <div class="section {'section-alt' if slug == 'website-development' else ''}">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Process</span>
        <h2>How we approach it</h2>
        <p style="margin:0 auto;">The same steps on every project, scaled to its size.</p>
      </div>
      {process_track()}
    </div>
  </div>

  <!-- RELATED -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Related Services</span>
        <h2>Often paired with this</h2>
      </div>
      {related(svc["related"])}
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Tell us what you're trying to solve</h2>
        <p>Describe the problem in your own words. We'll tell you honestly whether this is the right service for it.</p>
        <a href="contact.html" class="btn btn-accent">Start a Conversation <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

    page(
        filename=page_file(slug),
        active="services",
        title=svc["seo_title"],
        description=svc["seo_desc"],
        extra_keywords=svc["keywords"],
        body=body,
        extra_css=EXTRA_CSS,
        schema=schema,
        body_class="hero-dark",
    )


for _svc in SERVICES:
    build(_svc)
