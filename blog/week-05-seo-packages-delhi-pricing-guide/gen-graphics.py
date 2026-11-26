"""Week 5 graphics. Run from a copy of templates/graphics (needs base.css, gen.py, logo.py, render.js):
python3 gen-graphics.py  -> writes <name>.html files and prints the render.js arguments."""
import sys
sys.path.insert(0, '.')
from logo import LOGO, STAR
from gen import page, CHECK

g = {}
CROSS = '<svg width="34" height="34" style="flex:none" viewBox="0 0 24 24"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" fill="none" stroke="#0E0B1F" stroke-width="3" stroke-linecap="round"/></svg>'
SCHK = CHECK.replace('width="40" height="40"', 'width="34" height="34" style="flex:none"')
SRC = 'font-size:22px;color:var(--muted);width:1080px;line-height:1.35'
LENS = '<svg width="{s}" height="{s}" viewBox="0 0 60 60"><circle cx="24" cy="24" r="17" fill="#fff" stroke="#0E0B1F" stroke-width="5"/><path d="M37 37 L54 54" stroke="#0E0B1F" stroke-width="8" stroke-linecap="round"/><path d="M15 22 a10 10 0 0 1 9 -8" fill="none" stroke="#5B2EFF" stroke-width="4" stroke-linecap="round"/></svg>'

# ---------- Featured image: "price tags on a string" (white with a thick purple frame; centre-safe x 320..1280) ----------
def tag(label, price, note, bg, fg, rot, top):
    return f'''<div style="position:relative;width:290px;margin-top:{top}px;transform:rotate({rot}deg);transform-origin:50% -60px">
  <div style="position:absolute;left:143px;top:-64px;width:5px;height:66px;background:var(--ink)"></div>
  <div style="background:{bg};color:{fg};border:5px solid var(--ink);border-radius:34px 34px 30px 30px;box-shadow:10px 10px 0 var(--ink);padding:52px 22px 28px;text-align:center;position:relative">
    <div style="position:absolute;left:50%;top:16px;width:26px;height:26px;margin-left:-13px;border-radius:50%;background:#FBFAFF;border:5px solid var(--ink)"></div>
    <div style="font-weight:700;font-size:24px;letter-spacing:.14em">{label}</div>
    <div class="d" style="font-size:58px;margin-top:10px;white-space:nowrap">{price}</div>
    <div style="font-size:22px;font-weight:500;margin-top:6px">a month</div>
    <div style="margin-top:16px;border-top:4px dashed {fg};padding-top:14px;font-size:24px;font-weight:700">{note}</div>
  </div></div>'''
g['seo-packages-in-delhi'] = (page(f'''
<div style="position:absolute;inset:0;border:34px solid var(--purple)"></div>
<div style="position:absolute;inset:34px;border:5px solid var(--ink)"></div>
<div style="position:absolute;left:70px;top:620px;transform:rotate(-18deg)">{LENS.format(s=200)}</div>
<div style="position:absolute;right:86px;top:120px;transform:rotate(12deg)">{STAR.replace('width="46" height="46"','width="120" height="120"').replace('#5B2EFF','#FF4F9A')}</div>
<div style="position:absolute;right:150px;top:760px">{STAR.replace('width="46" height="46"','width="80" height="80"').replace('#5B2EFF','#FFE14D')}</div>
<div style="position:absolute;left:110px;top:150px">{STAR.replace('width="46" height="46"','width="70" height="70"')}</div>
<div style="position:absolute;left:320px;top:96px;width:960px;text-align:center">
  <div class="pill" style="font-size:24px;padding:12px 28px">SEO packages in Delhi · 2026</div>
  <div class="d" style="font-size:84px;margin-top:22px">What does each <span class="hl" style="background:var(--pink)">price tier</span> really buy?</div>
</div>
<svg style="position:absolute;left:0;top:0" width="1600" height="1000" viewBox="0 0 1600 1000"><path d="M200 420 Q800 520 1400 420" fill="none" stroke="#0E0B1F" stroke-width="6"/></svg>
<div style="position:absolute;left:330px;top:470px;width:940px;display:flex;justify-content:space-between;align-items:flex-start">
  {tag('ENTRY', '₹10–20k', 'Basics + upkeep', 'var(--yellow)', 'var(--ink)', -5, 0)}
  {tag('GROWTH', '₹20–50k', 'Content + local', 'var(--purple)', '#fff', 1, 20)}
  {tag('ADVANCED', '₹50k–1L+', 'Scale + links', 'var(--mint)', 'var(--ink)', 5, 0)}
</div>
<div style="position:absolute;left:320px;top:890px;width:960px;display:flex;justify-content:center"><div style="display:inline-block;background:#fff;border:4px solid var(--ink);border-radius:999px;padding:6px 22px">{LOGO}</div></div>
''', '#FBFAFF', 1000), 'jpg')

