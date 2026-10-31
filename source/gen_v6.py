# v6 README panels: Linux desktop (status bar, neofetch, tiled windows, git log, dock) in the Halloween palette.
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
W = 1000
def save(name, s): open(os.path.join(OUT, name), "w").write(s)
def fits(t, size, maxw, fam="Instrument", wt=400):
    w = tw(t, size, fam, wt); assert w <= maxw, f"overflow {t!r}: {w:.0f} > {maxw}"; return w

# ---------- 1. status bar ----------
b = f'<rect x=".5" y=".5" width="{W-1}" height="43" rx="10" fill="{SURF}" stroke="{BD}"/>'
b += icon("archlinux", 16, 11, 22, PEACH)
x = 52
for i, ws in enumerate(["about", "stack", "work", "projects", "contact"]):
    lab = f"{i+1}  {ws}"; wd = tw(lab, 14, wt=500) + 22
    if i == 0: b += f'<rect x="{x}" y="9" width="{wd}" height="26" rx="6" fill="{PEACH}"/>'
    b += text(x+11, 27, lab, 14, BG if i == 0 else MUT, 600 if i == 0 else 500)
    x += wd + 6
r = W - 18
for lab, dot in [("UTC+5:30", None), ("pune, in", None), ("open to internships", YEL)]:
    wd = tw(lab, 14, wt=500); b += text(r, 27, lab, 14, TXT if dot else MUT, 500, anchor="end")
    if dot: b += f'<circle class="blink" cx="{r-wd-12}" cy="22" r="4" fill="{dot}"/>'; wd += 18
    r -= wd + 26
assert r > x, "status bar overflow"
save("bar.svg", svg(W, 44, b, bg=False))

# ---------- 2. neofetch hero ----------
H = 440
b = window(0, 0, W, H, "shreeshail@arch: ~", "zsh")
# pixel logo: "SC" in contribution cells
G = {"S":["01111","10000","10000","01110","00001","00001","11110"], "C":["01111","10000","10000","10000","10000","10000","01111"]}
rows = [G["S"][r] + "0" + G["C"][r] for r in range(7)]
sz, gp = 24, 6; st = sz + gp; lx, ly = 44, 74
random.seed(3); pal = [PEACH]*5 + [ORANGE]*3 + [YEL]
for r in range(11):
    for c in range(11):
        rr, cc = r-2, c
        on = 0 <= rr < 7 and cc < 11 and rows[rr][cc] == "1"
        col = random.choice(pal) if on else CELL
        b += f'<rect x="{lx+c*st}" y="{ly+r*st}" width="{sz}" height="{sz}" rx="4" fill="{col}"/>'
logo_r = lx + 11*st
X = logo_r + 52
b += text(X, 86, "~  $  neofetch", 15, MUT, 500)
b += text(X, 130, "shreeshail", 38, PEACH, 800, "Bricolage", ls=-1) 
nw = tw("shreeshail", 38, "Bricolage", 800, -1)
b += text(X+nw+2, 130, "@arch", 38, DIM, 800, "Bricolage", ls=-1)
b += f'<path d="M{X} 148H{W-48}" stroke="{BD}"/>'
info = [("role", "Backend & LLM systems engineer"),
        ("focus", "Scalable APIs · distributed systems · LLM infrastructure"),
        ("langs", "Python · Go · TypeScript · SQL"),
        ("edu", "PICT Pune, B.E. E&TC 2027 · CGPA 8.57"),
        ("shipped", "3 startups · 110+ endpoints led · 50–70% faster APIs"),
        ("status", "Open to internships + 2027 graduate roles")]
for i, (k, v) in enumerate(info):
    y = 184 + i*31
    b += text(X, y, k, 16, ORANGE, 600)
    fits(v, 16.5, W-48-(X+92)); b += text(X+92, y, v, 16.5, FG if k != "status" else YEL, 400 if k != "status" else 500)
for i, c in enumerate([BG, RUST, ORANGE, PEACH, YEL, BD, MUT, FG]):
    b += f'<rect x="{X+i*30}" y="{H-52}" width="24" height="16" rx="3" fill="{c}" stroke="{BD}"/>'
b += f'<rect class="blink" x="{X+8*30+10}" y="{H-54}" width="10" height="20" fill="{PEACH}"/>'
save("hero.svg", svg(W, H, b, bg=False))

# ---------- 3. section headers ----------
def header(fn, num, title, sub):
    s = f'<rect x="0" y="10" width="34" height="34" rx="8" fill="{SURF}" stroke="{PEACH}"/>' + text(17, 33, str(num), 16, PEACH, 700, "Bricolage", "middle")
    s += text(50, 37, title, 28, FG, 800, "Bricolage", ls=-.6)
    tx = 50 + tw(title, 28, "Bricolage", 800, -.6) + 16
    s += text(tx, 36, sub, 15, MUT)
    s += text(W, 36, f"super + {num}", 13, DIM, 500, anchor="end")
    s += f'<path d="M0 58.5H{W}" stroke="{BD}"/>'
    save(fn, svg(W, 62, s, bg=False))
