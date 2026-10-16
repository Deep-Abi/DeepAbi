import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import (page, SERVICE_REGISTRY, WEBSITE_ONLY_MODE,
                        EMAIL, EMAIL_SECONDARY, PHONE_1_DISPLAY, PHONE_1_TEL,
                        PHONE_2_DISPLAY, PHONE_2_TEL, WHATSAPP_URL)

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.deepabi.com/"},
    {"@type": "ListItem", "position": 2, "name": "Contact", "item": "https://www.deepabi.com/contact.html"}
  ]
}
</script>'''

# The selector offers only what is publicly on sale. The full set of
# service labels stays in SERVICE_REGISTRY (scripts/build_site.py) and the
# website breakdown stays in WEBSITE_ENQUIRY_OPTIONS below, so restoring a
# service restores its option automatically.
WEBSITE_ENQUIRY_OPTIONS = [
    "Website Development",
    "Landing Page",
    "Corporate / Business Website",
    "Portfolio Website",
    "Website Maintenance",
    "Website SEO",
    "Website Performance Optimization",
    "Other Website Enquiry",
]

if WEBSITE_ONLY_MODE:
    _options = WEBSITE_ENQUIRY_OPTIONS
else:
    _options = [s["contact"] for s in SERVICE_REGISTRY if s["public"]] + ["Other / Not Sure"]

service_options = "\n".join(
    ['                <option value="" disabled selected>Select a service</option>'] +
    ['                <option>%s</option>' % o for o in _options])

body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Contact</span>
      <h1>Let's Build Your Digital Future</h1>
      <p>Tell us about your project and we'll get back to you within one business day.</p>
    </div>
  </div>

  <div class="section" style="padding-bottom:0;">
    <div class="container contact-grid">
      <div data-reveal>
        <form id="contactForm" novalidate>
          <div class="form-row">
            <div class="form-field">
              <label for="cf-name">Name</label>
              <input type="text" id="cf-name" name="name" placeholder="Your full name" required autocomplete="name">
            </div>
            <div class="form-field">
              <label for="cf-email">Email</label>
              <input type="email" id="cf-email" name="email" placeholder="you@company.com" required autocomplete="email">
            </div>
          </div>
          <div class="form-row">
            <div class="form-field">
              <label for="cf-phone">Phone</label>
              <input type="tel" id="cf-phone" name="phone" placeholder="+1 (555) 000-0000" autocomplete="tel">
            </div>
            <div class="form-field">
              <label for="cf-service">Service Required</label>
              <select id="cf-service" name="service" required>
{service_options}
              </select>
            </div>
          </div>
          <div class="form-field">
            <label for="cf-message">Message</label>
            <textarea id="cf-message" name="message" rows="5" placeholder="Tell us a bit about your project..." required></textarea>
          </div>
          <button type="submit" class="btn btn-accent" style="width:100%;">Compose Enquiry Email <i class="fa-solid fa-paper-plane" aria-hidden="true"></i></button>
          <p class="form-note">This opens your own email app with the details filled in, addressed to <a href="mailto:{EMAIL}">{EMAIL}</a> &mdash; nothing is sent until you send it. Prefer to skip the form? Email, call or WhatsApp us directly using the details alongside.</p>
          <p class="form-note">We use what you send only to answer your enquiry, and we don't share your details with third parties.</p>
        </form>
      </div>

      <div data-reveal>
        <div class="contact-info-card">
          <div class="contact-info-row">
            <div class="ic"><i class="fa-solid fa-location-dot" aria-hidden="true"></i></div>
            <div><h2 class="contact-info-title">Office</h2><p>Mogappair, Chennai - 37,<br>Tamil Nadu, India</p></div>
          </div>
          <div class="contact-info-row">
            <div class="ic"><i class="fa-solid fa-envelope" aria-hidden="true"></i></div>
            <div><h2 class="contact-info-title">Email</h2><a href="mailto:{EMAIL}">{EMAIL}</a><br><span class="contact-email-role">Technical</span> <a href="mailto:{EMAIL_SECONDARY}">{EMAIL_SECONDARY}</a></div>
          </div>
          <div class="contact-info-row">
            <div class="ic"><i class="fa-solid fa-phone" aria-hidden="true"></i></div>
            <div><h2 class="contact-info-title">Phone</h2><a href="tel:{PHONE_1_TEL}">{PHONE_1_DISPLAY}</a><br><a href="tel:{PHONE_2_TEL}">{PHONE_2_DISPLAY}</a></div>
          </div>
          <div class="contact-info-row">
            <div class="ic"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></div>
            <div><h2 class="contact-info-title">WhatsApp</h2><a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">Chat with us</a></div>
          </div>
          <div class="contact-info-row">
            <div class="ic"><i class="fa-solid fa-clock" aria-hidden="true"></i></div>
            <div><h2 class="contact-info-title">Response Time</h2><p>Within 1 business day</p></div>
          </div>
          <div class="contact-info-row">
            <div class="ic"><i class="fa-solid fa-headset" aria-hidden="true"></i></div>
            <div><h2 class="contact-info-title">Free Consultation</h2><p>30-minute scoping call, no obligation</p></div>
          </div>
          <div class="contact-info-row">
            <div class="ic"><i class="fa-solid fa-share-nodes" aria-hidden="true"></i></div>
            <div>
              <h2 class="contact-info-title">Follow Us</h2>
              <div class="footer-social" style="margin-top:10px;">
                <a href="https://www.instagram.com/deepabi_innovations/" target="_blank" rel="noopener noreferrer" aria-label="DeepAbi Innovations on Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
                <a href="https://www.facebook.com/profile.php?id=61593491164948" target="_blank" rel="noopener noreferrer" aria-label="DeepAbi Innovations on Facebook"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ FULL-WIDTH MAP ============ -->
  <div class="section">
    <div class="container">
      <div class="map-section" data-reveal>
        <div class="map-embed">
          <iframe
            src="https://www.google.com/maps?q=Mogappair,+Chennai,+Tamil+Nadu,+India&output=embed"
            title="DeepAbi location on Google Maps — Mogappair, Chennai, Tamil Nadu"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
  </div>
'''

page(
    filename="contact.html",
    active="contact",
    title="Contact DeepAbi Innovations | Software Development Chennai",
    description="Talk to DeepAbi Innovations about your software project. Based in Mogappair, Chennai — call, WhatsApp or email for a free 30-minute consultation.",
    body=body,
    extra_css='<link rel="stylesheet" href="css/pages/contact.css">',
    extra_js='<script src="js/pages/contact.js"></script>',
    schema=SCHEMA,
)
