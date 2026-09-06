"""Website Development — dedicated service page.

This page is where the detailed Website Development material from the old
Services page now lives. All eight blocks (Website Development, Landing Pages,
Corporate Websites, Business Websites, Portfolio Websites, Website
Maintenance, SEO, Performance Optimization) are carried over verbatim: same
markup, same copy, same capability lists, same images, same anchors, same
alternating layout. The sub-service pill row came across too.

The one deliberately new piece is the hero, which is a proper service-page
hero rather than the old first block promoted into that role.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Website Development",
  "name": "Website Development",
  "description": "Professional website development for businesses, companies and brands — corporate, business, landing page and portfolio websites, built responsive, SEO-ready and fast.",
  "provider": {"@type": "Organization", "name": "DeepAbi Innovations", "url": "https://www.deepabi.com"},
  "areaServed": [
    {"@type": "Place", "name": "Mogappair, Chennai"},
    {"@type": "Place", "name": "Ambattur, Chennai"},
    {"@type": "Place", "name": "Anna Nagar, Chennai"},
    {"@type": "City", "name": "Chennai"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.deepabi.com/"},
    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://www.deepabi.com/services.html"},
    {"@type": "ListItem", "position": 3, "name": "Website Development", "item": "https://www.deepabi.com/service-website-development.html"}
  ]
}
</script>'''


def service_block(anchor, eyebrow, title, desc, items, image_name, image_alt, icon, reverse=False):
    """Carried over from the Services page unchanged."""
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
          <a href="contact.html" class="service-learn-more">Get Started <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>'''


body = f'''
  <!-- Redesigned service-page hero. Uses an existing project image for now. -->
  <div class="page-header page-header-gradient services-hero">
    <div class="hero-bg" aria-hidden="true">
      <div class="mesh-blob blob-1"></div>
      <div class="mesh-blob blob-2"></div>
    </div>
    <div class="container services-hero-grid">
      <div>
        <nav class="wd-breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
          <a href="services.html">Services</a>
          <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
          <span aria-current="page">Website Development</span>
        </nav>
        <span class="eyebrow gold">Website Development</span>
        <h1>Professional Websites Built for Business Growth</h1>
        <p>DeepAbi builds responsive, scalable and professionally structured websites for businesses, brands and organizations &mdash; fast to load, easy to update, and architected so they can grow without a rebuild.</p>
        <div class="services-hero-actions">
          <a href="contact.html" class="btn btn-accent btn-lg">Start a Website Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          <a href="#website-development" class="btn btn-secondary btn-lg services-hero-btn-outline">Explore Website Services</a>
        </div>
      </div>
      <div class="services-hero-visual">
        <div class="hero-visual-glow" aria-hidden="true"></div>
        {picture("corporate_website_design", "Illustration of a professionally structured corporate website layout", 480, 400, "assets/images/projects")}
      </div>
    </div>
  </div>

  <div class="section" style="padding-bottom:0;">
    <div class="container">
      <!-- Sub-service pill row, carried over from the Services page. -->
      <div class="service-quicknav" data-reveal>
        <a href="#website-development">Website Development</a>
        <a href="#landing-pages">Landing Pages</a>
        <a href="#corporate-websites">Corporate Websites</a>
        <a href="#business-websites">Business Websites</a>
        <a href="#portfolio-websites">Portfolio Websites</a>
        <a href="#website-maintenance">Website Maintenance</a>
        <a href="#seo">SEO</a>
        <a href="#performance-optimization">Performance Optimization</a>
      </div>

      {service_block(
        "website-development", "01 · Build", "Website Development",
        "We design and build fast, responsive websites and custom web applications tailored to your business — architected for growth from day one.",
        ["Custom Web Applications", "Component-Driven Front Ends", "API &amp; CMS Integration", "Responsive, Cross-Device Development", "Accessibility Built In", "Clean, Documented Codebase"],
        "website-development-workspace", "Illustration representing a website development project interface", "fa-solid fa-code"
      )}

      {service_block(
        "landing-pages", "02 · Convert", "Landing Pages",
        "Single-purpose pages engineered around one campaign goal — built to load fast and convert visitors without distraction.",
        ["Conversion-Focused Layouts", "A/B Test-Ready Structure", "Fast Mobile Load Times", "Lead Capture Integration", "Analytics Event Tracking", "Copy Written for the Funnel"],
        "landing_page", "Real landing page design example built by DeepAbi", "fa-solid fa-rocket", reverse=True
      )}

      {service_block(
        "corporate-websites", "03 · Represent", "Corporate Websites",
        "Structured, trust-building sites for organizations with multiple departments, offices, or product lines.",
        ["Multi-Department IA", "Investor &amp; Press Sections", "Careers &amp; Culture Pages", "Multi-Region Content Support", "Brand System Implementation", "Governance-Ready CMS Roles"],
        "corporate_websites", "Real corporate website design example built by DeepAbi", "fa-solid fa-building"
      )}

      {service_block(
        "business-websites", "04 · Establish", "Business Websites",
        "A clean, conversion-aware digital presence for service-based and local businesses that need to look credible fast.",
        ["Service &amp; Pricing Pages", "Local SEO Foundations", "Booking / Contact Integration", "Testimonials &amp; Case Studies", "Mobile-First Layouts", "Fast, Low-Maintenance CMS"],
        "business_websites", "Real business website design example built by DeepAbi", "fa-solid fa-store", reverse=True
      )}

      {service_block(
        "portfolio-websites", "05 · Showcase", "Portfolio Websites",
        "Image-forward, fast-loading portfolio sites for studios, agencies, and individual professionals.",
        ["Project Case Study Templates", "Optimized Image Galleries", "Filterable Work Grids", "Personal Brand Styling", "Contact &amp; Inquiry Forms", "Simple Content Updates"],
        "portfolio_websites", "Real portfolio website design example built by DeepAbi", "fa-solid fa-images"
      )}

      {service_block(
        "website-maintenance", "06 · Support", "Website Maintenance",
        "Launch day is the beginning, not the finish line. We keep your site updated, secure, and running smoothly with proactive, ongoing care.",
        ["Website Updates", "Bug Fixes", "Security Monitoring", "Performance Optimization", "Scheduled Backups", "Content Updates"],
        "website_maintenance", "Website maintenance and monitoring dashboard example", "fa-solid fa-screwdriver-wrench", reverse=True
      )}

      {service_block(
        "seo", "07 · Grow", "SEO",
        "We help your site get found. Technical foundations, on-page optimization, and proper analytics setup so growth is measurable.",
        ["Technical SEO", "On-Page SEO", "Speed Optimization", "Search Console Setup", "Analytics Implementation", "Keyword &amp; Content Strategy"],
        "seo", "SEO analytics and search performance dashboard example", "fa-solid fa-magnifying-glass-chart"
      )}

      {service_block(
        "performance-optimization", "08 · Optimize", "Performance Optimization",
        "Speed is a feature. We tune every layer of your site so pages load fast and score well on the metrics that matter.",
        ["Core Web Vitals", "Image Optimization", "Caching Strategy", "Code-Level Optimization", "CDN &amp; Edge Configuration", "Ongoing Performance Monitoring"],
        "performance_optimization", "Website performance optimization metrics example", "fa-solid fa-gauge-high", reverse=True
      )}

    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow gold">Want More Detail?</span> -->
        <h2>See It In Detail</h2>
        <p style="margin:0 auto;">Our full Website Development service detail page walks through overview, benefits, process, and FAQs &mdash; the same depth we apply to every engagement.</p>
      </div>
      <div style="text-align:center;" data-reveal>
        <a href="service-detail.html" class="btn btn-accent btn-lg btn-glow">View Full Service Detail <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Ready to start your website project?</h2>
        <p>Tell us what your business needs and we'll come back with a realistic scope and starting point &mdash; no obligation.</p>
        <a href="contact.html" class="btn btn-accent">Start a Website Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="service-website-development.html",
    active="services",
    title="Website Development Company in Chennai | DeepAbi Innovations",
    description="Professional website development in Chennai — corporate, business, landing page and portfolio websites built responsive, SEO-ready and fast by DeepAbi Innovations.",
    extra_keywords="website development company in Chennai, website developers Chennai, corporate website development Chennai, business website development Chennai",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/services.css">',
    schema=SCHEMA,
    body_class="hero-dark",
)
