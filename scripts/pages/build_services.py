"""Services page — high-level overview of DeepAbi's eight service categories.

The detailed Website Development material that used to live on this page has
moved, unchanged, to service-website-development.html (built by
build_website_development.py). This page now carries one overview block per
service, using the same .service-block component the page always used:
alternating image side, small label, title, short description, capability
list, CTA.

Each block's id matches the slug used by the navbar mega menu
(services.html#web-applications and friends), so those links now land on real
content instead of the top of the page.

Images are temporary re-uses of existing project assets. Swapping in a real
one later means changing the (image, folder) pair in SERVICES below — nothing
else changes.
"""
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
    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://www.deepabi.com/services.html"}
  ]
}
</script>'''


def service_block(anchor, eyebrow, title, desc, items, image_name, image_alt, icon,
                  cta_label, cta_href, folder="assets/images/services", reverse=False):
    """The page's existing service block, unchanged apart from two additions:
    a `folder` argument (so a block can use an image from any asset folder) and
    a per-service CTA label/href in place of a fixed 'Get Started'."""
    order_class = " reverse" if reverse else ""
    items_html = "\n".join(
        f'            <div class="service-list-item"><i class="fa-solid fa-check" aria-hidden="true"></i>{i}</div>'
        for i in items)
    return f'''
      <div class="service-block{order_class}" id="{anchor}" data-reveal>
        <div class="service-visual-wrap">
          <div class="service-visual">
            {picture(image_name, image_alt, 560, 373, folder)}
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
          <a href="{cta_href}" class="service-learn-more">{cta_label} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>'''


# (anchor, eyebrow, title, description, capabilities, image, folder, alt, icon,
#  cta label, cta href)
# Only Website Development has a dedicated page so far. The other seven CTAs
# point at their own section here until their pages are built — one href edit
# each when that happens.
SERVICES = [
    ("website-development", "01 · Build", "Website Development",
     "Professional websites for businesses, companies and brands — from landing pages and portfolios to complete corporate websites.",
     ["Corporate Websites", "Business Websites", "Landing Pages",
      "Responsive Design", "SEO-ready Structure", "Performance Optimization"],
     "website-development-workspace", "assets/images/services",
     "Illustration representing a website development project interface",
     "fa-solid fa-window-maximize",
     "Explore Website Development", "service-website-development.html"),

    ("web-applications", "02 · Operate", "Web Applications",
     "Browser-based applications that help a business manage information, customers and day-to-day operations from one place.",
     ["Business Dashboards", "Client Portals", "Internal Systems",
      "Database Integration", "Workflow Applications", "API Integration"],
     "web_application_development", "assets/images/projects",
     "Illustration representing a browser-based business application",
     "fa-solid fa-table-columns",
     "Explore Web Applications", "services.html#web-applications"),

    ("mobile-applications", "03 · Reach", "Mobile Applications",
     "Mobile applications built around a business service — for customers, for field teams, or for staff who work away from a desk.",
     ["Android Applications", "iOS Applications", "Cross-platform Apps",
      "Business Apps", "Customer Apps", "Backend Integration"],
     "mobile_portrait", "assets/images/projects",
     "Illustration of a business application shown on a mobile phone",
     "fa-solid fa-mobile-screen",
     "Explore Mobile Solutions", "services.html#mobile-applications"),

    ("desktop-applications", "04 · Equip", "Desktop Applications",
     "Software installed on the computers your team already uses, built for one job and able to work without a connection.",
     ["Windows Applications", "Internal Business Tools", "Productivity Software",
      "Data Management Tools", "Custom Workflows", "Offline/Hybrid Applications"],
     "desktop", "assets/images/projects",
     "Illustration of business software running on a desktop computer",
     "fa-solid fa-desktop",
     "Explore Desktop Software", "services.html#desktop-applications"),

    ("custom-software", "05 · Tailor", "Custom Software",
     "For processes no off-the-shelf product fits. Software designed around how your business actually works, rather than the other way round.",
     ["Tailored Business Systems", "Custom Workflows", "Process Automation",
      "Integration Solutions", "Operational Tools", "Scalable Architecture"],
     "mission", "assets/images/about",
     "Abstract illustration representing purpose-built software",
     "fa-solid fa-code",
     "Explore Custom Software", "services.html#custom-software"),

    ("saas-products", "06 · Scale", "SaaS Products",
     "Cloud-based products many customers can sign up for and use online, each with their own account and their own data kept separate.",
     ["Cloud-based Platforms", "Subscription Systems", "Multi-user Applications",
      "Secure Access", "Scalable Infrastructure", "Ongoing Product Development"],
     "enterprise_website_framework", "assets/images/projects",
     "Abstract illustration representing a cloud-based software platform",
     "fa-solid fa-cloud",
     "Explore SaaS Solutions", "services.html#saas-products"),

    ("ai-automation", "07 · Automate", "AI &amp; Automation",
     "Practical automation and AI applied to specific tasks — less retyping, less chasing, less copying between systems.",
     ["AI-powered Workflows", "Business Automation", "AI Assistants",
      "Intelligent Processing", "Repetitive Task Automation", "AI Integrations"],
     "technology-stack-network", "assets/images/technology",
     "Illustration of connected systems representing automated workflows",
     "fa-solid fa-robot",
     "Explore AI Solutions", "services.html#ai-automation"),

    ("software-maintenance", "08 · Sustain", "Software Maintenance",
     "Software stays useful only if it keeps up. Ongoing support, fixes and improvements for websites and applications alike.",
     ["Software Updates", "Bug Fixing", "Performance Optimization",
      "Security Improvements", "Feature Enhancements", "Ongoing Technical Support"],
     "website_maintenance", "assets/images/services",
     "Illustration representing ongoing software maintenance and monitoring",
     "fa-solid fa-screwdriver-wrench",
     "Explore Maintenance Services", "services.html#software-maintenance"),
]

blocks = "\n".join(
    service_block(anchor, eyebrow, title, desc, items, img, alt, icon, cta_label, cta_href,
                  folder=folder, reverse=(i % 2 == 1))
    for i, (anchor, eyebrow, title, desc, items, img, folder, alt, icon, cta_label, cta_href)
    in enumerate(SERVICES))

quicknav = "\n".join(
    f'        <a href="#{anchor}">{title}</a>' for anchor, _e, title, *_rest in SERVICES)

body = f'''
  <div class="page-header page-header-gradient services-hero">
    <div class="hero-bg" aria-hidden="true">
      <div class="mesh-blob blob-1"></div>
      <div class="mesh-blob blob-2"></div>
    </div>
    <div class="container services-hero-grid">
      <div>
        <span class="eyebrow gold">Our Services</span>
        <h1>Everything you need for a high-performing digital presence</h1>
        <p>Eight focused service lines covering the full lifecycle of your website or product &mdash; from first pixel to long-term performance.</p>
        <div class="services-hero-actions">
          <a href="contact.html" class="btn btn-accent btn-lg">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          <a href="#website-development" class="btn btn-secondary btn-lg services-hero-btn-outline">Explore Services</a>
        </div>
      </div>
      <div class="services-hero-visual">
        <div class="hero-visual-glow" aria-hidden="true"></div>
        {picture("services-hero-illustration", "Illustration of connected service modules orbiting a central hub, representing DeepAbi's full-lifecycle service offering", 480, 400, "assets/images/services")}
      </div>
    </div>
  </div>

  <div class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="service-quicknav" data-reveal>
{quicknav}
      </div>
{blocks}
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Not sure which service fits?</h2>
        <p>Tell us about your project and we'll recommend the right starting point &mdash; no obligation.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="services.html",
    active="services",
    title="Software Development Services in Chennai | DeepAbi Innovations",
    description="Website development, web and mobile applications, custom software, SaaS, AI automation and software maintenance — built around how your business actually works.",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/services.css">',
    schema=SCHEMA,
    body_class="hero-dark",
)
