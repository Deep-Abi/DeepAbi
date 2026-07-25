"""
Generates original abstract brand illustrations for the DeepAbi site.
No photography is available in this environment, so every "photo" placeholder
is an original geometric/gradient illustration built programmatically and
rendered in PNG -> WebP -> JPEG so <picture> fallback chains are real, valid
files. Each function writes directly into the page-scoped asset folder a real
photograph would occupy (assets/images/<page>/<format>/<name>.<ext>), so
swapping in real photography later is a same-path file replace.
"""
import math
import random
import os as _os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

random.seed(7)

# ---- Luxury Enterprise palette ----
NAVY = (8, 31, 77)           # Primary — Royal Midnight #081F4D
NAVY2 = (5, 21, 48)           # Deeper navy for gradient depth
CYAN = (0, 217, 200)          # Secondary — Aqua Emerald #00D9C8
VIOLET = (139, 92, 246)       # Accent — Royal Purple #8B5CF6
MINT = (16, 185, 129)         # Utility green for success/checkmarks #10B981
GOLD = (255, 176, 0)          # Highlight — Premium Gold #FFB000
WHITE = (255, 255, 255)
SLATE = (100, 116, 139)

ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
ASSETS = _os.path.join(ROOT, "assets", "images")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        col = lerp(top, bottom, t)
        for x in range(w):
            px[x, y] = col
    return img


def radial_glow(img, center, radius, color, alpha=140):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    cx, cy = center
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=color + (alpha,))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius / 2))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"), (0, 0))
    return img


def add_grid(img, step=48, color=(255, 255, 255, 18)):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    w, h = img.size
    for x in range(0, w, step):
        d.line([(x, 0), (x, h)], fill=color, width=1)
    for y in range(0, h, step):
        d.line([(0, y), (w, y)], fill=color, width=1)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def add_nodes(img, n=26, colors=(CYAN, VIOLET, MINT)):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    w, h = img.size
    pts = [(random.randint(int(w*0.05), int(w*0.95)), random.randint(int(h*0.05), int(h*0.95))) for _ in range(n)]
    for i, p in enumerate(pts):
        for q in pts[i+1:]:
            dist = math.hypot(p[0]-q[0], p[1]-q[1])
            if dist < w * 0.16:
                d.line([p, q], fill=CYAN + (40,), width=1)
    for p in pts:
        c = random.choice(colors)
        r = random.randint(3, 6)
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=c + (230,))
        d.ellipse([p[0]-r-4, p[1]-r-4, p[0]+r+4, p[1]+r+4], outline=c + (60,), width=2)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def rounded_panel(img, box, radius, color, alpha=60, outline=None):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rounded_rectangle(box, radius=radius, fill=color + (alpha,), outline=(outline or color) + (140,), width=2)
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")


def save_all(img, page_folder, name, w=None, h=None):
    """page_folder e.g. 'home', 'services', 'about', 'projects', 'technology', 'testimonials'."""
    if w and h:
        img = img.resize((w, h), Image.LANCZOS)
    for ext, pil_fmt, kwargs in [
        ("png", "PNG", {"optimize": True}),
        ("webp", "WEBP", {"quality": 82, "method": 6}),
        ("jpg", "JPEG", {"quality": 82, "optimize": True}),
    ]:
        out_dir = _os.path.join(ASSETS, page_folder, ext)
        _os.makedirs(out_dir, exist_ok=True)
        target = img.convert("RGB") if pil_fmt == "JPEG" else img
        target.save(_os.path.join(out_dir, f"{name}.{ext}"), pil_fmt, **kwargs)


