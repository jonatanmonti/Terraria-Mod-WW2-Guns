from pix import G

# ---------- shared parts ----------
def tguard(g, x, y, m='black'):
    g.R(x, y, x, y+2, m); g.R(x, y+2, x+4, y+2, m); g.D(x+4, y+1, m)
    g.D(x+2, y, m, 'd'); g.D(x+2, y+1, m, 'd')

def rifle_stock(g, xw, m, top=8, butt=15, wb=12, pg=False):
    g.P([(0, top-1), (xw, top), (xw, wb), (xw-5, wb), (0, butt)], m)
    g.R(0, top-1, 0, butt, 'black', 'd')
    if pg:
        g.P([(xw-5, wb), (xw, wb), (xw-1, wb+5), (xw-5, wb+5)], m)

def pgrip(g, x, y, m='bake', h=6, w=4, slant=1):
    g.P([(x, y), (x+w, y), (x+w-slant, y+h), (x-slant, y+h)], m)

def bolt_handle(g, x, y, turned=True):
    if turned:
        g.D(x, y, 'metal'); g.D(x+1, y+1, 'metal'); g.R(x+1, y+2, x+2, y+2, 'steel')
    else:
        g.R(x, y, x+2, y, 'metal'); g.D(x+3, y, 'steel')

def rifle(L, m='wood', xw=16, recv=11, fore=None, hg0=None, hg1=None, bands=(), bolt=True,
          bolt_x=None, turned=True, scope=False, mag=0, magx=None, brake=False, bay=0,
          barrel='black', recv_m='black', pg=False, butt=15, thick=False, muzzle=None):
    g = G()
    rifle_stock(g, xw, m, butt=butt, pg=pg)
    rx1 = xw + recv
    fore = fore if fore is not None else L - 9
    g.R(rx1, 9, L, 9 if not thick else 10, barrel)
    g.R(xw, 10, fore, 12, m)
    g.R(xw, 8, rx1, 10, recv_m)
    h0 = hg0 if hg0 is not None else rx1 + 2
    h1 = hg1 if hg1 is not None else fore - 2
    if h1 > h0:
        g.R(h0, 8, h1, 9, m)
    for b in bands:
        g.R(b, 8, b, 12, 'metal')
    g.D(L-1, 8, barrel, 'd')
    g.R(xw+1, 7, xw+2, 7, recv_m)  # rear sight
    if bolt:
        bolt_handle(g, bolt_x if bolt_x is not None else rx1-3, 11, turned)
    tguard(g, xw+1, 13)
    mx = magx if magx is not None else xw+7
    if mag:
        g.R(mx, 13, mx+3, 12+mag, 'black')
    else:
        g.R(mx, 13, mx+3, 13, 'black')
    if scope:
        g.R(xw-1, 4, rx1+5, 5, 'black'); g.D(xw-2, 4, 'black', 'd'); g.D(xw-2, 5, 'black', 'd')
        g.R(rx1+6, 3, rx1+7, 6, 'black'); g.D(xw+2, 6, 'black'); g.D(rx1, 6, 'black')
        g.D(rx1+7, 4, 'steel', 'h')
    if brake:
        g.R(L-2, 8, L+1, 10, 'black')
    if bay:
        g.R(L-4, 11, L+bay, 11, 'steel'); g.D(L+bay+1, 11, 'steel', 'h'); g.R(L-5, 10, L-3, 11, 'black')
    if muzzle:
        muzzle(g, L)
    return g

# ---------- pistols ----------
def auto_pistol(slen=14, sh=3, grip='bake', gw=5, gh=8, gx=1, barrel=0, frame='black', slide='black',
                hammer=True, luger=False, slant=2, guard_x=None):
    g = G()
    y = 4
    g.R(0, y, slen, y+sh, slide)
    if barrel:
        g.R(slen+1, y+1, slen+barrel, y+2, 'black')
        g.D(slen+barrel, y, 'black', 'd')
    g.R(1, y+sh+1, slen-3, y+sh+1, frame)
    gy = y+sh+1
    g.P([(gx, gy), (gx+gw, gy), (gx+gw-slant, gy+gh), (gx-slant, gy+gh)], grip)
    g.R(gx-slant, gy+gh, gx+gw-slant, gy+gh, frame, 'd')
    tguard(g, gx+gw, gy+1, frame)
    g.D(slen-1, y-1, slide, 'd')
    if hammer:
        g.D(-1, y, frame, 'd'); g.D(-2, y-1, frame, 'd')
    if luger:
        g.R(1, y-1, 6, y-1, 'steel'); g.C(3, y-1, 1, 'steel')
    return g

