import sys
sys.path.insert(0, '.')
from logo import LOGO
from gen import page, WA
# Centre-safe layout: all text sits in the middle 960px so the /blog/ card can crop the sides (down to ~1:1).
bub = 'border:4px solid var(--ink);padding:14px 20px;font-size:24px;box-shadow:6px 6px 0 var(--ink);position:absolute;white-space:nowrap'
html = page(f'''
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 330px">
  <div class="pill">Automation guide · 2026</div>
  <div class="d" style="font-size:104px;margin-top:44px">AI automation for <span class="hl">small business</span> in India.</div>
  <div style="font-size:34px;font-weight:500;margin-top:34px;color:var(--muted);max-width:700px">What to automate first, what it costs, and a 30-day plan.</div>
  <div style="margin-top:56px">{LOGO}</div>
</div>
<div style="{bub};left:-40px;top:150px;background:#fff;border-radius:24px 24px 24px 6px;transform:rotate(-6deg)">Hi, what are your prices?</div>
<div style="{bub};left:40px;top:290px;background:var(--mint);border-radius:24px 24px 6px 24px;transform:rotate(3deg)">Here's our price list 📄</div>
<div style="{bub};left:-20px;top:430px;background:#fff;border-radius:24px 24px 24px 6px;transform:rotate(-3deg)">Yes, book 5 pm!</div>
<div style="{bub};left:30px;top:570px;background:var(--pink);color:#fff;border-radius:24px 24px 6px 24px;transform:rotate(4deg)">Booked ✅ Reminder sent</div>
<div style="position:absolute;left:70px;bottom:90px">{WA.replace('54','110')}</div>
<div style="position:absolute;right:60px;top:110px;width:190px;height:190px;border-radius:50%;background:var(--purple);border:6px solid var(--ink);box-shadow:8px 8px 0 var(--ink);display:flex;align-items:center;justify-content:center;color:#fff;font-family:'Bricolage Grotesque';font-weight:800;font-size:110px">₹</div>
<div class="card" style="position:absolute;right:-30px;top:420px;background:var(--mint);padding:22px 30px;border-radius:999px;font-weight:700;font-size:30px;transform:rotate(-5deg);white-space:nowrap">Reply in under 1 min</div>
<div class="card" style="position:absolute;right:50px;bottom:110px;background:#fff;padding:20px 26px;border-radius:28px;font-weight:700;font-size:28px;transform:rotate(4deg)">⚡ 10 tasks<br>₹ real costs<br>📅 30-day plan</div>
''', 'var(--yellow)', 1000)
open('ai-automation-small-business-india-guide.html', 'w').write(html.replace('₹', '<span style="font-family:Bricolage Grotesque">₹</span>'))
