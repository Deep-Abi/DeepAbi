# -*- coding: utf-8 -*-
"""
Build script for the DeepAbi static site.
Assembles each HTML page from a shared <head> SEO block, navbar, mobile menu,
floating contact launcher, and footer, plus page-specific body content and
page-specific CSS/JS includes. Run once during development; output is plain
static HTML with no runtime dependency on this script.
"""
import os as _os

ROOT = _os.path.dirname(_os.path.abspath(__file__))  # deepabi-site/ (parent of scripts/)
ROOT = _os.path.dirname(ROOT) if _os.path.basename(ROOT) == "scripts" else ROOT
SITE_URL = "https://www.deepabi.com"

# ---------------- Brand copy ----------------
MISSION = "Driving Economic Empowerment for People"
MISSION_DETAIL = "We build technology that creates real economic opportunity for the businesses and people behind it."
ABOUT_MISSION_PARAGRAPH = "DeepAbi is committed to driving economic empowerment by helping businesses, entrepreneurs and organizations establish a strong digital presence through modern, scalable and innovative technology solutions. Every website, application and digital experience we build is designed to create opportunities, improve accessibility and contribute to sustainable business growth."
VISION_HEADLINE = "Ambition Beyond Imagination"
VISION_BODY = "We envision DeepAbi becoming a globally trusted technology company delivering innovative digital experiences that transform businesses and empower communities worldwide."
VISION_DETAIL = "Becoming a globally trusted technology company delivering experiences that transform businesses worldwide."
ABOUT_VISION_PARAGRAPH = "DeepAbi envisions becoming a globally respected technology company that continuously pushes the boundaries of innovation, engineering excellence and digital transformation. Our ambition extends beyond conventional solutions, striving to create technologies that inspire growth, empower businesses and shape the future of digital experiences."
TAGLINE_PRIMARY = "Driving Economic Empowerment Through Technology"
TAGLINE_SECONDARY = "Ambition Beyond Imagination"
TAGLINE_THIRD = "Engineering Digital Excellence"

# ---------------- Contact ----------------
EMAIL = "deepabi.tech@gmail.com"
PHONE_1_DISPLAY = "+91 8946097125"
PHONE_1_TEL = "+918946097125"
PHONE_2_DISPLAY = "+91 8925279380"
PHONE_2_TEL = "+918925279380"
WHATSAPP_URL = f"https://wa.me/{PHONE_1_TEL.replace('+','')}"

# ---------------- SEO keyword pool (used sparingly, naturally, across pages) ----------------
SEO_KEYWORDS = (
    "website development, website design, corporate website, business website, "
    "website maintenance, website support, SEO, technical SEO, responsive website, "
    "landing page, professional website, website agency, website company, "
    "web development, business growth, modern website, portfolio website, "
    "custom website, digital solutions, technology company, "
    "custom website development, business website development, corporate website design, "
    "performance optimization, small business website, enterprise website, "
    "web application development, e-commerce website, website redesign, DeepAbi"
)

LOGO_SVG = '''<svg class="logo-mark" viewBox="0 0 40 40" fill="none" role="img" aria-label="DeepAbi logo">
  <circle cx="10" cy="10" r="4" fill="#00D9C8"/><circle cx="30" cy="10" r="4" fill="#8B5CF6"/>
  <circle cx="10" cy="30" r="4" fill="#8B5CF6"/><circle cx="30" cy="30" r="4" fill="#10B981"/>
  <circle cx="20" cy="20" r="5" fill="#081F4D"/>
  <line x1="10" y1="10" x2="20" y2="20" stroke="#00D9C8" stroke-width="2" opacity="0.65"/>
  <line x1="30" y1="10" x2="20" y2="20" stroke="#8B5CF6" stroke-width="2" opacity="0.65"/>
  <line x1="10" y1="30" x2="20" y2="20" stroke="#8B5CF6" stroke-width="2" opacity="0.65"/>
  <line x1="30" y1="30" x2="20" y2="20" stroke="#10B981" stroke-width="2" opacity="0.65"/>
</svg>'''

NAV_ITEMS = [
    ("home", "index.html", "Home"),
    ("services", "services.html", "Services"),
    ("projects", "projects.html", "Projects"),
    ("technologies", "technologies.html", "Technologies"),
    ("about", "about.html", "About"),
    ("contact", "contact.html", "Contact"),
]


