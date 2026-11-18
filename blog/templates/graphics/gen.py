import sys
sys.path.insert(0, '.')
from logo import LOGO, STAR

def page(body, bg, h=None):
    hs = f'height:{h}px;' if h else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"></head><body><div class="c" id="g" style="background:{bg};{hs}">{body}</div></body></html>'

CHECK = '<svg width="40" height="40" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#0E0B1F" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
WA = '<svg width="54" height="54" viewBox="0 0 32 32"><circle cx="16" cy="16" r="15" fill="#3DEBB0" stroke="#0E0B1F" stroke-width="2.5"/><path d="M11 10.5c.6-1 1.6-1 2 .2l.8 2c.2.6 0 1-.5 1.5l-.6.6c.8 1.8 2.3 3.3 4.1 4.1l.6-.6c.5-.5.9-.7 1.5-.5l2 .8c1.2.4 1.2 1.4.2 2-2 1.5-4.5.8-7-1.7s-3.2-5-1.1-8.4z" fill="#0E0B1F"/></svg>'

g = {}

# 1. Featured image 1600x1000
g['ai-automation-small-business-india'] = (page(f'''
<div class="pill">Automation guide · 2026</div>
<div class="d" style="font-size:118px;margin-top:70px;width:900px">AI automation for <span class="hl">small business</span> in India.</div>
<div style="font-size:38px;font-weight:500;margin-top:40px;width:820px;color:var(--muted)">What to automate first, what it costs in ₹, and a 30-day plan.</div>
<div style="position:absolute;left:110px;bottom:80px">{LOGO}</div>
<div style="position:absolute;right:110px;top:110px;width:500px">
  <div class="card" style="padding:28px 30px;border-radius:44px">
    <div style="display:flex;align-items:center;gap:18px;border-bottom:4px solid var(--ink);padding-bottom:20px">{WA}<div><div style="font-weight:700;font-size:30px">Your business</div><div style="font-size:22px;color:var(--muted)">auto-reply · online</div></div></div>
    <div style="margin-top:24px;background:#EEEAF7;border:3px solid var(--ink);border-radius:26px 26px 26px 6px;padding:16px 22px;font-size:26px;width:330px">Hi, what are your prices?</div>
    <div style="margin:18px 0 0 auto;background:var(--mint);border:3px solid var(--ink);border-radius:26px 26px 6px 26px;padding:16px 22px;font-size:26px;width:370px">Here's our price list 📄 Want to book a slot today?</div>
    <div style="margin-top:18px;background:#EEEAF7;border:3px solid var(--ink);border-radius:26px 26px 26px 6px;padding:16px 22px;font-size:26px;width:200px">Yes, 5 pm!</div>
    <div style="margin:18px 0 0 auto;background:var(--yellow);border:3px solid var(--ink);border-radius:26px 26px 6px 26px;padding:16px 22px;font-size:26px;width:330px">Booked ✅ Reminder sent.</div>
  </div>
  <div class="card" style="position:absolute;left:-90px;bottom:-110px;background:var(--pink);color:#fff;padding:18px 28px;border-radius:999px;font-weight:700;font-size:30px;transform:rotate(-4deg)">Reply time: under 1 min</div>
</div>
<div style="position:absolute;right:70px;bottom:60px;width:120px;height:120px;border-radius:50%;background:var(--purple);border:5px solid var(--ink);display:flex;align-items:center;justify-content:center;color:#fff;font-family:'Bricolage Grotesque';font-weight:800;font-size:64px">₹</div>
''', 'var(--yellow)', 1000), 'jpg')

# 2. Rules vs AI
def col(title, bg, icon, lines, ex):
    li = ''.join(f'<li style="display:flex;gap:14px;align-items:flex-start;margin-top:16px">{CHECK}<span>{l}</span></li>' for l in lines)
    return f'''<div class="card" style="flex:1;padding:44px;display:flex;flex-direction:column">
      <div style="display:flex;align-items:center;gap:20px"><div style="width:84px;height:84px;border-radius:24px;background:{bg};border:4px solid var(--ink);display:flex;align-items:center;justify-content:center;font-size:44px">{icon}</div>
      <div class="d" style="font-size:54px">{title}</div></div>
      <ul style="list-style:none;font-size:30px;margin:26px 0 30px">{li}</ul>
      <div style="margin-top:auto;padding-top:0;background:#F3F0FB;border:3px dashed var(--ink);border-radius:22px;padding:20px 24px;font-size:26px"><b>Example:</b> {ex}</div></div>'''
