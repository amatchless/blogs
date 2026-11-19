"""Upload week 4 to WordPress as a DRAFT via REST with the Application Password.
Credentials come only from env vars WP_USER and WP_APP_PASSWORD (never written to disk).
Writes wp.json (post id, media ids) next to this file. Usage: python3 upload.py"""
import json, os, subprocess, sys, urllib.parse
import requests

D = os.path.dirname(os.path.abspath(__file__))
API = 'https://amatchless.com/wp-json/wp/v2'
S = requests.Session()
S.headers['User-Agent'] = 'Mozilla/5.0 (blog-uploader)'
S.auth = (os.environ['WP_USER'], os.environ['WP_APP_PASSWORD'])

class HTTPErr(Exception): pass

def req(method, path, data=None, raw=None, headers=None):
    r = S.request(method, API + path, json=data, data=raw, headers=headers or {}, timeout=120)
    if r.status_code >= 400:
        print(method, path, r.status_code, r.text[:500]); raise HTTPErr(r.status_code)
    return r.json()

me = req('GET', '/users/me?context=edit')
print('logged in as', me['name'], me.get('roles'))

state_path = f'{D}/wp.json'
state = json.load(open(state_path)) if os.path.exists(state_path) else {}

COVER = 'meta-ads-for-d2c-brands-india'
images = {
    COVER: ('Meta ads for D2C brands in India: budgets, break-even ROAS and what a 4x return looks like',
            'Meta ads for D2C brands in India'),
    'meta-ads-cost-india-2026': ('Meta ads cost in India 2026: CPM, CPC and cost per lead ranges for Facebook and Instagram, plus 18% GST',
                                 'Meta ads cost in India 2026'),
    'break-even-roas-calculator-india': ('Break-even ROAS calculator for D2C brands in India: contribution margin vs the ROAS you need, with and without GST on ad spend',
                                         'Break-even ROAS calculator for India'),
    'meta-ads-budget-india-test-plan': ('Meta ads budget plan for D2C brands in India: test, learn and scale phases with daily spend and when to move on',
                                        'Meta ads budget plan for India'),
    'reported-roas-vs-blended-mer': ('Reported ROAS vs blended MER for D2C brands in India: what each measures and when to use it',
                                     'Reported ROAS vs blended MER'),
    'meta-ads-creative-testing-plan': ('Meta ads creative testing plan for D2C brands: a weekly review, brief, make and launch loop',
                                       'Meta ads creative testing plan'),
}

media = state.setdefault('media', {})
for name, (alt, title) in images.items():
    if name in media: continue
    ext = 'jpg' if name == COVER else 'webp'
    fn = f'{name}.{ext}'
    raw = open(f'{D}/images/{fn}', 'rb').read()
    m = req('POST', '/media', raw=raw, headers={'Content-Disposition': f'attachment; filename="{fn}"',
            'Content-Type': 'image/jpeg' if ext == 'jpg' else 'image/webp'})
    m = req('POST', f"/media/{m['id']}", {'alt_text': alt, 'title': title, 'caption': ''})
    media[name] = dict(id=m['id'], url=m['source_url'], alt=alt,
                       w=m['media_details'].get('width'), h=m['media_details'].get('height'))
    json.dump(state, open(state_path, 'w'), indent=1)
    print('uploaded', fn, m['id'])

mj = '/tmp/week04-media.json'
json.dump({k: v for k, v in media.items() if k != COVER}, open(mj, 'w'), ensure_ascii=False)
subprocess.check_call([sys.executable, f'{D}/build.py', mj])
content = open(f'{D}/post-wordpress.html').read()

def tag_id(name):
    for t in req('GET', f'/tags?search={urllib.parse.quote(name)}'):
        if t['name'].lower() == name.lower(): return t['id']
    try:
        return req('POST', '/tags', {'name': name})['id']
    except HTTPErr:
        print('could not create tag', name); return None
tags = [t for t in (tag_id(n) for n in ['India', 'Meta ads', 'D2C', 'ROAS', 'Instagram ads']) if t]

desc = ('Meta ads for D2C brands in India: 2026 costs with GST, how to work out break-even ROAS, test budgets, '
        'reported ROAS vs MER, and how a 4x account is built.')
post = {
    'title': 'Meta Ads for D2C Brands in India: Budgets, Break-even ROAS and What 4x Looks Like',
    'slug': 'meta-ads-for-d2c-brands-india', 'status': 'draft', 'content': content, 'excerpt': desc,
    'categories': [5], 'tags': tags, 'featured_media': media[COVER]['id'],
    'meta': {'_yoast_wpseo_title': 'Meta Ads for D2C Brands in India: Budget & ROAS (2026)',
             '_yoast_wpseo_metadesc': desc, '_yoast_wpseo_focuskw': 'meta ads for d2c brands india'},
}
if 'post_id' in state:
    p = req('POST', f"/posts/{state['post_id']}", post)
else:
    p = req('POST', '/posts', post); state['post_id'] = p['id']
state.update(status=p['status'], slug=p['slug'], preview=p['link'])
json.dump(state, open(state_path, 'w'), indent=1)
for name, m in media.items():
    try: req('POST', f"/media/{m['id']}", {'post': p['id']})
    except HTTPErr: pass
print('draft', p['id'], p['status'], p['link'])
chk = req('GET', f"/posts/{p['id']}?context=edit")
print('meta', {k: chk.get('meta', {}).get(k) for k in post['meta']})
print('tables', chk['content']['raw'].count('amx-table'), 'figures', chk['content']['raw'].count('<figure'),
      'len', len(chk['content']['raw']), 'sent', len(content))
