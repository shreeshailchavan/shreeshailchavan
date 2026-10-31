# Shared design kit for the v6 README: palette, fonts, text metrics, window chrome.
import base64, json, os
from fontTools.ttLib import TTFont
HERE = os.path.dirname(os.path.abspath(__file__))
BG="#15181d"; SURF="#1c2128"; SURF2="#22272e"; CELL="#22272e"; BD="#30363d"; FG="#eff6fc"; TXT="#d6dde4"; MUT="#9ea7b0"; DIM="#5c636c"
PEACH="#fac58e"; ORANGE="#c36219"; RUST="#974c17"; YEL="#e2cf50"
FONTS = {("Bricolage",800):"bricolage-grotesque-latin-800-normal.woff2",("Bricolage",700):"bricolage-grotesque-latin-700-normal.woff2",
         ("Instrument",400):"instrument-sans-latin-400-normal.woff2",("Instrument",500):"instrument-sans-latin-500-normal.woff2",
         ("Instrument",600):"instrument-sans-latin-600-normal.woff2"}
_m = {}
def _font(fam, wt):
    k = (fam, wt)
    if k not in _m:
        f = TTFont(os.path.join(HERE, "fonts", FONTS[k])); _m[k] = (f.getBestCmap(), f["hmtx"].metrics, f["head"].unitsPerEm)
    return _m[k]
def tw(text, size, fam="Instrument", wt=400, ls=0):
    cmap, hm, upm = _font(fam, wt); w = 0
    for ch in text:
        g = cmap.get(ord(ch)); w += hm[g][0] if g else upm*0.5
    return w*size/upm + ls*len(text)
def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def faces(used):
    out = ""
    for (fam, wt) in used:
        b = base64.b64encode(open(os.path.join(HERE, "fonts", FONTS[(fam, wt)]), "rb").read()).decode()
        out += f"@font-face{{font-family:'{fam}';font-weight:{wt};src:url(data:font/woff2;base64,{b}) format('woff2')}}"
    return out
ALL = list(FONTS.keys())
def svg(W, H, body, css="", bg=True, used=ALL):
    style = faces(used) + "text{white-space:pre;font-family:'Instrument',sans-serif}.d{font-family:'Bricolage',sans-serif}" \
            ".blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{50%{opacity:0}}" + css
    back = f'<rect width="{W}" height="{H}" fill="{BG}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>{style}</style>{back}{body}</svg>'
def text(x, y, t, size, fill=TXT, wt=400, fam="Instrument", anchor="start", ls=0, extra=""):
    cls = ' class="d"' if fam == "Bricolage" else ""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    return f'<text{cls} x="{x}" y="{y}" font-size="{size}" font-weight="{wt}" fill="{fill}"{a}{l}{extra}>{esc(t)}</text>'
def window(x, y, w, h, title, right=None, right_col=MUT, fill=SURF):
    s = f'<g transform="translate({x},{y})"><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="{fill}" stroke="{BD}"/>'
    s += f'<path d="M1 36.5H{w-1}" stroke="{BD}"/>'
    for i, c in enumerate([RUST, ORANGE, YEL]): s += f'<rect x="{16+i*18}" y="13" width="10" height="10" rx="2" fill="{c}"/>'
    s += text(w/2, 23, title, 13, MUT, 500, anchor="middle")
    if right: s += text(w-16, 23, right, 12.5, right_col, 500, anchor="end")
    return s + "</g>"

# hand-drawn 24x24 stroke icons for tools without a brand logo
CUSTOM = {
 "sql": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
 "api": '<path d="M8 3C5 3 5 5 5 8s-2 4-2 4 2 1 2 4 0 5 3 5"/><path d="M16 3c3 0 3 2 3 5s2 4 2 4-2 1-2 4 0 5-3 5"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "vector": '<circle cx="5" cy="19" r="2"/><path d="M6.5 17.5L19 5M6.5 18.5L21 14M5.5 17L9 3"/><path d="M15 5h4v4"/>',
 "tune": '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
 "queue": '<rect x="3" y="4" width="18" height="4" rx="1"/><rect x="3" y="10" width="18" height="4" rx="1"/><rect x="3" y="16" width="18" height="4" rx="1"/>',
 "cloud": '<path d="M7 18h10a4 4 0 0 0 .5-8A6 6 0 0 0 6 9a4.5 4.5 0 0 0 1 9z"/>',
 "orbit": '<ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(-30 12 12)"/><circle cx="12" cy="12" r="3"/>',
 "plug": '<path d="M9 2v5M15 2v5M6 7h12v4a6 6 0 0 1-12 0z"/><path d="M12 17v5"/>',
 "play": '<circle cx="12" cy="12" r="10"/><path d="M10 8l6 4-6 4z"/>',
 "check": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 9l2 2 4-4M8 16h8"/>',
 "nodes": '<circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><path d="M7 6h10M6 8l5 8M18 8l-5 8"/>',
 "tree": '<circle cx="12" cy="4" r="2"/><circle cx="6" cy="13" r="2"/><circle cx="18" cy="13" r="2"/><circle cx="3" cy="21" r="1.5"/><circle cx="9" cy="21" r="1.5"/><path d="M11 6l-4 5M13 6l4 5M5 15l-1.5 4.5M7 15l1.5 4.5"/>',
 "cube": '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
 "term": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M6 9l3 3-3 3M12 15h5"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2c3 3 3 17 0 20M12 2c-3 3-3 17 0 20"/>',
 "shield": '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/><path d="M9 12l2 2 4-4"/>',
}
ICONS = json.load(open(os.path.join(HERE, "icons.json")))
def icon(name, x, y, size, fill=PEACH):
    if name == "linkedin":
        return (f'<g transform="translate({x},{y})"><rect width="{size}" height="{size}" rx="{size*.18}" fill="{fill}"/>'
                f'<text x="{size*.18}" y="{size*.8}" font-size="{size*.72}" font-weight="600" fill="{BG}">in</text></g>')
    if name in CUSTOM:
        return (f'<g transform="translate({x},{y}) scale({size/24})" fill="none" stroke="{fill}" stroke-width="1.9" '
                f'stroke-linecap="round" stroke-linejoin="round">{CUSTOM[name]}</g>')
    if name in ICONS:
        return f'<g transform="translate({x},{y}) scale({size/24})"><path fill="{fill}" d="{ICONS[name]}"/></g>'
    return f'<rect x="{x+size*.2}" y="{y+size*.2}" width="{size*.6}" height="{size*.6}" rx="2" fill="none" stroke="{fill}" stroke-width="1.5"/>'
