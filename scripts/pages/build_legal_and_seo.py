import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, is_service_public, ROOT, SITE_URL, EMAIL, TAGLINE_SECONDARY

privacy_body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Legal</span>
      <h1>Privacy Policy</h1>
      <p>Last updated: January 2026</p>
    </div>
  </div>
  <div class="section">
    <div class="container legal-copy" data-reveal>
      <h2>Overview</h2>
      <p>This is placeholder legal content for demonstration purposes. Replace it with a privacy policy reviewed by qualified counsel before this site goes live for a real business.</p>
      <h2>Information We Collect</h2>
      <p>When you submit the contact form, we collect the name, email, phone number, service selection, and message you provide, solely to respond to your enquiry.</p>
      <h2>How We Use Information</h2>
      <p>We use the information you provide to respond to enquiries, scope potential projects, and, where you've agreed, follow up about DeepAbi services. We do not sell your data to third parties.</p>
      <h2>Cookies</h2>
      <p>This site does not currently set marketing or tracking cookies. If analytics are added in production, this section should be updated to disclose them.</p>
      <h2>Contact</h2>
      <p>Questions about this policy can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
'''

terms_body = f'''
  <div class="page-header">
    <div class="container">
      <span class="eyebrow cyan">Legal</span>
      <h1>Terms of Service</h1>
      <p>Last updated: January 2026</p>
    </div>
  </div>
  <div class="section">
    <div class="container legal-copy" data-reveal>
      <h2>Overview</h2>
      <p>This is placeholder legal content for demonstration purposes. Replace it with terms of service reviewed by qualified counsel before this site goes live for a real business.</p>
      <h2>Use of This Site</h2>
      <p>Content on this site is provided for general information about DeepAbi's services. Nothing on this site constitutes a binding quote or contract; project scope and pricing are confirmed in a signed agreement.</p>
      <h2>Intellectual Property</h2>
      <p>All illustrations, copy, and code on this site are the property of DeepAbi unless otherwise noted, and may not be reproduced without permission.</p>
      <h2>Limitation of Liability</h2>
      <p>DeepAbi is not liable for indirect or consequential damages arising from use of this website, to the fullest extent permitted by law.</p>
      <h2>Contact</h2>
      <p>Questions about these terms can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
'''

page(filename="privacy.html", active="", title="Privacy Policy | DeepAbi",
     description="DeepAbi's privacy policy covering what information is collected through this website and how it is used.",
     body=privacy_body, extra_css='<link rel="stylesheet" href="css/pages/legal.css">')

page(filename="terms.html", active="", title="Terms of Service | DeepAbi",
     description="DeepAbi's terms of service governing use of this website.",
     body=terms_body, extra_css='<link rel="stylesheet" href="css/pages/legal.css">')

# ---------------- robots.txt ----------------
robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(robots)

# ---------------- sitemap.xml ----------------
# Hidden services are left out of the sitemap while their registry flag is
# False; their pages stay on disk and keep working at their URLs.
pages = [
    ("", "1.0", "weekly"),
    ("services.html", "0.9", "monthly"),
    ("service-website-development.html", "0.9", "monthly"),
    ("service-web-applications.html", "0.8", "monthly"),
    ("service-mobile-applications.html", "0.8", "monthly"),
    ("service-desktop-applications.html", "0.8", "monthly"),
    ("service-custom-software.html", "0.8", "monthly"),
    ("service-saas-products.html", "0.8", "monthly"),
    ("service-ai-automation.html", "0.8", "monthly"),
    ("service-software-maintenance.html", "0.8", "monthly"),
    ("projects.html", "0.8", "weekly"),
    ("technologies.html", "0.6", "monthly"),
    ("about.html", "0.7", "monthly"),
    ("contact.html", "0.9", "monthly"),
    ("privacy.html", "0.2", "yearly"),
    ("terms.html", "0.2", "yearly"),
]

pages = [row for row in pages
         if not row[0].startswith("service-")
         or is_service_public(row[0][len("service-"):-len(".html")])]
urls = "\n".join(
    f'''  <url>
    <loc>{SITE_URL}/{p}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{pr}</priority>
  </url>''' for p, pr, freq in pages
)
sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write(sitemap)

# ---------------- site.webmanifest ----------------
manifest = {
    "name": "DeepAbi",
    "short_name": "DeepAbi",
    "description": f"{TAGLINE_SECONDARY}. Driving Economic Empowerment Through Technology.",
    "start_url": "/index.html",
    "display": "standalone",
    "background_color": "#FFFFFF",
    "theme_color": "#081F4D",
    "icons": [
        {"src": "assets/images/logos/favicon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "assets/images/logos/favicon-512.png", "sizes": "512x512", "type": "image/png"},
    ],
}
with open(os.path.join(ROOT, "site.webmanifest"), "w") as f:
    json.dump(manifest, f, indent=2)

print("wrote robots.txt, sitemap.xml, site.webmanifest, privacy.html, terms.html")