# ---------- 1. Pricing models ----------
def model(title, price, how, good, bad, bg, fg='var(--ink)'):
    return f'''<div class="card" style="flex:1;padding:0;overflow:hidden;display:flex;flex-direction:column">
  <div style="background:{bg};color:{fg};padding:26px 30px;border-bottom:5px solid var(--ink)"><div class="d" style="font-size:48px">{title}</div><div style="font-size:30px;font-weight:700;margin-top:10px">{price}</div></div>
  <div style="padding:24px 30px 30px;font-size:25px;line-height:1.35;display:flex;flex-direction:column;flex:1">
    <div>{how}</div>
    <div style="display:flex;gap:12px;margin-top:20px;align-items:flex-start">{SCHK}<span><b>Good for:</b> {good}</span></div>
    <div style="display:flex;gap:12px;margin-top:14px;align-items:flex-start">{CROSS}<span><b>Watch:</b> {bad}</span></div>
  </div></div>'''
g['seo-pricing-models-delhi'] = (page(f'''
<div class="pill">How SEO is charged</div>
<div class="d" style="font-size:80px;margin-top:34px">Three ways Delhi agencies <span class="hl">price SEO</span></div>
<div style="display:flex;gap:30px;margin-top:50px;align-items:stretch">
{model('Monthly retainer', '₹10,000 – ₹1,00,000+ / month', 'A fixed fee for an agreed list of work every month.', 'ongoing growth', 'vague scopes with no deliverables list', 'var(--yellow)')}
{model('One-time project', 'Audit: ₹5,000 – ₹40,000', 'A fixed fee for a defined job: an audit, a migration, a clean-up.', 'a health check before you commit', 'an audit nobody acts on', 'var(--mint)')}
{model('Performance-linked', 'No reliable published range', 'Part of the fee depends on rankings or leads.', 'rarely the best fit', 'easy keywords picked to hit bonuses; risky shortcuts', 'var(--pink)')}
</div>
<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Ranges: ZestRank (updated Nov 2026, excl. GST) and Beyond DigitA (Sept 2026) Delhi SEO price guides. Asking prices, not audited data.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 2. By business type (range bars on a ₹0 - ₹1L+ scale) ----------
SCALE = 900
def bar(name, sub, lo, hi, bg, label, plus=False, fg='var(--ink)'):
    x = lo / 100 * SCALE; w = (hi - lo) / 100 * SCALE
    inside = w >= 220
    txt = label + ('+' if plus else '')
    lab_in = txt if inside else ''
    lab_out = '' if inside else f'<div style="position:absolute;left:{x + w + 26}px;top:20px;font-weight:700;font-size:32px;white-space:nowrap;background:#FBFAFF;padding:0 10px">{txt}</div>'
    return f'''<div style="display:flex;align-items:center;gap:36px;margin-top:40px">
  <div style="width:380px"><div class="d" style="font-size:44px">{name}</div><div style="font-size:24px;color:var(--muted);margin-top:6px">{sub}</div></div>
  <div style="position:relative;width:{SCALE}px;height:90px;border-left:4px solid var(--ink)">
    <div style="position:absolute;left:0;right:0;top:43px;border-top:3px dashed #B9B2D3"></div>
    <div style="position:absolute;left:{x}px;width:{w}px;top:8px;height:74px;background:{bg};color:{fg};border:5px solid var(--ink);border-radius:999px;box-shadow:6px 6px 0 var(--ink);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:30px;white-space:nowrap">{lab_in}</div>{lab_out}
  </div></div>'''
ticks = ''.join(f'<div style="position:absolute;left:{v/100*SCALE-40}px;width:80px;text-align:center;font-weight:700;font-size:24px">{t}</div>' for v, t in [(0, '₹0'), (25, '₹25k'), (50, '₹50k'), (75, '₹75k'), (100, '₹1L')])
g['seo-charges-in-delhi-by-business-type'] = (page(f'''
<div class="pill">SEO charges in Delhi</div>
<div class="d" style="font-size:80px;margin-top:34px">What SEO costs <span class="hl" style="background:var(--pink)">by business type</span></div>
<div style="font-size:30px;margin-top:20px;font-weight:500">Typical monthly asking prices, 2026</div>
{bar('Local shop or clinic', 'one location · Maps and "near me"', 15, 30, 'var(--yellow)', '₹15k – 30k')}
{bar('B2B or service firm', 'service keywords · enquiries', 25, 50, 'var(--mint)', '₹25k – 50k')}
{bar('Crowded sectors', 'real estate · education · health', 50, 80, '#fff', '₹50k – 80k', True)}
{bar('D2C or online store', 'category and product pages', 40, 100, 'var(--purple)', '₹40k – 1L', True, '#fff')}
<div style="margin-left:416px;position:relative;height:40px;margin-top:22px">{ticks}</div>
<div style="margin-top:40px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Source: Beyond DigitA, "SEO services cost in Delhi: 2026 pricing", Sept 2026. Agency asking prices; your quote depends on your site and competition.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 3. Tiers side by side ----------
def tier(name, price, fit, items, bg, fg='var(--ink)', lift=0):
    li = ''.join(f'<li style="display:flex;gap:12px;align-items:flex-start;margin-top:14px">{SCHK if ok else CROSS}<span style="{"" if ok else "color:var(--muted)"}">{t}</span></li>' for ok, t in items)
    return f'''<div class="card" style="flex:1;padding:0;overflow:hidden;margin-top:{lift}px">
  <div style="background:{bg};color:{fg};padding:28px 32px;border-bottom:5px solid var(--ink)"><div style="font-weight:700;font-size:24px;letter-spacing:.12em">{name}</div><div class="d" style="font-size:60px;margin-top:8px;white-space:nowrap">{price}</div><div style="font-size:23px;margin-top:6px;font-weight:500">{fit}</div></div>
  <ul style="list-style:none;font-size:26px;line-height:1.25;padding:12px 32px 32px">{li}</ul></div>'''
g['seo-packages-in-delhi-price-tiers'] = (page(f'''
<div class="pill">SEO packages in Delhi</div>
<div class="d" style="font-size:80px;margin-top:34px">Entry, growth, advanced: <span class="hl">what you get</span></div>
<div style="display:flex;gap:30px;margin-top:50px;align-items:flex-start">
{tier('ENTRY', '₹10–20k', 'one location, low competition', [(1,'Basic audit and fixes'),(1,'A few key pages'),(1,'Business Profile basics'),(0,'Little or no content'),(0,'No real link building')], 'var(--yellow)')}
{tier('GROWTH', '₹20–50k', 'growing, moderate competition', [(1,'Regular technical fixes'),(1,'Main service pages'),(1,'Local SEO and reviews'),(1,'A few articles a month'),(1,'Some outreach')], 'var(--purple)', '#fff', -20)}
{tier('ADVANCED', '₹50k–1L+', 'competitive, multi-city, e-com', [(1,'Full technical programme'),(1,'All key templates'),(1,'Content at scale'),(1,'Digital PR and links'),(1,'AI answers (AEO / GEO)')], 'var(--mint)')}
</div>
<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Per month. Price bands: ZestRank (updated Nov 2026, excl. GST); Battersea Web Expert and Beyond DigitA show similar bands. Inclusions vary by agency.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 4. Red flags ----------
flags = [('“Guaranteed #1 ranking”', 'Google: no one can guarantee a #1 ranking.', 'var(--pink)'),
         ('“500 backlinks a month”', 'Links built to game rankings are link spam.', 'var(--yellow)'),
         ('No access to your data', 'You should own Search Console and Analytics.', 'var(--mint)'),
         ('Secret methods', 'A good SEO explains every change.', '#fff'),
         ('Rankings-only reports', 'Ask for clicks, enquiries and sales.', 'var(--purple)'),
         ('Lock-in, no exit', 'Know the notice period and what you keep.', 'var(--yellow)')]
cards = ''
for i, (t, d, bg) in enumerate(flags):
    fg = '#fff' if bg == 'var(--purple)' else 'var(--ink)'
    rot = [-1.5, 1, -1, 1.5, -1, 1][i]
    cards += f'''<div class="card" style="background:{bg};color:{fg};padding:30px 32px;transform:rotate({rot}deg)">
  <div style="display:flex;align-items:center;gap:16px"><div style="width:58px;height:58px;flex:none;border-radius:50%;background:#fff;border:4px solid var(--ink);display:flex;align-items:center;justify-content:center">{CROSS}</div><div class="d" style="font-size:40px">{t}</div></div>
  <div style="font-size:27px;margin-top:16px;line-height:1.3;font-weight:500">{d}</div></div>'''
g['cheap-seo-red-flags-delhi'] = (page(f'''
<div class="pill">Cheap SEO in Delhi</div>
<div class="d" style="font-size:80px;margin-top:34px">Six <span class="hl" style="background:var(--pink)">red flags</span> before you pay</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:34px;margin-top:54px">{cards}</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Based on Google Search Central: "Do you need an SEO?" and "Spam policies for Google web search".</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 5. Quote checklist ----------
qs = ['What exactly do I get each month?', 'Who does the work?', 'What did you find on my site?', 'Which keywords, and why?', 'How will you get links?',
      'Do you follow Google Search Essentials?', 'What results, in what timeframe?', 'Do I own every account and article?', 'What does the report show?', 'How do I leave?']
def q(i, t):
    return f'''<div style="display:flex;align-items:center;gap:20px;background:#fff;border:4px solid var(--ink);border-radius:22px;padding:16px 22px;box-shadow:6px 6px 0 var(--ink)">
  <div style="width:50px;height:50px;flex:none;border-radius:12px;border:4px solid var(--ink);background:{'var(--mint)' if i % 2 == 0 else 'var(--yellow)'};display:flex;align-items:center;justify-content:center">{SCHK}</div>
  <div style="font-size:29px;font-weight:700;line-height:1.15"><span style="color:var(--purple)">{i+1}.</span> {t}</div></div>'''
g['compare-seo-quotes-checklist'] = (page(f'''
<div class="pill" style="background:var(--purple)">Quote A vs quote B</div>
<div class="d" style="font-size:80px;margin-top:34px">Ask both agencies <span class="hl" style="background:var(--ink)">these 10</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px 30px;margin-top:50px">{''.join(q(i, t) for i, t in enumerate(qs))}</div>
<div class="card" style="margin-top:40px;padding:24px 32px;background:var(--pink);display:flex;align-items:center;gap:24px"><div class="d" style="font-size:44px;white-space:nowrap">Then compare</div><div style="font-size:29px;font-weight:500">rupees per deliverable, not the monthly number.</div></div>
<div style="margin-top:40px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Questions 6 and 7 are from Google's own list in "Do you need an SEO?".</div>{LOGO}</div>
''', 'var(--yellow)'), 'png')

for name, (html, ext) in g.items():
    open(f'{name}.html', 'w').write(html)
print(' '.join(f'{n}:{e}' for n, (h, e) in g.items()))
