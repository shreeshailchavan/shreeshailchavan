"""Redraw assets/contributions.svg from the GitHub GraphQL contribution calendar."""
import json, os, re, sys, urllib.request
from datetime import date

LOGIN = os.environ["GH_LOGIN"]
TOKEN = os.environ["GH_TOKEN"]
OUT = "assets/contributions.svg"

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{contributionCount contributionLevel date}}}}}}"""

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
    headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
)
data = json.load(urllib.request.urlopen(req))
if "errors" in data:
    sys.exit(data["errors"])
cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]

# reuse the embedded fonts from the existing file
style = re.search(r"<style>.*?</style>", open(OUT).read(), re.S).group(0)

COL = {"NONE": "#211a1d", "FIRST_QUARTILE": "#a8142f", "SECOND_QUARTILE": "#d11c3d",
       "THIRD_QUARTILE": "#f2334c", "FOURTH_QUARTILE": "#ff6b7d"}
FG, MUTED = "#f8eef0", "#ab9ca1"
X0, Y0, STEP, CELL = 64.0, 98.0, 17.2, 14.2
H = 42.5 + 233.45283018867923
LY = 248.45283018867923

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="276" viewBox="0 0 1000 276">', style,
     f'<text x="2" y="26" font-size="20" font-weight="500" fill="{FG}">{cal["totalContributions"]} contributions in the last year</text>',
     f'<rect x=".5" y="42.5" width="999" height="233.45283018867923" rx="10" fill="#141013" stroke="#3a2a30"/>']
last_month = None
for i, w in enumerate(cal["weeks"]):
    x = X0 + i * STEP
    days = w["contributionDays"]
    m = date.fromisoformat(days[0]["date"]).strftime("%b")
    if m != last_month and i > 0:
        o.append(f'<text x="{x:.1f}" y="86" font-size="13" fill="{FG}">{m}</text>')
    last_month = m
    for j, d in enumerate(days):
        o.append(f'<rect x="{x:.1f}" y="{Y0 + j * STEP:.1f}" width="{CELL}" height="{CELL}" rx="2.5" '
                 f'fill="{COL[d["contributionLevel"]]}"><title>{d["contributionCount"]} on {d["date"]}</title></rect>')
for label, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
    o.append(f'<text x="24" y="{Y0 + row * STEP + 13.2 - 0.0:.1f}" font-size="13" fill="{FG}">{label}</text>')
o.append(f'<text x="834" y="{LY}" text-anchor="end" font-size="13" fill="{MUTED}">Less</text>')
for k, c in enumerate(COL.values()):
    o.append(f'<rect x="{842 + k * 18}" y="237.45283018867923" width="14" height="14" rx="2.5" fill="{c}"/>')
o.append(f'<text x="936" y="{LY}" font-size="13" fill="{MUTED}">More</text>')
o.append(f'<text x="24" y="{LY}" font-size="13" fill="{MUTED}">updated {date.today():%d %b %Y}</text>')
o.append("</svg>")
open(OUT, "w").write("\n".join(o) + "\n")
