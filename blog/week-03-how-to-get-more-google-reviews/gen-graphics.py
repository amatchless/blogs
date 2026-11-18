"""Week 3 graphics. Run from a copy of templates/graphics (needs base.css, gen.py, logo.py, render.js):
python3 gen-graphics.py  -> writes <name>.html files and prints the render.js arguments."""
import sys
sys.path.insert(0, '.')
from logo import LOGO
from gen import page, CHECK, WA

g = {}
STARSVG = '<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M12 2.5l2.9 6 6.6.8-4.9 4.6 1.3 6.5L12 17.2l-5.9 3.2 1.3-6.5L2.5 9.3l6.6-.8z" fill="{c}" stroke="#0E0B1F" stroke-width="1.6" stroke-linejoin="round"/></svg>'
def stars(n=5, s=40, c='#FFE14D'):
    return ''.join(STARSVG.format(s=s, c=c) for _ in range(n))
PIN = '<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M12 22s7-6.5 7-12.2A7 7 0 0 0 5 9.8C5 15.5 12 22 12 22z" fill="#FF4F9A" stroke="#0E0B1F" stroke-width="1.8"/><circle cx="12" cy="9.8" r="2.8" fill="#fff" stroke="#0E0B1F" stroke-width="1.6"/></svg>'
CROSS = '<svg width="40" height="40" viewBox="0 0 24 24"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" fill="none" stroke="#0E0B1F" stroke-width="3" stroke-linecap="round"/></svg>'

def qr(size=200):
    # decorative QR-like block (not a real code)
    import random
    random.seed(7)
    n = 21; c = size / n; cells = ''
    for y in range(n):
        for x in range(n):
            finder = any(x0 <= x < x0 + 7 and y0 <= y < y0 + 7 for x0, y0 in ((0, 0), (14, 0), (0, 14)))
            if finder:
                xx, yy = x % 7 if x < 7 else (x - 14) % 7, y % 7 if y < 7 else (y - 14) % 7
                on = xx in (0, 6) or yy in (0, 6) or (2 <= xx <= 4 and 2 <= yy <= 4)
            else:
                on = random.random() < .45
            if on:
                cells += f'<rect x="{x*c:.1f}" y="{y*c:.1f}" width="{c+.3:.1f}" height="{c+.3:.1f}"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" fill="#0E0B1F">{cells}</svg>'

# ---------- Featured image: "Maps results" concept (unique to this post; centre-safe x 320..1280) ----------
streets = ''.join(f'<path d="{d}" stroke="#7A55FF" stroke-width="{w}" fill="none" stroke-linecap="round"/>' for d, w in [
    ('M-50 180 C 300 120, 500 260, 900 200 S 1400 120, 1700 230', 22), ('M-50 760 C 400 700, 700 860, 1100 780 S 1500 700, 1700 820', 22),
    ('M220 -50 C 260 300, 140 600, 240 1100', 16), ('M1380 -50 C 1340 260, 1460 640, 1360 1100', 16),
    ('M-50 470 L 1700 520', 10), ('M600 -50 L 640 1100', 8), ('M1020 -50 L 980 1100', 8)])

def row(rank, name, rating, n, hi):
    bg = 'var(--mint)' if hi else '#fff'
    box = 'border:4px solid var(--ink);border-radius:22px;box-shadow:6px 6px 0 var(--ink);' if hi else 'border-top:3px solid #E4DFF2;margin-top:10px;'
    badge = '<div class="tag" style="background:#fff;font-size:22px">Top pick</div>' if hi else ''
    return (f'<div style="display:flex;align-items:center;gap:22px;padding:16px 26px;background:{bg};{box}">'
            f'<div class="d" style="width:58px;height:58px;flex:none;border-radius:50%;background:{"var(--ink)" if hi else "#EEEAF7"};color:{"#fff" if hi else "var(--ink)"};display:flex;align-items:center;justify-content:center;font-size:30px">{rank}</div>'
            f'<div style="flex:1"><div class="d" style="font-size:34px">{name}</div>'
            f'<div style="display:flex;align-items:center;gap:10px;margin-top:6px;font-weight:700;font-size:24px">{rating}<span style="display:flex;gap:2px">{stars(5 if hi else 4, 26)}</span><span style="color:var(--muted);font-weight:500">({n})</span></div></div>{badge}</div>')

