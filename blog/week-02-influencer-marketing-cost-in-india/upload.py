"""Upload week 2 as a WordPress DRAFT via REST with an Application Password.
Credentials come only from env vars WP_USER and WP_APP_PASS (or WP_PASS for cookie login) (never written to disk).
Usage: WP_USER=... WP_APP_PASS=... python3 upload.py"""
import json, os, subprocess, sys, urllib.parse

D = os.path.dirname(os.path.abspath(__file__))
S = '/tmp/claude-0/-home-user/a2244e3e-ebe2-5a93-8b37-347f8381d6e9/scratchpad'
API = 'https://amatchless.com/wp-json/wp/v2'
import requests
SESSION = requests.Session()
SESSION.headers['User-Agent'] = 'Mozilla/5.0 (blog-uploader)'
if os.environ.get('WP_APP_PASS'):
    SESSION.auth = (os.environ['WP_USER'], os.environ['WP_APP_PASS'])
else:  # cookie login + rest nonce (password only in env, never on disk)
    SESSION.get('https://amatchless.com/wp-login.php')
    r = SESSION.post('https://amatchless.com/wp-login.php', data={'log': os.environ['WP_USER'], 'pwd': os.environ['WP_PASS'],
        'wp-submit': 'Log In', 'redirect_to': 'https://amatchless.com/wp-admin/', 'testcookie': '1'})
    nonce = SESSION.get('https://amatchless.com/wp-admin/admin-ajax.php?action=rest-nonce').text.strip()
    assert nonce and nonce != '0', 'login failed'
    SESSION.headers['X-WP-Nonce'] = nonce

class HTTPErr(Exception): pass

def req(method, path, data=None, raw=None, headers=None):
    r = SESSION.request(method, API + path, json=data, data=raw, headers=headers or {})
    if r.status_code >= 400:
        print(method, path, r.status_code, r.text[:500]); raise HTTPErr(r.status_code)
    return r.json()

me = req('GET', '/users/me?context=edit')
print('logged in as', me['name'], me.get('roles'))

state_path = f'{S}/upload-state.json'
state = json.load(open(state_path)) if os.path.exists(state_path) else {}

alts = json.load(open(f'{S}/alts.json'))
alts['influencer-marketing-cost-in-india'] = 'Influencer marketing cost in India 2026: creator rate card by tier, from nano to celebrity'
titles = {
 'influencer-marketing-cost-in-india': 'Influencer marketing cost in India 2026',
 'influencer-rates-india-2026-by-tier': 'Influencer rates in India 2026 by tier',
 'true-cost-of-an-influencer-reel-india': 'True cost of an influencer Reel in India',
 'influencer-marketing-budget-india': 'Influencer marketing budget in India',
 'influencer-campaign-roi-example-india': 'Influencer campaign ROI example',
 'how-to-run-an-influencer-campaign-india': 'How to run an influencer campaign in India',
}

media = state.setdefault('media', {})
for name in titles:
    if name in media: continue
    ext = 'jpg' if name == 'influencer-marketing-cost-in-india' else 'webp'
    fn = f'{name}.{ext}'
    raw = open(f'{D}/images/{fn}', 'rb').read()
    m = req('POST', '/media', raw=raw, headers={'Content-Disposition': f'attachment; filename="{fn}"',
            'Content-Type': 'image/jpeg' if ext == 'jpg' else 'image/webp'})
    m = req('POST', f"/media/{m['id']}", {'alt_text': alts[name], 'title': titles[name], 'caption': ''})
    media[name] = dict(id=m['id'], url=m['source_url'], alt=alts[name],
                       w=m['media_details'].get('width'), h=m['media_details'].get('height'))
    json.dump(state, open(state_path, 'w'))
    print('uploaded', fn, m['id'])

json.dump({k: v for k, v in media.items() if k != 'influencer-marketing-cost-in-india'}, open(f'{S}/media.json', 'w'), ensure_ascii=False)
subprocess.check_call([sys.executable, f'{D}/build.py', f'{S}/media.json'])
content = open(f'{D}/post-wordpress.html').read()

def tag_id(name):
    found = req('GET', f'/tags?search={urllib.parse.quote(name)}')
    for t in found:
        if t['name'].lower() == name.lower(): return t['id']
    try:
        return req('POST', '/tags', {'name': name})['id']
    except HTTPErr:
        print('could not create tag', name); return None
tags = [t for t in (tag_id(n) for n in ['India', 'Influencer marketing', 'Instagram']) if t]

desc = 'What Indian influencers charge in 2026 by tier and format, the hidden costs, what your budget buys, and how to run a campaign that pays back.'
post = {
    'title': 'Influencer Marketing in India: What Creators Charge in 2026 and How to Run a Campaign That Pays Back',
    'slug': 'influencer-marketing-cost-in-india', 'status': 'draft', 'content': content, 'excerpt': desc,
    'categories': [7], 'tags': tags, 'featured_media': media['influencer-marketing-cost-in-india']['id'],
    'meta': {'_yoast_wpseo_title': 'Influencer Marketing Cost in India (2026 Rates & Guide)',
             '_yoast_wpseo_metadesc': desc, '_yoast_wpseo_focuskw': 'influencer marketing cost in india'},
}
if 'post_id' in state:
    p = req('POST', f"/posts/{state['post_id']}", post)
else:
    p = req('POST', '/posts', post); state['post_id'] = p['id']; json.dump(state, open(state_path, 'w'))
for name, m in media.items():
    try: req('POST', f"/media/{m['id']}", {'post': p['id']})
    except HTTPErr: pass
print('draft', p['id'], p['status'], p['link'])
chk = req('GET', f"/posts/{p['id']}?context=edit")
print('meta', {k: chk.get('meta', {}).get(k) for k in post['meta']})
print('tables', chk['content']['raw'].count('amx-table'), 'figures', chk['content']['raw'].count('<figure'), 'len', len(chk['content']['raw']), 'sent', len(content))