def hero_illustration():
    """Premium typographic composition for the hero: DEEP and ABI rendered
    large, connected by a glowing link, each with its full-form meaning
    beneath, on a soft-glowing gradient field with floating particles.
    Elegant and minimal rather than flashy — static base; CSS adds the
    animated pulse/glow layer on top once placed in the page."""
    w, h = 1200, 1100
    img = vertical_gradient((w, h), NAVY, NAVY2)
    img = radial_glow(img, (w*0.28, h*0.24), 380, CYAN, 65)
    img = radial_glow(img, (w*0.75, h*0.78), 380, VIOLET, 65)
    img = radial_glow(img, (w*0.5, h*0.5), 460, GOLD, 22)
    img = add_grid(img, 60)

    base = img.convert("RGBA")

    try:
        f_word = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 128)
        f_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    except Exception:
        f_word = f_sub = ImageFont.load_default()

    def centered_text(draw_target, text, font, cy, fill, tracking=0):
        # crude letter-spacing: draw glyph by glyph
        widths = [draw_target.textbbox((0, 0), ch, font=font)[2] for ch in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = w/2 - total/2
        for ch, cwidth in zip(text, widths):
            draw_target.text((x, cy), ch, font=font, fill=fill, anchor="lm")
            x += cwidth + tracking
        return total

    # ---- Glow layer behind the big words (soft blurred duplicate) ----
    glow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    deep_y = h*0.27
    abi_y = h*0.68
    centered_text(gd, "DEEP", f_word, deep_y, CYAN + (255,), tracking=14)
    centered_text(gd, "ABI", f_word, abi_y, VIOLET + (255,), tracking=14)
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(18))
    base = Image.alpha_composite(base, glow_layer)

    # ---- Sharp text layer ----
    text_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    td = ImageDraw.Draw(text_layer)
    centered_text(td, "DEEP", f_word, deep_y, WHITE + (255,), tracking=14)
    centered_text(td, "ABI", f_word, abi_y, WHITE + (255,), tracking=14)

    # Subtitles beneath each word
    sub1 = "DRIVING ECONOMIC EMPOWERMENT FOR PEOPLE"
    sub2 = "AMBITION BEYOND IMAGINATION"
    centered_text(td, sub1, f_sub, deep_y + 92, (203, 213, 225, 235), tracking=3)
    centered_text(td, sub2, f_sub, abi_y + 92, (203, 213, 225, 235), tracking=3)

    # Connector between the two words: a slim glowing vertical line with a node
    conn_x = w/2
    conn_top = deep_y + 130
    conn_bottom = abi_y - 46
    td.line([(conn_x, conn_top), (conn_x, conn_bottom)], fill=GOLD + (170,), width=2)
    mid_y = (conn_top + conn_bottom) / 2
    for r, alpha in [(16, 40), (9, 120), (4, 255)]:
        td.ellipse([conn_x-r, mid_y-r, conn_x+r, mid_y+r], fill=GOLD + (alpha,))

    base = Image.alpha_composite(base, text_layer)

    # ---- Floating particles + fine highlight dots ----
    particle_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    pd = ImageDraw.Draw(particle_layer)
    random.seed(58)
    for _ in range(30):
        px = random.uniform(w*0.04, w*0.96)
        py = random.uniform(h*0.04, h*0.96)
        rr = random.uniform(1.2, 3)
        col = random.choice([CYAN, VIOLET, GOLD, WHITE])
        pd.ellipse([px-rr, py-rr, px+rr, py+rr], fill=col + (random.randint(90, 200),))
    base = Image.alpha_composite(base, particle_layer)

    # Thin elegant frame corners (minimal, premium)
    frame_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    fd = ImageDraw.Draw(frame_layer)
    m = 46
    L = 44
    for (x0, y0, dx, dy) in [(m, m, 1, 1), (w-m, m, -1, 1), (m, h-m, 1, -1), (w-m, h-m, -1, -1)]:
        fd.line([(x0, y0), (x0+L*dx, y0)], fill=CYAN + (90,), width=2)
        fd.line([(x0, y0), (x0, y0+L*dy)], fill=CYAN + (90,), width=2)
    base = Image.alpha_composite(base, frame_layer)

    img = base.convert("RGB")
    save_all(img, "home", "deep-abi-concept", 1200, 1100)


