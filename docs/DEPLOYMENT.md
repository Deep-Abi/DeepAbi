# Deployment Guide

This is a fully static site — no server-side runtime, no build step, no environment variables required. Any static host works.

## Before you deploy

1. Update `SITE_URL` references — search the project for `deepabi.com` (in `robots.txt`, `sitemap.xml`, and the `<meta>`/JSON-LD blocks in every page's `<head>`) and replace with your real domain.
2. Replace placeholder imagery in `assets/images/{home,services,about,projects,technology,testimonials}/` with real photography if desired — same filenames, same folders, all three formats (see README).
3. Confirm the contact details in `scripts/build_site.py` (`EMAIL`, `PHONE_1_*`, `PHONE_2_*`) are correct, then re-run the generator scripts so every page picks up the change.
4. Wire the contact form (`js/pages/contact.js`) to a real email/form backend — see options below.
5. Update the social links (`#` placeholders) in the navbar/footer to your real GitHub, LinkedIn, Instagram, and X accounts.
6. Replace the legal placeholder text in `privacy.html` and `terms.html` with copy reviewed by qualified counsel.

## Option A — Netlify (recommended for simplicity)

1. Drag-and-drop the `deepabi-site` folder onto [app.netlify.com/drop](https://app.netlify.com/drop), **or** connect a Git repo containing this folder and set:
   - Build command: *(none)*
   - Publish directory: `deepabi-site` (or `.` if the repo root **is** this folder)
2. Add a custom domain under **Site settings → Domain management**.
3. For the contact form, either:
   - Add `data-netlify="true"` to the `<form id="contactForm">` tag and let Netlify Forms capture submissions (no code change needed beyond that attribute), or
   - Point the form at a serverless function / third-party form service (see Option D).

## Option B — Vercel

1. `vercel` CLI: run `vercel` from inside `deepabi-site/` and accept the defaults (no framework detected → static deploy).
2. Or connect the Git repo in the Vercel dashboard with **Framework Preset: Other** and **Output Directory:** `.`.

## Option C — GitHub Pages

1. Push `deepabi-site/` (or its contents) to a repo.
2. Repo **Settings → Pages → Source**: deploy from the `main` branch, root folder.
3. GitHub Pages serves `index.html` at the repo's Pages URL automatically. Add a `CNAME` file at the root with your custom domain if using one.

## Option D — Any static host / your own server

Upload the contents of `deepabi-site/` to the web root of any static host (S3 + CloudFront, Cloudflare Pages, Firebase Hosting, nginx, Apache, etc.). There is nothing to build or install.

For **nginx**, a minimal server block:

```nginx
server {
  listen 80;
  server_name www.deepabi.com;
  root /var/www/deepabi-site;
  index index.html;

  location / {
    try_files $uri $uri.html $uri/ =404;
  }

  location ~* \.(css|js|png|jpg|jpeg|webp|svg|ico|woff2?)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
  }
}
```

## Wiring the contact form to a real backend

The form (`contact.html` → `js/pages/contact.js`) currently only validates client-side and shows a success toast — it does not send anywhere. Pick one:

- **Formspree / Getform / Basin** (no backend code): point the `<form>`'s `action` at the service's endpoint and let it POST natively, or call their API via `fetch` inside `contact.js`.
- **Netlify Forms**: add `data-netlify="true"` to the form tag (Option A above).
- **Your own serverless function** (AWS Lambda, Vercel Functions, Cloudflare Workers): replace the `submit` handler in `js/pages/contact.js` with a `fetch('/api/contact', { method: 'POST', body: JSON.stringify(data) })` call, and implement that endpoint to send an email (e.g. via SES, SendGrid, or Resend).

## Performance checklist before going live

- [ ] Run [PageSpeed Insights](https://pagespeed.web.dev/) against the deployed URL and address any flagged Core Web Vitals issues.
- [ ] Confirm `robots.txt` and `sitemap.xml` are reachable at the domain root.
- [ ] Submit the sitemap in Google Search Console.
- [ ] Verify Open Graph tags render correctly using a share-preview tool (e.g. the LinkedIn Post Inspector or Twitter Card Validator).
- [ ] Enable HTTPS (most hosts above provision this automatically).
- [ ] Set long cache lifetimes for `images/`, `css/`, and `js/` (immutable filenames aside from content changes).
