import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture, WEBSITE_ONLY_MODE, MISSION, VISION_HEADLINE, TAGLINE_THIRD, ABOUT_MISSION_PARAGRAPH, ABOUT_VISION_PARAGRAPH

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

# Who we are stays the same; what we say we currently build follows the
# service registry. The journey timeline below is deliberately untouched -
# it describes direction, not an offer, and is marked "Next"/"Future Vision".
if WEBSITE_ONLY_MODE:
    studio_intro = ("DeepAbi is a digital product and engineering studio. We build websites for "
                    "businesses that need a technology partner they can actually reach "
                    "&mdash; not a ticketing queue.")
else:
    studio_intro = ("DeepAbi is a digital product and engineering studio. We build websites, "
                    "software, and AI-powered solutions for businesses that need a technology "
                    "partner they can actually reach \u2014 not a ticketing queue.")

# The "Who We Are" illustration is temporarily hidden.
#
# The artwork itself has statistics rendered into the image - "50+ Experts",
# "100+ Projects Delivered", "30+ Happy Clients", "5+ Years of Excellence" -
# none of which has been verified. Because they are pixels rather than text, no
# content audit catches them, so the image is withheld until it can be replaced
# with artwork that makes no unverified claim.
#
# Nothing is destroyed: the asset stays on disk at assets/images/about/<fmt>/
# team-collaboration.<fmt>, and its full picture() configuration - name, alt
# text, dimensions, folder - is preserved below. Set the flag to True to bring
# it back exactly as it was. No replacement artwork has been generated and no
# substitute numbers have been invented.
# ---------------------------------------------------------------------------
# Unconfirmed claims, held back until the facts are confirmed.
#
# Each original line is preserved verbatim below so it can be restored by
# flipping one flag - nothing has to be rewritten from memory. None of the
# replacements invent anything: they restate wording already approved elsewhere
# on the site, or simply drop the unconfirmed clause.

# "small and senior" describes staffing that has not been confirmed. Held back
# in both places it appeared.
SHOW_TEAM_COMPOSITION_CLAIM = False
TEAM_CLAIM_PARAGRAPH = ('        <p>We keep our team small and senior on purpose. Every project is led by '
                        'people who write the code and make the design decisions, which means fewer '
                        'handoffs, faster iteration, and a lot less lost in translation.</p>')
PARTNER_LEDE_WITH_CLAIM = ("We keep teams small and senior, communicate directly, and stay invested "
                           "in your project long after launch.")
# Same sentence with the staffing clause removed. What remains is exactly what
# the three cards underneath it already say.
PARTNER_LEDE_NEUTRAL = ("We communicate directly and stay invested in your project long after launch.")

team_claim_paragraph = TEAM_CLAIM_PARAGRAPH if SHOW_TEAM_COMPOSITION_CLAIM else ""
partner_lede = PARTNER_LEDE_WITH_CLAIM if SHOW_TEAM_COMPOSITION_CLAIM else PARTNER_LEDE_NEUTRAL

# The Current Stage entry claimed delivery of web applications - not a public
# service while only Website Development is - and asserted an existing client
# base ("for early clients"), which has not been confirmed. The replacement
# names only the services this site actually offers, in the Services page's own
# approved wording, and makes no claim about clients.
SHOW_UNCONFIRMED_CURRENT_STAGE_CLAIM = False
CURRENT_STAGE_WITH_CLAIM = ("Building our foundation — delivering websites, web applications, "
                            "maintenance, and SEO for early clients with hands-on attention to "
                            "every project.")
CURRENT_STAGE_NEUTRAL = ("Building our foundation — focused on website development, with the "
                         "maintenance, SEO and performance work that keeps sites earning their "
                         "place after launch.")
current_stage_text = (CURRENT_STAGE_WITH_CLAIM if SHOW_UNCONFIRMED_CURRENT_STAGE_CLAIM
                      else CURRENT_STAGE_NEUTRAL)

