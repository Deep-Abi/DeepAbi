import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Website Development",
  "provider": {"@type": "Organization", "name": "DeepAbi", "url": "https://www.deepabi.com"},
  "areaServed": "Worldwide",
  "description": "Custom website and web application development, including business, corporate, landing page, and portfolio websites, built on a modern, scalable stack."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a typical website development project take?",
      "acceptedAnswer": {"@type": "Answer", "text": "Most business and corporate websites take four to eight weeks from kickoff to launch, depending on scope, content readiness, and the number of review rounds. Custom web applications generally take longer and are scoped individually."}
    },
    {
      "@type": "Question",
      "name": "Do you write the content, or do we provide it?",
      "acceptedAnswer": {"@type": "Answer", "text": "Either. We can work from content you provide, or draft professional copy for your review as part of the engagement. Most projects use a mix of both."}
    },
    {
      "@type": "Question",
      "name": "What happens after the site launches?",
      "acceptedAnswer": {"@type": "Answer", "text": "Every build includes a 30-day post-launch support window at no extra cost. After that, most clients move to an ongoing maintenance plan covering updates, monitoring, and backups."}
    },
    {
      "@type": "Question",
      "name": "Can you work with our existing design or brand guidelines?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes. If you have an existing design system or brand guide, we build within it. If not, we can establish one as part of the design phase."}
    }
  ]
}
</script>'''

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Service Detail</span>
      <h1>Website Development</h1>
      <p>Fast, responsive, scalable websites and web applications, engineered for growth from the first commit.</p>
      <div style="display:flex; gap:16px; margin-top:32px; flex-wrap:wrap;">
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        <a href="#faq" class="btn btn-secondary">View FAQs</a>
      </div>
    </div>
  </div>

  <!-- OVERVIEW -->
  <div class="section">
    <div class="container detail-overview" data-reveal>
      <div>
        <span class="eyebrow">Overview</span>
        <h2 style="font-size:28px; margin-bottom:16px;">A website built like a product, not a brochure</h2>
        <p style="margin-bottom:14px;">Website Development at DeepAbi covers business websites, corporate websites, landing pages, portfolio sites, and fully custom web applications. Every engagement starts from the same principle: the site should be fast, accessible, easy for your team to update, and built on an architecture that won't need a rebuild the moment you outgrow it.</p>
        <p>We work in a modern component-based stack, which means new pages, sections, and features can be added later without touching the foundation. Every project ships with clean, documented code and a clear handover — you're never locked into us to make a basic content change.</p>
      </div>
      <div class="img-frame">
        {picture("website-development-workspace", "Illustration representing a website development interface with component blocks", 560, 425, "assets/images/services")}
      </div>
    </div>
  </div>

  <!-- BENEFITS -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Benefits</span>
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

  <!-- PROCESS -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">Process</span>
        <h2>How a website development project runs</h2>
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

  <!-- FAQ -->
  <div class="section" id="faq">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow">FAQs</span>
        <h2>Common questions</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="faq-item" open>
          <summary>How long does a typical website development project take?</summary>
          <p>Most business and corporate websites take four to eight weeks from kickoff to launch, depending on scope, content readiness, and the number of review rounds. Custom web applications generally take longer and are scoped individually.</p>
        </details>
        <details class="faq-item">
          <summary>Do you write the content, or do we provide it?</summary>
          <p>Either. We can work from content you provide, or draft professional copy for your review as part of the engagement. Most projects use a mix of both.</p>
        </details>
        <details class="faq-item">
          <summary>What happens after the site launches?</summary>
          <p>Every build includes a 30-day post-launch support window at no extra cost. After that, most clients move to an ongoing maintenance plan covering updates, monitoring, and backups.</p>
        </details>
        <details class="faq-item">
          <summary>Can you work with our existing design or brand guidelines?</summary>
          <p>Yes. If you have an existing design system or brand guide, we build within it. If not, we can establish one as part of the design phase.</p>
        </details>
      </div>
    </div>
  </div>

  <!-- RELATED -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <span class="eyebrow cyan">Related Services</span>
        <h2>Often paired with Website Development</h2>
      </div>
      <div class="grid-3" data-reveal>
        <a href="services.html#website-maintenance" class="card"><div class="card-icon"><i class="fa-solid fa-screwdriver-wrench"></i></div><h3>Website Maintenance</h3><p>Keep your new site updated, secure, and monitored after launch.</p></a>
        <a href="services.html#seo" class="card"><div class="card-icon"><i class="fa-solid fa-magnifying-glass-chart"></i></div><h3>SEO</h3><p>Make sure your new site can actually be found in search.</p></a>
        <a href="services.html#performance-optimization" class="card"><div class="card-icon"><i class="fa-solid fa-gauge-high"></i></div><h3>Performance Optimization</h3><p>Tune Core Web Vitals for a faster, smoother experience.</p></a>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>Let's scope your website development project</h2>
        <p>Share a few details and we'll come back with a realistic timeline and starting quote.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="service-detail.html",
    active="services",
    title="Custom Website Development Company | DeepAbi Services",
    description="Custom website development, business website development, and web application development from DeepAbi — overview, benefits, process, and FAQs for a fast, scalable, SEO-ready build.",
    extra_keywords="hire website developers, custom web app developers, professional website company",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/service-detail.css">',
    schema=SCHEMA,
)