def head(title, description, canonical_path, og_image="assets/images/backgrounds/og-social-banner.jpg",
         extra_css="", schema="", extra_keywords=""):
    canonical = f"{SITE_URL}/{canonical_path}" if canonical_path else SITE_URL
    keywords = SEO_KEYWORDS + (f", {extra_keywords}" if extra_keywords else "")
    return f'''<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="keywords" content="{keywords}" />
<meta name="author" content="DeepAbi" />
<link rel="canonical" href="{canonical}" />
<meta name="robots" content="index, follow" />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{SITE_URL}/{og_image}" />
<meta property="og:site_name" content="DeepAbi" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{SITE_URL}/{og_image}" />

<!-- Favicons -->
<link rel="icon" type="image/x-icon" href="assets/images/logos/favicon.ico" />
<link rel="icon" type="image/png" sizes="32x32" href="assets/images/logos/favicon-32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="assets/images/logos/favicon-16.png" />
<link rel="apple-touch-icon" sizes="180x180" href="assets/images/logos/favicon-180.png" />
<link rel="manifest" href="site.webmanifest" />
<meta name="theme-color" content="#081F4D" />

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
      integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA=="
      crossorigin="anonymous" referrerpolicy="no-referrer" />

<!-- Styles -->
<link rel="stylesheet" href="css/common.css">
{extra_css}
{schema}'''


def navbar(active):
    main_links = []
    for key, href, label in NAV_ITEMS:
        if key == active:
            main_links.append(f'      <a href="{href}" class="active" aria-current="page">{label}</a>')
        else:
            main_links.append(f'      <a href="{href}">{label}</a>')
    main_links_html = "\n".join(main_links)

    mobile_links = "\n".join(
        f'    <a href="{href}">{label}</a>' for key, href, label in NAV_ITEMS
    )

    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header id="navbar">
  <div class="navbar-topbar">
    <div class="container topbar-inner">
      <div class="topbar-contact">
        <a href="tel:{PHONE_1_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {PHONE_1_DISPLAY}</a>
        <a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
        <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i> {EMAIL}</a>
      </div>
      <div class="topbar-tagline">{TAGLINE_THIRD}</div>
    </div>
  </div>
  <div class="container nav-inner">
    <a href="index.html" class="logo">
      {LOGO_SVG}
      DeepAbi
    </a>
    <nav class="nav-links" aria-label="Primary">
{main_links_html}
    </nav>
    <div class="nav-right">
      <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><i class="fa-solid fa-bars" aria-hidden="true"></i></button>
    </div>
  </div>
</header>

<div id="mobile-menu">
  <div class="mobile-menu-head">
    <a href="index.html" class="logo">DeepAbi</a>
    <button class="menu-toggle" id="menuClose" aria-label="Close menu"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
  </div>
  <nav aria-label="Mobile">
{mobile_links}
  </nav>
  <div class="mobile-contact">
    <a href="tel:{PHONE_1_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {PHONE_1_DISPLAY}</a>
    <a href="tel:{PHONE_2_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i> {PHONE_2_DISPLAY}</a>
    <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i> {EMAIL}</a>
  </div>
</div>'''


def contact_fab():
    return f'''<div class="contact-fab" id="contactFab">
  <div class="fab-menu" id="fabMenu" role="menu" aria-hidden="true">
    <a role="menuitem" class="fab-item" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" aria-label="Chat with DeepAbi on WhatsApp">
      <span class="fab-icon fab-whatsapp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></span><span class="fab-label">WhatsApp</span>
    </a>
    <a role="menuitem" class="fab-item" href="tel:{PHONE_1_TEL}" aria-label="Call DeepAbi at {PHONE_1_DISPLAY}">
      <span class="fab-icon fab-call"><i class="fa-solid fa-phone" aria-hidden="true"></i></span><span class="fab-label">Call Us</span>
    </a>
    <a role="menuitem" class="fab-item" href="mailto:{EMAIL}" aria-label="Email DeepAbi">
      <span class="fab-icon fab-email"><i class="fa-solid fa-envelope" aria-hidden="true"></i></span><span class="fab-label">Email</span>
    </a>
  </div>
  <button class="fab-main" id="fabToggle" aria-expanded="false" aria-controls="fabMenu" aria-label="Open contact options">
    <i class="fa-solid fa-comment-dots" id="fabIconOpen" aria-hidden="true"></i>
    <i class="fa-solid fa-xmark" id="fabIconClose" aria-hidden="true"></i>
  </button>
