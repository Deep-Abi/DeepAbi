# DeepAbi Innovations — project structure and build procedure

This is a static site. There is no framework, no bundler and no runtime
dependency on the build scripts: what ships is plain HTML, CSS, JS and images.

## Which files are authoritative

| Kind | Path | Authoritative? |
|---|---|---|
| Page generators | `scripts/pages/build_*.py` | **Yes** — edit these |
| Shared template, nav, footer, contact constants | `scripts/build_site.py` | **Yes** — edit this |
| Generated pages | `*.html` in the project root | No — regenerated output |
| `sitemap.xml`, `robots.txt`, `site.webmanifest` | project root | No — written by `build_legal_and_seo.py` |
| Stylesheets | `css/common.css`, `css/pages/*.css` | **Yes** — hand-written |
| Scripts | `js/common.js`, `js/pages/*.js` | **Yes** — hand-written |
| Images | `assets/images/<group>/<format>/<name>.<ext>` | **Yes** — source assets |
| Documentation | `docs/`, `README.md` | **Yes** |
| Reports | `reports/` | Output; not deployed |

Everything in the project root that ends in `.html` is generated. Editing one
by hand works until someone runs the generator, at which point the edit is
gone. Change the generator instead.

## Building

Every generator is standalone and writes its own page(s) into the project root:

```
cd scripts/pages
python3 build_home.py                 # index.html
python3 build_about.py                # about.html
python3 build_contact.py              # contact.html
python3 build_projects.py             # projects.html
python3 build_technologies.py         # technologies.html
python3 build_services.py             # services.html
python3 build_website_development.py  # service-website-development.html
python3 build_service_pages.py        # the other seven service-*.html pages
python3 build_service_detail.py       # service-detail.html (redirect stub)
python3 build_legal_and_seo.py        # privacy, terms, sitemap.xml, robots.txt, site.webmanifest
```

Python 3 only; no third-party packages are needed.

`scripts/generate_images.py` is a separate, occasional tool for producing image
derivatives. It is **not** part of the page build and should not be run as part
of a normal edit — it can overwrite optimised assets.

## Rule: a rebuild must never change approved content

The generators are the source of truth, so any hand-edit made directly to a
generated `.html` file has to be mirrored back into its generator immediately.
Several were not, historically, and a later rebuild silently reverted approved
copy (the home page's featured story, the "Built & Tested Across All Devices"
section, and eyebrow labels the design had deliberately removed). Those are now
carried in the generators, including the deliberately commented-out eyebrow
labels, which carry a comment saying not to uncomment them.

After changing any generator, verify before committing:

```
# regenerate, then diff the output against the previous committed version
git diff --stat
git diff -- index.html            # read every line; nothing unexpected
```

If a diff shows content you did not intend to change, the generator has drifted
from the approved page. Fix the generator — do not re-hand-edit the HTML.

## Service visibility

The site is currently in **website-only mode**: Website Development is the one
publicly offered service and the other seven are hidden. This is a reversible
visibility setting, not a deletion — their generators, pages, demos and assets
are all still here and still build.

The switch is `SERVICE_REGISTRY` in `scripts/build_site.py`: one `"public"`
flag per service. Navigation, the Services page, the home grid, Projects, the
Contact selector, related-service links, structured data, `noindex` and the
sitemap all derive from it.

To restore all eight: set every `"public"` to `True` and rebuild. To restore
one: set just that one. Full detail, including what each flag controls and why
`robots.txt` must not block the hidden pages, is in
**[docs/SERVICE-VISIBILITY.md](SERVICE-VISIBILITY.md)**.

Never hide a service with CSS — hidden services are filtered out during
generation so their markup never reaches the page, which keeps them out of the
tab order and away from screen readers.

## Contact details

All of them live in one place, `scripts/build_site.py`:

```python
EMAIL_PRIMARY   = "hello@deepabi.com"        # public / general enquiries
EMAIL_SECONDARY = "deepabi.tech@gmail.com"   # technical contact
PHONE_1_DISPLAY = "+91 89460 97125"          # primary, also the WhatsApp number
PHONE_2_DISPLAY = "+91 90255 48401"          # secondary
```

Change the constant, rebuild every page, and the header, mobile menu, footer,
floating contact button, Contact page and structured data all follow. Do not
hard-code an address or number in a page generator.

`tel:` and WhatsApp destinations are derived from the `*_TEL` constants in
international format (`+918946097125`); the `*_DISPLAY` values carry the
readable spacing. Keep the two in step.

## Adding a page

1. Copy the closest existing generator in `scripts/pages/`.
2. Build the body, then call `page(...)` from `build_site` with a unique
   `title`, `description` and `canonical_path`.
3. Add the new file to the `pages` list in `build_legal_and_seo.py` so it
   reaches `sitemap.xml`.
4. Add the page-specific stylesheet under `css/pages/` if it needs one, and
   pass it through `extra_css`.

## Adding an image

Put the file in `assets/images/<group>/<format>/<name>.<ext>` and refer to it by
name; `picture()` in `build_site.py` finds every format that exists on disk and
emits AVIF → WebP → PNG `<source>` entries with a JPEG (or PNG) `<img>`
fallback, plus `width`/`height` so no layout shift occurs.

Keep the longest side at or below **1200px**. The largest any image is displayed
at is about 560 CSS pixels, so 1200px still covers a 2× screen; shipping the
3000px original is what made the pages heavy.

`picture(..., skip_formats=("avif",))` omits a format that exists but is not
wanted — used for the home hero, whose AVIF encode is larger than its JPEG.

## Checks worth running before publishing

- Regenerate everything and read `git diff`.
- Confirm every internal link and anchor resolves, and every referenced CSS,
  JS and image path exists.
- Load the site with JavaScript disabled: all content must still be visible.
  (`[data-reveal]` blocks are hidden only under `html.js`.)
- Check 360px, 768px and 1366px for horizontal overflow.
- Confirm the contact form still says only what is true — it composes an email
  in the visitor's own mail client and sends nothing itself.