def luger():
    g = G()
    g.R(4, 7, 12, 9, 'black')            # receiver
    g.R(13, 8, 26, 8, 'black'); g.R(13, 7, 26, 7, 'black', 'l')  # long thin barrel
    g.D(26, 6, 'black', 'd')
    g.R(2, 5, 9, 6, 'steel'); g.C(4, 5, 1, 'steel'); g.C(8, 5, 1, 'steel')  # toggle
    g.P([(3, 10), (8, 10), (5, 18), (0, 18)], 'lwood')
    g.R(0, 18, 5, 18, 'black', 'd')
    tguard(g, 8, 10)
    return g

def m1911():
    g = auto_pistol(slen=17, sh=3, grip='wood', gw=5, gh=9, gx=2, slant=2)
    g.R(8, 4, 12, 4, 'black', 'h')  # ejection port shine
    g.D(-1, 8, 'black', 'd')        # grip safety
    return g

def tt33():
    g = auto_pistol(slen=16, sh=3, grip='bake', gw=5, gh=8, gx=2, slant=2)
    for x in (1, 3): g.R(x, 4, x, 7, 'black', 'd')
    g.D(4, 10, 'bake', 'h'); g.D(4, 11, 'bake', 'h')   # star medallion
    return g

def nambu():
    g = G()
    g.R(6, 6, 24, 7, 'black')         # long barrel/receiver
    g.R(3, 5, 14, 8, 'black')
    g.C(1, 6, 1, 'metal')             # cocking knob
    g.P([(4, 9), (10, 9), (7, 18), (1, 18)], 'wood')
    g.R(1, 18, 7, 18, 'black', 'd')
    g.R(9, 9, 12, 9, 'black'); tguard(g, 10, 9)
    g.R(10, 12, 14, 12, 'black'); g.R(13, 9, 14, 12, 'black')   # large wartime guard
    g.D(24, 5, 'black', 'd')
    return g

def beretta34():
    g = auto_pistol(slen=13, sh=3, grip='bake', gw=5, gh=8, gx=1, slant=1)
    g.X(6, 4, 11, 4)                  # open-top slide
    g.R(6, 5, 11, 5, 'steel')         # exposed barrel
    g.D(1, 13, 'black'); g.D(2, 13, 'black')  # finger rest
    return g

def mas35():
    g = auto_pistol(slen=15, sh=3, grip='black', gw=5, gh=8, gx=2, slant=1)
    for x in (1, 2, 3): g.D(x, 5, 'black', 'd')
    g.R(3, 9, 5, 14, 'bake')
    return g

def webley():
    g = G()
    g.R(14, 5, 30, 6, 'black')               # barrel
    g.R(14, 4, 30, 4, 'black', 'l')          # top rib
    g.D(30, 3, 'black', 'd')
    g.R(16, 7, 24, 7, 'black')               # ejector rod housing
    g.R(7, 3, 14, 9, 'black')                # cylinder
    for x in (8, 10, 12): g.R(x, 4, x, 8, 'black', 'd')
    g.R(3, 4, 7, 7, 'black')                 # frame
    g.D(2, 2, 'black', 'd'); g.D(3, 3, 'black')   # hammer
    g.P([(2, 8), (7, 8), (5, 16), (-1, 16)], 'bake')
    g.C(1, 16, 1, 'black')
    tguard(g, 7, 10)
    return g

