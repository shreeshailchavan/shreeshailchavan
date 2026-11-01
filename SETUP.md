# Publish the profile (v7: Linux desktop, crimson)

1. Create a public repo named exactly like the GitHub username (e.g. `shreeshailchavan`).
2. Upload `README.md`, `assets/`, `resume/` and the hidden `.github/` folder from this folder.
3. Contribution map: in the repo go to Settings → Actions → General → Workflow permissions, pick "Read and write", then Actions → "contribution map" → Run workflow once. After that it redraws `assets/contributions.svg` from his real GitHub data every day at 07:47 IST. The file shipped here is a preview drawn from his screenshot (227 contributions).

Layout: a status bar (workspaces 1–5), a neofetch window as the intro, then numbered sections like tiling-WM workspaces:
2 Stack (eight tiled windows with icons), 3 Work (git log graph: work lane + education lane),
4 Projects (one app window per project with a live request-flow diagram), 5 Contact (keycap buttons).

Palette: dark crimson (#141013 background, #e2717f rose, #c41e3a crimson, #6e0f22 deep crimson, #e23a50 scarlet).
Type: Bricolage Grotesque (headings) + Instrument Sans (body), embedded in each SVG. No monospace, no italics.
Motion: in the hero, a colour wave runs through the SC logo forever while the right side plays as a terminal (types `neofetch`, prints the info line by line, 14s loop); otherwise only a blinking status dot and one dot travelling along each diagram edge.

Check before going live
- Repo links assume `shreeshailchavan/routemem`, `/nailstore`, `/nailstore-events-worker`.
- Remove the Events worker window if that repo has no commits yet.
- To change wording, edit `source/gen_v6.py` and run `python3 source/gen_v6.py` (needs `pip install fonttools brotli`).
