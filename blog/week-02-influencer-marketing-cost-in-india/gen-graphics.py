import sys
sys.path.insert(0, '.')
from logo import LOGO
from gen import page, CHECK

g = {}
R = '<span style="font-family:Bricolage Grotesque">₹</span>'

PLAY = '<svg width="{s}" height="{s}" viewBox="0 0 32 32"><circle cx="16" cy="16" r="15" fill="#FF4F9A" stroke="#0E0B1F" stroke-width="2.5"/><path d="M13 10.5v11l9-5.5z" fill="#fff" stroke="#0E0B1F" stroke-width="1.5" stroke-linejoin="round"/></svg>'
HEART = '<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-9.5-9.3C1.2 8.5 3.3 5 6.7 5c2 0 3.5 1.1 5.3 3 1.8-1.9 3.3-3 5.3-3 3.4 0 5.5 3.5 4.2 6.7C19.5 16.4 12 21 12 21z" fill="#FF4F9A" stroke="#0E0B1F" stroke-width="1.8"/></svg>'

# ---------- Featured image (centre-safe: all text within x 320..1280) ----------
bub = 'border:4px solid var(--ink);box-shadow:6px 6px 0 var(--ink);position:absolute;white-space:nowrap;font-weight:700'
g['influencer-marketing-cost-in-india'] = (page(f'''
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 330px">
  <div class="pill">Influencer marketing · 2026</div>
  <div class="d" style="font-size:100px;margin-top:44px">What influencers <span class="hl">charge</span> in India.</div>
  <div style="font-size:34px;font-weight:500;margin-top:34px;color:var(--muted);max-width:720px">Rates by tier, hidden costs, and a campaign that pays back.</div>
  <div style="margin-top:56px">{LOGO}</div>
</div>
<div style="position:absolute;left:-30px;top:120px;width:250px;height:330px;background:var(--purple);border:5px solid var(--ink);border-radius:30px;box-shadow:8px 8px 0 var(--ink);transform:rotate(-7deg);display:flex;align-items:center;justify-content:center">{PLAY.format(s=110)}</div>
<div style="{bub};left:40px;top:500px;background:#fff;border-radius:999px;padding:14px 24px;font-size:26px;transform:rotate(4deg)">{HEART.format(s=30)} 12.4K</div>
<div style="{bub};left:-20px;top:610px;background:var(--mint);border-radius:24px;padding:14px 22px;font-size:26px;transform:rotate(-4deg)">#ad #collab</div>
<div style="{bub};left:60px;bottom:90px;background:var(--pink);color:#fff;border-radius:24px;padding:14px 22px;font-size:26px;transform:rotate(3deg)">Code: SAVE15</div>
<div style="position:absolute;right:60px;top:100px;width:190px;height:190px;border-radius:50%;background:var(--purple);border:6px solid var(--ink);box-shadow:8px 8px 0 var(--ink);display:flex;align-items:center;justify-content:center;color:#fff;font-family:'Bricolage Grotesque';font-weight:800;font-size:110px">₹</div>
<div class="card" style="position:absolute;right:-20px;top:380px;background:#fff;padding:22px 28px;border-radius:28px;font-weight:700;font-size:26px;transform:rotate(-4deg);line-height:1.5">Nano ₹1K+<br>Micro ₹8K+<br>Mid ₹50K+</div>
<div class="card" style="position:absolute;right:40px;bottom:100px;background:var(--mint);padding:18px 26px;border-radius:999px;font-weight:700;font-size:28px;transform:rotate(5deg);white-space:nowrap">ROAS 1.9x</div>
''', 'var(--yellow)', 1000), 'jpg')

# ---------- 1. Rates by tier ----------
tiers = [('Nano', '1K – 10K', '₹1,000 – ₹12,000', 'var(--mint)', 560),
         ('Micro', '10K – 100K', '₹8,000 – ₹80,000', 'var(--yellow)', 700),
         ('Mid-tier', '100K – 500K', '₹50,000 – ₹3.5 lakh', 'var(--pink)', 800),
         ('Macro', '500K – 1M', '₹1 lakh – ₹8 lakh', 'var(--purple)', 900),
         ('Mega / celeb', '1M+', '₹5 lakh – ₹25 lakh+', 'var(--ink)', 1000)]
