"""Week 4 graphics. Run from a copy of templates/graphics (needs base.css, gen.py, logo.py, render.js):
python3 gen-graphics.py  -> writes <name>.html files and prints the render.js arguments."""
import sys
sys.path.insert(0, '.')
from logo import LOGO
from gen import page, CHECK

g = {}
CROSS = '<svg width="40" height="40" viewBox="0 0 24 24"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" fill="none" stroke="#0E0B1F" stroke-width="3" stroke-linecap="round"/></svg>'
COIN = '<svg width="{s}" height="{s}" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#FFE14D" stroke="#0E0B1F" stroke-width="3"/><circle cx="20" cy="20" r="12.5" fill="none" stroke="#0E0B1F" stroke-width="2" stroke-dasharray="3 3"/><text x="20" y="27" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="19" fill="#0E0B1F">₹</text></svg>'
ARROW = '<svg width="{s}" height="{s}" viewBox="0 0 40 40"><path d="M6 32 L32 6 M14 6 H32 V24" fill="none" stroke="#0E0B1F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SRC = 'font-size:22px;color:var(--muted);width:1080px;line-height:1.35'

# ---------- Featured image: "ad receipt" concept (mint, diagonal stripes, a till receipt as the hero; centre-safe x 320..1280) ----------
stripes = ''.join(f'<path d="M{x} -40 L{x-700} 1040" stroke="#2FD69E" stroke-width="34"/>' for x in range(0, 2400, 120))
def rline(a, b, bold=False, big=False):
    fs = 40 if big else 28
    return (f'<div style="display:flex;justify-content:space-between;font-family:\'DM Sans\';font-size:{fs}px;font-weight:{700 if bold else 500};margin-top:12px">'
            f'<span>{a}</span><span>{b}</span></div>')
receipt = f'''
<div style="position:relative;width:560px;background:#fff;border:5px solid var(--ink);box-shadow:12px 12px 0 var(--ink);padding:34px 40px 46px;transform:rotate(-2.5deg)">
  <div style="text-align:center;font-weight:700;font-size:22px;letter-spacing:.2em">META ADS · NOVEMBER</div>
  <div style="border-top:4px dashed var(--ink);margin:18px 0 6px"></div>
  {rline('Ad spend', '₹1,00,000')}
  {rline('GST @18%', '₹18,000')}
  {rline('Orders', '412')}
  {rline('Sales', '₹4,00,000', True)}
  <div style="border-top:4px dashed var(--ink);margin:18px 0 6px"></div>
  {rline('ROAS', '4.0x', True, True)}
  <div style="margin-top:14px;font-size:20px;color:var(--muted);text-align:center">Illustration only</div>
</div>'''
g['meta-ads-for-d2c-brands-india'] = (page(f'''
<svg style="position:absolute;inset:0" width="1600" height="1000" viewBox="0 0 1600 1000">{stripes}</svg>
<div style="position:absolute;left:40px;top:90px;transform:rotate(-14deg)">{COIN.format(s=150)}</div>
<div style="position:absolute;left:150px;top:640px;transform:rotate(10deg)">{COIN.format(s=110)}</div>
<div style="position:absolute;right:50px;top:160px;transform:rotate(12deg)">{COIN.format(s=120)}</div>
<div style="position:absolute;right:120px;top:700px;transform:rotate(-8deg)">{COIN.format(s=160)}</div>
<div style="position:absolute;left:330px;top:70px;width:940px;text-align:center">
  <div class="pill" style="font-size:26px;padding:12px 30px">Meta ads for D2C · India 2026</div>
  <div class="d" style="font-size:86px;margin-top:22px">What does <span class="hl" style="background:var(--pink)">4x ROAS</span> really take?</div>
</div>
<div style="position:absolute;left:360px;top:360px">{receipt}</div>
<div style="position:absolute;left:930px;top:380px;width:330px">
  <div class="card" style="padding:22px 26px;background:var(--yellow);transform:rotate(3deg)"><div style="font-weight:700;font-size:22px;letter-spacing:.06em;text-transform:uppercase">Break-even</div><div class="d" style="font-size:56px;margin-top:6px;white-space:nowrap">1 ÷ margin</div></div>
  <div class="card" style="padding:20px 26px;margin-top:30px;background:var(--purple);color:#fff;transform:rotate(-2deg)"><div class="d" style="font-size:40px">Budgets in ₹</div><div style="font-size:24px;margin-top:4px">test · learn · scale</div></div>
  <div style="margin-top:34px;display:inline-block;background:#fff;border:4px solid var(--ink);border-radius:999px;padding:6px 22px">{LOGO}</div>
</div>
''', 'var(--mint)', 1000), 'jpg')

