"""Restyle tables and insert images into the post HTML. Usage: transform.py in.html out.html media.json"""
import json, re, sys

src, dst, media_path = sys.argv[1:4]
media = json.load(open(media_path))  # name -> {url, alt, w, h}
s = open(src).read()

# Theme already prints the byline, so drop the duplicate one at the top.
s = re.sub(r'^<p><em>By Amatchless Team[^\n]*</em></p>\n', '', s)

# Fix the bullet list that was left as markdown inside a <p>.
s = s.replace('''<p>On top of Meta's charge, add:
- <strong>18% GST</strong> on messaging charges.
- <strong>Your BSP's platform fee</strong>''', '''<p>On top of Meta's charge, add:</p>
<ul>
<li><strong>18% GST</strong> on messaging charges.</li>
<li><strong>Your BSP's platform fee</strong>''')
s = s.replace('''(<a target="_blank" rel="noopener" href="https://ecorpit.com/whatsapp-business-api-cost-india-d2c-2026/">eCorpIT</a>).</p>
<p><strong>A worked example.</strong>''', '''(<a target="_blank" rel="noopener" href="https://ecorpit.com/whatsapp-business-api-cost-india-d2c-2026/">eCorpIT</a>).</li>
</ul>
<p><strong>A worked example.</strong>''')

# Sources: make the whole citation the link (raw URLs don't wrap on mobile and don't look clickable).
s = re.sub(r'<li>([^\n]*?)\.? (https?://[^\s<]+)</li>',
           lambda m: f'<li><a target="_blank" rel="noopener" href="{m.group(2)}">{m.group(1)}</a></li>', s)

# Images and tables break out of the 760px text column to up to 1100px, centred, and fit the screen on mobile.
WIDE = 'width:min(1100px, calc(100vw - 32px));max-width:none;margin-left:calc(50% - min(550px, calc(50vw - 16px)))'

# Tables
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
assert s.count('class="amx-table"') == 4

def fig(name):
    m = media[name]
    return (f'<figure class="wp-block-image size-full" style="{WIDE};margin-top:2em;margin-bottom:2em">'
            f'<img src="{m["url"]}" alt="{m["alt"]}" width="{m["w"]}" height="{m["h"]}" loading="lazy" decoding="async" class="wp-image-{m["id"]}" style="width:100%;height:auto;display:block" /></figure>\n')

anchors = [
    ('<p>Two different things get called "AI automation", and it helps to separate them.</p>\n', 'rule-based-vs-ai-automation'),
    ("roughly in the order we'd tackle them.</p>\n", '10-tasks-to-automate-first'),
    ('</strong>, plus the BSP fee.</li>\n</ul>\n', 'whatsapp-business-api-cost-india-2026'),
    ('Here are the three levels we see, with indicative ranges.</p>\n', 'ai-automation-cost-india-3-levels'),
    ('<h2>7. A 30-day plan to launch your first automation</h2>\n', '30-day-ai-automation-plan'),
]
for a, name in anchors:
    assert s.count(a) == 1, a
    s = s.replace(a, a + fig(name))

open(dst, 'w').write(s)
print('ok', len(s))