def responsive_devices_showcase():
    """A large, polished multi-device mockup (desktop + tablet + mobile)
    for the 'Built for Every Screen' section — sized as a genuine visual
    focal point rather than a small supporting graphic."""
    w, h = 1400, 950
    img = vertical_gradient((w, h), (248, 250, 252), (255, 255, 255))
    img = radial_glow(img, (w*0.5, h*0.5), 480, CYAN, 40)
    img = radial_glow(img, (w*0.85, h*0.15), 260, VIOLET, 35)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # Desktop frame (back, large, centered)
    dx0, dy0, dx1, dy1 = w*0.16, h*0.14, w*0.86, h*0.70
    d.rounded_rectangle([dx0, dy0, dx1, dy1], radius=26, fill=NAVY+(255,), outline=CYAN+(160,), width=2)
    d.rounded_rectangle([dx0+16, dy0+52, dx1-16, dy1-16], radius=14, fill=(255, 255, 255, 255))
    # desktop "browser" chrome
    d.rounded_rectangle([dx0+16, dy0+16, dx1-16, dy0+50], radius=10, fill=(15, 23, 42, 255))
    for i, c in enumerate([(239, 68, 68), (245, 158, 11), MINT]):
        d.ellipse([dx0+34+i*22, dy0+26, dx0+46+i*22, dy0+38], fill=c+(255,))
    # desktop content mock
    cix0, ciy0 = dx0+50, dy0+90
    d.rounded_rectangle([cix0, ciy0, cix0+260, ciy0+34], radius=8, fill=NAVY+(255,))
    d.rounded_rectangle([cix0, ciy0+56, cix0+420, ciy0+80], radius=6, fill=(203, 213, 225, 255))
    d.rounded_rectangle([cix0, ciy0+96, cix0+180, ciy0+130], radius=10, fill=VIOLET+(255,))
    gridw = (dx1-16-cix0) 
    for i in range(3):
        gx0 = cix0 + i * (gridw/3) + 10
        d.rounded_rectangle([gx0, ciy0+170, gx0+gridw/3-24, ciy0+300], radius=14, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255), width=2)
        d.rounded_rectangle([gx0+14, ciy0+186, gx0+gridw/3-38, ciy0+230], radius=10, fill=CYAN+(45,))

    # Tablet frame (left-front, overlapping)
    tx0, ty0, tx1, ty1 = w*0.05, h*0.52, w*0.30, h*0.90
    d.rounded_rectangle([tx0, ty0, tx1, ty1], radius=22, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=3)
    d.rounded_rectangle([tx0+14, ty0+14, tx1-14, ty1-14], radius=12, fill=(248, 250, 252, 255))
    d.rounded_rectangle([tx0+24, ty0+30, tx1-24, ty0+62], radius=8, fill=VIOLET+(255,))
    d.rounded_rectangle([tx0+24, ty0+80, tx1-24, ty0+180], radius=10, fill=(226, 232, 240, 255))
    d.rounded_rectangle([tx0+24, ty0+196, tx1-24, ty0+296], radius=10, fill=CYAN+(35,))

    # Mobile frame (right-front, overlapping)
    mx0, my0, mx1, my1 = w*0.74, h*0.50, w*0.94, h*0.94
    d.rounded_rectangle([mx0, my0, mx1, my1], radius=32, fill=NAVY+(255,), outline=GOLD+(180,), width=3)
    d.rounded_rectangle([mx0+10, my0+34, mx1-10, my1-18], radius=20, fill=(255, 255, 255, 255))
    d.rounded_rectangle([mx0+24, my0+56, mx1-24, my0+90], radius=8, fill=GOLD+(255,))
    for i in range(3):
        yy = my0 + 112 + i*46
        d.rounded_rectangle([mx0+24, yy, mx1-24, yy+30], radius=8, fill=(226, 232, 240, 255))

    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    save_all(img, "home", "responsive-devices-showcase", 1400, 950)


def team_collaboration():
    w, h = 1400, 950
    img = vertical_gradient((w, h), (248, 250, 252), (226, 232, 240))
    img = radial_glow(img, (w*0.15, h*0.2), 300, VIOLET, 40)
    img = radial_glow(img, (w*0.9, h*0.8), 340, CYAN, 40)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    cols, rows = 6, 4
    pad = 60
    cw = (w - pad*2) / cols
    ch = (h - pad*2) / rows
    random.seed(3)
    for r in range(rows):
        for c in range(cols):
            if random.random() < 0.55:
                x0 = pad + c*cw + 8
                y0 = pad + r*ch + 8
                x1 = x0 + cw - 16
                y1 = y0 + ch - 16
                tone = random.choice([NAVY, VIOLET, CYAN, MINT, SLATE])
                d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=tone + (26,), outline=tone + (90,), width=2)
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    save_all(img, "about", "team-collaboration", 1400, 950)