HL = 'background:var(--yellow);color:var(--ink);padding:0 .14em .04em;border-radius:.18em;display:inline-block;transform:rotate(-2deg);text-shadow:none;border:5px solid var(--ink)'
g['how-to-get-more-google-reviews'] = (page(f'''
<svg style="position:absolute;inset:0" width="1600" height="1000" viewBox="0 0 1600 1000">{streets}</svg>
<div style="position:absolute;left:30px;top:250px;transform:rotate(-10deg)">{PIN.format(s=150)}</div>
<div style="position:absolute;left:150px;top:660px;transform:rotate(8deg)">{PIN.format(s=96)}</div>
<div style="position:absolute;right:60px;top:110px;transform:rotate(9deg)">{PIN.format(s=120)}</div>
<div style="position:absolute;right:10px;top:600px;transform:rotate(-6deg)">{PIN.format(s=170)}</div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 340px">
  <div class="d" style="font-size:92px;color:#fff;text-shadow:5px 5px 0 var(--ink)">Get more Google <span style="{HL}">reviews</span></div>
  <div style="font-size:32px;font-weight:700;margin-top:24px;color:#fff">and climb the Google Maps results</div>
  <div class="card" style="width:880px;margin-top:38px;padding:22px;text-align:left">
    <div style="display:flex;align-items:center;gap:14px;border:3px solid var(--ink);border-radius:999px;padding:12px 22px;font-size:26px;font-weight:500;color:var(--muted)">{PIN.format(s=30)} salon near me</div>
    <div style="margin-top:18px">{row(1, 'Your business', '4.9', '312 reviews', True)}{row(2, 'The shop next door', '4.1', '38 reviews', False)}</div>
  </div>
  <div style="margin-top:32px;background:#fff;border:4px solid var(--ink);border-radius:999px;padding:8px 26px">{LOGO}</div>
</div>
''', 'var(--purple)', 1000), 'jpg')

# ---------- 1. Maps ranking factors ----------
def factor(name, q, levers, bg, fc='var(--ink)', note=''):
    li = ''.join(f'<div style="display:flex;gap:12px;align-items:flex-start;margin-top:14px"><span style="flex:none;margin-top:2px">{CHECK.replace("40", "30")}</span><span>{l}</span></div>' for l in levers)
    return f'''<div class="card" style="flex:1;padding:36px;background:#fff;display:flex;flex-direction:column">
    <div style="background:{bg};color:{fc};border:4px solid var(--ink);border-radius:22px;padding:18px 24px"><div class="d" style="font-size:52px">{name}</div><div style="font-size:24px;margin-top:6px;font-weight:500">{q}</div></div>
    <div style="font-size:26px;line-height:1.3;margin-top:10px">{li}</div>
    <div style="margin-top:auto;padding-top:22px;font-weight:700;font-size:24px">{note}</div></div>'''
