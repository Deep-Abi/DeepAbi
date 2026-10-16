"""service-detail.html — retired.

Everything this page carried now lives on service-website-development.html
(overview, benefits, process, related services). The old URL is kept alive
only so that existing links and any indexed copy land somewhere sensible
instead of a 404.

It is deliberately NOT built through build_site.page(): it needs no nav,
footer, CSS or JS, and it must not be indexed. It emits a bare document with
noindex, a canonical pointing at the real page, a meta refresh, and a visible
link for anyone who lands there with JavaScript or refresh disabled.

The file cannot simply be deleted from here — deletion is done by hand on the
server/repo. Overwriting it with this stub is the safe equivalent.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TARGET = "service-website-development.html"

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Website Development | DeepAbi Innovations</title>
<meta name="robots" content="noindex, follow" />
<link rel="canonical" href="https://www.deepabi.com/{TARGET}" />
<meta http-equiv="refresh" content="0; url={TARGET}" />
<link rel="icon" type="image/png" sizes="32x32" href="assets/images/logos/favicon-32.png" />
<style>
  body {{ margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center;
         font-family:system-ui,-apple-system,'Segoe UI',sans-serif; background:#F8FAFC; color:#111827; }}
  .r {{ text-align:center; padding:32px; }}
  a {{ color:#5B21B6; font-weight:600; }}
</style>
</head>
<body>
  <div class="r">
    <p>This page has moved.</p>
    <p><a href="{TARGET}">Continue to Website Development</a></p>
  </div>
  <script>window.location.replace("{TARGET}");</script>
</body>
</html>
'''

with open(os.path.join(ROOT, "service-detail.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("service-detail.html -> redirect stub")
