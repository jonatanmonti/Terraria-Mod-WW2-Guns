"""Tiny pixel-art engine: draw material shapes, then auto-shade + outline Terraria style."""
from PIL import Image, ImageDraw

PAL = {
    # mat: (highlight, light, mid, dark, outline)
    'wood':   ((214,150,88),(184,120,66),(146,88,46),(106,60,30),(52,28,14)),
    'dwood':  ((168,104,62),(136,82,46),(104,60,34),(74,40,22),(38,20,10)),
    'lwood':  ((232,190,122),(206,160,98),(172,126,72),(132,92,50),(66,44,22)),
    'metal':  ((206,214,224),(160,168,182),(116,122,138),(80,84,100),(30,30,40)),
    'black':  ((150,156,172),(104,108,124),(70,72,86),(46,46,58),(18,18,24)),
    'brass':  ((255,236,150),(236,198,96),(198,154,58),(150,108,36),(70,46,14)),
    'bake':   ((196,104,76),(160,76,54),(122,52,38),(86,34,26),(40,14,10)),
    'olive':  ((170,178,112),(138,146,88),(104,110,64),(74,78,44),(34,36,18)),
    'steel':  ((230,234,240),(190,196,206),(146,152,166),(104,108,122),(36,36,46)),
}
TONE = {'h':0,'l':1,'m':2,'d':3,'x':4}

class G:
    def __init__(self, w=100, h=48):
        self.w, self.h = w, h
        self.px = {}
    def R(self, x0, y0, x1, y1, m, t=None):
        for y in range(min(y0,y1), max(y0,y1)+1):
            for x in range(min(x0,x1), max(x0,x1)+1):
                self.px[(x,y)] = (m,t)
    def D(self, x, y, m, t=None):
        self.px[(x,y)] = (m,t)
    def P(self, pts, m, t=None):
        O = 20
        img = Image.new('1', (self.w+2*O, self.h+2*O), 0)
        ImageDraw.Draw(img).polygon([(x+O,y+O) for x,y in pts], fill=1, outline=1)
        for y in range(img.height):
            for x in range(img.width):
                if img.getpixel((x,y)):
                    self.px[(x-O,y-O)] = (m,t)
    def L(self, x0, y0, x1, y1, m, t=None):
        dx, dy = abs(x1-x0), -abs(y1-y0)
        sx, sy = (1 if x0<x1 else -1), (1 if y0<y1 else -1)
        err = dx+dy
        while True:
            self.px[(x0,y0)] = (m,t)
            if x0==x1 and y0==y1: break
            e2 = 2*err
            if e2 >= dy: err += dy; x0 += sx
            if e2 <= dx: err += dx; y0 += sy
    def C(self, cx, cy, r, m, t=None):
        for y in range(cy-r, cy+r+1):
            for x in range(cx-r, cx+r+1):
                if (x-cx)**2+(y-cy)**2 <= r*r+r*0.8:
                    self.px[(x,y)] = (m,t)
    def X(self, x0, y0, x1, y1):
        for y in range(min(y0,y1), max(y0,y1)+1):
            for x in range(min(x0,x1), max(x0,x1)+1):
                self.px.pop((x,y), None)

    def render(self):
        px = self.px
        out = {}
        for (x,y),(m,t) in px.items():
            if t is None:
                up = px.get((x,y-1)); dn = px.get((x,y+1))
                if up is None:
                    t = 'l'
                elif dn is None:
                    t = 'd'
                elif up[0] != m:
                    t = 'l'
                else:
                    t = 'm'
            out[(x,y)] = PAL[m][TONE[t]]
        # outline
        for (x,y),(m,t) in list(px.items()):
            for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if (nx,ny) not in px and (nx,ny) not in out:
                    out[(nx,ny)] = PAL[m][4]
        xs = [p[0] for p in out]; ys = [p[1] for p in out]
        x0, y0 = min(xs), min(ys)
        W, H = max(xs)-x0+1, max(ys)-y0+1
        img = Image.new('RGBA', (W, H), (0,0,0,0))
        for (x,y),c in out.items():
            img.putpixel((x-x0, y-y0), c+(255,))
        return img