</div>'''


def footer():
    return f'''<footer>
  <div class="footer-mission">
    <div class="container">
      <span class="footer-mission-label">Our Mission</span>
      <p>&ldquo;{MISSION}&rdquo;</p>
    </div>
  </div>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <svg width="30" height="30" viewBox="0 0 40 40" fill="none" aria-hidden="true">
            <circle cx="10" cy="10" r="4" fill="#00D9C8"/><circle cx="30" cy="10" r="4" fill="#8B5CF6"/>
            <circle cx="10" cy="30" r="4" fill="#8B5CF6"/><circle cx="30" cy="30" r="4" fill="#10B981"/>
            <circle cx="20" cy="20" r="5" fill="#FFFFFF"/>
          </svg>
          DeepAbi
        </div>
        <p>{TAGLINE_PRIMARY}. Websites, software, and long-term technology partnerships for ambitious businesses.</p>
        <div class="footer-social">
          <a href="#" aria-label="DeepAbi on GitHub"><i class="fa-brands fa-github" aria-hidden="true"></i></a>
          <a href="#" aria-label="DeepAbi on LinkedIn"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a>
          <a href="#" aria-label="DeepAbi on Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
          <a href="#" aria-label="DeepAbi on X"><i class="fa-brands fa-x-twitter" aria-hidden="true"></i></a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <ul>
          <li><a href="index.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Home</a></li>
          <li><a href="about.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> About</a></li>
          <li><a href="projects.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Projects</a></li>
          <li><a href="technologies.html"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Technologies</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="services.html#website-development"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Website Development</a></li>
          <li><a href="services.html#website-maintenance"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Website Maintenance</a></li>
          <li><a href="services.html#seo"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> SEO Services</a></li>
          <li><a href="services.html#performance-optimization"><i class="fa-solid fa-chevron-right" aria-hidden="true"></i> Performance Optimization</a></li>
        </ul>
      </div>
      <div class="footer-col footer-col-contact">
        <h5>Contact</h5>
        <ul>
          <li><a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope" aria-hidden="true"></i><span><em>Email</em>{EMAIL}</span></a></li>
          <li><a href="tel:{PHONE_1_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i><span><em>Phone</em>{PHONE_1_DISPLAY}</span></a></li>
          <li><a href="tel:{PHONE_2_TEL}"><i class="fa-solid fa-phone" aria-hidden="true"></i><span><em>Phone</em>{PHONE_2_DISPLAY}</span></a></li>
          <li><a href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i><span><em>WhatsApp</em>Chat with us</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year"></span> DeepAbi Technologies. All rights reserved.</span>
      <span class="legal"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></span>
    </div>
  </div>
</footer>

