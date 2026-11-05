import math, random, os
from PIL import Image, ImageDraw
from roster import ROSTER
from stats import STATS, TYPE_EN, COUNTRY_EN
import font
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = f'{OUT}/workshop'; os.makedirs(WS, exist_ok=True)
sprite = {c: f().render() for c, _, _, f in ROSTER}

def lerp(a, b, t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

def scene(W, H, seed=1, top=(40,70,130), bot=(150,170,200), clouds=True):
    random.seed(seed)
    img = Image.new('RGBA', (W, H))
    d = ImageDraw.Draw(img)
    bands = 12
    for y in range(H):
        t = min(1, int(y / H * bands) / bands * 1.2)
        d.line([(0, y), (W, y)], fill=lerp(top, bot, t))
    # clouds
    for _ in range(W // 40 if clouds else 0):
        cx, cy = random.randint(0, W), random.randint(4, H // 3)
        for k in range(4):
            r = random.randint(3, 7)
            d.ellipse([cx + k*5 - r, cy - r//2, cx + k*5 + r, cy + r//2], fill=(220, 228, 240))
    # hills layers
    for layer, col, base, amp in ((0, (70, 96, 110), 0.62, 14), (1, (50, 78, 74), 0.72, 10)):
        ph = random.random() * 10
        for x in range(W):
            h = int(H*base + math.sin(x/23+ph)*amp*0.6 + math.sin(x/9+ph*2)*amp*0.25)
            d.line([(x, h), (x, H)], fill=col)
    # ground: grass + dirt
    gy = H - 14
    for x in range(W):
        top_y = gy + (1 if (x//7) % 3 == 0 else 0)
        d.line([(x, top_y), (x, top_y+2)], fill=(64, 160, 52))
        d.point((x, top_y), fill=(110, 200, 70))
        d.line([(x, top_y+3), (x, H)], fill=(120, 80, 52))
    for _ in range(W*2):
        x, y = random.randint(0, W-1), random.randint(gy+4, H-1)
        d.point((x, y), fill=random.choice([(98, 64, 40), (140, 96, 62), (90, 90, 96)]))
    return img

def panel(img, x0, y0, x1, y1):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rectangle([x0, y0, x1, y1], fill=(40, 54, 110, 200), outline=(20, 24, 50, 255))
    d.rectangle([x0+1, y0+1, x1-1, y1-1], outline=(90, 110, 190, 255))
    img.alpha_composite(ov)

def up(img, s): return img.resize((img.width*s, img.height*s), Image.NEAREST)

# ---------- icon 80x80 ----------
ic = scene(80, 80, seed=3, top=(150, 70, 40), bot=(230, 170, 90), clouds=False)
d = ImageDraw.Draw(ic)
d.rectangle([0, 0, 79, 79], outline=(30, 20, 14)); d.rectangle([1, 1, 78, 78], outline=(200, 150, 70))
font.text(ic, (80 - font.width('WW2', 3)) // 2, 5, 'WW2', (255, 214, 90), 3, shadow=(60, 30, 10))
g = sprite['MG42']; ic.alpha_composite(g, ((80 - g.width) // 2, 31))
font.text(ic, (80 - font.width('GUNS', 2)) // 2, 57, 'GUNS', (240, 240, 240), 2, shadow=(30, 30, 40))
d.rectangle([0, 0, 79, 79], outline=(30, 20, 14))
ic.save(f'{OUT}/icon.png')
up(ic, 6).save(f'{OUT}/icon_workshop.png')

# ---------- cover 480x270 -> 1920x1080 ----------
cv = scene(480, 270, seed=7, top=(150, 70, 40), bot=(236, 176, 96), clouds=False)
font.text(cv, (480 - font.width('WW2 GUNS', 6)) // 2, 12, 'WW2 GUNS', (255, 214, 90), 6, shadow=(60, 30, 10))
sub = '42 WEAPONS - 7 NATIONS'
font.text(cv, (480 - font.width(sub, 2)) // 2, 62, sub, (255, 255, 255), 2, shadow=(40, 20, 10))
show = ['Kar98k', 'ThompsonM1928', 'PPSh41', 'MG42', 'Bren', 'StG44', 'ColtM1911', 'LugerP08', 'M1Garand']
for n, k in enumerate(show):
    sp = up(sprite[k], 2)
    cx = 80 + (n % 3) * 160; cy = 110 + (n // 3) * 50
    cv.alpha_composite(sp, (cx - sp.width // 2, cy - sp.height // 2 + 10))
up(cv, 4).save(f'{WS}/01_cover.png')

# ---------- one image per country 480x270 -> 1920x1080 ----------
COL = {'Germany': (110, 116, 100), 'Italy': (40, 120, 60), 'Japan': (180, 40, 40), 'USA': (40, 60, 140),
       'UK': (30, 40, 100), 'USSR': (170, 30, 30), 'France': (40, 70, 160)}
order = ['Germany', 'Italy', 'Japan', 'USA', 'UK', 'USSR', 'France']
for i, c in enumerate(order, start=2):
    im = scene(480, 270, seed=10+i)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 479, 24], fill=COL[c]); d.line([(0, 25), (479, 25)], fill=(20, 20, 20))
    font.text(im, 8, 5, COUNTRY_EN[c].upper(), (255, 255, 255), 2, shadow=(20, 20, 20))
    font.text(im, 480 - font.width('WW2 GUNS', 2) - 8, 5, 'WW2 GUNS', (255, 214, 90), 2, shadow=(20, 20, 20))
    guns = [r for r in ROSTER if r[2] == c]
    for j, (cls, disp, _, _) in enumerate(guns):
        col, row = j % 2, j // 2
        x0, y0 = 6 + col * 236, 31 + row * 79
        panel(im, x0, y0, x0 + 231, y0 + 75)
        st = STATS[cls]
        font.text(im, x0 + 5, y0 + 5, disp.replace('Mk', 'MK'), (255, 255, 255), 1, shadow=(10, 10, 30))
        font.text(im, x0 + 5, y0 + 15, f'DMG {st[2]}', (255, 200, 80), 1)
        font.text(im, x0 + 5, y0 + 24, TYPE_EN[st[1]].upper(), (170, 190, 255), 1)
        sp = up(sprite[cls], 2)
        im.alpha_composite(sp, (x0 + 226 - sp.width, y0 + 72 - sp.height))
    up(im, 4).save(f'{WS}/{i:02d}_{c.lower()}.png')

# full sprite sheet for README
cols = 6; cw, ch = 82, 30
sh = Image.new('RGBA', (cols*cw, 7*ch), (40, 54, 110, 255))
for i, (cls, _, _, _) in enumerate(ROSTER):
    sp = sprite[cls]
    sh.alpha_composite(sp, ((i % cols)*cw + (cw-sp.width)//2, (i//cols)*ch + (ch-sp.height)//2))
up(sh, 3).save(f'{WS}/all_guns.png')
print('done')
