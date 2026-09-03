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
    {"@type": "ListItem", "position": 2, "name": "Technologies", "item": "https://www.deepabi.com/technologies.html"}
  ]
}
</script>'''

TECHS = [
    ("fa-brands fa-html5", "HTML5", "Semantic markup foundation for accessible, SEO-ready pages.", "frontend", None),
    ("fa-brands fa-css3-alt", "CSS3", "Modern layout, animation, and theming without heavy frameworks.", "frontend", None),
    ("fa-brands fa-js", "JavaScript", "Core interactivity across every custom website development project.", "frontend", None),
    ("fa-brands fa-react", "React", "Component-driven UIs for complex, stateful web applications.", "frontend", None),
    ("fa-solid fa-n", "Next.js", "Server-rendered React for fast, SEO-friendly enterprise websites.", "frontend", None),
    ("fa-solid fa-wind", "Tailwind CSS", "Utility-first styling for consistent, rapid UI development.", "frontend", None),
    ("fa-brands fa-python", "Python", "Reliable, readable backend logic and automation scripting.", "backend", None),
    ("fa-solid fa-bolt", "FastAPI", "High-performance Python APIs for web application development.", "backend", None),
    ("fa-brands fa-node-js", "Node.js", "JavaScript backend runtime, on our near-term roadmap.", "backend", "Future"),
    ("fa-solid fa-database", "PostgreSQL", "Our default relational database for structured, transactional data.", "database", None),
    ("fa-solid fa-database", "MySQL", "A dependable relational option for common CMS and web stacks.", "database", None),
    ("fa-solid fa-leaf", "MongoDB", "Flexible document storage for rapidly evolving data models.", "database", None),
    ("fa-brands fa-aws", "AWS", "Scalable compute and storage infrastructure for enterprise workloads.", "cloud", None),
    ("fa-solid fa-cloud", "Cloudflare", "Global CDN, DNS, and edge security in front of every build.", "cloud", None),
    ("fa-solid fa-fire", "Firebase", "Managed backend services for fast-moving MVP and startup projects.", "cloud", None),
    ("fa-brands fa-docker", "Docker", "Containerized environments for consistent deployment pipelines.", "deployment", None),
    ("fa-brands fa-github", "GitHub Actions", "Automated CI/CD pipelines for testing and shipping releases.", "deployment", None),
    ("fa-solid fa-bolt-lightning", "Vercel / Netlify", "Zero-downtime static and edge deployment for front-end projects.", "deployment", None),
    ("fa-solid fa-globe", "GoDaddy", "Domain registration and DNS management for client websites.", "deployment", None),
    ("fa-solid fa-server", "Hostinger", "Reliable, cost-effective hosting for small business and startup websites.", "deployment", None),
    ("fa-brands fa-git-alt", "Git", "Version control discipline across every DeepAbi engagement.", "tools", None),
    ("fa-brands fa-github", "GitHub", "Source hosting, code review, and project tracking.", "tools", None),
    ("fa-solid fa-code", "VS Code", "Our standard editor for consistent tooling across the team.", "tools", None),
]

FILTERS = [
    ("all", "All"),
    ("frontend", "Frontend"),
    ("backend", "Backend"),
    ("database", "Database"),
    ("cloud", "Cloud"),
    ("deployment", "Deployment"),
    ("tools", "Tools"),
]


def tech_card(icon, name, desc, category, note):
    note_html = f'<span class="tech-note">{note}</span>' if note else ''
    cat_label = dict(FILTERS)[category]
    return f'''<div class="tech-card" data-cat="{category}">
        <div class="tech-card-top">
          <div class="tech-card-icon"><i class="{icon}" aria-hidden="true"></i></div>
          {note_html}
        </div>
        <h3>{name}</h3>
        <p>{desc}</p>
        <span class="tech-card-tag">{cat_label}</span>
      </div>'''


tech_cards_html = "\n      ".join(tech_card(*t) for t in TECHS)
filter_buttons_html = "\n        ".join(
    f'<button class="filter-btn{" active" if key == "all" else ""}" data-filter="{key}">{label}</button>'
    for key, label in FILTERS
)

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Technologies</span>
      <h1>Our technology stack</h1>
      <p>We choose tools for stability, performance, and long-term maintainability &mdash; not trend-chasing. Here's exactly what powers a DeepAbi custom website development and web application development project.</p>
    </div>
  </div>

  <div class="section" style="padding-bottom:0;">
    <div class="container">
      <div class="img-frame" data-reveal>
        {picture("technology-stack-network", "Abstract network illustration representing DeepAbi's connected technology stack", 1160, 700, "assets/images/technology", eager=False)}
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Stacks We Use</span>
        <h2>Explore Our Technology Stack</h2>
      </div>
      <div class="filter-bar center-bar" data-reveal>
        {filter_buttons_html}
      </div>
      <div class="tech-card-grid" id="techGrid" data-reveal>
      {tech_cards_html}
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Curious how we'd architect your project?</h2>
        <p>We're happy to walk through stack choices before you commit to anything.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="technologies.html",
    active="technologies",
    title="Software Development Technologies | DeepAbi Innovations",
    description="The engineering stack behind DeepAbi Innovations' software: React, Next.js, Tailwind CSS, Python, FastAPI, PostgreSQL, AWS and Cloudflare.",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/technologies.css">',
    extra_js='<script src="js/pages/technologies.js"></script>',
    schema=SCHEMA,
    extra_keywords="modern website design tools, technology solutions provider",
)