g['rule-based-vs-ai-automation'] = (page(f'''
<div class="pill">Know the difference</div>
<div class="d" style="font-size:84px;margin-top:36px">Rules move the data. <span class="hl" style="background:var(--pink)">AI reads it.</span></div>
<div style="display:flex;gap:44px;margin-top:60px">
{col('Rule-based', 'var(--mint)', '⚙️', ['Fixed “if this, then that” steps','Moving data, reminders, reports','Low risk: does exactly what you set'], 'new form entry → Google Sheet → WhatsApp template')}
{col('AI automation', 'var(--yellow)', '✨', ['Reads, writes and decides on messy inputs','Answers questions, qualifies leads, reads invoices','Medium risk: needs guardrails and a human fallback'], 'reads a WhatsApp message, replies in your voice, flags hot leads')}
</div>
<div style="margin-top:56px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:30px;font-weight:500">Best small-business systems use both.</div>{LOGO}</div>
''', 'var(--mint)'), 'png')

# 3. 10 tasks
tasks = [('Lead capture','Low'),('First reply to every lead','Low'),('Follow-up sequences','Low'),('WhatsApp FAQs','Medium'),('Appointment booking and reminders','Low'),('Payment reminders','Low'),('Review requests','Low'),('Invoice and document reading','Medium'),('Weekly reporting','Medium'),('Content first drafts','Low')]
cols = ['var(--yellow)','var(--mint)','var(--pink)','#fff','var(--purple)']
rows = ''
for i,(t,e) in enumerate(tasks):
    c = cols[i%5]; fc = '#fff' if c=='var(--purple)' else 'var(--ink)'
    eb = 'var(--mint)' if e=='Low' else 'var(--yellow)'
    rows += f'''<div class="card" style="display:flex;align-items:center;gap:24px;padding:20px 26px;border-radius:999px;box-shadow:7px 7px 0 var(--ink)">
      <div style="width:74px;height:74px;flex:none;border-radius:50%;background:{c};color:{fc};border:4px solid var(--ink);display:flex;align-items:center;justify-content:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:38px">{i+1}</div>
      <div style="flex:1;font-weight:700;font-size:32px;line-height:1.1">{t}</div>
      <div class="tag" style="background:{eb};font-size:22px">{e}</div></div>'''