g['google-maps-ranking-factors'] = (page(f'''
<div class="pill">Google Maps ranking</div>
<div class="d" style="font-size:84px;margin-top:36px">How Google ranks <span class="hl">local businesses</span></div>
<div style="display:flex;gap:34px;margin-top:56px;align-items:stretch">
{factor('Relevance', 'Do you match the search?', ['Specific primary category', 'Services and description', 'Website page per service'], 'var(--mint)', note='You control this')}
{factor('Distance', 'How close are you?', ['Real, verified address', 'Service areas set correctly', 'Same NAP everywhere'], '#fff', note='Mostly fixed')}
{factor('Prominence', 'How well known are you?', ['Steady flow of reviews', 'Ratings and replies', 'Links, photos, mentions'], 'var(--purple)', '#fff', note='Reviews live here ⭐')}
</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Google: "More reviews and positive ratings can help your business's local ranking." Source: Google Business Profile Help.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 2. Review link and QR code ----------
steps = [('Open your profile', 'On a computer, search your business name while signed in'),
         ('Read reviews', 'Select Read reviews on your Business Profile'),
         ('Get more reviews', 'Copy the short link, right-click to save the QR code'),
         ('Share it everywhere', 'WhatsApp quick reply, bill, counter standee')]
cols = ['var(--yellow)', 'var(--mint)', 'var(--pink)', 'var(--purple)']
sc = ''
for i, (t, d) in enumerate(steps):
    c = cols[i]; fc = '#fff' if c == 'var(--purple)' else 'var(--ink)'
    sc += f'''<div style="display:flex;gap:24px;align-items:center;margin-top:{0 if i == 0 else 26}px">
      <div class="d" style="flex:none;width:80px;height:80px;border-radius:50%;background:{c};color:{fc};border:4px solid var(--ink);box-shadow:5px 5px 0 var(--ink);display:flex;align-items:center;justify-content:center"><span style="font-size:42px">{i+1}</span></div>
      <div><div class="d" style="font-size:40px">{t}</div><div style="font-size:25px;margin-top:4px;color:var(--muted)">{d}</div></div></div>'''
g['google-review-link-qr-code'] = (page(f'''
<div class="pill">Step 1</div>
<div class="d" style="font-size:84px;margin-top:36px">Get your Google <span class="hl">review link</span> and QR code</div>
<div style="display:flex;gap:60px;margin-top:56px;align-items:center">
  <div style="flex:1">{sc}</div>
  <div class="card" style="width:430px;padding:36px;text-align:center;background:#fff;transform:rotate(3deg)">
    <div class="d" style="font-size:40px">Enjoyed your visit?</div>
    <div style="font-size:24px;margin-top:8px">Tell others on Google</div>
    <div style="margin:24px auto 0;width:240px;padding:20px;border:4px solid var(--ink);border-radius:20px;background:#fff">{qr(196)}</div>
    <div style="display:flex;gap:4px;justify-content:center;margin-top:22px">{stars(5, 38)}</div>
  </div>
</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Review QR codes can only be made in a computer browser. Test the link on your phone before you print.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 3. WhatsApp review request ----------
msg = 'Hi Priya, thank you for visiting Glow Salon today. We\'d love to hear how it went. If you have a minute, could you share your honest feedback on Google? It helps other people in Rohini choose. g.page/r/xxxx 🙏'
dos = [('Use their name and the visit', True), ('Send the direct link', True), ('Ask every customer', True), ('One reminder after 3–4 days', True),
       ('"Please give 5 stars"', False), ('"Mention Dr Sharma"', False), ('"Get 10% off for a review"', False)]
dl = ''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-top:16px;font-size:28px;{"" if ok else "color:var(--muted)"}"><span style="flex:none;width:52px;height:52px;border-radius:50%;border:4px solid var(--ink);background:{"var(--mint)" if ok else "var(--pink)"};display:flex;align-items:center;justify-content:center">{(CHECK if ok else CROSS).replace("40", "30")}</span><span style="font-weight:{700 if ok else 500}">{t}</span></div>' for t, ok in dos)
g['whatsapp-google-review-request-template'] = (page(f'''
<div class="pill">WhatsApp template</div>
<div class="d" style="font-size:84px;margin-top:36px">The review request <span class="hl" style="background:var(--pink)">that works</span></div>
<div style="display:flex;gap:70px;margin-top:56px;align-items:flex-start">
  <div style="width:600px;flex:none;background:var(--ink);border-radius:56px;padding:22px;box-shadow:12px 12px 0 var(--purple)">
    <div style="background:#ECE5DD;border-radius:40px;overflow:hidden">
      <div style="background:#075E54;color:#fff;padding:22px 28px;display:flex;gap:16px;align-items:center"><div style="width:56px;height:56px;border-radius:50%;background:var(--yellow);border:3px solid #fff"></div><div><div style="font-weight:700;font-size:26px">Glow Salon</div><div style="font-size:19px;opacity:.85">Business account</div></div></div>
      <div style="padding:30px 26px 40px">
        <div style="background:#fff;border-radius:22px 22px 22px 6px;padding:20px 22px;font-size:25px;line-height:1.4;width:470px">Thanks for today! Loved the new look 😍</div>
        <div style="background:#DCF8C6;border-radius:22px 22px 6px 22px;padding:20px 22px;font-size:25px;line-height:1.4;width:500px;margin:22px 0 0 auto">{msg.replace('g.page/r/xxxx', '<span style="color:#1B6AC9;text-decoration:underline">g.page/r/xxxx</span>')}</div>
      </div>
    </div>
  </div>
  <div style="flex:1;padding-top:10px"><div style="font-weight:700;font-size:24px;text-transform:uppercase;letter-spacing:.06em">Do and don't</div>{dl}</div>
</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Example only. English, Hinglish and Hindi versions are in the post.</div>{LOGO}</div>
''', 'var(--mint)'), 'png')

# ---------- 4. Policy allowed vs banned ----------
ok = ['Ask every customer for honest feedback', 'QR standee, bill link, WhatsApp message', 'One polite reminder', 'Reply to every review', 'Report reviews that break the rules']
no = ['Discounts, cashback or freebies for reviews', 'Asking only happy customers (gating)', 'Asking for 5 stars or specific words', 'Staff quotas or naming staff', 'Reviews from owners, staff or family', 'Buying review packages']
def lst(items, icon, bg):
    return ''.join(f'<div style="display:flex;gap:16px;align-items:center;margin-top:18px;font-size:29px;line-height:1.25"><span style="flex:none;width:50px;height:50px;border-radius:50%;border:4px solid var(--ink);background:{bg};display:flex;align-items:center;justify-content:center">{icon.replace("40", "28")}</span><span>{t}</span></div>' for t in items)
g['google-review-policy-allowed-vs-banned'] = (page(f'''
<div class="pill">Google's review policy</div>
<div class="d" style="font-size:84px;margin-top:36px">What's allowed, and what gets you <span class="hl" style="background:var(--pink)">flagged</span></div>
<div style="display:flex;gap:40px;margin-top:56px;align-items:stretch">
  <div class="card" style="flex:1;padding:40px;background:var(--mint)"><div class="d" style="font-size:52px">Allowed</div>{lst(ok, CHECK, '#fff')}</div>
  <div class="card" style="flex:1;padding:40px;background:#fff"><div class="d" style="font-size:52px">Not allowed</div>{lst(no, CROSS, 'var(--pink)')}</div>
</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Google blocked or removed 292 million policy-violating reviews in 2025. Source: Google Maps user-generated content policy.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 5. 30-day plan ----------
weeks = [('Week 1', 'Fix the profile', ['Category, hours, phone', '10+ real photos', 'Copy link, make QR', 'Reply to old reviews'], 'var(--yellow)'),
         ('Week 2', 'Start asking', ['WhatsApp every customer', 'Print the counter standee', 'Link on every bill', 'Brief staff: no pressure'], 'var(--mint)'),
         ('Week 3', 'Build the habit', ['Ask last month\'s customers', 'One reminder each', 'Reply within 48 hours', 'Count asks vs reviews'], 'var(--pink)'),
         ('Week 4', 'Review and automate', ['Compare reviews and rating', 'Check calls and directions', 'Keep the best channel', 'Automate the request'], 'var(--purple)')]
wc = ''
for i, (w, t, ls, c) in enumerate(weeks):
    fc = '#fff' if c == 'var(--purple)' else 'var(--ink)'
    li = ''.join(f'<div style="margin-top:12px;display:flex;gap:10px"><span>•</span><span>{l}</span></div>' for l in ls)
    wc += f'''<div class="card" style="flex:1;padding:0;overflow:hidden;margin-top:{(3-i)*28}px">
      <div style="background:{c};color:{fc};padding:24px 28px;border-bottom:5px solid var(--ink)"><div style="font-weight:700;font-size:22px;text-transform:uppercase;letter-spacing:.06em">{w}</div><div class="d" style="font-size:42px;margin-top:6px;line-height:1">{t}</div></div>
      <div style="padding:16px 28px 30px;font-size:25px;line-height:1.3">{li}</div></div>'''
g['30-day-google-review-plan'] = (page(f'''
<div class="pill">30-day plan</div>
<div class="d" style="font-size:84px;margin-top:36px">Get more Google reviews <span class="hl">in 30 days</span></div>
<div style="display:flex;gap:28px;margin-top:40px;align-items:flex-start">{wc}</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div class="d" style="font-size:40px">Goal: every customer asked, every review answered.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

if __name__ == "__main__":
    for name, (html, ext) in g.items():
        open(f'{name}.html', 'w').write(html)
    print(' '.join(f'{k}:{v[1]}' for k, v in g.items()))
