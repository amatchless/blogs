"""New unique covers for week 1 and week 2 (18 Nov 2026). Run from a copy of templates/graphics."""
import sys
sys.path.insert(0, '.')
from logo import LOGO
from gen import page, WA, CHECK
R = '<span style="font-family:Bricolage Grotesque">₹</span>'
g = {}

# ---------- Week 1: ink background, automation flow ----------
dots = ''.join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#3A3550"/>' for x in range(20, 1600, 40) for y in range(20, 1000, 40))
def node(icon, label, bg, rot):
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px;transform:rotate({rot}deg)">'
            f'<div style="width:118px;height:118px;border-radius:30px;background:{bg};border:5px solid #fff;box-shadow:7px 7px 0 var(--purple);display:flex;align-items:center;justify-content:center;font-size:58px">{icon}</div>'
            f'<div style="color:#fff;font-weight:700;font-size:24px;white-space:nowrap">{label}</div></div>')
arrow = '<svg width="54" height="30" viewBox="0 0 54 30" style="margin-top:44px;flex:none"><path d="M2 15 H44 M34 4 L48 15 L34 26" fill="none" stroke="#FFE14D" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
flow = arrow.join([node('💬', 'New enquiry', 'var(--mint)', -3), node('⚡', 'Instant reply', 'var(--yellow)', 2), node('📅', 'Booked', 'var(--pink)', -2), node('🧾', 'Invoice sent', '#fff', 3)])
logo_w = LOGO.replace('<div class="logo">', '<div class="logo" style="color:#fff">')
g['ai-automation-small-business-india-cover'] = (page(f'''
<svg style="position:absolute;inset:0" width="1600" height="1000">{dots}</svg>
<div style="position:absolute;left:-60px;top:-60px;width:300px;height:300px;border-radius:50%;background:var(--purple);border:6px solid #fff"></div>
<div style="position:absolute;right:-80px;bottom:-90px;width:340px;height:340px;border-radius:50%;background:var(--mint);border:6px solid #fff"></div>
<div style="position:absolute;left:70px;bottom:110px;color:var(--yellow);font-family:'Bricolage Grotesque';font-weight:800;font-size:120px;transform:rotate(-12deg)">⚙</div>
<div style="position:absolute;right:90px;top:120px;background:var(--pink);color:#fff;border:5px solid #fff;border-radius:999px;padding:14px 26px;font-weight:700;font-size:28px;transform:rotate(8deg)">24/7</div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 330px">
  <div style="color:var(--mint);font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase">Small business · India · 2026</div>
  <div class="d" style="font-size:96px;color:#fff;margin-top:26px">Put your busywork on <span style="background:var(--mint);color:var(--ink);padding:0 .14em .04em;border-radius:.18em;display:inline-block;transform:rotate(-2deg)">autopilot</span></div>
  <div style="font-size:32px;color:#C9C3E0;margin-top:24px">AI automation: what to automate first, real costs, a 30-day plan</div>
  <div style="display:flex;align-items:flex-start;gap:14px;margin-top:52px">{flow}</div>
  <div style="margin-top:50px">{logo_w}</div>
</div>
''', 'var(--ink)', 1000), 'jpg')

# ---------- Week 2: pink background, row of creator price cards ----------
def creator(tier, price, bg, rot, top, fc='var(--ink)'):
    return (f'<div class="card" style="width:196px;padding:22px 18px;background:{bg};color:{fc};transform:rotate({rot}deg);margin-top:{top}px;text-align:center">'
            f'<div style="width:84px;height:84px;margin:0 auto;border-radius:50%;background:#fff;border:4px solid var(--ink);display:flex;align-items:center;justify-content:center;font-size:44px">🤳</div>'
            f'<div class="d" style="font-size:34px;margin-top:14px">{tier}</div>'
            f'<div style="font-weight:700;font-size:23px;margin-top:6px;white-space:nowrap">{price}</div></div>')
cards = ''.join([creator('Nano', f'from {R}1K', 'var(--mint)', -5, 30), creator('Micro', f'from {R}8K', 'var(--yellow)', 3, 0),
                 creator('Mid-tier', f'from {R}50K', '#fff', -3, 24), creator('Celeb', f'{R}25L+', 'var(--purple)', 5, 4, '#fff')])
HEART = '<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-9.5-9.3C1.2 8.5 3.3 5 6.7 5c2 0 3.5 1.1 5.3 3 1.8-1.9 3.3-3 5.3-3 3.4 0 5.5 3.5 4.2 6.7C19.5 16.4 12 21 12 21z" fill="#fff" stroke="#0E0B1F" stroke-width="1.8"/></svg>'
g['influencer-marketing-cost-in-india-cover'] = (page(f'''
<div style="position:absolute;left:40px;top:90px;transform:rotate(-12deg)">{HEART.format(s=140)}</div>
<div style="position:absolute;left:150px;top:700px;transform:rotate(10deg)">{HEART.format(s=80)}</div>
<div style="position:absolute;right:50px;top:160px;transform:rotate(14deg)">{HEART.format(s=100)}</div>
<div style="position:absolute;right:-10px;top:620px;background:#fff;border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);border-radius:999px;padding:14px 26px;font-weight:700;font-size:30px;transform:rotate(-8deg)">#ad #collab</div>
<div style="position:absolute;left:-30px;top:430px;background:var(--yellow);border:5px solid var(--ink);box-shadow:8px 8px 0 var(--ink);border-radius:999px;padding:14px 26px;font-weight:700;font-size:30px;transform:rotate(6deg)">▶ 1.2M views</div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 330px">
  <div class="pill" style="background:#fff;color:var(--ink);border:4px solid var(--ink)">India rate card · 2026</div>
  <div class="d" style="font-size:94px;margin-top:34px">What do <span style="background:var(--ink);color:#fff;padding:0 .14em .04em;border-radius:.18em;display:inline-block;transform:rotate(-2deg)">influencers</span> really cost?</div>
  <div style="display:flex;gap:22px;margin-top:50px;align-items:flex-start">{cards}</div>
  <div style="margin-top:48px;background:#fff;border:4px solid var(--ink);border-radius:999px;padding:8px 26px">{LOGO}</div>
</div>
''', 'var(--pink)', 1000), 'jpg')

if __name__ == '__main__':
    for name, (html, ext) in g.items():
        open(f'{name}.html', 'w').write(html.replace('₹', R) if '₹' in html else html)
    print(' '.join(f'{k}:{v[1]}' for k, v in g.items()))
