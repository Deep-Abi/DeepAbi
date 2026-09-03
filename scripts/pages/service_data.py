"""Single source of truth for DeepAbi's eight primary service categories.

Both the Services landing page (build_services.py) and the eight dedicated
service pages (build_service_pages.py) are generated from this list, so a card
description, an icon or a URL can never drift between them.

Content rules baked into this data:
  * Every service is explained in plain business language first, technology second.
  * Use cases are written as things a business COULD build ("a distributor could
    ..."), never as completed DeepAbi projects, because that evidence does not
    exist yet.
  * Images are temporary re-uses of existing project assets. Each entry names an
    (image, folder) pair — swapping in a real photograph later means changing
    those two strings, nothing else.
"""

# key: slug used for the filename, the landing-page card anchor and cross-links.
SERVICES = [
    {
        "slug": "website-development",
        "name": "Website Development",
        "icon": "fa-solid fa-window-maximize",
        # Shown on the Services landing page and Home -> What We Build
        "card": "Professional websites for businesses, companies and brands — from landing pages and portfolios to complete corporate websites.",
        "hero_line": "Websites that make your business easy to find, easy to understand and easy to contact.",
        "image": ("website-development-workspace", "assets/images/services"),
        "image_alt": "Illustration of a website development workspace with component blocks",
        "what_is": [
            "A website is usually the first place a customer checks before they call, visit or buy. It has to load quickly, read clearly on a phone, explain what you do, and make getting in touch obvious.",
            "DeepAbi builds websites around those basics rather than around decoration — from a single focused landing page to a complete corporate site with multiple sections and departments.",
        ],
        "build": [
            ("fa-solid fa-store", "Business Websites", "A clear presence for local and service businesses so customers can find you and get in touch."),
            ("fa-solid fa-building", "Corporate Websites", "Structured sites for companies with several departments, services or product lines."),
            ("fa-solid fa-rocket", "Landing Pages", "A single focused page built around one campaign, offer or enquiry goal."),
            ("fa-solid fa-images", "Portfolio Websites", "Image-forward sites for studios, agencies and individual professionals."),
            ("fa-solid fa-box-open", "Product &amp; Catalogue Sites", "Browsable product or service catalogues with enquiry options."),
            ("fa-solid fa-arrows-rotate", "Website Redesign", "A rebuild of an existing site that has aged, slowed down or stopped converting."),
        ],
        "use_cases": [
            ("Local business", "A shop or service business needs customers searching nearby to find it, see what it offers and call or message in one tap."),
            ("Distributor", "A distributor needs a professional catalogue website where buyers can browse products and send an enquiry."),
            ("Company", "A growing company needs a corporate site that explains its services, capabilities and contact channels to serious clients."),
            ("Professional", "A consultant, photographer or designer needs a portfolio that presents work properly and makes enquiries easy."),
        ],
        "audience": ["Local and service businesses", "Distributors and traders", "Companies and corporates", "Studios and freelancers", "Startups launching a first site"],
        "capabilities": [
            "Responsive, cross-device development", "SEO-ready structure from day one",
            "Performance and Core Web Vitals tuning", "Accessibility built in, not retrofitted",
            "Content that your team can update", "Clean, documented, handover-ready code",
        ],
        "related": ["web-applications", "software-maintenance", "custom-software"],
        "seo_title": "Website Development Company in Chennai | DeepAbi Innovations",
        "seo_desc": "Professional website development in Chennai — business, corporate, landing page and portfolio websites built to load fast, rank well and convert enquiries.",
        "keywords": "website development company in Chennai, website developers Chennai, business website development Chennai, corporate website development Chennai",
    },
    {
        "slug": "web-applications",
        "name": "Web Applications",
        "icon": "fa-solid fa-table-columns",
        "card": "Browser-based applications that help businesses manage information, customers, operations and online services.",
        "hero_line": "Software your team opens in a browser to run the day-to-day work of the business.",
        "image": ("web_application_development", "assets/images/projects"),
        "image_alt": "Illustration representing a browser-based business application interface",
        "what_is": [
            "A web application is software that runs through a web browser. Instead of only reading information, people <em>do</em> things with it — log in, add records, check status, generate a report, approve a request.",
            "Nothing to install, and it works from an office computer, a laptop at home or a phone on site. That is usually the difference between a website and a web application: a website tells people about your business, a web application helps you run it.",
        ],
        "build": [
            ("fa-solid fa-user-group", "Customer Portals", "A logged-in area where customers check orders, requests or project status."),
            ("fa-solid fa-gauge", "Admin Dashboards", "One screen that shows what is happening across the business."),
            ("fa-solid fa-calendar-check", "Booking Systems", "Appointments, slots or reservations managed in one place."),
            ("fa-solid fa-boxes-stacked", "Inventory Systems", "Stock, products and movement tracked accurately."),
            ("fa-solid fa-file-invoice", "Order Management", "Orders, enquiries and fulfilment followed from start to finish."),
            ("fa-solid fa-diagram-project", "Internal Workflow Tools", "Approvals, handovers and internal processes made trackable."),
        ],
        "use_cases": [
            ("Restaurant", "An online reservation system where customers book a table and staff see the day's bookings on one screen."),
            ("Distributor", "A dashboard for products, stock levels and incoming enquiries, replacing scattered spreadsheets."),
            ("Service company", "A customer portal where clients raise requests and follow the status of their work."),
            ("Small business", "An internal application for customers, invoices and daily operations that fits how the team already works."),
        ],
        "audience": ["Businesses outgrowing spreadsheets", "Teams juggling several disconnected tools", "Companies with repeatable internal processes", "Service businesses managing many customer requests"],
        "capabilities": [
            "Secure user accounts and roles", "Dashboards and reporting views",
            "Search, filtering and data export", "Integration with tools you already use",
            "Works on desktop, tablet and mobile", "Built to add features later without a rebuild",
        ],
        "related": ["custom-software", "ai-automation", "saas-products"],
        "seo_title": "Web Application Development in Chennai | DeepAbi Innovations",
        "seo_desc": "Custom web application development in Chennai — customer portals, dashboards, booking and inventory systems built around your business operations.",
        "keywords": "web application development Chennai, web app development company Chennai, custom web application Chennai, business web application development",
    },
    {
        "slug": "mobile-applications",
        "name": "Mobile Applications",
        "icon": "fa-solid fa-mobile-screen",
        "card": "Mobile apps designed around business services, customer experiences and everyday mobile workflows.",
        "hero_line": "Put your service in your customers' pocket — or your operations in your team's hand.",
        "image": ("mobile_portrait", "assets/images/projects"),
        "image_alt": "Illustration of a business application shown on a mobile phone screen",
        "what_is": [
            "A mobile application gives customers, employees or partners direct access to a service from their phone — booking, ordering, checking, updating or tracking, wherever they are.",
            "Not every business needs one. A mobile app earns its place when people use the service repeatedly, when they need it away from a desk, or when a phone's camera, location or notifications genuinely make the job easier.",
        ],
        "build": [
            ("fa-solid fa-mobile-button", "Customer Apps", "Booking, ordering or account access for the people you serve."),
            ("fa-solid fa-briefcase", "Business Apps", "Tools for staff who work away from a computer."),
            ("fa-solid fa-bell", "Service &amp; Booking Apps", "Appointments, reminders and status updates."),
            ("fa-solid fa-list-check", "Field &amp; Delivery Tools", "Job lists, updates and proof of completion from the field."),
            ("fa-solid fa-book-open", "Catalogue Apps", "Products or services browsable on mobile with enquiry options."),
            ("fa-solid fa-users-gear", "Employee Apps", "Internal workflows accessible from a phone."),
        ],
        "use_cases": [
            ("Restaurant", "Customers browse the menu, order or reserve a table, and receive updates without calling."),
            ("Service business", "Customers book an appointment and get reminders and status notifications automatically."),
            ("Distributor", "Sales staff open product and customer information on mobile while visiting a client."),
            ("Company", "Employees submit and approve routine requests from their phones instead of chasing email."),
        ],
        "audience": ["Businesses whose customers return regularly", "Teams working away from a desk", "Service companies with bookings or visits", "Businesses already running a web application that needs a mobile companion"],
        "capabilities": [
            "Designed mobile-first, not shrunk down", "Works alongside your website or web application",
            "Push notifications and reminders", "Offline-tolerant screens where it matters",
            "Clear, simple interfaces for non-technical users", "Store-ready build and release support",
        ],
        "related": ["web-applications", "custom-software", "software-maintenance"],
        "seo_title": "Mobile App Development in Chennai | DeepAbi Innovations",
        "seo_desc": "Mobile application development in Chennai — customer, booking, field and employee apps designed around real business workflows, not app-store templates.",
        "keywords": "mobile app development Chennai, mobile application development company Chennai, custom mobile app development Chennai",
    },
    {
        "slug": "desktop-applications",
        "name": "Desktop Applications",
        "icon": "fa-solid fa-desktop",
        "card": "Software that runs on desktop computers for business operations, internal tools and specialized work.",
        "hero_line": "Software installed on the computers your team already uses, built for one job and built to do it well.",
        "image": ("desktop", "assets/images/projects"),
        "image_alt": "Illustration of business software running on a desktop computer",
        "what_is": [
            "A desktop application is a program installed directly on a computer, like the billing software at a counter or a tool that processes files in bulk. It runs whether or not the internet is working, and it can use the computer's own files, printers and hardware directly.",
            "This still matters. Plenty of real business work — billing, stock, reports, repetitive file handling — is faster and more reliable as a desktop tool than as a website.",
        ],
        "build": [
            ("fa-solid fa-receipt", "Billing &amp; Invoicing Tools", "Fast counter or back-office billing with printing."),
            ("fa-solid fa-warehouse", "Inventory Software", "Products, stock and movement recorded in one place."),
            ("fa-solid fa-database", "Data Management Tools", "Records organised, searchable and safe to work with."),
            ("fa-solid fa-file-arrow-down", "File Processing Utilities", "Bulk renaming, converting, merging or extracting."),
            ("fa-solid fa-chart-column", "Reporting Applications", "Scheduled or on-demand reports from your own data."),
            ("fa-solid fa-sliders", "Internal Admin Tools", "Small, purpose-built utilities for a specific team task."),
        ],
        "use_cases": [
            ("Retail or trading", "A business managing inventory across several Excel files could use one desktop application that organises products, stock and reports together."),
            ("Publishing or operations", "A team doing repetitive file-processing work could use a custom tool that automates most of those steps."),
            ("Back office", "A finance or admin team could replace a fragile spreadsheet with a proper tool that validates entries and prints clean reports."),
            ("Specialist work", "A business with an unusual process no off-the-shelf product supports could have a tool built exactly around it."),
        ],
        "audience": ["Businesses running critical work in spreadsheets", "Counter or in-store operations", "Teams doing repetitive computer work", "Offices with limited or unreliable internet"],
        "capabilities": [
            "Windows desktop applications", "Works offline where required",
            "Local printing and file handling", "Import and export with existing spreadsheets",
            "Simple interfaces for non-technical staff", "Installer and update support",
        ],
        "related": ["custom-software", "ai-automation", "software-maintenance"],
        "seo_title": "Desktop Application Development in Chennai | DeepAbi Innovations",
        "seo_desc": "Desktop application development in Chennai — billing, inventory, reporting and file-processing tools built for the way your business actually works.",
        "keywords": "desktop application development Chennai, desktop software development Chennai, business software development Chennai, custom Windows application Chennai",
    },
    {
        "slug": "custom-software",
        "name": "Custom Software",
        "icon": "fa-solid fa-code",
        "card": "Software designed specifically around a company's unique processes, requirements and challenges.",
        "hero_line": "When your business does not work the way standard software expects, the software should change — not your business.",
        "image": ("mission", "assets/images/about"),
        "image_alt": "Abstract illustration representing purpose-built software design",
        "what_is": [
            "Off-the-shelf software is built for the average business. It fits most companies roughly and no company exactly. That is fine until the gap starts costing time — duplicate data entry, workarounds, five tools that do not talk to each other, a process that lives in one person's head.",
            "Custom software is designed around how your business actually works. You are not paying for features you will never use, and the parts you depend on every day get built properly.",
        ],
        "build": [
            ("fa-solid fa-gears", "Internal Business Systems", "One system for the process your business runs on."),
            ("fa-solid fa-route", "Workflow Management", "Steps, owners and approvals made visible and trackable."),
            ("fa-solid fa-boxes-packing", "Inventory &amp; Operations", "Stock, jobs and resources managed accurately."),
            ("fa-solid fa-address-book", "Customer Management", "Customer records and history in one reliable place."),
            ("fa-solid fa-plug", "System Integrations", "Existing tools connected so data stops being retyped."),
            ("fa-solid fa-screwdriver-wrench", "Business Utilities", "Small tools that remove a specific daily bottleneck."),
        ],
        "use_cases": [
            ("Today", "Orders arrive on WhatsApp, stock lives in Excel, delivery notes are on paper, and someone reconciles it all at the end of the week."),
            ("Possible", "One purpose-built system where an order is entered once and flows through stock, delivery and reporting automatically."),
            ("Growing team", "A process that worked with three people breaks at fifteen — custom software makes the process explicit instead of tribal knowledge."),
            ("Integration", "Two systems the business already pays for are connected so information moves between them without manual copying."),
        ],
        "audience": ["Businesses with a process no product fits", "Teams doing heavy duplicate data entry", "Companies running on spreadsheets and messages", "Businesses paying for several tools that do not connect"],
        "capabilities": [
            "Requirement study before any code", "Built around your existing process",
            "Phased delivery, usable early", "Integration with current tools",
            "Your data stays yours and exportable", "Documented and extendable later",
        ],
        "related": ["web-applications", "desktop-applications", "ai-automation"],
        "seo_title": "Custom Software Development in Chennai | DeepAbi Innovations",
        "seo_desc": "Custom software development in Chennai — business systems, workflow tools and integrations designed around your processes instead of forcing a product to fit.",
        "keywords": "custom software development Chennai, custom software company Chennai, business software development Chennai, software developers in Chennai",
    },
    {
        "slug": "saas-products",
        "name": "SaaS Products",
        "icon": "fa-solid fa-cloud",
        "card": "Online software platforms that users can access through subscriptions, accounts or recurring services.",
        "hero_line": "Turning a software idea into a product that many customers can sign up for and use online.",
        "image": ("vision", "assets/images/about"),
        "image_alt": "Abstract illustration representing a cloud-based software platform",
        "what_is": [
            "<strong>SaaS</strong> stands for <strong>Software as a Service</strong>. Instead of buying and installing software, customers create an account and use it online, usually paying monthly or yearly.",
            "The difference from a normal business application is who uses it. A business application serves one company. A SaaS product serves many customers at once, each with their own account and their own data kept separate — which changes how it has to be built from the very first decision.",
        ],
        "build": [
            ("fa-solid fa-id-card", "Subscription Platforms", "Sign-up, plans and account management."),
            ("fa-solid fa-people-roof", "Multi-Customer Systems", "Many organisations on one platform, data kept separate."),
            ("fa-solid fa-calendar-days", "Booking Platforms", "An online service many businesses can use."),
            ("fa-solid fa-chart-pie", "Reporting Platforms", "Dashboards customers log in to check."),
            ("fa-solid fa-industry", "Industry-Specific Software", "A product built for one trade or profession."),
            ("fa-solid fa-user-shield", "Admin &amp; Owner Tools", "The controls you need to run the product itself."),
        ],
        "use_cases": [
            ("Product idea", "A business idea that needs one online platform serving many registered customers can be developed as a SaaS product."),
            ("Existing service", "A service currently delivered manually to each client could become a platform clients use themselves."),
            ("Trade software", "A tool built for one industry — clinics, tuition centres, workshops — offered to many businesses in that field."),
            ("First version", "A focused first release that proves demand before the full product is built out."),
        ],
        "audience": ["Founders with a software product idea", "Businesses productising a manual service", "Teams that need a first version to test the market", "Companies serving many similar customers"],
        "capabilities": [
            "User accounts, roles and permissions", "Separate, secure data per customer",
            "Subscription-ready structure", "Owner and admin management tools",
            "Built to grow with user numbers", "Start small, expand in stages",
        ],
        "related": ["web-applications", "ai-automation", "software-maintenance"],
        "seo_title": "SaaS Development Services in Chennai | DeepAbi Innovations",
        "seo_desc": "SaaS product development in Chennai — subscription platforms and multi-customer software built with accounts, roles and room to grow from the first version.",
        "keywords": "SaaS development Chennai, SaaS application development Chennai, custom SaaS development Chennai, SaaS product development company",
    },
    {
        "slug": "ai-automation",
        "name": "AI &amp; Automation",
        "icon": "fa-solid fa-robot",
        "card": "AI-powered tools and automated workflows that help reduce repetitive work and improve business efficiency.",
        "hero_line": "Less retyping, less chasing, less copying between systems — so people spend time on work that needs judgement.",
        "image": ("technology-stack-network", "assets/images/technology"),
        "image_alt": "Illustration of connected systems representing automated workflows",
        "what_is": [
            "Most businesses lose hours a week to work nobody chose to do: copying enquiry details into a second system, renaming files, compiling the same report, answering the same question.",
            "Automation removes those steps. AI helps where the work involves reading, sorting or summarising information rather than following a fixed rule. Both are useful in specific places — neither is a reason to rebuild everything, and we will say so when a simple fix is the better answer.",
        ],
        "build": [
            ("fa-solid fa-arrows-turn-right", "Workflow Automation", "Routine steps that run without anyone remembering to do them."),
            ("fa-solid fa-file-lines", "Document Processing", "Information pulled out of documents and organised."),
            ("fa-solid fa-magnifying-glass", "AI-Assisted Search", "Finding the right record or answer in your own data."),
            ("fa-solid fa-comments", "Support Assistance", "Faster answers to repeated customer questions."),
            ("fa-solid fa-envelope-open-text", "Automated Notifications", "Alerts and reminders triggered by real events."),
            ("fa-solid fa-plug-circle-bolt", "System Integrations", "Two tools connected so data moves by itself."),
        ],
        "use_cases": [
            ("Enquiry handling", "A business repeatedly copying enquiry information between a form, a spreadsheet and a messaging app could automate most of that path."),
            ("Document-heavy work", "A team handling large numbers of documents could use software to organise and extract the information it needs."),
            ("Inside an application", "A business application could include AI-assisted search or summarising so staff find answers without digging."),
            ("Routine reporting", "A report someone rebuilds every Monday could generate and send itself."),
        ],
        "audience": ["Teams doing repetitive data entry", "Businesses handling many documents", "Companies running the same report repeatedly", "Support teams answering the same questions daily"],
        "capabilities": [
            "Automation of clearly repeatable steps", "AI applied where it genuinely helps",
            "Works with the systems you already have", "Human review kept where accuracy matters",
            "Start with one workflow, expand later", "Honest advice when automation is not worth it",
        ],
        "related": ["custom-software", "web-applications", "software-maintenance"],
        "seo_title": "AI &amp; Business Automation Solutions Chennai | DeepAbi Innovations",
        "seo_desc": "Practical AI and business automation in Chennai — workflow automation, document processing and AI-assisted tools that cut repetitive work, without the hype.",
        "keywords": "AI solutions Chennai, business automation Chennai, workflow automation Chennai, AI automation solutions Chennai",
    },
    {
        "slug": "software-maintenance",
        "name": "Software Maintenance",
        "icon": "fa-solid fa-screwdriver-wrench",
        "card": "Ongoing support, fixes, improvements, optimization and updates for websites and software applications.",
        "hero_line": "Software is not finished at launch. It stays useful only if it keeps up with your business.",
        "image": ("website_maintenance", "assets/images/services"),
        "image_alt": "Illustration representing ongoing software maintenance and monitoring",
        "what_is": [
            "Browsers update, devices change, security issues are discovered, and your own business changes what it needs. Software that is never touched after launch slowly stops working properly — usually starting with the parts customers see.",
            "Maintenance keeps things working, keeps them secure, and adds the small improvements that come from actually using the software for a year.",
        ],
        "build": [
            ("fa-solid fa-bug", "Bug Fixes", "Problems investigated and corrected properly."),
            ("fa-solid fa-shield-halved", "Security Updates", "Dependencies and patches kept current."),
            ("fa-solid fa-gauge-high", "Performance Improvements", "Pages and screens kept fast as content grows."),
            ("fa-solid fa-pen-to-square", "Content &amp; Updates", "Text, products, pages and details kept accurate."),
            ("fa-solid fa-circle-plus", "Feature Improvements", "Small additions as the business needs them."),
            ("fa-solid fa-heart-pulse", "Monitoring &amp; Checks", "Uptime and errors watched so issues surface early."),
        ],
        "use_cases": [
            ("Website", "A business site needs updates as products, services, prices and team details change through the year."),
            ("Application", "A live application needs fixes, small improvements and compatibility updates as it is used daily."),
            ("Inherited system", "Software built by someone else can be taken over, documented and kept running."),
            ("After launch", "The first months of real use always reveal improvements worth making."),
        ],
        "audience": ["Businesses with a live website or application", "Companies without an in-house developer", "Owners of software built by someone else", "Teams that want changes made safely"],
        "capabilities": [
            "Website and application maintenance", "Security and dependency updates",
            "Performance monitoring and tuning", "Content and feature updates",
            "Backups and recovery checks", "Clear response expectations, agreed upfront",
        ],
        "related": ["website-development", "web-applications", "custom-software"],
        "seo_title": "Software Maintenance &amp; Support Chennai | DeepAbi Innovations",
        "seo_desc": "Software and website maintenance in Chennai — bug fixes, security updates, performance tuning and ongoing improvements that keep your software reliable.",
        "keywords": "software maintenance Chennai, software support Chennai, application maintenance Chennai, website maintenance Chennai",
    },
]

BY_SLUG = {s["slug"]: s for s in SERVICES}


def page_file(slug):
    """Flat, root-level filenames matching the project's existing convention
    (index.html, services.html, service-detail.html). Keeps every relative
    asset path in the shared header/footer valid and needs no server rewrite
    rules or deployment changes."""
    return f"service-{slug}.html"
