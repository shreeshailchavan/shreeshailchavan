# Publish the profile (v6: Linux desktop)

1. Create a public repo named exactly like the GitHub username (e.g. `shreeshailchavan`).
2. Upload `README.md`, `assets/`, `resume/` and the hidden `.github/` folder from this folder.
3. Contribution map: in the repo go to Settings → Actions → General → Workflow permissions, pick "Read and write", then Actions → "contribution map" → Run workflow once. After that it redraws `assets/contributions.svg` from his real GitHub data every day at 07:47 IST. The file shipped here is a preview drawn from his screenshot (227 contributions).

Layout: a status bar (workspaces 1–5), a neofetch window as the intro, then numbered sections like tiling-WM workspaces:
2 Stack (eight tiled windows with icons), 3 Work (git log graph: work lane + education lane),
4 Projects (one app window per project with a live request-flow diagram), 5 Contact (keycap buttons).

Palette: GitHub Halloween contribution colours (#15181d, #fac58e, #c36219, #974c17, #e2cf50).
Type: Bricolage Grotesque (headings) + Instrument Sans (body), embedded in each SVG. No monospace, no italics.
Motion: only a blinking status dot/cursor and one dot travelling along each diagram edge.

Check before going live
- Repo links assume `shreeshailchavan/routemem`, `/nailstore`, `/nailstore-events-worker`.
- Remove the Events worker window if that repo has no commits yet.
- To change wording, edit `source/gen_v6.py` and run `python3 source/gen_v6.py` (needs `pip install fonttools brotli`).