def service_visual(page_folder, name, primary, secondary, icon_seed):
    w, h = 1000, 760
    img = vertical_gradient((w, h), (248, 250, 252), (255, 255, 255))
    img = radial_glow(img, (w*0.8, h*0.15), 260, primary, 55)
    img = radial_glow(img, (w*0.15, h*0.85), 220, secondary, 45)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    random.seed(icon_seed)
    cx, cy = w*0.5, h*0.5
    d.rounded_rectangle([cx-180, cy-130, cx+180, cy+130], radius=32, fill=NAVY + (235,))
    for i in range(3):
        yy = cy - 70 + i*55
        wbar = random.randint(120, 260)
        col = [CYAN, VIOLET, GOLD][i % 3]
        d.rounded_rectangle([cx-150, yy, cx-150+wbar, yy+18], radius=9, fill=col + (255,))
    d.ellipse([cx+90, cy-110, cx+150, cy-50], outline=CYAN + (255,), width=4)
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    save_all(img, page_folder, name, 1000, 760)


def project_mock(name, seed, accent):
    w, h = 1100, 760
    img = vertical_gradient((w, h), (255, 255, 255), (248, 250, 252))
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rounded_rectangle([40, 40, w-40, h-40], radius=22, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=2)
    d.rounded_rectangle([40, 40, w-40, 100], radius=22, fill=(248, 250, 252, 255))
    for i, c in enumerate([(239, 68, 68), (245, 158, 11), MINT]):
        d.ellipse([70+i*24, 62, 82+i*24, 74], fill=c + (255,))
    random.seed(seed)
    d.rounded_rectangle([70, 130, 260, 160], radius=8, fill=NAVY + (255,))
    for i in range(4):
        d.rounded_rectangle([300+i*140, 135, 400+i*140, 155], radius=6, fill=(203, 213, 225, 255))
    d.rounded_rectangle([70, 190, w-70, 420], radius=24, fill=accent + (28,), outline=accent + (140,), width=2)
    d.rounded_rectangle([110, 240, 480, 280], radius=8, fill=NAVY + (255,))
    d.rounded_rectangle([110, 300, 620, 330], radius=6, fill=(148, 163, 184, 255))
    d.rounded_rectangle([110, 360, 260, 396], radius=12, fill=accent + (255,))
    for i in range(3):
        x0 = 70 + i * ((w-140-40)/3 + 20)
        d.rounded_rectangle([x0, 450, x0 + (w-140-40)/3, 660], radius=18, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=2)
        d.rounded_rectangle([x0+20, 470, x0+(w-140-40)/3-20, 540], radius=12, fill=accent + (35,))
        d.rounded_rectangle([x0+20, 560, x0+(w-140-40)/3-30, 580], radius=6, fill=(148, 163, 184, 255))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    save_all(img, "projects", name, 1100, 760)


def featured_project():
    w, h = 1400, 950
    img = vertical_gradient((w, h), NAVY, (10, 42, 99))
    img = radial_glow(img, (w*0.85, h*0.2), 400, MINT, 90)
    img = radial_glow(img, (w*0.1, h*0.85), 340, VIOLET, 70)
    img = add_grid(img, 60)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rounded_rectangle([w*0.30, h*0.28, w*0.70, h*0.62], radius=36, fill=(255, 255, 255, 245), outline=CYAN + (200,), width=3)
    cx0, cy0 = w*0.34, h*0.34
    d.rounded_rectangle([cx0, cy0, cx0+340, cy0+200], radius=20, fill=NAVY + (255,))
    d.rounded_rectangle([cx0+24, cy0+130, cx0+90, cy0+150], radius=6, fill=CYAN + (255,))
    d.rounded_rectangle([cx0+24, cy0+34, cx0+70, cy0+58], radius=6, fill=GOLD + (255,))
    for i in range(3):
        d.ellipse([cx0+250-i*18, cy0+30, cx0+280-i*18, cy0+60], fill=[VIOLET, CYAN, MINT][i] + (220,))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    save_all(img, "projects", "featured-cardsession-platform", 1400, 950)