# ---------- SMGs ----------
def mp40():
    g = G()
    g.R(6, 7, 26, 10, 'black')
    for x in range(8, 24, 3): g.R(x, 10, x+1, 10, 'black', 'd')
    g.R(27, 8, 38, 9, 'black'); g.D(37, 7, 'black', 'd')
    g.R(31, 10, 34, 11, 'black')           # barrel rest
    g.R(0, 8, 6, 8, 'black'); g.R(0, 7, 0, 13, 'black', 'd'); g.L(0, 13, 8, 11, 'black')  # stock
    pgrip(g, 9, 11, 'bake', h=7, w=4, slant=1)
    g.R(15, 11, 19, 13, 'black'); g.R(16, 14, 18, 22, 'black')   # long mag
    g.D(13, 6, 'steel'); g.D(14, 6, 'steel')
    tguard(g, 12, 11)
    return g

def stg44():
    g = G()
    g.R(14, 7, 34, 11, 'black')
    g.R(0, 7, 13, 12, 'wood'); g.R(0, 6, 0, 13, 'black', 'd')
    g.P([(6, 12), (13, 12), (13, 10), (6, 13)], 'wood')
    g.R(35, 8, 50, 9, 'black'); g.R(46, 7, 46, 7, 'black', 'd')
    g.R(49, 7, 51, 10, 'black')            # muzzle nut
    g.R(35, 10, 42, 11, 'black')           # gas tube
    g.R(22, 5, 24, 6, 'black')             # rear sight
    g.D(48, 6, 'black', 'd')
    pgrip(g, 14, 12, 'bake', h=6, w=4, slant=1)
    # curved magazine
    for i in range(10):
        g.R(23+i//3, 12+i, 26+i//3, 12+i, 'black')
    tguard(g, 18, 12)
    return g

def thompson():
    g = G()
    rifle_stock(g, 14, 'wood', top=8, butt=15, wb=12)
    g.R(14, 7, 30, 11, 'black')
    g.R(31, 8, 46, 9, 'black')
    for x in range(32, 40, 2): g.R(x, 7, x, 10, 'black', 'd')   # finned barrel
    g.R(44, 7, 47, 10, 'black')             # compensator
    pgrip(g, 15, 12, 'wood', h=6, w=4, slant=1)
    g.C(25, 16, 4, 'black'); g.C(25, 16, 1, 'black', 'd')     # drum
    g.P([(36, 10), (40, 10), (40, 16), (36, 16)], 'wood')      # vertical foregrip
    g.R(20, 5, 21, 6, 'black')
    tguard(g, 19, 12)
    return g

def sten():
    g = G()
    g.R(0, 7, 0, 14, 'black', 'd'); g.L(0, 9, 10, 9, 'metal'); g.L(0, 13, 10, 10, 'metal')  # skeleton stock
    g.R(10, 7, 30, 9, 'black')
    for x in range(22, 30, 2): g.D(x, 7, 'black', 'd')
    g.R(31, 8, 38, 8, 'black'); g.D(37, 7, 'black', 'd')
    g.R(25, 10, 29, 11, 'metal'); g.R(26, 12, 28, 19, 'black')    # magazine housing + mag (drawn downward for readability)
    g.L(10, 10, 14, 13, 'metal'); g.R(14, 10, 15, 13, 'metal')  # skeleton grip
    g.D(19, 6, 'steel')
    tguard(g, 16, 10)
    return g

def ppsh():
    g = G()
    rifle_stock(g, 18, 'wood', top=8, butt=16, wb=12)
    g.R(18, 8, 30, 12, 'wood')
    g.R(20, 7, 31, 9, 'black')
    g.R(31, 7, 44, 10, 'black')             # perforated jacket
    for x in range(32, 43, 3): g.R(x, 8, x+1, 9, 'black', 'x')
    g.R(43, 6, 45, 10, 'black', 'd')        # slanted compensator
    g.C(27, 17, 5, 'black'); g.C(27, 17, 2, 'black', 'd'); g.R(26, 12, 28, 12, 'black')
    tguard(g, 19, 13)
    return g

def pps43():
    g = G()
    g.R(0, 5, 0, 8, 'metal', 'd'); g.L(0, 6, 9, 7, 'metal'); g.L(0, 8, 9, 10, 'metal')   # folding stock
    g.R(9, 6, 26, 10, 'black')
    g.R(27, 7, 34, 9, 'black')
    for x in (28, 31): g.D(x, 8, 'black', 'x')
    g.R(34, 6, 36, 10, 'black', 'd')
    pgrip(g, 10, 11, 'bake', h=6, w=4, slant=1)
    for i in range(9): g.R(18+i//3, 11+i, 20+i//3, 11+i, 'black')  # curved mag
    tguard(g, 14, 11)
    return g

def mab38():
    g = rifle(44, m='lwood', xw=16, recv=6, fore=34, hg0=99, hg1=0, bands=(), bolt=False,
              mag=10, magx=24, thick=True)
    g.R(18, 7, 34, 10, 'black')
    for x in range(26, 34, 2): g.D(x, 8, 'black', 'x')
    g.R(42, 8, 45, 11, 'black')    # compensator
    g.D(10, 15, 'lwood'); tguard(g, 20, 13)
    return g

def type100():
    g = rifle(42, m='wood', xw=15, recv=8, fore=32, hg0=99, hg1=0, bolt=False)
    g.R(17, 7, 31, 10, 'black')
    for x in range(24, 31, 2): g.D(x, 8, 'black', 'x')
    for i in range(8): g.R(22+i//4, 11+i, 24+i//4, 11+i, 'black')   # curved mag (shown downward)
    g.R(40, 8, 43, 10, 'black')
    return g

def mas38():
    g = G()
    rifle_stock(g, 12, 'wood', top=9, butt=16, wb=13)
    g.R(12, 8, 26, 11, 'black')
    g.R(27, 9, 36, 10, 'black'); g.D(36, 8, 'black', 'd')
    pgrip(g, 13, 12, 'wood', h=6, w=4, slant=1)
    for i in range(8): g.R(20 + i//4, 12+i, 22+i//4, 12+i, 'black')
    tguard(g, 16, 12)
    return g

def fnab43():
    g = mas38()
    g.R(26, 7, 33, 11, 'black')
    for x in range(27, 33, 2): g.D(x, 9, 'black', 'x')
    g.R(34, 8, 37, 11, 'black', 'd')
    return g

def type100_():
    return type100()

# ---------- shotgun ----------
def trenchgun():
    g = rifle(52, m='wood', xw=16, recv=12, fore=30, hg0=99, hg1=0, bolt=False)
    g.R(28, 8, 50, 8, 'black', 'l'); g.R(28, 10, 46, 10, 'black')   # mag tube
    g.R(32, 9, 42, 12, 'wood')                                   # pump slide
    for x in range(30, 48, 2): g.R(x, 6, x, 7, 'metal')          # heat shield
    g.R(30, 7, 48, 7, 'metal')
    g.R(48, 9, 52, 11, 'steel'); g.R(50, 10, 56, 10, 'steel', 'l')   # bayonet lug + bayonet
    g.D(57, 10, 'steel', 'h')
    return g

# ---------- machine guns ----------
def bipod(g, x, y, ln=6):
    g.L(x, y, x-3, y+ln, 'metal'); g.L(x+1, y, x+4, y+ln, 'metal')

def mg42():
    g = G()
    g.P([(0, 6), (12, 8), (12, 12), (0, 14)], 'black')   # bakelite-like stock (black)
    g.R(0, 6, 0, 14, 'black', 'd')
    g.R(12, 7, 28, 11, 'black')
    g.R(29, 6, 48, 11, 'black')                           # barrel jacket
    for x in range(30, 47, 3): g.R(x, 7, x+1, 9, 'black', 'x')
    g.R(31, 10, 46, 10, 'black', 'd')
    g.R(49, 7, 53, 10, 'black')                           # muzzle booster
    g.D(47, 5, 'black', 'd')
    pgrip(g, 14, 12, 'bake', h=6, w=4, slant=1)
    tguard(g, 18, 12)
    g.R(22, 12, 24, 15, 'brass'); g.R(22, 16, 24, 19, 'brass')    # belt
    for y in range(12, 20, 2): g.D(23, y, 'brass', 'd')
    bipod(g, 44, 12, 6)
    return g

def mg34():
    return mg42()

def bren():
    g = G()
    g.P([(0, 7), (14, 9), (14, 12), (6, 12), (0, 15)], 'black')
    g.R(0, 7, 0, 15, 'black', 'd')
    g.R(14, 8, 32, 11, 'black')
    g.R(33, 9, 50, 9, 'black'); g.R(33, 10, 44, 10, 'black')
    g.R(48, 7, 51, 11, 'black')                   # flash hider
    g.R(36, 8, 40, 8, 'black', 'd')               # carry handle base
    g.L(34, 6, 41, 6, 'metal')
    # curved top mag
    for i in range(9):
        g.R(23+i//3, 7-i, 26+i//3, 7-i, 'black')
    pgrip(g, 15, 12, 'wood', h=6, w=4, slant=1)
    tguard(g, 19, 12)
    bipod(g, 44, 11, 6)
    return g

def dp27():
    g = G()
    rifle_stock(g, 16, 'wood', top=8, butt=15, wb=12)
    g.R(16, 8, 30, 11, 'black')
    g.R(31, 7, 46, 11, 'black')
    for x in range(32, 45, 3): g.D(x, 9, 'black', 'x')
    g.R(47, 8, 52, 9, 'black'); g.R(51, 7, 53, 10, 'black', 'd')
    g.R(16, 6, 34, 7, 'black')                    # pan mag (edge-on)
    g.R(18, 5, 32, 5, 'black', 'l'); g.R(23, 4, 27, 4, 'black')
    g.R(18, 12, 21, 13, 'wood'); tguard(g, 21, 12)
    bipod(g, 46, 12, 6)
    return g

def bar():
    g = rifle(58, m='wood', xw=16, recv=18, fore=44, hg0=99, hg1=0, bolt=False, mag=7, magx=24, thick=True)
    g.R(16, 7, 34, 11, 'black')
    g.R(35, 10, 44, 12, 'wood')
    g.R(44, 11, 50, 11, 'black')                  # gas cylinder
    g.R(56, 8, 59, 11, 'black')                   # flash hider
    bipod(g, 54, 12, 6)
    return g

def fm2429():
    g = G()
    rifle_stock(g, 15, 'wood', top=8, butt=15, wb=12)
    g.R(15, 8, 31, 11, 'black')
    g.R(32, 9, 50, 9, 'black'); g.R(32, 10, 40, 11, 'wood')
    g.R(49, 8, 51, 10, 'black')
    for i in range(7): g.R(22+i//4, 7-i, 25+i//4, 7-i, 'black')   # top mag
    pgrip(g, 17, 12, 'wood', h=5, w=3, slant=1)
    tguard(g, 20, 12)     # double trigger feel
    g.D(22, 13, 'black', 'd')
    bipod(g, 46, 10, 7)
    return g

def type96():
    g = G()
    rifle_stock(g, 16, 'wood', top=8, butt=15, wb=12)
    g.R(16, 8, 30, 11, 'black')
    g.R(31, 8, 42, 10, 'black')
    for x in range(31, 42, 2): g.R(x, 7, x, 11, 'black', 'd')   # finned barrel
    g.R(43, 9, 52, 9, 'black'); g.R(51, 8, 53, 10, 'black')
    for i in range(7): g.R(21+i//3, 7-i, 24+i//3, 7-i, 'black')
    g.R(29, 4, 33, 5, 'black')       # offset sight
    pgrip(g, 17, 12, 'wood', h=5, w=3, slant=1)
    tguard(g, 20, 12)
    bipod(g, 44, 11, 6)
    return g

def breda30():
    g = G()
    rifle_stock(g, 16, 'dwood', top=8, butt=15, wb=12)
    g.R(16, 8, 30, 11, 'black')
    g.R(31, 9, 50, 9, 'black'); g.R(31, 10, 38, 10, 'black')
    g.R(23, 12, 30, 14, 'black')     # fixed side magazine (hinged box)
    g.R(30, 7, 32, 12, 'black', 'd')  # barrel handle block
    g.R(49, 8, 51, 10, 'black')
    pgrip(g, 17, 12, 'dwood', h=5, w=3, slant=1)
    tguard(g, 19, 12)
    bipod(g, 44, 10, 7)
    return g

def breda37():
    g = G()
    g.R(0, 7, 2, 8, 'wood'); g.R(0, 11, 2, 12, 'wood'); g.R(2, 7, 4, 12, 'black')  # spade grips
    g.R(4, 6, 24, 12, 'olive')
    g.R(8, 5, 18, 5, 'olive', 'l')
    g.R(25, 8, 54, 10, 'black')
    for x in range(26, 40, 2): g.R(x, 7, x, 11, 'black', 'd')
    g.R(52, 7, 55, 11, 'black')
    g.R(10, 4, 22, 4, 'brass')        # feed strip
    for x in range(11, 22, 2): g.D(x, 3, 'brass', 'l')
    g.L(14, 13, 8, 20, 'metal'); g.L(16, 13, 22, 20, 'metal'); g.R(13, 13, 17, 14, 'metal')  # tripod
    return g

def type92():
    g = G()
    g.R(0, 6, 2, 7, 'wood'); g.R(0, 11, 2, 12, 'wood'); g.R(2, 6, 4, 12, 'black')
    g.R(4, 6, 22, 12, 'olive')
    g.R(23, 7, 40, 11, 'olive')
    for x in range(23, 40, 2): g.R(x, 6, x, 12, 'olive', 'd')     # big cooling fins
    g.R(41, 8, 54, 10, 'black'); g.R(53, 7, 56, 11, 'black')
    g.R(6, 13, 18, 13, 'brass')      # strip
    g.L(14, 13, 8, 20, 'metal'); g.L(16, 13, 22, 20, 'metal')
    g.R(12, 4, 16, 5, 'black')
    return g

def hotchkiss():
    g = G()
    g.R(0, 7, 2, 8, 'wood'); g.R(0, 11, 2, 12, 'wood'); g.R(2, 7, 4, 12, 'black')
    g.R(4, 7, 22, 12, 'brass')
    g.R(23, 8, 32, 11, 'brass')
    for x in range(23, 33, 1): g.R(x, 7, x, 12, 'brass', 'd' if x % 2 else 'l')   # brass doughnut fins
    g.R(33, 9, 54, 9, 'black'); g.R(33, 10, 40, 10, 'black'); g.R(53, 8, 55, 10, 'black')
    g.R(6, 13, 18, 13, 'brass')      # feed strip
    for x in range(7, 18, 2): g.D(x, 14, 'brass', 'l')
    g.L(14, 14, 8, 21, 'metal'); g.L(16, 14, 22, 21, 'metal')
    return g

def boys():
    g = G()
    g.P([(0, 8), (12, 9), (12, 12), (4, 12), (0, 15)], 'black')
    g.R(0, 8, 0, 15, 'black', 'd')
    g.R(2, 10, 6, 11, 'bake')                # cheek pad
    g.R(12, 8, 28, 11, 'black')
    g.R(29, 9, 66, 10, 'black')
    g.R(66, 7, 70, 12, 'black'); g.R(67, 8, 69, 11, 'black', 'x')   # muzzle brake
    for i in range(6): g.R(19, 7-i, 23, 7-i, 'black')                # top mag
    pgrip(g, 13, 12, 'wood', h=6, w=4, slant=1)
    tguard(g, 17, 12)
    bolt_handle(g, 25, 12)
    g.L(56, 11, 54, 18, 'metal'); g.L(57, 11, 60, 18, 'metal')        # bipod
    g.R(3, 16, 4, 18, 'metal')                                       # monopod
    return g

# ---------- rifles (data) ----------
def kar98k():
    return rifle(60, 'wood', xw=17, recv=12, fore=50, hg0=31, hg1=46, bands=(42, 49), turned=True)
def g43():
    g = rifle(58, 'wood', xw=17, recv=12, fore=48, hg0=31, hg1=45, bands=(46,), bolt=False, mag=4)
    g.R(30, 7, 40, 7, 'black')   # gas tube
    g.D(27, 7, 'steel'); g.D(28, 7, 'steel')
    return g
def k98scoped():
    return rifle(60, 'wood', xw=17, recv=12, fore=50, hg0=31, hg1=46, bands=(42, 49), scope=True)
def carcano():
    return rifle(54, 'lwood', xw=16, recv=12, fore=46, hg0=31, hg1=42, bands=(38, 45), turned=False, bay=0)
def carcano_long():
    return rifle(62, 'lwood', xw=16, recv=12, fore=54, hg0=31, hg1=50, bands=(44, 53), turned=False, bay=8)
def arisaka():
    g = rifle(60, 'dwood', xw=17, recv=12, fore=51, hg0=31, hg1=48, bands=(40, 50), turned=False)
    g.R(21, 6, 27, 7, 'metal')   # dust cover
    return g
def type97():
    g = rifle(66, 'dwood', xw=17, recv=12, fore=57, hg0=31, hg1=54, bands=(44, 56), turned=True)
    g.R(30, 4, 40, 5, 'black'); g.D(31, 6, 'black'); g.D(39, 6, 'black'); g.D(41, 4, 'steel', 'h')  # offset scope
    g.L(54, 13, 52, 19, 'metal'); g.L(55, 13, 57, 19, 'metal')
    return g
def mosin():
    return rifle(64, 'wood', xw=17, recv=12, fore=55, hg0=31, hg1=52, bands=(42, 54), turned=False, bay=10)
def svt40():
    g = rifle(56, 'wood', xw=17, recv=12, fore=44, hg0=31, hg1=41, bands=(), bolt=False, mag=5)
    g.R(30, 7, 46, 8, 'metal')
    for x in range(34, 45, 3): g.D(x, 8, 'metal', 'x')   # perforated handguard cover
    g.R(55, 8, 58, 10, 'black')   # muzzle brake
    return g
def m1garand():
    g = rifle(58, 'wood', xw=17, recv=13, fore=47, hg0=33, hg1=46, bands=(), bolt=False)
    g.R(47, 10, 52, 10, 'black')   # gas cylinder
    g.D(25, 7, 'steel'); g.R(26, 7, 28, 7, 'brass')   # en-bloc clip
    g.D(26, 11, 'metal')
    return g
def m1carbine():
    g = rifle(46, 'wood', xw=15, recv=10, fore=38, hg0=27, hg1=36, bands=(36,), bolt=False, mag=4)
    g.D(23, 11, 'steel')
    return g
def springfield():
    return rifle(60, 'wood', xw=17, recv=12, fore=50, hg0=31, hg1=46, bands=(42, 49), pg=False, scope=True)
def enfield():
    g = rifle(58, 'wood', xw=17, recv=12, fore=51, hg0=28, hg1=49, bands=(40, 50), mag=4, magx=22)
    g.R(27, 6, 29, 7, 'black')   # peep sight
    return g
def delisle():
    g = rifle(52, 'wood', xw=17, recv=12, fore=40, hg0=30, hg1=36, bands=(), mag=4, magx=22)
    g.R(30, 7, 52, 11, 'black')   # huge suppressor
    g.R(30, 7, 52, 7, 'black', 'l')
    return g
def mas36():
    g = rifle(54, 'wood', xw=16, recv=12, fore=46, hg0=30, hg1=44, bands=(44,), turned=True)
    g.R(16, 10, 30, 12, 'wood'); g.X(17, 13, 26, 15)  # two-piece stock
    tguard(g, 17, 13)
    g.L(24, 11, 22, 13, 'metal'); g.D(21, 13, 'steel')   # forward-bent bolt
    g.R(50, 11, 58, 11, 'steel')   # spike bayonet
    return g
def lebel():
    g = rifle(66, 'wood', xw=17, recv=12, fore=58, hg0=31, hg1=54, bands=(44, 57), turned=False)
    g.R(30, 11, 56, 11, 'black', 'd')   # tube magazine
    g.R(62, 10, 74, 10, 'steel'); g.D(75, 10, 'steel', 'h')   # Rosalie bayonet
    return g
def berthier():
    return rifle(50, 'wood', xw=16, recv=12, fore=44, hg0=30, hg1=42, bands=(41,), mag=4, magx=21)
