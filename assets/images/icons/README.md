# assets/images/icons

Reserved for custom UI icon assets (SVG/PNG) if you move away from the
Font Awesome CDN currently used for all interface icons across the site.

Nothing is stored here yet — every icon in the current build is loaded via
`https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/` in each page's
`<head>` (see `scripts/build_site.py` → `head()`).

If you add custom icons here, prefer SVG for crisp rendering at any size,
and keep filenames descriptive (e.g. `icon-whatsapp.svg`, not `icon1.svg`).
