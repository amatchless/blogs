# Amatchless blog: standing rules for every weekly post

Agreed with the owner on 30 Oct 2026 while publishing week 1. Apply all of this to every new post without being asked. Week 1 is the reference: https://amatchless.com/ai-automation-small-business-india/ (files in `week-01-ai-automation-small-business-india/`).

## Workflow
1. Pick the post from the calendar. **From Fri 27 Nov 2026 to Fri 5 Mar 2027 the owner's own strategy sheet runs in sheet order** (owner's decision, 19 Nov 2026): take the Friday's entry from `calendars/content-calendar-2026-11-27-strategy-sheet.md` (source: `calendars/Amatchless_Final_SEO_AEO_GEO_LLMO_Content_Strategy.xlsx`) and follow its brief exactly: title, H1/H2/H3 outline, keywords with usage counts as a guide (never forced), word count, slug (the sheet's slug overrides "slug = primary keyword"), schema, internal links, competitor pages to beat, and the "Rules that apply to every post" at the top of that file. Do not change the topic or the order; a monthly calendar run only fixes dates and statuses. Weeks 5 to 9 of `content-calendar-2026-11-12.md` are replaced and are not scheduled. For any price or package, use `pricing-amatchless-and-delhi-market.md` (Amatchless prices from the owner and Delhi market ranges). Then research keywords and what's ranking, as in week 1's `topic-keywords-and-serp.md`.
2. Write the post, make the graphics, and upload everything to WordPress as a **draft**.
3. Posts publish on Friday **without the owner's review** (owner's decision, 18 Nov 2026). So never state an uncertain fact as certain: cite a source for every price, rate or statistic, label estimates as ranges, and only name clients and results that are already on amatchless.com/work/. After publishing, post the link and anything worth a second look in the thread.
4. After publishing, check the live page on desktop (1440px) and mobile (390px), and check the /blog/ list card.
5. Remind the owner to request indexing in Google Search Console, and to add internal links from relevant service pages (the account can't edit pages).

## WordPress access
- Login: the owner's created account (Author role, display name "Amatchless Team"). Never write credentials to a file. If the owner sends an Application Password, use that instead.
- Use the REST API with cookie login + `rest-nonce`. The server blocks the DELETE verb; use `X-HTTP-Method-Override: DELETE`.
- Author role limits: `<script>` and `<style>` tags are stripped (so no JSON-LD; Yoast already outputs Article schema). Inline `style=""` works, including `min()`, `calc()`, `overflow:auto`; `overflow-x` is stripped. Pages (e.g. /ai-automation/) can't be edited.

## Author and byline
- Author: **Amatchless Team** (no individual founder name).
- Don't put a byline at the top of the content; the theme already prints "By Amatchless Team · date · read time".
- End with a short "About the author" line for Amatchless Team (software, AI and marketing partner in Rohini, New Delhi, serving India, US and Canada) with the LinkedIn link.

## SEO setup on every post
- Yoast SEO title, meta description and focus keyphrase (set via `meta._yoast_wpseo_title`, `_yoast_wpseo_metadesc`, `_yoast_wpseo_focuskw`).
- Slug = primary keyword. One category (existing: Automation, AI, Branding, Paid Ads, SEO, Content Marketing, Insights, Company News). Tags as relevant.
- Excerpt = meta description (the /blog/ card shows it).
- British/Indian English spelling. Rupee prices for India.

## Images (required, no text-only posts)
- Make images in the brand style with the kit in `templates/graphics/` (see its README). Brand: ink #0E0B1F, purple #5B2EFF, pink #FF4F9A, yellow #FFE14D, mint #3DEBB0, bg #FBFAFF; Bricolage Grotesque headings, DM Sans body; thick ink borders, rounded corners, hard offset shadow, a tilted purple/pink highlight on a key word; small amatchless logo on each graphic.
- **Featured image:** 1600x1000 JPG, with a **unique concept per post** (owner's request, 18 Nov 2026): different background, layout and motif from recent covers; see `templates/graphics/covers-log.md`. **Keep all text and the logo in the centre 960px** (x 320 to 1280). The /blog/ list card crops the sides to as narrow as 1:1, so only decoration may sit near the left and right edges. Preview a centred 1000x1000 crop before uploading (`featured.py` shows the layout).
- **In-post graphics:** 4 to 6 per post, WebP, 1600px wide, one per major section (comparisons, ranked lists, cost breakdowns, plans/timelines, worked examples).
- File names = keyword phrases (e.g. `whatsapp-business-api-cost-india-2026.webp`). Every image gets descriptive alt text with the keyword, a title, and is attached to the post.

## Layout and tables
- **Text, images and tables are all the same width** (owner's request, 18 Nov 2026): up to 1100px, centred, with a 16px gutter on phones. `widen.py` adds the inline style to the text blocks; `transform.py`/`build.py` do the images and tables.
- Tables: wrapped in a scroll container (swipe on mobile, min-width 640px), dark ink header row with white text, alternating white / #F6F3FF rows, 2px ink border, 20px radius, hard shadow. Never leave bare tables.
- No raw markdown in the HTML (check lists inside `<p>`).

## Sources and credits
- Every source must be a **clickable link**: the whole citation text is the link (`<li><a href="url">Org, "Title", date</a></li>`). Never paste a bare URL (it doesn't wrap and widens the page on mobile).
- Credit competitors or data you borrowed, as in week 1.

## Known theme issues (developer's job, not fixable from a post)
- On phones, article text runs to the screen edge on every post (no side padding inside `.sec-in`).
- The text column is `.prose { max-width: 760px }`. If the owner wants wider text, the developer changes it in the theme's `site.css`.
- The /blog/ featured card crops images with `object-fit: cover` to a box whose shape changes with the title length. A fixed `aspect-ratio: 16 / 10` on `.pcard-media` would stop the cropping.

## Publishing without a password (from week 3, 18 Nov 2026)
Claude can't type passwords into login pages. What worked for week 3: the owner signs in to amatchless.com/wp-admin in the Claude desktop app's built-in browser; the owner downloads the graphics (now from the repo's week folder) and drags them into Media → Add New (the browser can't upload files); Claude then does everything else (alt text, post, Yoast meta, publish) through the REST API from that signed-in browser tab, using the `rest-nonce` from admin-ajax.

## Scheduled runs (from 18 Nov 2026)
- **Last day of each month, ~10:23 IST:** build the next month's calendar in `calendars/` (same format as `content-calendar-2026-11-12.md`), one post per Friday, topics from `topic-backlog.md` and `research/`.
- **Thursday ~14:37 IST:** write the coming Friday's post from the calendar, make a unique cover image (no shared template layout; see `templates/graphics/README.md`) and 4 to 6 in-post graphics, upload it all as a WordPress draft.
- **Friday ~10:17 IST:** final checks, publish, check the live page, update calendar and backlog status.
- Unattended publishing uses a WordPress Application Password for the Author account, read from the environment variables `WP_USER` and `WP_APP_PASSWORD` (HTTP Basic auth to `https://amatchless.com/wp-json/wp/v2/`, media upload via `POST /wp/v2/media`). Until those exist, fall back to the signed-in-browser method above and ask the owner to sign in.

## Where files live (from 18 Nov 2026)
The GitHub repo **amatchless/blogs** (branch `main`) is the home for everything: calendars, backlog, posts, graphics, templates, research. Pull before starting, commit and push to `main` at the end of every run. Don't save work to the owner's laptop. If the owner has to upload images by hand (no Application Password yet), point them to the `images/` folder of that week in the repo.
