# SciVis Contest 2027 website

Plain static HTML + one CSS file. No JavaScript, no Jekyll, no build step required.

## Deploy on GitHub Pages

1. Push the contents of this `website/` folder to the root of a repository
   (e.g. `sciviscontest2027.github.io`), or keep it in a `docs/` folder.
2. In the repository settings, under **Pages**, choose "Deploy from a branch"
   and select the branch (and `/` or `/docs`).
3. `.nojekyll` is included so GitHub serves the files as-is.

## Editing

Edit the `.html` files directly. The nav and footer are repeated in every page;
if you change them, either update all eight files or edit `build_site.py`
(which holds all page content and regenerates the HTML) and run
`python3 build_site.py` after adjusting the `OUT`/`SRC_IMG` paths at the top.

Pages: `index.html` (Home), `data.html`, `tasks.html`, `submissions.html`,
`archive.html` (empty for now), `acknowledgements.html` (includes references),
`pastcontests.html`, `faqs.html`.

Placeholders still to fill: jury (Acknowledgements), Archive page, and the
`LLNL-WEB-XXXXXX` release number
on the home page.
