import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture, MISSION, VISION_HEADLINE, TAGLINE_THIRD, ABOUT_MISSION_PARAGRAPH, ABOUT_VISION_PARAGRAPH

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.deepabi.com/"},
    {"@type": "ListItem", "position": 2, "name": "About", "item": "https://www.deepabi.com/about.html"}
  ]
}
</script>'''

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">About DeepAbi</span>
      <h1>Who we are</h1>
      <p>A focused technology studio engineering digital excellence, with a long-term, partnership-driven mindset.</p>
    </div>
  </div>

  <div class="section">
    <div class="container about-intro" data-reveal>
      <div class="img-frame">
        {picture("team-collaboration", "Abstract illustration representing a collaborative technology team workspace", 640, 434, "assets/images/about")}
      </div>
      <div>
        <span class="eyebrow">Who We Are</span>
        <h2 style="font-size:28px; margin-bottom:16px;">Engineers and designers, working as one team</h2>
        <p style="margin-bottom:14px;">DeepAbi is a digital product and engineering studio. We build websites, software, and AI-powered solutions for businesses that need a technology partner they can actually reach — not a ticketing queue.</p>
        <p>We keep our team small and senior on purpose. Every project is led by people who write the code and make the design decisions, which means fewer handoffs, faster iteration, and a lot less lost in translation.</p>
      </div>
    </div>
  </div>

  <div class="section section-alt">
    <div class="container" data-reveal>
      <div class="section-head center">
        <span class="eyebrow">What Drives Us</span>
        <h2>Mission &amp; Vision</h2>
      </div>
      <div class="mv-grid">
        <div class="mv-card">
          <div class="mv-image">
            {picture("mission", "Illustration representing DeepAbi's mission of driving economic empowerment", 380, 253, "assets/images/about")}
          </div>
          <h3 class="mv-heading">Mission</h3>
          <p class="mv-catchline">{MISSION}</p>
          <p class="mv-paragraph">{ABOUT_MISSION_PARAGRAPH}</p>
        </div>
        <div class="mv-card">
          <div class="mv-image">
            {picture("vision", "Illustration representing DeepAbi's vision of ambition beyond imagination", 380, 253, "assets/images/about")}
          </div>
          <h3 class="mv-heading">Vision</h3>
          <p class="mv-catchline">{VISION_HEADLINE}</p>
          <p class="mv-paragraph">{ABOUT_VISION_PARAGRAPH}</p>
        </div>
      </div>
    </div>
  </div>

  <!-- CORE VALUES -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Core Values</span>
        <h2>What guides our work</h2>
      </div>
      <div class="grid-4" data-reveal>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-lightbulb" aria-hidden="true"></i></div><h3>Innovation</h3><p>We look for better ways to solve problems, not just familiar ones.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-eye" aria-hidden="true"></i></div><h3>Transparency</h3><p>Clear timelines, honest updates, and no surprises in scope or cost.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-code" aria-hidden="true"></i></div><h3>Engineering Excellence</h3><p>Every deliverable is held to a standard we'd put our own name on.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i></div><h3>Continuous Learning</h3><p>We refine our process and skills with every project we deliver.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-handshake" aria-hidden="true"></i></div><h3>Long-Term Relationships</h3><p>We aim to be the team you call for years, not just one project.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-shield-halved" aria-hidden="true"></i></div><h3>Security</h3><p>Security is treated as a foundation, not an afterthought.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-medal" aria-hidden="true"></i></div><h3>Quality</h3><p>We would rather ship later than ship something we're not proud of.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-heart" aria-hidden="true"></i></div><h3>Customer First</h3><p>Decisions are weighed against what actually serves the client.</p></div>
      </div>
    </div>
  </div>

  <!-- OUR PROCESS -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Our Process</span>
        <h2>How every DeepAbi project runs</h2>
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
  </div>

  <!-- JOURNEY / TIMELINE -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Our Journey</span>
        <h2>Where we are, and where we're headed</h2>
      </div>
      <div class="vtimeline" data-reveal>
        <div class="vtimeline-item">
          <div class="vtimeline-dot"></div>
          <span class="stage-pill now">Current Stage</span>
          <h4>Startup</h4>
          <p>Building our foundation — delivering websites, web applications, maintenance, and SEO for early clients with hands-on attention to every project.</p>
        </div>
        <div class="vtimeline-item future">
          <div class="vtimeline-dot"></div>
          <span class="stage-pill next">Next</span>
          <h4>AI &amp; Automation</h4>
          <p>Expanding into AI-powered features and workflow automation built directly into client products.</p>
        </div>
        <div class="vtimeline-item future">
          <div class="vtimeline-dot"></div>
          <span class="stage-pill future">Future Vision</span>
          <h4>Enterprise Software</h4>
          <p>Growing into a full enterprise software partner, supporting larger, more complex digital transformation projects.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- WHY DEEPABI -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Why DeepAbi</span>
        <h2>A partner, not just a vendor</h2>
        <p style="margin:0 auto;">We keep teams small and senior, communicate directly, and stay invested in your project long after launch.</p>
      </div>
      <div class="grid-3" data-reveal>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-comments" aria-hidden="true"></i></div><h3>Direct Communication</h3><p>You work directly with the people building your project — no account-manager layers.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-file-invoice-dollar" aria-hidden="true"></i></div><h3>Honest Pricing</h3><p>Clear scope and pricing upfront, with no hidden costs added later.</p></div>
        <div class="card"><div class="card-icon"><i class="fa-solid fa-arrows-rotate" aria-hidden="true"></i></div><h3>Built to Evolve</h3><p>We build systems that are easy to extend as your business changes.</p></div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Let's build your next chapter together</h2>
        <p>Tell us about your project and we'll get back to you within one business day.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="about.html",
    active="about",
    title="About DeepAbi | Professional Website Company &amp; Software Company",
    description="Learn about DeepAbi's mission, vision, and core values &mdash; a professional website design agency and software company driving economic empowerment through digital transformation.",
    extra_keywords="about DeepAbi, website design agency team, technology solutions company",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/about.css">',
    schema=SCHEMA,
)
