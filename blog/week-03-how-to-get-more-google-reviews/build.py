"""Build week 3 HTML. Usage: build.py [media.json]
Writes post-base.html (plain) and, with media.json, post-wordpress.html (styled tables + figures)."""
import json, re, sys, markdown, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

md = open('post.md').read()
md = re.sub(r'<!--.*?-->\s*', '', md, count=1, flags=re.S)
md = re.sub(r'^# .*\n+', '', md, count=1)                      # title is the WP post title
md = re.sub(r'^\*By Amatchless Team[^\n]*\*\n+', '', md, flags=re.M)  # theme prints the byline
md = re.sub(r'^((?![-|>]|\d+\. )\S[^\n]*)\n(- |\d+\. )', r'\1\n\n\2', md, flags=re.M)
html = markdown.markdown(md, extensions=['tables'])
sys.path.insert(0, os.path.join('..', 'templates', 'graphics'))
from widen import widen
html = re.sub(r'<a href="(https?://)', r'<a target="_blank" rel="noopener" href="\1', html)
html = re.sub(r'<a target="_blank" rel="noopener" href="(https://amatchless\.com[^"]*)"', r'<a href="\1"', html)
# Sources: whole citation text becomes the link
html = re.sub(r'<li>([^\n]*?)\.? (https?://[^\s<]+)</li>',
              lambda m: f'<li><a target="_blank" rel="noopener" href="{m.group(2)}">{m.group(1)}</a></li>', html)
assert '](' not in html and '\n- ' not in html, 'raw markdown left'
open('post-base.html', 'w').write(html)
print('base ok', len(html))

if len(sys.argv) < 2:
    sys.exit()
media = json.load(open(sys.argv[1]))
s = html
WIDE = 'width:min(1100px, calc(100vw - 32px));max-width:none;margin-left:calc(50% - min(550px, calc(50vw - 16px)))'
WRAP = WIDE + ';overflow:auto;border:2px solid #0E0B1F;border-radius:20px;box-shadow:5px 5px 0 #0E0B1F;background:#fff;margin-top:1.8em;margin-bottom:1.8em'
TABLE = 'width:100%;min-width:640px;border-collapse:separate;border-spacing:0;font-size:15px;line-height:1.45;margin:0'
TH = 'background:#0E0B1F;color:#fff;text-align:left;padding:12px 14px;font-weight:700;font-size:14px;vertical-align:bottom'
TD = 'padding:12px 14px;border-top:1px solid #E4DFF2;vertical-align:top;text-align:left'

def style_table(m):
    t = m.group(0).replace('<table>', f'<table style="{TABLE}">')
    head, body = t.split('</thead>')
    ths = head.split('<th>')
    head = ths[0] + ''.join(
        f'<th style="{TH}' + (';border-top-left-radius:18px' if i == 0 else '') + (';border-top-right-radius:18px' if i == len(ths) - 2 else '') + '">' + x
        for i, x in enumerate(ths[1:]))
    rows = body.split('<tr>')
    out = [rows[0]]
    for ri, r in enumerate(rows[1:]):
        bg = '#FFFFFF' if ri % 2 == 0 else '#F6F3FF'
        last = ri == len(rows) - 2
        tds = r.split('<td>')
        r = tds[0] + ''.join(
            f'<td style="{TD};background:{bg}' + (';border-bottom-left-radius:18px' if last and i == 0 else '') + (';border-bottom-right-radius:18px' if last and i == len(tds) - 2 else '') + '">' + x
            for i, x in enumerate(tds[1:]))
        out.append('<tr>' + r)
    return f'<div class="amx-table" style="{WRAP}">' + head + '</thead>' + ''.join(out) + '</div>'

s = re.sub(r'<table>.*?</table>', style_table, s, flags=re.S)
assert s.count('class="amx-table"') == 4, s.count('class="amx-table"')

def fig(name):
    m = media[name]
    return (f'<figure class="wp-block-image size-full" style="{WIDE};margin-top:2em;margin-bottom:2em">'
            f'<img src="{m["url"]}" alt="{m["alt"]}" width="{m["w"]}" height="{m["h"]}" loading="lazy" decoding="async" class="wp-image-{m["id"]}" style="width:100%;height:auto;display:block" /></figure>\n')

anchors = [
    ('<h2>2. How Google reviews affect your Google Maps ranking</h2>\n', 'google-maps-ranking-factors'),
    ('<h2>3. Step 1: Get your Google review link and QR code</h2>\n', 'google-review-link-qr-code'),
    ('<h2>5. WhatsApp and SMS review request templates</h2>\n', 'whatsapp-google-review-request-template'),
    ("<h2>8. What Google's review policy bans</h2>\n", 'google-review-policy-allowed-vs-banned'),
    ('<h2>10. A 30-day plan to get more Google reviews</h2>\n', '30-day-google-review-plan'),
]
for a, name in anchors:
    assert s.count(a) == 1, a
    s = s.replace(a, a + fig(name))
s = widen(s)  # text as wide as the images and tables
open('post-wordpress.html', 'w').write(s)
print('wp ok', len(s))