rows = ''
for name, f, price, c, w in tiers:
    fc = '#fff' if c in ('var(--purple)', 'var(--ink)') else 'var(--ink)'
    star = '<div class="tag" style="background:#fff;font-size:20px;margin-left:auto;white-space:nowrap;color:var(--ink)">Best value</div>' if name in ('Micro', 'Mid-tier') else ''
    rows += f'''<div style="display:flex;align-items:center;gap:30px">
      <div style="width:330px;flex:none"><div class="d" style="font-size:42px;white-space:nowrap">{name}</div><div style="font-size:24px;color:var(--muted);margin-top:6px">{f} followers</div></div>
      <div style="flex:1"><div style="width:{w}px;background:{c};color:{fc};border:5px solid var(--ink);border-radius:999px;box-shadow:7px 7px 0 var(--ink);padding:16px 30px;display:flex;align-items:center"><span class="d" style="font-size:40px;white-space:nowrap">{price}</span>{star}</div></div></div>'''
g['influencer-rates-india-2026-by-tier'] = (page(f'''
<div class="pill">Rate card · India 2026</div>
<div class="d" style="font-size:84px;margin-top:36px">How much do influencers <span class="hl">charge</span> per Reel?</div>
<div style="display:flex;flex-direction:column;gap:30px;margin-top:60px">{rows}</div>
<div style="margin-top:56px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Typical rate for one Instagram Reel, before usage rights, GST and fees. Ranges combine published 2026 rate cards (Grynow, upGrowth, StarClinch, Dazzlerr).</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 2. Hidden costs ----------
parts = [('Creator fee', '₹50,000', 'var(--yellow)', 330),
         ('Usage rights, 30 days (+30%)', '₹15,000', 'var(--mint)', 110),
         ('Management fee (20%)', '₹13,000', 'var(--pink)', 100),
         ('GST (18%)', '₹11,700', '#fff', 92)]
stack = ''
for n, v, c, h in parts:
    stack += f'<div style="height:{h}px;background:{c};border-top:4px solid var(--ink);display:flex;align-items:center;justify-content:space-between;padding:0 30px;font-weight:700;font-size:28px"><span>{n}</span><span class="d" style="font-size:36px">{v}</span></div>'
g['true-cost-of-an-influencer-reel-india'] = (page(f'''
<div class="pill">Hidden costs</div>
<div class="d" style="font-size:84px;margin-top:36px">The real cost of a <span class="hl" style="background:var(--pink)">₹50,000 Reel</span></div>
<div style="display:flex;gap:60px;margin-top:60px;align-items:flex-end">
  <div class="card" style="width:720px;overflow:hidden;display:flex;flex-direction:column-reverse;padding:0;border-top:1px solid var(--ink)">{stack}</div>
  <div style="flex:1">
    <div style="font-weight:700;font-size:26px;text-transform:uppercase;letter-spacing:.06em">Before you boost it</div>
    <div class="d" style="font-size:150px;margin-top:10px;color:var(--purple)">₹89,700</div>
    <div style="font-size:30px;margin-top:14px;line-height:1.4">That's <b>79% more</b> than the quote. GST is claimable if you're GST-registered.</div>
    <div style="margin-top:30px;background:#F3F0FB;border:3px dashed var(--ink);border-radius:22px;padding:20px 24px;font-size:26px;line-height:1.4"><b>Also budget for:</b> exclusivity (+10–30%), product and shipping, revisions, ad spend.</div>
  </div>
</div>
<div style="margin-top:56px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Example for a mid-tier creator. Usage-rights and management percentages vary by creator and partner.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 3. Budget ----------
def bud(amount, buys, use, bg, top):
    return f'''<div class="card" style="flex:1;padding:36px;background:{bg};margin-top:{top}px">
    <div style="font-weight:700;font-size:22px;text-transform:uppercase;letter-spacing:.06em">Budget</div>
    <div class="d" style="font-size:60px;margin-top:8px;line-height:1">{amount}</div>
    <div style="margin-top:26px;font-size:22px;font-weight:700;text-transform:uppercase;letter-spacing:.06em">Buys</div>
    <div style="font-size:27px;margin-top:8px;line-height:1.3">{buys}</div>
    <div style="margin-top:24px;border-top:3px solid var(--ink);padding-top:18px;font-size:25px;line-height:1.3"><b>Use it to:</b> {use}</div></div>'''
g['influencer-marketing-budget-india'] = (page(f'''
<div class="pill">Budget planner</div>
<div class="d" style="font-size:84px;margin-top:36px">What your influencer budget <span class="hl">actually buys</span></div>
<div style="display:flex;gap:30px;margin-top:40px;align-items:flex-start">
{bud('Under ₹50K', '10–30 nano creators, or 2–4 micro', 'test messages and collect UGC', 'var(--mint)', 90)}
{bud('₹1L – ₹3L', '6–15 micro, or micro plus 1 mid-tier', 'run your first tracked campaign', 'var(--yellow)', 60)}
{bud('₹5L', '1 macro, ~3 mid-tier, ~12 micro or up to 80 nano', 'spread wide, keep 20–30% to boost winners', 'var(--pink)', 30)}
{bud('₹10L+', 'ambassador deals, regional waves, a celebrity moment', 'feed your ads every month', '#fff', 0)}
</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div class="d" style="font-size:40px">First campaign? 10 micro creators beat 1 big name.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 4. ROI example ----------
def stepc(n, title, lines, roas, ok, bg):
    badge = 'var(--mint)' if ok else '#fff'
    li = ''.join(f'<div style="margin-top:10px">{l}</div>' for l in lines)
    return f'''<div class="card" style="flex:1;padding:34px;background:{bg};display:flex;flex-direction:column">
    <div style="font-weight:700;font-size:22px;text-transform:uppercase;letter-spacing:.06em">Step {n}</div>
    <div class="d" style="font-size:42px;margin-top:8px;line-height:1">{title}</div>
    <div style="font-size:25px;margin-top:16px;line-height:1.3">{li}</div>
    <div style="margin-top:auto;padding-top:26px"><div style="background:{badge};border:4px solid var(--ink);border-radius:24px;padding:14px 20px;display:flex;justify-content:space-between;align-items:center"><span style="font-weight:700;font-size:24px">ROAS</span><span class="d" style="font-size:58px">{roas}</span></div></div></div>'''
g['influencer-campaign-roi-example-india'] = (page(f'''
<div class="pill">Worked example · D2C skincare</div>
<div class="d" style="font-size:80px;margin-top:36px">Does an influencer campaign <span class="hl" style="background:var(--pink)">pay back?</span></div>
<div style="font-size:30px;margin-top:24px">Order ₹1,500 · ₹900 left per order · <b>break-even ROAS 1.67</b> · 8 micro creators, ₹1.7 lakh</div>
<div style="display:flex;gap:30px;margin-top:44px;align-items:stretch">
{stepc(1, 'Creator posts alone', ['4 lakh views', '3,200 visits', '96 orders = ₹1.44L'], '0.85', False, 'var(--yellow)')}
{stepc(2, '+ best 3 Reels as ads', ['₹1L ad spend at 2.5 ROAS', '+167 orders', 'Total sales ₹3.95L'], '1.46', False, '#fff')}
{stepc(3, '+ repeat orders', ['30% reorder in 90 days', '+79 orders', 'Total sales ₹5.13L'], '1.90', True, 'var(--mint)')}
</div>
<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Illustrative rates (0.8% tap-through, 3% conversion). Total cost ₹2.7 lakh excl. GST; about ₹37,800 profit at step 3.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 5. 8 steps ----------
steps = [('Set one goal', 'and the number that means it worked'), ('Find your break-even', 'so you know what each creator can cost'),
         ('Shortlist creators', 'by engagement, city and real comments'), ('Write a 1-page brief', 'message, must-says, label, link'),
         ('Sign a contract', 'usage rights, exclusivity, GST, TDS'), ('Track every creator', 'own code and UTM link each'),
         ('Boost the winners', 'run the best Reels as partnership ads'), ('Report and rebook', 'keep the top 20% on longer deals')]
cols = ['var(--yellow)', 'var(--mint)', 'var(--pink)', 'var(--purple)']
cards = ''
for i, (t, d) in enumerate(steps):
    c = cols[i % 4]; fc = '#fff' if c == 'var(--purple)' else 'var(--ink)'
    cards += f'''<div class="card" style="padding:28px;box-shadow:8px 8px 0 var(--ink)">
      <div style="width:76px;height:76px;border-radius:50%;background:{c};color:{fc};border:4px solid var(--ink);display:flex;align-items:center;justify-content:center" class="d"><span style="font-size:40px">{i+1}</span></div>
      <div class="d" style="font-size:36px;margin-top:20px;line-height:1">{t}</div><div style="font-size:24px;margin-top:12px;line-height:1.3">{d}</div></div>'''
g['how-to-run-an-influencer-campaign-india'] = (page(f'''
<div class="pill">Step by step</div>
<div class="d" style="font-size:84px;margin-top:36px">How to run an influencer campaign <span class="hl">that sells</span></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:30px;margin-top:56px">{cards}</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="display:flex;gap:14px;align-items:center;font-size:28px;font-weight:700">{CHECK} Label every post #ad or #collab (ASCI)</div>{LOGO}</div>
''', 'var(--mint)'), 'png')

if __name__ == "__main__":
    for name, (html, ext) in g.items():
        open(f'{name}.html', 'w').write(html.replace('₹', R))
    print(' '.join(f'{k}:{v[1]}' for k, v in g.items()))
