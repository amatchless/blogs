# Blog graphics kit

Brand: ink #0E0B1F, purple #5B2EFF, pink #FF4F9A, yellow #FFE14D, mint #3DEBB0, bg #FBFAFF. Fonts: Bricolage Grotesque (headings), DM Sans (body). Thick ink borders, 36px radius, hard offset shadow, purple/pink tilted highlight on a key word. Matches the site theme and existing featured images.

- `gen.py` builds each graphic as HTML (copy and edit the `g[...]` blocks per post); `render.js name:ext ...` renders them to `out/` at 1600px wide with Playwright.
- Featured image: 1600x1000 JPG (theme crops to 16:10). **Every post gets its own cover concept**: check `covers-log.md`, choose a background, layout and motif that differ from the last three covers, and add a row. `featured.py` is only the week 1 example, not a template to reuse. In-post graphics: WebP, 1600 wide.
- File names = target keyword phrases; every upload gets a descriptive alt text and is attached to the post.
- `transform.py` restyles tables with inline styles (Author role: `overflow:auto` and `calc()` survive WordPress filtering, `overflow-x` does not), turns raw source URLs into short links, and inserts the figures.

- `widen.py` makes the post text as wide as the images and tables (inline breakout on each top-level block, since Author accounts can't change the theme's 760px `.prose` width). `build.py` calls it last.