header("h-stack.svg", 2, "Stack", "languages, frameworks, data, infra and the tools around them")
header("h-work.svg", 3, "Work", "git log of where I've shipped and studied")
header("h-projects.svg", 4, "Projects", "systems I designed and built end to end")
header("h-contact.svg", 5, "Contact", "the fastest ways to reach me")

# ---------- 4. stack: tiled windows ----------
groups = [
 ("languages", [("python","Python"),("typescript","TypeScript"),("javascript","JavaScript"),("go","Go"),("cplusplus","C++"),("sql","SQL"),("php","PHP")]),
 ("backend", [("fastapi","FastAPI"),("nestjs","NestJS"),("nodedotjs","Node.js"),("express","Express"),("flask","Flask"),("dotnet",".NET Core"),("api","REST · OpenAPI · SSE")]),
 ("frontend", [("nextdotjs","Next.js"),("react","React"),("angular","Angular"),("turborepo","Turborepo"),("vercel","Vercel"),("zod","zod"),("clerk","Clerk")]),
 ("ai / llm", [("ollama","Ollama"),("openai","OpenAI API"),("googlegemini","Gemini"),("bolt","Groq"),("vector","Qdrant · FAISS"),("tune","QLoRA · GRPO"),("onnx","ONNX")]),
 ("data", [("postgresql","PostgreSQL"),("redis","Redis"),("queue","BullMQ"),("mongodb","MongoDB"),("mysql","MySQL"),("sqlite","SQLite")]),
 ("infra", [("amazonwebservices","AWS"),("docker","Docker"),("kubernetes","Kubernetes"),("linux","Linux"),("cloud","LocalStack"),("github","Git · GitHub")]),
 ("ai tooling", [("claude","Claude Code"),("orbit","Antigravity"),("plug","MCP servers"),("play","Playwright MCP"),("check","Spec-driven dev")]),
 ("fundamentals", [("nodes","System design"),("tree","DSA"),("cube","OOP · DBMS"),("term","Operating systems"),("globe","Networks"),("shield","OAuth 2.0 · RBAC")]),
]
cols, gap = 4, 14; ww = (W - gap*(cols-1)) / cols; rh = 32; wh = 36 + 20 + 7*rh + 10
b = ""
for i, (name, items) in enumerate(groups):
    x = (i % cols)*(ww+gap); y = (i // cols)*(wh+gap)
    b += window(x, y, ww, wh, name, f"{len(items)}", DIM)
    for j, (ic, lab) in enumerate(items):
        yy = y + 36 + 18 + j*rh
        b += icon(ic, x+18, yy, 18, PEACH if ic else DIM)
        fits(lab, 15.5, ww-18-30-12); b += text(x+48, yy+14, lab, 15.5, TXT)
save("stack.svg", svg(W, 2*wh+gap, b, bg=False))

# ---------- 5. work: git log --graph ----------
ents = [  # lane 0 = work, lane 1 = education
 (0, "Jan – Apr 2026", "NixOut", "Software Engineer Intern · London, remote", "Built a CRM from zero to AWS; tuned SQL, CDN and assets to cut page load 40–60%.", ["aws", "0 → 1", "rest apis"]),
 (1, "2024 – 2027", "PICT, Pune", "B.E. Electronics & Telecommunication · CGPA 8.57", "Peer-reviewed paper on deep-learning malicious URL detection.", ["research", "dsa 900+"]),
 (0, "Dec 2023 – Apr 2024", "iGAP Technologies", "Full-Stack Engineer & Team Lead · Kolhapur", "Led 110+ REST endpoints and RBAC; cut API latency 50–70% on production SQL.", ["team lead", "angular", ".net"]),
 (0, "Jun 2023 – Sep 2024", "Government Polytechnic Kolhapur", "Project Developer · solo", "Exam, results and feedback system serving 3,000+ users on results day.", ["php", "mysql", "gemini"]),
 (1, "2021 – 2024", "Diploma in Information Technology", "Government Polytechnic Kolhapur · 95.5%", "Where it started.", []),
]
RH = 126; top = 74; H = top + RH*len(ents) + 10
b = window(0, 0, W, H, "git log --graph --oneline career", "HEAD → main", PEACH)
L = [56, 92]
lane_rows = {0: [i for i, e in enumerate(ents) if e[0] == 0], 1: [i for i, e in enumerate(ents) if e[0] == 1]}
def cy(i): return top + 12 + i*RH
b += f'<path d="M{L[0]} {cy(0)} V{cy(len(ents)-1)+20}" stroke="{PEACH}" stroke-opacity=".55" stroke-width="2.5" fill="none"/>'
e1 = lane_rows[1]
b += (f'<path d="M{L[0]} {cy(0)-30} C{L[0]} {cy(0)-10} {L[1]} {cy(0)-10} {L[1]} {cy(e1[0])} V{cy(e1[-1])} '
      f'C{L[1]} {cy(e1[-1])+40} {L[0]} {cy(e1[-1])+20} {L[0]} {cy(e1[-1])+50}" stroke="{YEL}" stroke-opacity=".55" stroke-width="2.5" fill="none"/>')
TX = 130
for i, (lane, when, org, role, desc, tags) in enumerate(ents):
    y = cy(i); col = PEACH if lane == 0 else YEL
    b += f'<circle cx="{L[lane]}" cy="{y}" r="8" fill="{SURF}" stroke="{col}" stroke-width="3"/>'
    if i == 0: b += f'<circle cx="{L[lane]}" cy="{y}" r="3.5" fill="{col}"/>'
    b += text(TX, y+7, org, 21, FG, 800, "Bricolage", ls=-.3)
    ow = tw(org, 21, "Bricolage", 800, -.3)
    b += text(W-28, y+6, when, 14, ORANGE if lane == 0 else YEL, 600, anchor="end")
    fits(org, 21, W-28-tw(when, 14, wt=600)-24-TX, "Bricolage", 800)
    b += text(TX, y+32, role, 15, MUT, 500)
    fits(desc, 15.5, W-28-TX); b += text(TX, y+58, desc, 15.5, TXT)
    tx = TX
    for t in tags:
        cw = tw(t, 12.5, wt=500) + 20
        b += f'<rect x="{tx}" y="{y+70}" width="{cw}" height="22" rx="11" fill="none" stroke="{BD}"/>' + text(tx+cw/2, y+85, t, 12.5, MUT, 500, anchor="middle")
        tx += cw + 8
save("work.svg", svg(W, H, b, bg=False))

# ---------- 6. projects ----------
def box(x, y, w, t, hl=False, h=34):
    return (f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="8" fill="{BG}" stroke="{PEACH if hl else BD}" stroke-width="{1.5 if hl else 1}"/>'
            + text(x, y+5, t, 13.5, FG if hl else TXT, 500, anchor="middle"))
def wire(d, col=ORANGE, dur=2.4, dot=True):
    s = f'<path d="{d}" fill="none" stroke="{BD}" stroke-width="1.6"/>'
    if dot: s += f'<circle r="3.2" fill="{col}"><animateMotion dur="{dur}s" repeatCount="indefinite" path="{d}"/></circle>'
    return s
def project(fn, path, status, scol, title, desc, stats, chips, diagram, H=320):
    b = window(0, 0, W, H, path, status, scol)
    b += text(40, 98, title, 42, FG, 800, "Bricolage", ls=-1.2)
    lines = desc
    for i, l in enumerate(lines): fits(l, 17, 560); b += text(40, 132+i*24, l, 17, MUT)
    sy = 132 + len(lines)*24 + 46
    for i, (big, lab) in enumerate(stats):
        b += text(40+i*180, sy, big, 30, PEACH, 800, "Bricolage", ls=-.6) + text(40+i*180, sy+22, lab, 13.5, MUT, 500)
    cx = 40
    for ic, t in chips:
        cw = tw(t, 13, wt=500) + (44 if ic else 22)
        b += f'<rect x="{cx}" y="{H-50}" width="{cw}" height="28" rx="7" fill="{SURF2}" stroke="{BD}"/>'
        if ic: b += icon(ic, cx+10, H-43, 14, PEACH)
        b += text(cx+(32 if ic else 11), H-31, t, 13, TXT, 500); cx += cw + 8
    assert cx < 620, f"chips overflow {fn}"
    b += f'<rect x="640" y="56" width="{W-640-24}" height="{H-56-24}" rx="10" fill="{BG}" stroke="{BD}"/>' + diagram
    save(fn, svg(W, H, b, bg=False))
X = 640
d = wire(f"M{X+76} 110 L{X+126} 110") + wire(f"M{X+194} 110 L{X+244} 110") + wire(f"M{X+282} 128 L{X+282} 160 L{X+168} 160 L{X+168} 186", YEL, 2.8)
d += box(X+48, 110, 60, "app") + box(X+160, 110, 70, "redis") + box(X+282, 110, 76, "qdrant") + box(X+168, 204, 104, "router", True)
for i, (ox, lab) in enumerate([(X+62, "local"), (X+168, "groq"), (X+276, "gpt-4o")]):
    d = wire(f"M{X+168} 222 L{X+168} 236 L{ox} 236 L{ox} 252", [YEL, ORANGE, RUST][i], 2.2+.4*i) + d
    d += box(ox, 268, 82, lab)
project("p-routemem.svg", "~/projects/routemem", "research · deployed on aws", ORANGE, "RouteMem",
        ["An OpenAI-compatible gateway that sends each prompt", "to the cheapest model that can answer it."],
        [("80%", "cheaper than all-GPT-4o"), ("94.2%", "routing accuracy"), ("2-tier", "exact + semantic cache")],
        [("python", "Python"), ("fastapi", "FastAPI"), ("redis", "Redis"), ("vector", "Qdrant"), ("ollama", "Ollama")], d)
d = ""
for i, ty in enumerate([96, 146, 196]): d += wire(f"M{X+92} {ty} L{X+118} {ty} L{X+118} 146 L{X+138} 146", PEACH, 2+.4*i)
d += wire(f"M{X+212} 146 L{X+240} 146", YEL) + wire(f"M{X+175} 164 L{X+175} 222") + wire(f"M{X+218} 240 L{X+240} 240")
for ty, l in zip([96, 146, 196], ["artist a", "artist b", "artist c"]): d += box(X+54, ty, 76, l, h=30)
d += box(X+175, 146, 74, "nestjs", True) + box(X+282, 146, 84, "postgres") + box(X+175, 240, 84, "outbox") + box(X+282, 240, 84, "bullmq")
project("p-nailstore.svg", "~/projects/nailstore", "built · payments in progress", YEL, "NailStore",
        ["Multi-tenant storefronts where nail artists sell", "press-on sets and take custom orders."],
        [("RLS", "tenant isolation"), ("outbox", "idempotent async work"), ("15", "architecture decisions")],
        [("nextdotjs", "Next.js"), ("nestjs", "NestJS"), ("postgresql", "Postgres"), ("queue", "BullMQ"), ("turborepo", "Turborepo")], d)
d = wire(f"M{X+92} 150 L{X+132} 150", PEACH) 
for i, py in enumerate([100, 150, 200]): d += wire(f"M{X+206} 150 L{X+232} 150 L{X+232} {py} L{X+256} {py}", YEL, 2+.4*i)
d += box(X+56, 150, 72, "outbox") + box(X+170, 150, 72, "go", True)
for py in [100, 150, 200]: d += box(X+292, py, 66, "pod", h=30)
project("p-worker.svg", "~/projects/events-worker", "in progress", ORANGE, "Events worker",
        ["A Go service that drains NailStore's outbox,", "deployed on Kubernetes with Helm."],
        [("Go", "idempotent handlers"), ("Helm", "kubernetes deploy"), ("OTel", "traces + metrics")],
        [("go", "Go"), ("kubernetes", "Kubernetes"), ("helm", "Helm"), ("opentelemetry", "OpenTelemetry")], d)

# ---------- 7. contact dock ----------
def key(fn, ic, lab, primary=False):
    w = tw(lab, 15, wt=600) + 64; h = 52
    face, txt, ico = (PEACH, BG, BG) if primary else (SURF, FG, PEACH)
    s = f'<rect x=".5" y="6.5" width="{w-1}" height="{h-7}" rx="11" fill="{RUST if primary else BD}"/>'
    s += f'<rect x=".5" y=".5" width="{w-1}" height="{h-7}" rx="11" fill="{face}" stroke="{ORANGE if primary else BD}"/>'
    if ic == "doc":
        s += f'<g transform="translate(20,13)" fill="none" stroke="{ico}" stroke-width="1.8"><path d="M1 1h10l5 5v14H1z"/><path d="M11 1v5h5M4 11h9M4 15h9"/></g>'
    elif ic == "mail":
        s += f'<g transform="translate(19,15)" fill="none" stroke="{ico}" stroke-width="1.8"><rect x="1" y="1" width="18" height="14" rx="2"/><path d="M1 3l9 6 9-6"/></g>'
    else: s += icon(ic, 20, 13, 20, ico)
    s += text(50, 29, lab, 15, txt, 600)
    save(fn, svg(int(w)+1, h, s, bg=False))
key("k-email.svg", "mail", "Email me", True)
key("k-linkedin.svg", "linkedin", "LinkedIn")
key("k-resume.svg", "doc", "Resume")
key("k-paper.svg", "doc", "Research paper")

# ---------- 8. footer bar ----------
b = f'<rect x=".5" y=".5" width="{W-1}" height="43" rx="10" fill="{SURF}" stroke="{BD}"/>'
b += text(18, 27, "~  $  exit", 14, MUT, 500)
b += text(W-18, 27, "thanks for reading · reach me at shreeshailchavan309@gmail.com", 14, MUT, 500, anchor="end")
save("footer.svg", svg(W, 44, b, bg=False))
print("ok")