def tech_illustration():
    w, h = 1200, 900
    img = vertical_gradient((w, h), (248, 250, 252), (255, 255, 255))
    img = radial_glow(img, (w*0.5, h*0.5), 380, CYAN, 40)
    img = add_grid(img, 52)
    img = add_nodes(img, n=34)
    save_all(img, "technology", "technology-stack-network", 1200, 900)


def avatar(name, initials, seed, tone):
    w = h = 240
    img = Image.new("RGB", (w, h), tone)
    d = ImageDraw.Draw(img)
    random.seed(seed)
    d.ellipse([-40, -40, w+40, h+40], fill=tone)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([w*0.15, h*0.55, w*0.85, h*1.25], fill=(255, 255, 255, 235))
    od.ellipse([w*0.30, h*0.18, w*0.70, h*0.58], fill=(255, 255, 255, 235))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except Exception:
        font = ImageFont.load_default()
    d.rectangle([0, h-34, w, h], fill=NAVY)
    bbox = d.textbbox((0, 0), initials, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    d.text(((w-tw)/2, h-34+(34-th)/2-4), initials, font=font, fill=WHITE)
    save_all(img, "testimonials", name, 240, 240)


def services_hero_illustration():
    """Professional illustration for the Services hero — a set of connected
    service modules (cards/icons) orbiting a central hub, symbolizing the
    full-lifecycle service offering, on the dark navy hero background."""
    w, h = 1200, 1000
    img = vertical_gradient((w, h), NAVY, NAVY2)
    img = radial_glow(img, (w*0.5, h*0.42), 420, VIOLET, 70)
    img = radial_glow(img, (w*0.75, h*0.75), 300, CYAN, 60)
    img = add_grid(img, 56)

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    cx, cy = w*0.5, h*0.44

    # central hub
    for r, alpha in [(64, 35), (46, 80), (30, 200)]:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=CYAN+(alpha,))
    d.ellipse([cx-16, cy-16, cx+16, cy+16], fill=WHITE+(255,))

    # service module cards orbiting the hub
    random.seed(77)
    labels_colors = [VIOLET, CYAN, GOLD, MINT, VIOLET, CYAN]
    n = 6
    for i in range(n):
        ang = (i / n) * 2 * math.pi - math.pi/2
        r = 260
        px = cx + math.cos(ang) * r
        py = cy + math.sin(ang) * r * 0.8
        d.line([(cx, cy), (px, py)], fill=CYAN+(50,), width=1)
        col = labels_colors[i]
        cw_, ch_ = 108, 78
        d.rounded_rectangle([px-cw_/2, py-ch_/2, px+cw_/2, py+ch_/2], radius=14, fill=(255, 255, 255, 245), outline=col+(200,), width=2)
        d.rounded_rectangle([px-cw_/2+12, py-ch_/2+14, px-cw_/2+40, py-ch_/2+30], radius=6, fill=col+(255,))
        d.rounded_rectangle([px-cw_/2+12, py-ch_/2+40, px+cw_/2-12, py-ch_/2+50], radius=4, fill=(203, 213, 225, 255))
        d.rounded_rectangle([px-cw_/2+12, py-ch_/2+56, px+cw_/2-30, py-ch_/2+66], radius=4, fill=(203, 213, 225, 255))

    # ascending small bars (growth) bottom-left, echoing the hero motif subtly
    base_y = h*0.90
    for i, hh in enumerate([50, 80, 110, 150]):
        x0 = w*0.08 + i*38
        col = [VIOLET, CYAN, GOLD, MINT][i]
        d.rounded_rectangle([x0, base_y-hh, x0+26, base_y], radius=6, fill=col+(160,))

    # floating particles
    for _ in range(22):
        px = random.uniform(w*0.05, w*0.95)
        py = random.uniform(h*0.05, h*0.95)
        rr = random.uniform(1.2, 3)
        col = random.choice([CYAN, VIOLET, GOLD, WHITE])
        d.ellipse([px-rr, py-rr, px+rr, py+rr], fill=col+(random.randint(80, 190),))

    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    save_all(img, "services", "services-hero-illustration", 1200, 1000)


