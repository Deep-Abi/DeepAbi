"""The seven dedicated service pages (everything except Website Development,
which has its own builder because it carries migrated legacy content).

Shared shell, service-specific content
--------------------------------------
Every page uses the same components as service-website-development.html —
the gradient hero, `.service-block` alternating rows, a `.card` grid of
deliverables, `.process-track`, a `.card` grid of related services — so the
seven read as one family without being seven copies. What differs per page is
all of the substance: solution types, deliverables, process steps, related
services, CTA wording, SEO and imagery.

The three supporting sections are deliberately NOT parallel across services.
Each carries its own heading, its own lead sentence, and as many cards as that
service actually needs — `deliverables_cols` and `related_cols` switch a grid
between three and four columns, so a five- or six-card section is laid out
properly rather than padded to four. The Website Development page keeps its
own wording ("What you get with a DeepAbi build" and friends); nothing here
restates it with the service name swapped in.

Related-service cards say WHY the two connect, in one sentence, and are only
listed where that reason is real.

No eyebrow labels above the deliverables / process / related headings, per
the current content direction, and no FAQ sections.

TEMPORARY IMAGERY
-----------------
Every image below is an existing project asset re-used as a stand-in. The
mapping lives in the `hero_img` / `blocks` entries of each SERVICE dict —
replacing one later means changing that (name, folder) pair and its alt text,
nothing else. No new files were generated or downloaded.

Truthfulness
------------
Copy describes what can be built and the business need it serves. No
completed products, client names, results, certifications, team size or
experience are claimed anywhere.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_site import page, picture, SITE_URL, is_service_public

CSS = '<link rel="stylesheet" href="css/pages/services.css">'


# ---------------------------------------------------------------------------
# Shared building blocks
# ---------------------------------------------------------------------------
def breadcrumb(name):
    return f'''<nav class="wd-breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
          <a href="services.html">Services</a>
          <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
          <span aria-current="page">{name}</span>
        </nav>'''


def service_block(anchor, eyebrow, title, desc, items, image_name, image_alt, icon,
                  folder="assets/images/services", reverse=False):
    """Same component the Website Development page uses."""
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
          <a href="contact.html" class="service-learn-more">{'{cta}'} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>'''


def cards(items, cols=4):
    body = "\n".join(
        f'        <div class="card"><div class="card-icon"><i class="{icon}"></i></div><h3>{t}</h3><p>{d}</p></div>'
        for icon, t, d in items)
    return f'      <div class="grid-{cols}" data-reveal>\n{body}\n      </div>'


def related(items, cols=3):
    body = "\n".join(
        f'        <a href="{href}" class="card"><div class="card-icon"><i class="{icon}"></i></div><h3>{t}</h3><p>{d}</p></a>'
        for icon, t, d, href in items)
    return f'      <div class="grid-{cols}" data-reveal>\n{body}\n      </div>'


def head(h2, lead=None):
    """Centred section heading, with an optional single lead sentence.

    No eyebrow label: the headings on these pages say what the section is,
    so a category label above them would only repeat it.
    """
    p = f'\n        <p>{lead}</p>' if lead else ''
    return f'''      <div class="section-head center" data-reveal>
        <h2>{h2}</h2>{p}
      </div>'''


def process(steps):
    body = "\n".join(
        f'        <div class="process-step"><div class="process-dot"><i class="{icon}" aria-hidden="true"></i>'
        f'<span class="process-num">{i:02d}</span></div><h3>{t}</h3><p>{d}</p></div>'
        for i, (icon, t, d) in enumerate(steps, start=1))
    return f'      <div class="process-track" data-reveal>\n{body}\n      </div>'


def schema(name, desc, slug):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{name}",
  "name": "{name}",
  "description": "{desc}",
  "provider": {{"@type": "Organization", "name": "DeepAbi Innovations", "url": "{SITE_URL}"}},
  "areaServed": [
    {{"@type": "Place", "name": "Mogappair, Chennai"}},
    {{"@type": "Place", "name": "Ambattur, Chennai"}},
    {{"@type": "Place", "name": "Anna Nagar, Chennai"}},
    {{"@type": "City", "name": "Chennai"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE_URL}/"}},
    {{"@type": "ListItem", "position": 2, "name": "Services", "item": "{SITE_URL}/services.html"}},
    {{"@type": "ListItem", "position": 3, "name": "{name}", "item": "{SITE_URL}/service-{slug}.html"}}
  ]
}}
</script>'''


# ---------------------------------------------------------------------------
# Per-service content
# ---------------------------------------------------------------------------
SERVICES = [
{
 "slug": "web-applications",
 "name": "Web Applications",
 "plain": "Web Applications",
 "h1": "Web Applications That Run Your Daily Operations",
 "lede": "Software your team opens in a browser to do the work of the business — record, check, approve, report. Nothing to install, and it works from an office computer, a laptop at home or a phone on site.",
 "hero_img": ("web_application_development", "assets/images/projects",
              "Illustration of a browser-based business application dashboard"),
 "cta_primary": "Discuss Your Web Application",
 "intro_h2": "Not a website, and not a subscription product",
 "intro": [
   "An informational website tells people about your business. A web application lets them <em>do</em> something: place an order, raise a request, approve a leave form, check where a job has got to. The difference matters because it changes what has to be built — accounts, permissions, stored data, and rules about who may see and change what.",
   "It is also different from a SaaS product. A web application is built for one organisation and its way of working. A SaaS product serves many separate customers on one platform. If that is what you have in mind, the <a href=\"service-saas-products.html\">SaaS Products</a> page covers it.",
 ],
 "blocks": [
   ("dashboards-portals", "01 · See", "Dashboards and customer portals",
    "One screen that shows what is actually happening, and a logged-in area where your customers can check their own orders, requests or project status without phoning anyone.",
    ["Business dashboards and reporting", "Customer and client portals",
     "Role-based access and permissions", "Filtered views and data export",
     "Status tracking your clients can see", "Works on desktop, tablet and phone"],
    "enterprise_website_framework", "assets/images/projects",
    "Illustration of a reporting dashboard interface", "fa-solid fa-gauge", False),
   ("operations-systems", "02 · Run", "Internal operations and approvals",
    "The processes that currently live in spreadsheets, message threads and someone's memory, turned into a system where each step has an owner and a record.",
    ["Internal operations systems", "Approval and sign-off workflows",
     "Order and enquiry management", "Inventory and stock tracking",
     "Audit trail of who changed what", "Notifications when something needs attention"],
    "business_websites", "assets/images/services",
    "Illustration of an internal business operations screen", "fa-solid fa-diagram-project", True),
   ("integrations", "03 · Connect", "Booking, scheduling and integrations",
    "Applications rarely stand alone. Bookings need calendars, orders need accounting, and data already living in another tool should not be retyped by hand.",
    ["Booking and service management", "Scheduling and resource allocation",
     "Database design and migration", "API integration with existing tools",
     "Scheduled imports and exports", "Secure authentication"],
    "professional_services_site", "assets/images/projects",
    "Illustration of connected systems exchanging data", "fa-solid fa-plug", False),
 ],
 "deliverables_h2": "Bring your daily operations into one system",
 "deliverables_p": "The practical difference a web application makes to a working day.",
 "deliverables": [
   ("fa-solid fa-database", "One Record, Not Five Copies", "An order lives in one place. Sales, accounts and dispatch read the same record, so nobody reconciles a spreadsheet against an email thread."),
   ("fa-solid fa-user-shield", "People See What They Should", "A supervisor approves, a technician updates, a client sees only their own job. Permissions are set per role rather than trusted to convention."),
   ("fa-solid fa-gauge", "The Current Position, on Screen", "Open jobs, pending approvals, this week's numbers — the question &ldquo;where is that?&rdquo; gets answered by looking, not by asking."),
   ("fa-solid fa-arrows-turn-right", "Steps That Hand Themselves On", "When one stage finishes the next person is notified and the record moves. The workflow is in the system, not in somebody's memory."),
 ],
 "process_h2": "From business workflow to working application",
 "process_p": "We start from how the work happens now, not from a feature list.",
 "process": [
   ("fa-solid fa-sitemap", "Map", "The workflow today"),
   ("fa-solid fa-clipboard-list", "Define", "Roles &amp; records"),
   ("fa-solid fa-pen-ruler", "Interface", "Screens per role"),
   ("fa-solid fa-database", "Data Layer", "Database &amp; APIs"),
   ("fa-solid fa-code", "Build", "In usable stages"),
   ("fa-solid fa-vial", "Test", "Your real cases"),
   ("fa-solid fa-users", "Roll Out", "Migrate &amp; train"),
 ],
 "related_h2": "Connect your application to the wider business",
 "related_p": "An application is rarely the whole answer. These are the three that most often sit next to it.",
 "related": [
   ("fa-solid fa-code", "Custom Software", "When the requirement reaches past the browser \u2014 a desktop tool at a counter, or a scheduled job moving data overnight \u2014 it is scoped as one custom system rather than two disconnected builds.", "service-custom-software.html"),
   ("fa-solid fa-robot", "AI &amp; Automation", "Once the work is in one system, the repeated steps inside it become visible: routing an enquiry, chasing an approval, compiling the same weekly report.", "service-ai-automation.html"),
   ("fa-solid fa-screwdriver-wrench", "Software Maintenance", "A live application accumulates real use, new edge cases and dependency updates. Ongoing support keeps a small issue from becoming a rebuild.", "service-software-maintenance.html"),
 ],
 "cta_h2": "Tell us how the work happens today",
 "cta_p": "Describe the process you want to replace or improve. We will come back with a realistic scope and a sensible first phase.",
 "seo_title": "Web Application Development in Chennai | DeepAbi Innovations",
 "seo_desc": "Custom web application development in Chennai — dashboards, customer portals, booking, inventory and internal operations systems built around how your business works.",
 "keywords": "web application development Chennai, web app development company Chennai, custom web application Chennai, business dashboard development",
},
{
 "slug": "mobile-applications",
 "name": "Mobile Applications",
 "plain": "Mobile Applications",
 "h1": "Mobile Applications for Customers and Field Teams",
 "lede": "Apps that put a service in your customers' hands, or give staff working away from a desk the tools they need on the device already in their pocket.",
 "hero_img": ("mobile_portrait", "assets/images/projects",
              "Illustration of a business application running on a mobile phone"),
 "cta_primary": "Discuss Your Mobile App",
 "intro_h2": "When a mobile app is worth building",
 "intro": [
   "A mobile app earns its place when people use a service repeatedly, when they need it away from a desk, or when the phone itself makes the job easier — its camera, its location, its ability to notify someone. If none of those apply, a well-built responsive website often serves better and costs less to run.",
   "We will say which of those we think applies to your idea before any development starts.",
 ],
 "blocks": [
   ("customer-apps", "01 · Serve", "Customer-facing applications",
    "The app your customers download: browse what you offer, order or book, pay, and see what is happening with their request afterwards.",
    ["Ordering and booking apps", "Service and account apps",
     "Product and catalogue browsing", "Customer accounts and history",
     "Push notifications and reminders", "Payment gateway integration where required"],
    "deepabi-mobile", "assets/images/home",
    "Illustration of a customer-facing mobile app screen", "fa-solid fa-mobile-button", False),
   ("field-apps", "02 · Equip", "Field-service and staff applications",
    "For teams who work away from an office — job lists, updates, photos and sign-offs captured where the work actually happens rather than typed up afterwards.",
    ["Field-service and job apps", "Staff and employee tools",
     "Photo and form capture on site", "Location features where the task needs them",
     "Offline capture with later sync", "Role-based access for staff"],
    "tablet_portrait", "assets/images/projects",
    "Illustration of a staff application shown on a tablet", "fa-solid fa-list-check", True),
   ("platforms-backend", "03 · Build", "Android, iOS and the system behind them",
    "Which platforms you need, and the backend that keeps the app, your website and your internal systems telling the same story.",
    ["Android applications", "iOS applications",
     "Cross-platform applications", "Backend and API integration",
     "Shared accounts with your web systems", "Release and store submission support"],
    "web_application_development", "assets/images/projects",
    "Illustration of a mobile application connected to backend services", "fa-solid fa-server", False),
 ],
 "deliverables_h2": "Put your services in your customers' hands",
 "deliverables_p": "What people should actually be able to do once the app is on the phone.",
 "deliverables": [
   ("fa-solid fa-right-to-bracket", "Sign In Once, Stay Signed In", "One account across your app and your web system, so a customer's history, addresses and saved details are already there."),
   ("fa-solid fa-bell", "Notifications Worth Keeping On", "An order is out for delivery, a job is assigned, a booking is tomorrow. Tied to real events, so the app does not get muted."),
   ("fa-solid fa-camera", "The Phone's Own Abilities", "Camera for proof of delivery, location for the nearest branch, saved documents for offline reference \u2014 used where the task needs them, not for show."),
   ("fa-solid fa-signal", "Usable on a Weak Signal", "Where staff work in basements, warehouses or on the road, entries are captured on the device and synced when the connection returns."),
   ("fa-solid fa-list-check", "Tools for Staff, Not Just Customers", "The same app family can carry a private side for your team \u2014 today's jobs, status updates, sign-offs at the door."),
   ("fa-solid fa-mobile-screen-button", "Comfortable One-Handed", "Reachable controls and readable text on a small screen, checked on real handsets rather than a desktop preview."),
 ],
 "deliverables_cols": 3,
 "process_h2": "From app concept to device-ready release",
 "process_p": "The stages between an idea and something installable, including the parts the app stores require.",
 "process": [
   ("fa-solid fa-route", "Journeys", "What users do"),
   ("fa-solid fa-mobile-screen", "Platforms", "Android, iOS or both"),
   ("fa-solid fa-pen-ruler", "Design", "Screens &amp; navigation"),
   ("fa-solid fa-code", "Build", "App &amp; backend"),
   ("fa-solid fa-vials", "Device Test", "Real handsets &amp; OS versions"),
   ("fa-solid fa-store", "Release", "Store listing &amp; submission"),
   ("fa-solid fa-arrows-rotate", "Post-Release", "Fixes &amp; OS updates"),
 ],
 "related_h2": "Support your app beyond the screen",
 "related_p": "Most of a mobile product is not the app. These are the parts that sit behind it.",
 "related": [
   ("fa-solid fa-table-columns", "Web Applications", "The back office you use to run the app \u2014 view orders, assign jobs, update the catalogue, answer a customer. Usually built alongside the app, sharing one database.", "service-web-applications.html"),
   ("fa-solid fa-code", "Custom Software", "The backend that holds accounts, business rules and data. Where the same logic has to serve an app, a website and an internal system, it is designed once.", "service-custom-software.html"),
   ("fa-solid fa-screwdriver-wrench", "Software Maintenance", "Android and iOS release new versions every year and can drop older ones. An unmaintained app eventually stops being accepted by the stores.", "service-software-maintenance.html"),
 ],
 "cta_h2": "Tell us what the app needs to do",
 "cta_p": "Describe who would use it and what they would do with it. We will tell you honestly whether an app is the right answer.",
 "seo_title": "Mobile App Development in Chennai | DeepAbi Innovations",
 "seo_desc": "Mobile app development in Chennai — Android, iOS and cross-platform apps for customer ordering, bookings, field service and staff workflows, with backend integration.",
 "keywords": "mobile app development Chennai, mobile application development company Chennai, Android app development Chennai, iOS app development Chennai",
},
{
 "slug": "desktop-applications",
 "name": "Desktop Applications",
 "plain": "Desktop Applications",
 "h1": "Desktop Software Built for the Work in Front of You",
 "lede": "Applications installed on the computers your team already uses — for billing at a counter, processing files in bulk, or any job that has to keep working when the internet does not.",
 "hero_img": ("desktop", "assets/images/projects",
              "Illustration of business software running on a desktop computer"),
 "cta_primary": "Discuss Your Desktop Tool",
 "intro_h2": "Why a desktop application, and not a website",
 "intro": [
   "Three reasons usually decide it. The work needs local files — reading a folder of documents, writing to a specific drive. It needs hardware — a receipt printer, a scanner, a card reader. Or it simply has to keep running when the connection drops, at a counter or on a shop floor.",
   "Where none of those apply, a browser-based system is usually the better long-term choice, and we will say so.",
 ],
 "blocks": [
   ("business-tools", "01 · Operate", "Business and administration tools",
    "The daily operational software a business runs on — entering, checking and printing, fast, with a keyboard, by someone who does it a hundred times a day.",
    ["Windows business applications", "Billing and counter software",
     "Inventory and stock tools", "Internal administration tools",
     "Keyboard-first, high-speed entry", "Local printing and receipts"],
    "deepabi-desktop", "assets/images/home",
    "Illustration of a Windows business application interface", "fa-solid fa-window-restore", False),
   ("data-tools", "02 · Process", "Data, file and reporting utilities",
    "The repetitive computer work nobody enjoys: renaming, converting, merging, extracting, checking and compiling the same report every week.",
    ["Data-processing utilities", "File and document workflows",
     "Bulk conversion and extraction", "Scheduled and on-demand reports",
     "Validation before data is saved", "Import and export with existing spreadsheets"],
    "performance_optimization", "assets/images/services",
    "Illustration of a data processing and reporting utility", "fa-solid fa-file-arrow-down", True),
   ("offline-integration", "03 · Connect", "Offline, hybrid and integrated setups",
    "Software that works on its own machine but does not stay on an island — syncing when a connection is available, or talking to equipment and systems you already own.",
    ["Offline and hybrid applications", "Sync when a connection returns",
     "Integration with existing systems", "Device and peripheral integration where technically appropriate",
     "Multi-machine shared data", "Installer and update support"],
    "technology-stack-network", "assets/images/technology",
    "Illustration of desktop software integrating with other systems", "fa-solid fa-network-wired", False),
 ],
 "deliverables_h2": "Tools built for the work on your desktop",
 "deliverables_p": "What a desktop application can do that a browser tab cannot.",
 "deliverables": [
   ("fa-solid fa-folder-open", "Works Directly With Your Files", "Reads a folder, writes to a drive, produces the output beside the source \u2014 no uploading and downloading to get a job done."),
   ("fa-solid fa-keyboard", "Built for Repetition", "Keyboard shortcuts, tab order and defaults arranged around the few actions someone performs a hundred times a day."),
   ("fa-solid fa-plug", "Talks to Attached Devices", "Receipt printers, barcode scanners, weighing scales, card readers \u2014 connected where the hardware supports it, confirmed before we commit to it."),
   ("fa-solid fa-wifi", "Keeps Going Without a Connection", "At a counter or on a shop floor, work continues through an outage and reconciles afterwards rather than stopping."),
 ],
 "process_h2": "Designed around your working environment",
 "process_p": "Which machines, which Windows versions, which hardware \u2014 settled before the build, because they shape it.",
 "process": [
   ("fa-solid fa-desktop", "Environment", "Machines, OS &amp; hardware"),
   ("fa-solid fa-sitemap", "Workflow", "The task, step by step"),
   ("fa-solid fa-pen-ruler", "Design", "Screens &amp; shortcuts"),
   ("fa-solid fa-code", "Build", "In usable stages"),
   ("fa-solid fa-box-open", "Install Test", "On your own machines"),
   ("fa-solid fa-graduation-cap", "Deploy", "Roll out &amp; train"),
   ("fa-solid fa-arrows-rotate", "Updates", "Ship fixes later"),
 ],
 "related_h2": "Link desktop work with your other systems",
 "related_p": "Installed software should not be an island. These are the usual ways it joins the rest of the business.",
 "related": [
   ("fa-solid fa-code", "Custom Software", "The integration work itself \u2014 pushing counter sales into accounts, pulling the price list down, keeping one machine's records in step with another's.", "service-custom-software.html"),
   ("fa-solid fa-table-columns", "Web Applications", "When head office needs to see what the desktop tools are recording, a browser system holds the shared data and the reporting the branches sync into.", "service-web-applications.html"),
   ("fa-solid fa-screwdriver-wrench", "Software Maintenance", "Windows updates, replaced hardware and new machines all reach installed software eventually. Upkeep covers the installer as well as the application.", "service-software-maintenance.html"),
 ],
 "cta_h2": "Tell us about the job it has to do",
 "cta_p": "Describe the task, the files or hardware involved, and who uses it. We will scope a tool that fits the way that work actually runs.",
 "seo_title": "Desktop Application Development in Chennai | DeepAbi Innovations",
 "seo_desc": "Desktop application development in Chennai — Windows business tools, billing and inventory software, data-processing utilities and offline-capable applications.",
 "keywords": "desktop application development Chennai, desktop software development Chennai, Windows application development Chennai, billing software development",
},
{
 "slug": "custom-software",
 "name": "Custom Software",
 "plain": "Custom Software",
 "h1": "Software Shaped Around How Your Business Works",
 "lede": "When no off-the-shelf product fits the way you actually operate, the software should be built around the process — not the process bent around the software.",
 "hero_img": ("mission", "assets/images/about",
              "Abstract illustration representing purpose-built business software"),
 "cta_primary": "Discuss Your Requirement",
 "intro_h2": "Custom describes the fit, not the platform",
 "intro": [
   "Web, mobile and desktop describe <em>how people reach</em> software. Custom describes <em>how closely it fits</em> your business. A custom solution can be any one of those, or several working together — a browser system for the office, a phone app for the field, and a scheduled job moving data between them.",
   "It is worth it when the gap is costing real time: the same information entered twice, a workaround everyone has learned to live with, a process that only one person fully understands. Where a standard product genuinely fits, we will tell you to buy it.",
 ],
 "blocks": [
   ("business-systems", "01 · Fit", "Systems built for one specific job",
    "Software dedicated to the work that makes your business different, rather than a general-purpose product configured until it nearly fits.",
    ["Tools for a specific job or workflow", "Tailored operational systems",
     "Industry-specific tools", "Custom approval and process management",
     "Rules that match how you really work", "Reporting on the numbers you actually track"],
    "team-collaboration", "assets/images/about",
    "Illustration representing a team working within a tailored business system", "fa-solid fa-gears", False),
   ("integration", "02 · Join", "Integration between existing systems",
    "Often the best custom software is small: the piece that makes two systems you already pay for finally talk to each other.",
    ["Integration between existing systems", "Automated data transfer",
     "One record instead of three copies", "Connecting accounts, stock and orders",
     "Scheduled synchronisation", "Clear handling when something fails"],
    "technology-stack-network", "assets/images/technology",
    "Illustration of separate business systems being connected", "fa-solid fa-plug-circle-bolt", True),
   ("modernisation", "03 · Extend", "Modernising software you already have",
    "Existing software that still does the job but is getting harder to run does not always need replacing — sometimes it needs extending, tidying or moving.",
    ["Modernisation of existing software", "Extending what already works",
     "Replacing fragile spreadsheet processes", "Migration to a maintainable codebase",
     "Documentation of how it works", "A phased path off legacy tools"],
    "enterprise_website_framework", "assets/images/projects",
    "Illustration representing modernisation of an existing system", "fa-solid fa-arrows-rotate", False),
 ],
 "deliverables_h2": "Software that fits the way your business works",
 "deliverables_p": "Built for one job in one business, rather than configured until it nearly fits.",
 "deliverables": [
   ("fa-solid fa-crosshairs", "One Job, Done Properly", "A tool for the thing your business actually does \u2014 how you quote, how you schedule, how you check \u2014 rather than a general product with three quarters of it switched off."),
   ("fa-solid fa-scale-balanced", "Your Rules, Encoded", "Pricing bands, approval limits, who may override what: the conditions your team currently applies from experience become rules the system applies consistently."),
   ("fa-solid fa-file-lines", "The Fields You Actually Track", "Records carry the information your work depends on, and reporting counts what you measure \u2014 not the nearest approximation a standard product allows."),
   ("fa-solid fa-arrows-up-down-left-right", "Changes When You Do", "A new branch, a new service line, a changed regulation. The structure is meant to absorb these rather than force a fresh procurement."),
 ],
 "process_h2": "Start with the problem. Build around the process.",
 "process_p": "No code until the problem is clear, and nothing built for a year before anyone can use it.",
 "process": [
   ("fa-solid fa-comments", "Discover", "Where time goes today"),
   ("fa-solid fa-clipboard-list", "Requirements", "Written &amp; agreed"),
   ("fa-solid fa-pen-ruler", "Prototype", "Clickable, before code"),
   ("fa-solid fa-layer-group", "Phase One", "Smallest useful build"),
   ("fa-solid fa-users", "Validate", "With the people who use it"),
   ("fa-solid fa-code", "Extend", "Later phases"),
   ("fa-solid fa-file-contract", "Hand Over", "Docs &amp; exportable data"),
 ],
 "related_h2": "Choose the right form for your solution",
 "related_p": "&ldquo;Custom&rdquo; describes the fit, not the platform. A single requirement often uses more than one of these.",
 "related": [
   ("fa-solid fa-table-columns", "Web Applications", "The usual choice: no installation, reachable from any office or home machine, and the easiest to update once it is live.", "service-web-applications.html"),
   ("fa-solid fa-mobile-screen", "Mobile Applications", "Added when part of the process happens away from a desk \u2014 a delivery confirmed, a reading taken, a customer served on site.", "service-mobile-applications.html"),
   ("fa-solid fa-desktop", "Desktop Applications", "Chosen when local files, attached hardware or working through an outage decide it, typically at a counter or on a floor.", "service-desktop-applications.html"),
   ("fa-solid fa-robot", "AI &amp; Automation", "Often the highest-value component rather than the whole system: the step in the middle that stops being done by hand.", "service-ai-automation.html"),
 ],
 "related_cols": 4,
 "cta_h2": "Describe the process you want to fix",
 "cta_p": "Tell us where the time goes today. We will map it with you and propose the smallest first phase that makes a real difference.",
 "seo_title": "Custom Software Development in Chennai | DeepAbi Innovations",
 "seo_desc": "Custom software development in Chennai — tailored business systems, workflow and approval tools, system integration and modernisation of existing software.",
 "keywords": "custom software development Chennai, custom software company Chennai, bespoke software development Chennai, business system integration Chennai",
},
{
 "slug": "saas-products",
 "name": "SaaS Products",
 "plain": "SaaS Products",
 "h1": "Building SaaS Products for Founders and Businesses",
 "lede": "Software delivered as an ongoing online product — customers sign up, get their own account and data, and pay for continued access. We build these for clients; the product is yours.",
 "hero_img": ("enterprise_website_framework", "assets/images/projects",
              "Abstract illustration representing a cloud software platform"),
 "cta_primary": "Discuss Your SaaS Idea",
 "intro_h2": "What makes something a SaaS product",
 "intro": [
   "<strong>SaaS</strong> means <strong>Software as a Service</strong>: customers use it online through an account instead of installing and running it themselves. The technical difference from a normal business application is who it serves. One company, or many separate ones — and if it is many, each customer's data must stay properly separated from the first line of code.",
   "To be clear about what this service is: DeepAbi builds SaaS products <em>for clients</em>. We are not selling access to established SaaS products of our own.",
 ],
 "blocks": [
   ("mvp", "01 · Start", "MVP and first product release",
    "A focused first version that does the core job well, so the idea can be put in front of real users before the full product is built out.",
    ["SaaS MVP development", "Core feature set defined with you",
     "A working product, not a prototype", "Built to be extended, not thrown away",
     "Early user feedback loop", "Clear scope for phase two"],
    "vision", "assets/images/about",
    "Abstract illustration representing an early-stage software product", "fa-solid fa-rocket", False),
   ("accounts-billing", "02 · Onboard", "Accounts, subscriptions and billing",
    "The parts every SaaS product needs before it can take a paying customer: signing up, choosing a plan, paying, and managing that afterwards.",
    ["User onboarding and sign-up", "Account and profile management",
     "Subscription plans and tiers", "Billing gateway integration",
     "Plan changes and cancellations", "Customer-facing account settings"],
    "corporate_websites", "assets/images/services",
    "Illustration of a subscription and account management screen", "fa-solid fa-id-card", True),
   ("workspaces-admin", "03 · Operate", "Workspaces, roles and administration",
    "Most SaaS products are used by teams, not individuals — and you need your own tools to run the product once customers are on it.",
    ["Organisation and workspace management", "Team members and invitations",
     "Roles, permissions and access control", "Separate data per customer",
     "Owner and admin back office", "Usage visibility for support"],
    "web_application_development", "assets/images/projects",
    "Illustration of a multi-tenant administration interface", "fa-solid fa-users-gear", False),
 ],
 "deliverables_h2": "Turn a product idea into an ongoing online service",
 "deliverables_p": "The machinery a product needs before it can take its first paying customer.",
 "deliverables": [
   ("fa-solid fa-door-open", "Sign-Up Without You in the Room", "A new customer creates an account, gets into the product and reaches something useful on their own. Onboarding is part of the product, not a support call."),
   ("fa-solid fa-building-user", "A Workspace Per Customer", "Each organisation gets its own space, its own members and its own data, kept separate by design rather than by a filter someone remembers to apply."),
   ("fa-solid fa-credit-card", "Plans, Payment and Changes", "Tiers, sign-up, upgrades, downgrades and cancellations \u2014 including what a customer keeps access to when a payment fails."),
   ("fa-solid fa-user-shield", "Roles Inside Each Account", "Owners, admins and ordinary members, so your customers can invite their own team without you administering it for them."),
   ("fa-solid fa-sliders", "A Back Office for You", "Your own view of accounts, plans and usage \u2014 so support can answer a question and you can see how the product is being used."),
 ],
 "deliverables_cols": 3,
 "process_h2": "Validate, launch and improve your product",
 "process_p": "A first version in front of real users early, then improved on what they actually do.",
 "process": [
   ("fa-solid fa-lightbulb", "Shape", "The core problem"),
   ("fa-solid fa-scissors", "MVP Scope", "What ships first"),
   ("fa-solid fa-pen-ruler", "Product Design", "Flows &amp; interface"),
   ("fa-solid fa-code", "Build", "First release"),
   ("fa-solid fa-vial", "Test", "Accounts, roles &amp; billing"),
   ("fa-solid fa-rocket", "Launch", "First real customers"),
   ("fa-solid fa-chart-line", "Improve", "Iterate on real use"),
 ],
 "related_h2": "Build the services around your SaaS product",
 "related_p": "A product is more than its web interface. These are the pieces founders usually need next.",
 "related": [
   ("fa-solid fa-mobile-screen", "Mobile Applications", "A companion app when customers need the product away from a desk \u2014 sharing the same accounts and data rather than running as a separate product.", "service-mobile-applications.html"),
   ("fa-solid fa-code", "Custom Software", "The integrations customers ask for during sales calls: importing their existing data, or connecting your product to the tools they already run.", "service-custom-software.html"),
   ("fa-solid fa-robot", "AI &amp; Automation", "Both inside the product as a feature, and behind it \u2014 onboarding sequences, usage alerts and the manual steps your own team repeats per customer.", "service-ai-automation.html"),
   ("fa-solid fa-screwdriver-wrench", "Software Maintenance", "A live product with paying customers cannot go unattended: uptime, security patching and fixes are continuous rather than occasional.", "service-software-maintenance.html"),
 ],
 "related_cols": 4,
 "cta_h2": "Tell us about the product you want to build",
 "cta_p": "Describe who would pay for it and what it does for them. We will help shape a first version worth putting in front of users.",
 "seo_title": "SaaS Product Development in Chennai | DeepAbi Innovations",
 "seo_desc": "SaaS product development in Chennai — MVPs, subscription and billing integration, workspaces, roles and admin tools, built for founders and businesses.",
 "keywords": "SaaS development Chennai, SaaS application development Chennai, SaaS MVP development, subscription software development Chennai",
},
{
 "slug": "ai-automation",
 "name": "AI &amp; Automation",
 "plain": "AI and Automation",
 "h1": "Automation and AI for the Work That Repeats",
 "lede": "Most businesses lose hours a week to work nobody chose to do — copying details between systems, compiling the same report, answering the same question. This is about removing those hours.",
 "hero_img": ("technology-stack-network", "assets/images/technology",
              "Illustration of connected systems representing automated workflows"),
 "cta_primary": "Plan Your Automation",
 "intro_h2": "Automation and AI do different jobs",
 "intro": [
   "If a task follows a predictable rule — when an enquiry arrives, create a record and notify the right person — conventional automation handles it, reliably and cheaply. No AI needed.",
   "AI earns its place with unstructured information: reading a document, sorting messy text, drafting a summary, answering from a body of material. It is very good at that and imperfect at all of it, which is why anything that commits your business to an action keeps a person in the loop. We will tell you which of the two your problem actually needs — often it is the simpler one.",
 ],
 "blocks": [
   ("workflow-automation", "01 · Remove", "Workflow and data automation",
    "The predictable, rule-based steps between your tools. These run the same way every time and need no AI at all.",
    ["Enquiry intake, classification and routing", "Repeated data entry between tools",
     "Synchronisation between systems", "Notifications, reminders and follow-ups",
     "Scheduled report preparation", "API integrations between platforms"],
    "seo", "assets/images/services",
    "Illustration of an automated workflow moving between systems", "fa-solid fa-arrows-turn-right", False),
   ("document-ai", "02 · Read", "Document and information processing",
    "Where the input is a document, an email or free text rather than a tidy form — extracting what matters and putting it somewhere useful.",
    ["Document information extraction", "Invoice, form and record processing",
     "Summarising long material", "Organising unstructured information",
     "Classification of incoming text", "Human review before anything is committed"],
    "mission", "assets/images/about",
    "Abstract illustration representing document and information processing", "fa-solid fa-file-lines", True),
   ("assistants", "03 · Assist", "AI assistants on your own information",
    "An assistant that answers from approved company material — your documentation, your policies, your product information — rather than from the open internet.",
    ["AI assistants on approved business information", "Internal knowledge search",
     "Support answer drafting for staff review", "AI features inside your own application",
     "Clear limits on what it can access", "Escalation to a person when unsure"],
    "web_application_development", "assets/images/projects",
    "Illustration of an AI assistant interface within a business application", "fa-solid fa-comments", False),
 ],
 "deliverables_h2": "Reduce the work your team repeats every day",
 "deliverables_p": "Four ordinary examples of work that usually does not need a person doing it by hand.",
 "deliverables": [
   ("fa-solid fa-inbox", "Enquiry Routing", "An enquiry arrives by form, email or WhatsApp. It is logged, categorised, assigned to the right person and acknowledged \u2014 without anyone watching an inbox."),
   ("fa-solid fa-file-invoice", "Document Processing", "Supplier invoices, delivery notes, filled-in forms. The details are extracted and put where they belong, with anything uncertain flagged for a person to check."),
   ("fa-solid fa-chart-column", "Recurring Reports", "The Monday figures that someone currently assembles from three systems, compiled on schedule and sent to the people who need them."),
   ("fa-solid fa-right-left", "Keeping Systems in Step", "A customer's details change in one tool and follow into the others, so nobody types the same address into three places."),
 ],
 "process_h2": "Map the task, test the automation, keep control",
 "process_p": "Automation is only useful if you can trust it, which means knowing what it does when something is unusual.",
 "process": [
   ("fa-solid fa-magnifying-glass", "Assess", "How the task runs now"),
   ("fa-solid fa-scale-balanced", "Choose", "Fixed rules or AI"),
   ("fa-solid fa-plug", "Integrate", "Connect the tools involved"),
   ("fa-solid fa-triangle-exclamation", "Exceptions", "Define the unusual cases"),
   ("fa-solid fa-user-check", "Human Review", "Approval before it commits"),
   ("fa-solid fa-play", "Run", "One workflow, in real use"),
   ("fa-solid fa-heart-pulse", "Monitor", "Alerts when it fails"),
 ],
 "related_h2": "Make automation work with your existing tools",
 "related_p": "Automation has to plug into something. These are what it usually plugs into.",
 "related": [
   ("fa-solid fa-table-columns", "Web Applications", "Where an automated step usually lives \u2014 the system holding the records it reads, updates and routes between people.", "service-web-applications.html"),
   ("fa-solid fa-code", "Custom Software", "When the tools in the chain have no usable connection between them, the bridge has to be built before anything can be automated across it.", "service-custom-software.html"),
   ("fa-solid fa-screwdriver-wrench", "Software Maintenance", "Automations depend on other people's systems. When a connected tool changes its interface, something silently stops \u2014 monitoring is how you find out.", "service-software-maintenance.html"),
 ],
 "cta_h2": "Tell us which task eats the most time",
 "cta_p": "Name one job your team repeats every week. We will tell you whether it can be automated, how, and whether it is worth doing.",
 "seo_title": "AI &amp; Business Automation in Chennai | DeepAbi Innovations",
 "seo_desc": "Practical AI and business automation in Chennai — enquiry routing, document processing, data synchronisation and AI assistants on your own approved information.",
 "keywords": "business automation Chennai, AI solutions Chennai, workflow automation Chennai, document processing automation, AI assistant development Chennai",
},
{
 "slug": "software-maintenance",
 "name": "Software Maintenance",
 "plain": "Software Maintenance",
 "h1": "Keeping Software Reliable, Secure and Improving",
 "lede": "Launch is the start. Browsers update, devices change, security issues surface and your own requirements move — maintenance is what keeps software useful through all of it.",
 "hero_img": ("website_maintenance", "assets/images/services",
              "Illustration representing ongoing software maintenance and monitoring"),
 "cta_primary": "Discuss Ongoing Support",
 "intro_h2": "Covering websites and applications alike",
 "intro": [
   "Maintenance applies to a business website, a web application, a mobile app or installed desktop software. What changes is the rhythm: a website may need content and security updates, an application needs dependency upgrades and fixes as people use it in ways nobody predicted.",
   "We also take on software built by someone else, where the code is in a reviewable state. That starts with an assessment rather than a promise.",
 ],
 "blocks": [
   ("fixes-updates", "01 · Fix", "Diagnosis, fixes and updates",
    "The core of any maintenance arrangement: something is wrong or out of date, and it gets investigated properly rather than patched over.",
    ["Bug diagnosis and fixes", "Dependency and library updates",
     "Browser and device compatibility", "Content and data updates",
     "Root-cause investigation, not workarounds", "Changes tested before they go live"],
    "performance_optimization", "assets/images/services",
    "Illustration representing software diagnosis and updates", "fa-solid fa-bug", False),
   ("security-performance", "02 · Protect", "Security, performance and configuration",
    "The work that keeps software safe and quick as content grows and the surrounding platforms change underneath it.",
    ["Security updates and patching", "Configuration and hardening improvements",
     "Performance tuning as data grows", "Backup and recovery checks",
     "Monitoring and error alerts", "Troubleshooting when something breaks"],
    "local_services_website", "assets/images/projects",
    "Illustration representing security and performance monitoring", "fa-solid fa-shield-halved", True),
   ("improve-takeover", "03 · Improve", "Enhancements and taking over existing software",
    "Real use always reveals improvements worth making — and sometimes the software that needs looking after was built by somebody else.",
    ["Feature enhancements over time", "Small improvements from real use",
     "Technical support for your team", "Review of existing software",
     "Takeover where the code is workable", "Documentation of what you own"],
    "team-collaboration", "assets/images/about",
    "Illustration representing a team reviewing and improving existing software", "fa-solid fa-circle-plus", False),
 ],
 "deliverables_h2": "Keep your software reliable as your business changes",
 "deliverables_p": "The work that keeps something built last year still working properly this year.",
 "deliverables": [
   ("fa-solid fa-bug", "Faults Fixed at the Cause", "Something is reported, reproduced and traced to why it happens \u2014 rather than patched at the surface and reported again next month."),
   ("fa-solid fa-rotate", "Compatibility Kept Current", "Browsers, phone operating systems and Windows all move. So do the libraries underneath your software. Keeping up is steady work, not an emergency."),
   ("fa-solid fa-shield-halved", "Security Patched, Not Deferred", "Known vulnerabilities in dependencies are applied and tested as they appear, and backups are verified rather than assumed."),
   ("fa-solid fa-gauge-high", "Performance as Data Grows", "A system that was quick with a thousand records is not automatically quick with a hundred thousand. Queries and indexes are tuned as volume builds."),
   ("fa-solid fa-circle-plus", "Small Improvements Worth Making", "Real use exposes the field everyone wants added and the screen that takes three clicks too many. These go in as ordinary maintenance work."),
 ],
 "deliverables_cols": 3,
 "process_h2": "Assess, prioritize, improve and monitor",
 "process_p": "Including for software somebody else built, where the code is in a reviewable state.",
 "process": [
   ("fa-solid fa-clipboard-check", "Assess", "Review what exists"),
   ("fa-solid fa-file-contract", "Agree Scope", "Coverage &amp; response"),
   ("fa-solid fa-list-ol", "Prioritise", "What matters first"),
   ("fa-solid fa-screwdriver-wrench", "Change", "Fix &amp; improve"),
   ("fa-solid fa-vial", "Test", "Before anything goes live"),
   ("fa-solid fa-heart-pulse", "Monitor", "Watch the result"),
   ("fa-solid fa-comments", "Review", "Check in periodically"),
 ],
 "related_h2": "When maintenance needs a larger next step",
 "related_p": "Most requests stay maintenance work. Occasionally one is genuinely a project \u2014 and it is worth saying so rather than stretching a support arrangement around it.",
 "related": [
   ("fa-solid fa-code", "Custom Software", "When a request is a new capability rather than a fix \u2014 a module the system never had \u2014 it is scoped and quoted as a piece of work, not absorbed quietly.", "service-custom-software.html"),
   ("fa-solid fa-table-columns", "Web Applications", "When a process has outgrown the spreadsheets and manual steps that maintenance keeps propping up, the honest answer is a system for it.", "service-web-applications.html"),
   ("fa-solid fa-mobile-screen", "Mobile Applications", "When customers or field staff need the software away from a desk, and the current site is being stretched to cover a job it was not built for.", "service-mobile-applications.html"),
   ("fa-solid fa-desktop", "Desktop Applications", "When local files, attached hardware or working through an outage have become requirements that a browser-based system cannot meet.", "service-desktop-applications.html"),
 ],
 "related_cols": 4,
 "cta_h2": "Tell us what needs looking after",
 "cta_p": "Whether we built it or not, describe the software and what is going wrong or going stale. We will start with an honest assessment.",
 "seo_title": "Software Maintenance &amp; Support in Chennai | DeepAbi Innovations",
 "seo_desc": "Software and website maintenance in Chennai — bug fixes, dependency and security updates, performance tuning, monitoring and enhancements, scoped per engagement.",
 "keywords": "software maintenance Chennai, website maintenance Chennai, application support Chennai, software support services Chennai",
},
]


def build(s):
    intro = "\n        ".join(f"<p>{p}</p>" for p in s["intro"])
    img, folder, alt = s["hero_img"]
    blocks = "\n".join(
        service_block(a, e, t, d, items, im, ia, ic, folder=f, reverse=r).replace("{cta}", s["cta_primary"])
        for a, e, t, d, items, im, f, ia, ic, r in s["blocks"])

    body = f'''
  <div class="page-header page-header-gradient services-hero">
    <div class="hero-bg" aria-hidden="true">
      <div class="mesh-blob blob-1"></div>
      <div class="mesh-blob blob-2"></div>
    </div>
    <div class="container services-hero-grid">
      <div>
        {breadcrumb(s["name"])}
        <span class="eyebrow gold">{s["name"]}</span>
        <h1>{s["h1"]}</h1>
        <p>{s["lede"]}</p>
        <div class="services-hero-actions">
          <a href="contact.html" class="btn btn-accent btn-lg">{s["cta_primary"]} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          <a href="#{s["blocks"][0][0]}" class="btn btn-secondary btn-lg services-hero-btn-outline">See What We Build</a>
        </div>
      </div>
      <div class="services-hero-visual">
        <div class="hero-visual-glow" aria-hidden="true"></div>
        {picture(img, alt, 480, 400, folder, eager=True)}
      </div>
    </div>
  </div>

  <div class="section">
    <div class="container detail-overview" data-reveal>
      <div>
        <h2 style="font-size:28px; margin-bottom:16px;">{s["intro_h2"]}</h2>
        {intro}
      </div>
      <div class="img-frame">
        {picture(s["blocks"][0][5], s["blocks"][0][7], 560, 425, s["blocks"][0][6])}
      </div>
    </div>
  </div>

  <div class="section" style="padding-top:0;">
    <div class="container">
{blocks}
    </div>
  </div>

  <div class="section section-alt">
    <div class="container">
{head(s["deliverables_h2"], s.get("deliverables_p"))}
{cards(s["deliverables"], s.get("deliverables_cols", 4))}
    </div>
  </div>

  <div class="section">
    <div class="container">
{head(s["process_h2"], s.get("process_p"))}
{process(s["process"])}
    </div>
  </div>

  <div class="section section-alt">
    <div class="container">
{head(s["related_h2"], s.get("related_p"))}
{related(s["related"], s.get("related_cols", 3))}
    </div>
  </div>

  <div class="section">
    <div class="container">
      <div class="cta-section" data-reveal>
        <h2>{s["cta_h2"]}</h2>
        <p>{s["cta_p"]}</p>
        <a href="contact.html" class="btn btn-accent">{s["cta_primary"]} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
      </div>
    </div>
  </div>
'''

    page(
        filename=f'service-{s["slug"]}.html',
        active="services",
        title=s["seo_title"],
        description=s["seo_desc"],
        extra_keywords=s["keywords"],
        body=body,
        extra_css=CSS + '\n<link rel="stylesheet" href="css/pages/service-detail.css">',
        schema=schema(s["plain"], s["seo_desc"].replace("&amp;", "and"), s["slug"]),
        body_class="hero-dark",
        # A service hidden from the public site keeps its page and its URL,
        # but asks search engines not to list it. "follow" is kept and
        # robots.txt still allows the page, so the directive can be read.
        noindex=not is_service_public(s["slug"]),
    )


for _s in SERVICES:
    build(_s)