SHOW_WHO_WE_ARE_IMAGE = False

WHO_WE_ARE_IMAGE = picture(
    "team-collaboration",
    "Abstract illustration representing a collaborative technology team workspace",
    640, 434, "assets/images/about")

if SHOW_WHO_WE_ARE_IMAGE:
    who_we_are_visual = '      <div class="img-frame">\n        ' + WHO_WE_ARE_IMAGE + '\n      </div>\n'
    about_intro_class = "container about-intro"
else:
    # With the image column gone the section would be a single grid cell
    # spanning the full container, which makes the paragraphs too wide to read.
    # The modifier narrows and centres the remaining text column instead of
    # leaving an empty half.
    who_we_are_visual = ""
    about_intro_class = "container about-intro about-intro-text-only"

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">About DeepAbi</span>
      <h1>Who we are</h1>
      <p>A focused technology studio engineering digital excellence, with a long-term, partnership-driven mindset.</p>
      <p>Our <a class="inline-link" href="service-website-development.html">website development services</a> support businesses in Mogappair, Nolambur and Anna Nagar.</p>
    </div>
  </div>

  <div class="section">
    <div class="{about_intro_class}" data-reveal>
{who_we_are_visual}      <div>
        <span class="eyebrow">Who We Are</span>
        <h2 style="font-size:28px; margin-bottom:16px;">Engineers and designers, working as one team</h2>
        <p style="margin-bottom:14px;">{studio_intro}</p>
{team_claim_paragraph}
      </div>
    </div>
  </div>

  <div class="section section-alt">
    <div class="container" data-reveal>
      <div class="section-head center">
        <!-- <span class="eyebrow">What Drives Us</span> -->
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
        <!-- <span class="eyebrow">Core Values</span> -->
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
        <!-- <span class="eyebrow cyan">Our Process</span> -->
        <h2>How every DeepAbi project runs</h2>
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

  <!-- JOURNEY / TIMELINE -->
  <div class="section">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow">Our Journey</span> -->
        <h2>Where we are, and where we're headed</h2>
      </div>
      <div class="vtimeline" data-reveal>
        <div class="vtimeline-item">
          <div class="vtimeline-dot"></div>
          <span class="stage-pill now">Current Stage</span>
          <h3>Startup</h3>
          <p>{current_stage_text}</p>
        </div>
        <div class="vtimeline-item future">
          <div class="vtimeline-dot"></div>
          <span class="stage-pill next">Next</span>
          <h3>AI &amp; Automation</h3>
          <p>Expanding into AI-powered features and workflow automation built directly into client products.</p>
        </div>
        <div class="vtimeline-item future">
          <div class="vtimeline-dot"></div>
          <span class="stage-pill future">Future Vision</span>
          <h3>Enterprise Software</h3>
          <p>Growing into a full enterprise software partner, supporting larger, more complex digital transformation projects.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- WHY DEEPABI -->
  <div class="section section-alt">
    <div class="container">
      <div class="section-head center" data-reveal>
        <!-- <span class="eyebrow cyan">Why DeepAbi</span> -->
        <h2>A partner, not just a vendor</h2>
        <p style="margin:0 auto;">{partner_lede}</p>
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
        <!-- The "within one business day" commitment was removed from the Contact page
             in Phase 3 because the response time has not been confirmed. This copy of it
             was missed at the time; removed here for the same reason. Restore it only
             once the actual response time is agreed. -->
        <p>Tell us about your project and the support you need.</p>
        <a href="contact.html" class="btn btn-accent">Start Your Project <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

page(
    filename="about.html",
    active="about",
    title="About DeepAbi Innovations | Website Development Company in Chennai",
    description="The mission, vision and values behind DeepAbi Innovations — a website development company in Chennai building digital products that create real economic opportunity.",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/about.css">',
    schema=SCHEMA,
)