def og_social_banner():
    w, h = 1200, 630
    img = vertical_gradient((w, h), NAVY, (10, 42, 99))
    img = radial_glow(img, (w*0.85, h*0.15), 340, CYAN, 100)
    img = radial_glow(img, (w*0.1, h*0.9), 280, VIOLET, 80)
    img = add_grid(img, 48)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    try:
        f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
        f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except Exception:
        f1 = f2 = ImageFont.load_default()
    d.text((80, 210), "DeepAbi", font=f1, fill=WHITE + (255,))
    d.text((80, 300), "Driving Economic Empowerment Through Technology", font=f2, fill=(203, 213, 225, 255))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    for ext, pil_fmt, kwargs in [
        ("png", "PNG", {"optimize": True}),
        ("webp", "WEBP", {"quality": 82, "method": 6}),
        ("jpg", "JPEG", {"quality": 82, "optimize": True}),
    ]:
        out_dir = _os.path.join(ASSETS, "backgrounds")
        _os.makedirs(out_dir, exist_ok=True)
        target = img.convert("RGB") if pil_fmt == "JPEG" else img
        target.save(_os.path.join(out_dir, f"og-social-banner.{ext}"), pil_fmt, **kwargs)


def favicon():
    w = h = 512
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w, h], radius=112, fill=NAVY + (255,))
    cx, cy = w/2, h/2
    d.ellipse([cx-150, cy-150, cx-90, cy-90], fill=CYAN + (255,))
    d.ellipse([cx+90, cy-150, cx+150, cy-90], fill=VIOLET + (255,))
    d.ellipse([cx-150, cy+90, cx-90, cy+150], fill=VIOLET + (255,))
    d.ellipse([cx+90, cy+90, cx+150, cy+150], fill=MINT + (255,))
    d.ellipse([cx-36, cy-36, cx+36, cy+36], fill=CYAN + (255,))
    for (x1, y1) in [(-120, -120), (120, -120), (-120, 120), (120, 120)]:
        d.line([(cx, cy), (cx+x1, cy+y1)], fill=CYAN + (120,), width=6)
    out_dir = _os.path.join(ASSETS, "logos")
    _os.makedirs(out_dir, exist_ok=True)
    img.save(_os.path.join(out_dir, "favicon-512.png"))
    for size in [16, 32, 180, 192]:
        img.resize((size, size), Image.LANCZOS).save(_os.path.join(out_dir, f"favicon-{size}.png"))
    icon_sizes = [(16, 16), (32, 32), (48, 48)]
    img.resize((256, 256), Image.LANCZOS).save(_os.path.join(out_dir, "favicon.ico"), sizes=icon_sizes)


if __name__ == "__main__":
    # NOTE: hero_illustration(), responsive_devices_showcase(), three of the
    # service_visual() calls, and all four project_mock() calls previously
    # generated placeholder art for slots that are now filled with real
    # client-provided photography/screenshots (see assets/images/{home,
    # services,projects}/ — landing_page.*, corporate_websites.*, desktop.*,
    # tablet_portrait.*, mobile_portrait.*, etc.). Those functions are left
    # defined above as fallback generators (useful if a real asset is ever
    # removed and needs a placeholder again) but are no longer called here,
    # so re-running this script won't regenerate now-unused dead files.
    services_hero_illustration()
    team_collaboration()
    service_visual("services", "website-development-workspace", VIOLET, CYAN, 1)
    featured_project()
    tech_illustration()
    avatar("client-avatar-1", "AR", 21, (30, 41, 59))
    avatar("client-avatar-2", "PK", 22, (76, 29, 149))
    avatar("client-avatar-3", "SN", 23, (12, 74, 110))
    avatar("client-avatar-4", "MJ", 24, (6, 78, 59))
    # avatar-5/avatar-6 removed: only 4 testimonial slides are used on the site currently.
    og_social_banner()
    favicon()
    print("done")
