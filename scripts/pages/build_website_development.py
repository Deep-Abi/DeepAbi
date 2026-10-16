"""Website Development — dedicated service page.

This page is where the detailed Website Development material from the old
Services page now lives. All eight blocks (Website Development, Landing Pages,
Corporate Websites, Business Websites, Portfolio Websites, Website
Maintenance, SEO, Performance Optimization) are carried over verbatim: same
markup, same copy, same capability lists, same images, same anchors, same
alternating layout. The sub-service pill row came across too.

The one deliberately new piece is the hero, which is a proper service-page
hero rather than the old first block promoted into that role.

This page also absorbed the three useful sections from the retired
service-detail.html — "What you get with a DeepAbi build", "How a website
development project runs" and "Often paired with Website Development" — with
their eyebrow labels removed. The legacy FAQ was not migrated. The old
"See It In Detail" cross-link section is gone with it, so this page is now the
single destination for Website Development.
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

  <!-- Migrated from the retired service-detail.html. Same copy and markup,
       with the small eyebrow labels dropped and the legacy FAQ left behind. -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <h2>What you get with a DeepAbi build</h2>
      </div>
      <div class="grid-4" data-reveal>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-gauge-high"></i></div><h3>Built for Speed</h3><p>Performance budgets are set before a single line of code is written.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-mobile-screen"></i></div><h3>Responsive by Default</h3><p>Every page is designed and tested across desktop, tablet, and mobile.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-magnifying-glass-chart"></i></div><h3>SEO-Ready Structure</h3><p>Semantic HTML and clean metadata from day one, not retrofitted later.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-universal-access"></i></div><h3>Accessible by Design</h3><p>Keyboard navigation, contrast, and screen-reader support are part of the build, not an afterthought.</p></div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <h2>How a website development project runs</h2>
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
  </div>

  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <h2>Often paired with Website Development</h2>
      </div>
      <div class="grid-3" data-reveal>
        <a href="#website-maintenance" class="card"><div class="card-icon"><i class="fa-solid fa-screwdriver-wrench"></i></div><h3>Website Maintenance</h3><p>Keep your new site updated, secure, and monitored after launch.</p></a>
        <a href="#seo" class="card"><div class="card-icon"><i class="fa-solid fa-magnifying-glass-chart"></i></div><h3>SEO</h3><p>Make sure your new site can actually be found in search.</p></a>
        <a href="#performance-optimization" class="card"><div class="card-icon"><i class="fa-solid fa-gauge-high"></i></div><h3>Performance Optimization</h3><p>Tune Core Web Vitals for a faster, smoother experience.</p></a>
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
