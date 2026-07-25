import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture

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

def project_card(cat, image, alt, tag, title, desc, reviewer, review):
    return f'''
        <div class="project-card" data-cat="{cat}">
          <div class="mock-wrap"><span class="coming-soon-badge">Case Study Soon</span>
            <div class="mock-browser"><div class="mock-browser-bar"><span></span><span></span><span></span></div>
            {picture(image, alt, 1100, 620, "assets/images/projects", css_class="mock-browser-body-img")}
            </div>
          </div>
          <div class="project-card-body">
            <span class="tag">{tag}</span>
            <h3 style="font-size:16.5px; margin-bottom:8px;">{title}</h3>
            <p style="font-size:13.5px; margin-bottom:14px;">{desc}</p>
            <div class="mini-review"><i class="fa-solid fa-quote-left" aria-hidden="true"></i> "{review}" <span>&mdash; {reviewer}</span></div>
          </div>
        </div>'''

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Our Work</span>
      <h1>Projects &amp; Success Stories</h1>
      <p>We're a young, senior-led website development company building our public case-study library one launch at a time. Here's our featured success story and current project types &mdash; from small business website builds to custom web application development.</p>
    </div>
  </div>

  <!-- FEATURED CASE STUDY -->
  <div class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="featured-case" data-reveal>
        <div class="featured-case-visual">
          <span class="launch-badge"><i class="fa-solid fa-rocket" aria-hidden="true"></i> Launched 2024</span>
          {picture("featured-cardsession-platform", "Abstract mockup illustration of the Card Session payments website", 700, 475, "assets/images/projects")}
        </div>
        <div class="featured-case-copy">
          <span class="eyebrow mint">Featured Success Story</span>
          <h2 style="font-size:30px; margin-bottom:14px;">Card Session</h2>
          <p style="margin-bottom:14px;">A payments-focused web application platform designed and built end-to-end for a fintech client &mdash; from information architecture through a production launch in 2024.</p>
          <p style="margin-bottom:22px;">The brief called for a fast, trustworthy interface that could explain session-based card payment tooling to both non-technical buyers and technical evaluators without losing credibility with either audience.</p>
          <div class="case-meta">
            <div><span>Industry</span><strong>Financial Technology</strong></div>
            <div><span>Timeline</span><strong>9 Weeks</strong></div>
            <div><span>Services</span><strong>Development, SEO, Performance</strong></div>
          </div>
          <div class="mini-review" style="margin-top:22px;">
            <i class="fa-solid fa-quote-left" aria-hidden="true"></i> "DeepAbi understood our product faster than any agency we'd talked to. The site shipped on time and our conversion rate improved within the first quarter." <span>&mdash; Devika Menon, Head of Product, Card Session</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- DEVICE PREVIEW -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Responsive Website Design</span>
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

  <!-- PROJECT GRID -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Our Work</span>
        <h2>What We Build</h2>
        <p style="margin:0 auto;">Small business websites, corporate website design, landing page development, portfolio websites, and custom web application development.</p>
      </div>
      <div class="filter-bar" data-reveal>
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="business">Business</button>
        <button class="filter-btn" data-filter="corporate">Corporate</button>
        <button class="filter-btn" data-filter="landing">Landing Page</button>
        <button class="filter-btn" data-filter="webapp">Web App</button>
      </div>

      <div class="grid-3" id="projectsGrid" data-reveal>
        {project_card("business", "local_services_website", "Screenshot of a local services website built by DeepAbi", "Business", "Local Services Website", "A clean, conversion-focused concept for a service-based small business website.", "Dummy Client — Northline Consulting", "Exactly the professional presence we needed to start winning bigger contracts.")}
        {project_card("corporate", "corporate_website_design", "Screenshot of a corporate website design built by DeepAbi", "Corporate", "Corporate Website Design", "Structured, trust-building corporate website design for a multi-department organization.", "Dummy Client — Verdant Foods Co.", "Our regional teams finally have one consistent site to point customers to.")}
        {project_card("landing", "landing_page_development", "Screenshot of a product launch landing page built by DeepAbi", "Landing Page", "Landing Page Development", "High-conversion landing page development built for a single campaign goal.", "Dummy Client — Harborview Logistics", "Our launch page converted noticeably better than the agency template we used before.")}
        {project_card("webapp", "web_application_development", "Screenshot of an internal dashboard web application built by DeepAbi", "Web App", "Web Application Development", "Custom web application development for internal operations and reporting.", "Dummy Client — Fieldstone Analytics", "The dashboard cut our weekly reporting time down from hours to minutes.")}
        {project_card("business", "professional_services_site", "Screenshot of a professional services website built by DeepAbi", "Business", "Professional Services Site", "A polished small business website concept for a consulting practice.", "Dummy Client — Elmswood Partners", "Clean, fast, and easy for our non-technical team to update.")}
        {project_card("corporate", "enterprise_website_framework", "Screenshot of an enterprise website framework built by DeepAbi", "Corporate", "Enterprise Website Framework", "A scalable enterprise website framework designed for multi-region content.", "Dummy Client — Aster Industrial Group", "It scaled to three regional sites without any structural rework.")}
      </div>

      <div style="text-align:center; margin-top:40px; color:var(--text-secondary); font-size:14.5px;" data-reveal>
        <i class="fa-solid fa-circle-notch" style="color:var(--violet); margin-right:8px;" aria-hidden="true"></i>
        Full case studies with live links and client results are being published as projects launch.
      </div>
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
    title="Projects &amp; Success Stories | DeepAbi Website Development Company",
    description="See DeepAbi's featured success story, Card Session, plus small business, corporate, landing page, and web application development project concepts across desktop, tablet, and mobile.",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/projects.css">',
    extra_js='<script src="js/pages/projects.js"></script>',
    schema=SCHEMA,
    extra_keywords="e-commerce website, portfolio website, success stories, client case studies",
)