g['10-tasks-to-automate-first'] = (page(f'''
<div style="display:flex;justify-content:space-between;align-items:flex-end">
<div><div class="pill">Start here</div>
<div class="d" style="font-size:92px;margin-top:36px">10 tasks to <span class="hl">automate</span> first</div>
<div style="font-size:30px;margin-top:26px;color:var(--muted)">Ranked by frequency, closeness to revenue and ease of setup.</div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;grid-auto-flow:column;grid-template-rows:repeat(5,auto);gap:30px 40px;margin-top:56px">{rows}</div>
<div style="margin-top:56px;display:flex;justify-content:space-between;align-items:center"><div style="display:flex;gap:16px;align-items:center;font-size:26px;font-weight:500">Effort to set up: <span class="tag" style="background:var(--mint);font-size:22px">Low</span><span class="tag" style="background:var(--yellow);font-size:22px">Medium</span></div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# 4. WhatsApp cost
def rate(cat, use, price, bg):
    return f'''<div class="card" style="padding:30px 32px;background:{bg}"><div style="font-weight:700;font-size:28px;text-transform:uppercase;letter-spacing:.06em">{cat}</div>
    <div class="d" style="font-size:76px;margin-top:14px">{price}</div><div style="font-size:24px;margin-top:10px">{use}</div></div>'''
g['whatsapp-business-api-cost-india-2026'] = (page(f'''
<div class="pill">WhatsApp Business API · India 2026</div>
<div class="d" style="font-size:84px;margin-top:36px">What a WhatsApp message <span class="hl" style="background:var(--pink)">really costs</span></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:30px;margin-top:56px">
{rate('Marketing','Offers, launches, re-engagement','₹0.86','var(--pink)')}
{rate('Utility','Order updates, bookings, payment reminders','₹0.12','var(--mint)')}
{rate('Authentication','One-time passwords (OTPs)','₹0.12','var(--yellow)')}
{rate('Service','Replies within 24 hours. First 1,000 a month free','Free','#fff')}
</div>
<div class="card" style="margin-top:50px;padding:40px 44px;display:flex;gap:50px;align-items:center;background:var(--ink);color:#fff;box-shadow:10px 10px 0 var(--purple)">
  <div style="flex:1"><div style="font-weight:700;font-size:26px;letter-spacing:.06em;text-transform:uppercase;color:var(--yellow)">Worked example: a clinic</div>
  <div style="font-size:30px;margin-top:18px;line-height:1.5">2,000 reminders × ₹0.115 = <b>₹230</b><br>2,000 offers × ₹0.8631 = <b>₹1,726</b><br>₹1,956 + 18% GST</div></div>
  <div style="text-align:right"><div class="d" style="font-size:120px;color:var(--mint)">₹2,308</div><div style="font-size:26px;margin-top:8px">a month in Meta charges, plus BSP fee</div></div>
</div>
<div style="margin-top:44px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Per delivered message, before 18% GST and provider fees. Indicative rates from Oct 2026; check Meta's rate card before budgeting.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# 5. Cost levels
def lvl(n, name, setup, monthly, best, bg, h):
    return f'''<div class="card" style="flex:1;padding:40px;background:{bg};margin-top:{h}px">
    <div style="width:84px;height:84px;border-radius:50%;background:#fff;border:4px solid var(--ink);display:flex;align-items:center;justify-content:center" class="d"><span style="font-size:46px">{n}</span></div>
    <div class="d" style="font-size:46px;margin-top:24px;line-height:1">{name}</div>
    <div style="margin-top:30px;font-size:22px;font-weight:700;text-transform:uppercase;letter-spacing:.06em">One-time setup</div>
    <div class="d" style="font-size:44px;margin-top:6px">{setup}</div>
    <div style="margin-top:24px;font-size:22px;font-weight:700;text-transform:uppercase;letter-spacing:.06em">Monthly</div>
    <div class="d" style="font-size:44px;margin-top:6px">{monthly}</div>
    <div style="margin-top:28px;border-top:3px solid var(--ink);padding-top:20px;font-size:26px"><b>Best for:</b> {best}</div></div>'''
g['ai-automation-cost-india-3-levels'] = (page(f'''
<div class="pill">Costs in ₹</div>
<div class="d" style="font-size:84px;margin-top:36px">How much does AI automation <span class="hl">cost in India?</span></div>
<div style="display:flex;gap:36px;margin-top:40px;align-items:flex-start">
{lvl(1,'DIY with off-the-shelf tools','₹0','₹0 – ₹5,000','solo founders and teams under 5','var(--mint)',80)}
{lvl(2,'Off-the-shelf, set up by pros','₹15k – ₹75k','₹3k – ₹20k','most small businesses with steady leads','var(--yellow)',40)}
{lvl(3,'Custom-built','₹1.5L – ₹6L+','₹8k – ₹60k','a proven process tools can’t handle','var(--pink)',0)}
</div>
<div style="margin-top:50px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:22px;color:var(--muted);width:1000px">Indicative ranges. Levels 1–2: Amatchless planning ranges. Level 3 per workflow, consistent with Nexolve's published SMB ranges.</div>{LOGO}</div>
''', 'var(--bg)'), 'png')

# 6. 30-day plan
weeks = [('Week 1','Find the bottleneck','List repetitive tasks, pick one, record today’s numbers.','var(--yellow)'),
         ('Week 2','Map it and clean it','Draw the process, fix messy data, submit WhatsApp templates.','var(--mint)'),
         ('Week 3','Build and test quietly','Run it alongside the manual process. Add a “talk to a person” option.','var(--pink)'),
         ('Week 4','Switch on and measure','Go live, compare with week 1. Keep it, fix it or kill it.','var(--purple)')]
wk = ''
for i,(w,t,d,c) in enumerate(weeks):
    fc = '#fff' if c=='var(--purple)' else 'var(--ink)'
    wk += f'''<div style="flex:1;position:relative"><div style="width:110px;height:110px;border-radius:50%;background:{c};color:{fc};border:5px solid var(--ink);display:flex;align-items:center;justify-content:center;position:relative;z-index:2" class="d"><span style="font-size:56px">{i+1}</span></div>
    <div class="card" style="margin-top:34px;padding:32px;height:360px;box-shadow:8px 8px 0 var(--ink)"><div style="font-weight:700;font-size:24px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)">{w}</div>
    <div class="d" style="font-size:42px;margin-top:12px;line-height:1">{t}</div><div style="font-size:26px;margin-top:18px;line-height:1.35">{d}</div></div></div>'''
g['30-day-ai-automation-plan'] = (page(f'''
<div class="pill">Your first 30 days</div>
<div class="d" style="font-size:84px;margin-top:36px">Launch your first automation in <span class="hl">30 days</span></div>
<div style="position:relative;margin-top:60px"><div style="position:absolute;left:55px;right:200px;top:52px;border-top:5px dashed var(--ink)"></div>
<div style="display:flex;gap:30px">{wk}</div></div>
<div style="margin-top:56px;display:flex;justify-content:space-between;align-items:center"><div class="d" style="font-size:40px">One automation that works beats ten that half-work.</div>{LOGO}</div>
''', 'var(--mint)'), 'png')

if __name__ == "__main__":
    for name, (html, ext) in g.items():
        html = html.replace('₹', '<span style="font-family:Bricolage Grotesque">₹</span>')
        open(f'{name}.html', 'w').write(html)
    print('\n'.join(f'{k} {v[1]}' for k, v in g.items()))
