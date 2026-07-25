import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture, MISSION, MISSION_DETAIL, VISION_HEADLINE, VISION_DETAIL, TAGLINE_PRIMARY

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "DeepAbi",
  "url": "https://www.deepabi.com",
  "logo": "https://www.deepabi.com/assets/images/logos/favicon-512.png",
  "description": "DeepAbi is a professional website design agency and software company delivering custom website development, corporate website design, SEO, and digital solutions for small business and enterprise clients.",
  "email": "deepabi.tech@gmail.com",
  "telephone": ["+91 8946097125", "+91 8925279380"],
  "sameAs": [
    "https://github.com/deepabi",
    "https://www.linkedin.com/company/deepabi",
    "https://www.instagram.com/deepabi"
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

WHAT_WE_BUILD = [
    ("fa-solid fa-store", "Business Websites", "Clean, conversion-aware sites that make small and local businesses look credible fast.", "business-websites"),
    ("fa-solid fa-building", "Corporate Websites", "Structured, trust-building corporate website design for multi-department organizations.", "corporate-websites"),
    ("fa-solid fa-rocket", "Landing Pages", "Single-purpose, high-conversion landing page builds engineered around one campaign goal.", "landing-pages"),
    ("fa-solid fa-images", "Portfolio Websites", "Image-forward, fast-loading portfolio sites for studios, agencies, and individual professionals.", "portfolio-websites"),
    ("fa-solid fa-screwdriver-wrench", "Website Maintenance", "Ongoing updates, security monitoring, and website support so your site never goes stale.", "website-maintenance"),
    ("fa-solid fa-magnifying-glass-chart", "SEO Optimization", "Technical SEO, on-page optimization, and analytics that make growth measurable.", "seo"),
    ("fa-solid fa-gauge-high", "Performance Optimization", "Core Web Vitals, caching, and code-level tuning for a genuinely fast website.", "performance-optimization"),
    ("fa-solid fa-diagram-project", "Scalable Architecture", "Systems designed to grow from first launch to enterprise-level traffic without a rebuild.", "website-development"),
]


def build_card(icon, title, desc, anchor):
    return f'''<div class="wwb-card" data-reveal>
        <div class="wwb-icon"><i class="{icon}" aria-hidden="true"></i></div>
        <h3>{title}</h3>
        <p>{desc}</p>
        <a href="services.html#{anchor}" class="wwb-more">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>'''


wwb_cards_html = "\n      ".join(build_card(*c) for c in WHAT_WE_BUILD)

RESPONSIVE_FEATURES = [
    ("fa-solid fa-mobile-screen-button", "Mobile-First Layouts", "Designed for the smallest screen first, then scaled up with intention."),
    ("fa-solid fa-text-height", "Fluid Typography", "Type scales smoothly across breakpoints instead of jumping at fixed sizes."),
    ("fa-solid fa-hand-pointer", "Touch-Friendly UI", "Tap targets, spacing, and gestures built for real fingers, not just a mouse."),
    ("fa-solid fa-display", "Cross-Device QA", "Every build is checked on real desktop, tablet, and mobile viewports before launch."),
]


def responsive_feature(icon, title, desc):
    return f'''<div class="rf-item">
        <div class="rf-icon"><i class="{icon}" aria-hidden="true"></i></div>
        <div class="rf-text"><h4>{title}</h4><p>{desc}</p></div>
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
                <div><h4>{name}</h4><span>{role}</span></div>
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
        <p class="hero-sub">We build modern, scalable and intelligent digital products &mdash; from custom website development to enterprise web applications &mdash; that help businesses grow faster.</p>

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
            700, 641, "assets/images/home", css_class="hero-illustration-img", eager=True
        )}
      </div>
    </div>

    <div class="container">
      <div class="hero-mv-grid" data-reveal>
        <div class="hero-mv-card">
          <div class="hero-mv-icon"><i class="fa-solid fa-bullseye" aria-hidden="true"></i></div>
          <span class="hero-mv-label">Mission</span>
          <h3>{MISSION}</h3>
          <p>{MISSION_DETAIL}</p>
        </div>
        <div class="hero-mv-card">
          <div class="hero-mv-icon"><i class="fa-solid fa-star" aria-hidden="true"></i></div>
          <span class="hero-mv-label">Vision</span>
          <h3>{VISION_HEADLINE}</h3>
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
        <span class="eyebrow cyan">What We Do</span>
        <h2>What We Build</h2>
        <p style="margin:0 auto;">From a first business website to a fully custom web application, DeepAbi covers the complete lifecycle of your digital presence.</p>
      </div>
      <div class="wwb-grid">
      {wwb_cards_html}
      </div>
    </div>
  </section>

  <!-- ============ RESPONSIVE DESIGN SHOWCASE ("Built for Every Screen") ============ -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow gold">Built for Every Screen</span>
        <h2>Built for Every Screen</h2>
        <p style="margin:0 auto;">Every DeepAbi build is designed mobile-first and tested across desktop, tablet, and mobile — so your site looks intentional on every screen, not just the one on your desk.</p>
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
        <span class="eyebrow">Why Choose Us</span>
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
        <span class="eyebrow">Our Process</span>
        <h2>How We Work</h2>
        <p style="margin:0 auto;">Seven stages take your project from first conversation to a fully supported, live product.</p>
      </div>
      <div class="process-track" data-reveal>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i><span class="process-num">01</span></div><h4>Discover</h4><p>Goals &amp; audience</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-chart-line" aria-hidden="true"></i><span class="process-num">02</span></div><h4>Research</h4><p>Market analysis</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-pen-ruler" aria-hidden="true"></i><span class="process-num">03</span></div><h4>Design</h4><p>Wireframes &amp; UI</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-code" aria-hidden="true"></i><span class="process-num">04</span></div><h4>Development</h4><p>Scalable build</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-vial" aria-hidden="true"></i><span class="process-num">05</span></div><h4>Testing</h4><p>Cross-device QA</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-rocket" aria-hidden="true"></i><span class="process-num">06</span></div><h4>Deployment</h4><p>Production launch</p></div>
        <div class="process-step"><div class="process-dot"><i class="fa-solid fa-screwdriver-wrench" aria-hidden="true"></i><span class="process-num">07</span></div><h4>Maintenance</h4><p>Ongoing support</p></div>
      </div>
    </div>
  </section>

  <!-- ============ FEATURED PROJECT ============ -->
  <section class="section">
    <div class="container">
      <div class="featured-project" data-reveal>
        <div class="featured-visual">
          {picture("featured-cardsession-platform", "Abstract mockup illustration representing the Card Session website interface", 640, 434, "assets/images/projects")}
        </div>
        <div class="featured-copy">
          <span class="badge badge-mint"><i class="fa-solid fa-circle-check" aria-hidden="true"></i> Launched 2024</span>
          <h2 style="margin:14px 0;">Featured Success Story: Card Session</h2>
          <p>Card Session is a payments-focused web application platform we designed and built end-to-end &mdash; from information architecture through a production launch.</p>
          <ul class="featured-list">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Custom web application front end</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Technical SEO &amp; analytics setup</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Core Web Vitals performance tuning</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Ongoing maintenance &amp; monitoring</li>
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
        <span class="eyebrow">Client Feedback</span>
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
    title="DeepAbi | Website Development &amp; Digital Solutions Company",
    description="DeepAbi is a professional website development and technology company delivering custom website development, corporate website design, SEO, and digital solutions for small business and enterprise clients.",
    body=body,
    canonical_path="",
    extra_css='<link rel="stylesheet" href="css/pages/home.css">',
    extra_js='<script src="js/pages/home.js"></script>',
    schema=SCHEMA,
    body_class="hero-dark",
    extra_keywords="website developers near me, hire website development company, business growth website",
)
