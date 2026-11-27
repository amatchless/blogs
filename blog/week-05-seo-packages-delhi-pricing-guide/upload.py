"""Upload week 5 to WordPress as a DRAFT via REST with the Application Password.
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

def req(method, path, data=None, raw=None, headers=None, tries=4):
    import time
    for i in range(tries):
        r = S.request(method, API + path, json=data, data=raw, headers=headers or {}, timeout=120)
        if r.status_code >= 400:
            print(method, path, r.status_code, r.text[:500]); raise HTTPErr(r.status_code)
        try:
            return r.json()
        except ValueError:  # host sometimes returns a non-JSON page; retry
            print('non-JSON reply, retrying', method, path, r.status_code, r.text[:120].replace('\n', ' '))
            if method != 'GET' and path == '/media': raise
            time.sleep(3 * (i + 1))
    raise HTTPErr('non-json')

me = req('GET', '/users/me?context=edit')
print('logged in as', me['name'], me.get('roles'))

state_path = f'{D}/wp.json'
state = json.load(open(state_path)) if os.path.exists(state_path) else {}

COVER = 'seo-packages-in-delhi'
images = {
    COVER: ('SEO packages in Delhi: entry, growth and advanced price tiers in rupees, and what each one includes',
            'SEO packages in Delhi'),
    'seo-pricing-models-delhi': ('SEO pricing models in Delhi: monthly retainer, one-time project and performance-linked deals compared',
                                 'SEO pricing models in Delhi'),
    'seo-charges-in-delhi-by-business-type': ('SEO charges in Delhi by business type: local shop, B2B service firm and D2C online store, with monthly price ranges',
                                              'SEO charges in Delhi by business type'),
    'seo-packages-in-delhi-price-tiers': ('SEO packages in Delhi: entry, growth and advanced tiers with monthly price ranges and what each includes',
                                          'SEO packages in Delhi price tiers'),
    'cheap-seo-red-flags-delhi': ('Cheap SEO red flags in Delhi: guaranteed rankings, bulk backlinks, no access to your own data, secret methods and long lock-ins',
                                  'Cheap SEO red flags'),
    'compare-seo-quotes-checklist': ('Checklist to compare two SEO quotes in Delhi: deliverables, people, access, links, reporting and exit terms',
                                     'Checklist to compare SEO quotes'),
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

mj = '/tmp/week05-media.json'
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
tags = [t for t in (tag_id(n) for n in ['India', 'Delhi', 'SEO', 'SEO pricing', 'Local SEO']) if t]

desc = ('SEO packages in Delhi explained: 2026 prices for entry, growth and advanced tiers, how agencies charge, cheap SEO red flags and how to compare quotes.')
post = {
    'title': 'SEO Packages in Delhi: What Each Price Tier Includes and What to Ask Before You Pay',
    'slug': 'seo-packages-delhi-pricing-guide', 'status': 'publish', 'content': content, 'excerpt': desc,
    'categories': [6], 'tags': tags, 'featured_media': media[COVER]['id'],
    'meta': {'_yoast_wpseo_title': 'SEO Packages in Delhi: Prices, Tiers & What to Ask (2026)',
             '_yoast_wpseo_metadesc': desc, '_yoast_wpseo_focuskw': 'seo packages in delhi'},
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