# ---------- 1. Cost ranges ----------
def cost(label, fb, ig, note, bg):
    return f'''<div class="card" style="flex:1;padding:0;overflow:hidden;display:flex;flex-direction:column">
      <div style="background:{bg};padding:24px 30px;border-bottom:5px solid var(--ink)"><div class="d" style="font-size:52px">{label}</div><div style="font-size:23px;margin-top:4px;font-weight:500">{note}</div></div>
      <div style="padding:22px 30px 30px">
        <div style="font-weight:700;font-size:21px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)">Facebook</div><div class="d" style="font-size:54px;margin-top:2px">{fb}</div>
        <div style="font-weight:700;font-size:21px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-top:18px">Instagram</div><div class="d" style="font-size:54px;margin-top:2px">{ig}</div>
      </div></div>'''
g['meta-ads-cost-india-2026'] = (page(f'''
<div class="pill">Facebook and Instagram ads cost</div>
<div class="d" style="font-size:84px;margin-top:36px">What Meta ads cost in <span class="hl">India in 2026</span></div>
<div style="display:flex;gap:32px;margin-top:52px;align-items:stretch">
{cost('CPM', '₹60–250', '₹45–400', 'per 1,000 impressions', 'var(--yellow)')}
{cost('CPC', '₹4–50', '₹4–55', 'per link click', 'var(--mint)')}
<div class="card" style="flex:1;padding:32px;background:var(--pink);display:flex;flex-direction:column">
  <div class="d" style="font-size:52px">+18% GST</div>
  <div style="font-size:27px;margin-top:14px;line-height:1.3">On ads billed in India. Claim it as input tax credit with your GSTIN.</div>
  <div style="margin-top:auto;background:#fff;border:4px solid var(--ink);border-radius:20px;padding:16px 20px;font-size:25px;line-height:1.3"><b>Can't claim it?</b> ₹1 lakh of ads really costs ₹1.18 lakh.</div>
</div>
</div>
<div style="margin-top:46px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Ranges: upGrowth estimate, Sept 2026 (Instagram CPM = prospecting). GST: Meta Business Help Centre. Prices rise in festive weeks. Judge cost per purchase, not CPM.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 2. Break-even ROAS calculator ----------
rows = [(20, 5.0, 5.9), (25, 4.0, 4.7), (30, 3.3, 3.9), (40, 2.5, 3.0), (50, 2.0, 2.4), (60, 1.7, 2.0), (70, 1.4, 1.7)]
bars = ''
for m, be, beg in rows:
    w = be / 6 * 820; wg = beg / 6 * 820
    hi = m == 40
    bars += f'''<div style="display:flex;align-items:center;gap:26px;margin-top:16px">
      <div class="d" style="width:150px;font-size:44px;text-align:right">{m}%</div>
      <div style="position:relative;flex:1;height:58px">
        <div style="position:absolute;left:0;top:0;height:58px;width:{wg:.0f}px;background:#fff;border:4px dashed var(--ink);border-radius:14px"></div>
        <div style="position:absolute;left:0;top:0;height:58px;width:{w:.0f}px;background:{'var(--pink)' if hi else 'var(--purple)'};border:4px solid var(--ink);border-radius:14px;box-shadow:5px 5px 0 var(--ink)"></div>
        <div class="d" style="position:absolute;left:{wg + 22:.0f}px;top:6px;font-size:40px">{be:.1f}x <span style="font-family:'DM Sans';font-weight:500;font-size:26px;color:var(--muted)">/ {beg:.1f}x</span></div>
      </div></div>'''
g['break-even-roas-calculator-india'] = (page(f'''
<div class="pill">Break-even ROAS</div>
<div class="d" style="font-size:84px;margin-top:36px">The ROAS you need <span class="hl">to break even</span></div>
<div style="display:flex;gap:40px;margin-top:40px;font-size:26px;font-weight:700;align-items:center">
  <div style="width:150px;text-align:right">Margin</div>
  <div style="display:flex;align-items:center;gap:12px"><span style="width:44px;height:28px;background:var(--purple);border:3px solid var(--ink);border-radius:8px"></span>Break-even ROAS</div>
  <div style="display:flex;align-items:center;gap:12px"><span style="width:44px;height:28px;background:#fff;border:3px dashed var(--ink);border-radius:8px"></span>If GST on ads isn't claimable</div>
</div>
<div style="margin-top:10px">{bars}</div>
<div style="margin-top:46px;display:flex;justify-content:space-between;align-items:center"><div class="d" style="font-size:40px">Break-even ROAS = 1 ÷ contribution margin</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 3. Budget plan ----------
phases = [('1', 'Test', '₹1,500–4,000 / day', '2–4 weeks', ['1 campaign, 1 broad ad set', '4–6 ads, find a winning hook', 'Tracking checked first'], 'Next: 2–3 ads beat break-even', 'var(--yellow)'),
          ('2', 'Learn', '₹4,000–10,000 / day', '4–6 weeks', ['New creative every week', 'Add retargeting', 'Fix the product page'], 'Next: MER on target 3 weeks', 'var(--mint)'),
          ('3', 'Scale', '₹10,000+ / day', 'Ongoing', ['Raise budgets in steps', 'Add catalogue ads', 'Check MER weekly'], 'Pull back if MER drops', 'var(--purple)')]
pc = ''
for i, (n, t, b, wk, ls, nx, c) in enumerate(phases):
    fc = '#fff' if c == 'var(--purple)' else 'var(--ink)'
    li = ''.join(f'<div style="margin-top:12px;display:flex;gap:10px"><span>•</span><span>{l}</span></div>' for l in ls)
    pc += f'''<div class="card" style="flex:1;padding:0;overflow:hidden;margin-top:{(2-i)*60}px">
      <div style="background:{c};color:{fc};padding:24px 30px;border-bottom:5px solid var(--ink)"><div style="font-weight:700;font-size:22px;text-transform:uppercase;letter-spacing:.06em">Phase {n} · {wk}</div><div class="d" style="font-size:60px;margin-top:4px">{t}</div><div style="font-weight:700;font-size:28px;margin-top:6px">{b}</div></div>
      <div style="padding:14px 30px 26px;font-size:26px;line-height:1.3">{li}<div style="margin-top:20px;font-weight:700;font-size:23px;border-top:3px dashed #CFC8E6;padding-top:14px">{nx}</div></div></div>'''
g['meta-ads-budget-india-test-plan'] = (page(f'''
<div class="pill">Meta ads budget plan</div>
<div class="d" style="font-size:84px;margin-top:36px">Test, learn, then <span class="hl">scale</span></div>
<div style="display:flex;gap:30px;margin-top:30px;align-items:flex-start">{pc}</div>
<div style="margin-top:40px;display:flex;justify-content:space-between;align-items:center"><div style="{SRC}"><b style="color:var(--ink)">Rule:</b> weekly budget per ad set ≈ 50 × cost per purchase (Meta's learning phase needs ~50 events a week). Budgets are Amatchless rules of thumb for a ₹400–900 cost per purchase.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 4. Reported ROAS vs blended MER ----------
def side(title, sub, f, items, bg, fc='var(--ink)'):
    li = ''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-top:16px;font-size:27px;line-height:1.25"><span style="flex:none;width:46px;height:46px;border-radius:50%;border:4px solid var(--ink);background:{"var(--mint)" if ok else "var(--pink)"};display:flex;align-items:center;justify-content:center">{(CHECK if ok else CROSS).replace("40", "26")}</span><span>{t}</span></div>' for t, ok in items)
    return f'''<div class="card" style="flex:1;padding:0;overflow:hidden">
      <div style="background:{bg};color:{fc};padding:26px 34px;border-bottom:5px solid var(--ink)"><div class="d" style="font-size:56px">{title}</div><div style="font-size:24px;margin-top:4px;font-weight:500">{sub}</div></div>
      <div style="padding:22px 34px 34px"><div style="background:#F6F3FF;border:3px solid var(--ink);border-radius:18px;padding:14px 20px;font-weight:700;font-size:26px">{f}</div>{li}</div></div>'''
g['reported-roas-vs-blended-mer'] = (page(f'''
<div class="pill">Measure what matters</div>
<div class="d" style="font-size:84px;margin-top:36px">Reported ROAS vs <span class="hl">blended MER</span></div>
<div style="display:flex;gap:40px;margin-top:50px;align-items:stretch">
{side('Meta ROAS', 'From Ads Manager', 'Meta-attributed sales ÷ Meta spend', [('Compare ads and creatives', True), ('Quick daily signal', True), ('Counts refused COD orders', False), ('Misses WhatsApp & marketplace sales', False)], 'var(--yellow)')}
{side('Blended MER', 'From your store data', 'All revenue ÷ all marketing spend', [('Decide total budget', True), ('Net of RTO and returns', True), ('Includes every channel', True), ("Can't pick the winning ad", False)], 'var(--purple)', '#fff')}
</div>
<div style="margin-top:46px;display:flex;justify-content:space-between;align-items:center"><div class="d" style="font-size:40px">ROAS picks the ads. MER picks the budget.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# ---------- 5. Creative testing loop ----------
steps = [('Mon', 'Review', 'Hook rate, CTR, cost per purchase. Keep winners, cut losers.', 'var(--yellow)'),
         ('Tue', 'Brief', '3–5 new concepts. Change one thing per test.', 'var(--mint)'),
         ('Wed–Thu', 'Make', 'Phone-shot, 9:16, a strong first 2 seconds.', 'var(--pink)'),
         ('Fri', 'Launch', 'Into the same testing campaign, so learning isn\'t reset.', 'var(--purple)')]
pos = [(150, 360), (840, 360), (840, 720), (150, 720)]
sc = ''
for (d, t, x, c), (l, tp) in zip(steps, pos):
    fc = '#fff' if c == 'var(--purple)' else 'var(--ink)'
    sc += f'''<div class="card" style="position:absolute;left:{l}px;top:{tp}px;width:610px;padding:26px 32px;display:flex;gap:26px;align-items:center">
      <div class="d" style="flex:none;width:130px;height:130px;border-radius:50%;background:{c};color:{fc};border:4px solid var(--ink);display:flex;align-items:center;justify-content:center;text-align:center;font-size:{40 if len(d) < 4 else 30}px">{d}</div>
      <div><div class="d" style="font-size:48px">{t}</div><div style="font-size:25px;margin-top:6px;line-height:1.3">{x}</div></div></div>'''
g['meta-ads-creative-testing-plan'] = (page(f'''
<div class="pill">Creative testing</div>
<div class="d" style="font-size:84px;margin-top:36px">A weekly loop that <span class="hl" style="background:var(--pink)">keeps ROAS up</span></div>
<svg style="position:absolute;left:0;top:0" width="1600" height="1080" viewBox="0 0 1600 1080"><path d="M770 460 H830 M1145 595 V710 M830 820 H770 M455 710 V595" stroke="#0E0B1F" stroke-width="8" stroke-linecap="round" fill="none"/>
<path d="M815 448 l18 12 -18 12 M1133 695 l12 18 12 -18 M785 808 l-18 12 18 12 M443 610 l12 -18 12 18" stroke="#0E0B1F" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
{sc}
<div style="height:700px"></div>
<div style="display:flex;justify-content:space-between;align-items:center"><div style="{SRC}">Angles that work for Indian D2C: problem first, proof, founder story, occasions (weddings, Diwali), price per use, COD and returns reassurance.</div>{LOGO}</div>
''', 'var(--bg)', 1080), 'png')

if __name__ == "__main__":
    for name, (html, ext) in g.items():
        open(f'{name}.html', 'w').write(html)
    print(' '.join(f'{k}:{v[1]}' for k, v in g.items()))