<div class="toast" id="toast"><i class="fa-solid fa-circle-check" aria-hidden="true"></i><span id="toastMsg">Message sent successfully!</span></div>'''


def picture(name, alt, w, h, folder, css_class="", loading="lazy", eager=False):
    """Build a <picture> element with automatic format detection and a strict
    priority order: AVIF > WebP > PNG > JPG/JPEG. Only <source> tags for
    formats that actually exist on disk for this image are emitted, so an
    image that only ships as AVIF+JPG (no WebP/PNG) still produces valid,
    minimal markup. `folder` is the page-scoped asset directory, e.g.
    "assets/images/home". Explicit width/height prevents layout shift;
    `eager=True` marks the hero-priority image (eager load + fetchpriority high),
    everything else lazy-loads with async decoding."""
    loading_attr = "eager" if eager else loading
    fetchpriority = ' fetchpriority="high"' if eager else ''
    cls = f' class="{css_class}"' if css_class else ''

    FORMAT_PRIORITY = [
        ("avif", "image/avif"),
        ("webp", "image/webp"),
        ("png", "image/png"),
    ]
    found = {}
    for ext, _ in FORMAT_PRIORITY:
        path = _os.path.join(ROOT, folder, ext, f"{name}.{ext}")
        if _os.path.exists(path):
            found[ext] = True
    # fallback <img> src: prefer jpg, then jpeg, then png, then whatever's found
    img_src = None
    for ext in ("jpg", "jpeg"):
        path = _os.path.join(ROOT, folder, ext, f"{name}.{ext}")
        if _os.path.exists(path):
            img_src = f"{folder}/{ext}/{name}.{ext}"
            break
    if img_src is None and "png" in found:
        img_src = f"{folder}/png/{name}.png"
    if img_src is None:
        # last resort: use the highest-priority format found as the <img> src too
        for ext, _ in FORMAT_PRIORITY:
            if ext in found:
                img_src = f"{folder}/{ext}/{name}.{ext}"
                break
    if img_src is None:
        raise FileNotFoundError(f"No image file found for '{name}' in '{folder}' (checked avif/webp/png/jpg/jpeg)")

    sources = "\n        ".join(
        f'<source srcset="{folder}/{ext}/{name}.{ext}" type="{mime}">'
        for ext, mime in FORMAT_PRIORITY if ext in found
    )

    return f'''<picture{cls}>
        {sources}
        <img src="{img_src}" alt="{alt}" width="{w}" height="{h}" loading="{loading_attr}"{fetchpriority} decoding="async">
      </picture>'''


def art_directed_picture(breakpoints, alt, w, h, folder, css_class="", eager=False):
    """Build a <picture> element that swaps to a DIFFERENT image per
    breakpoint (art direction), not just a different format of the same
    image. `breakpoints` is an ordered list of (media_query_or_None, name)
    tuples, most-specific first, ending with (None, default_name) for the
    default/desktop case. Each name still gets the full AVIF > WebP > PNG
    format-priority treatment, auto-detected from disk. Desktop images are
    NEVER downscaled for smaller screens — each breakpoint loads its own
    dedicated source image."""
    FORMAT_PRIORITY = [
        ("avif", "image/avif"),
        ("webp", "image/webp"),
        ("png", "image/png"),
    ]
    loading_attr = "eager" if eager else "lazy"
    fetchpriority = ' fetchpriority="high"' if eager else ''
    cls = f' class="{css_class}"' if css_class else ''

    def found_formats(name):
        found = {}
        for ext, _ in FORMAT_PRIORITY:
            if _os.path.exists(_os.path.join(ROOT, folder, ext, f"{name}.{ext}")):
                found[ext] = True
        return found

    sources = []
    default_name = breakpoints[-1][1]
    for media, name in breakpoints:
        found = found_formats(name)
        media_attr = f' media="{media}"' if media else ''
        for ext, mime in FORMAT_PRIORITY:
            if ext in found:
                sources.append(f'<source{media_attr} srcset="{folder}/{ext}/{name}.{ext}" type="{mime}">')

    img_src = None
    for ext in ("jpg", "jpeg"):
        path = _os.path.join(ROOT, folder, ext, f"{default_name}.{ext}")
        if _os.path.exists(path):
            img_src = f"{folder}/{ext}/{default_name}.{ext}"
            break
    if img_src is None:
        img_src = f"{folder}/png/{default_name}.png"

    sources_html = "\n        ".join(sources)
    return f'''<picture{cls}>
        {sources_html}
        <img src="{img_src}" alt="{alt}" width="{w}" height="{h}" loading="{loading_attr}"{fetchpriority} decoding="async">
      </picture>'''


def page(filename, active, title, description, body, canonical_path=None,
         extra_css="", extra_js="", og_image="assets/images/backgrounds/og-social-banner.jpg",
         schema="", body_class="", extra_keywords=""):
    canonical_path = canonical_path if canonical_path is not None else filename
    body_attr = f' class="{body_class}"' if body_class else ''
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{head(title, description, canonical_path, og_image, extra_css, schema, extra_keywords)}
</head>
<body{body_attr}>

{navbar(active)}

<main id="main">
{body}
</main>

{footer()}

{contact_fab()}

<script src="js/common.js"></script>
{extra_js}
</body>
</html>
'''
    with open(_os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {filename} ({len(html)} bytes)")
