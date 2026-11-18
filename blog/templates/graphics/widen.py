"""Make the post's text as wide as its images and tables (up to 1100px, 16px side gutter on phones).

The theme limits .prose to 760px and Author accounts can't change theme CSS, so every top-level
text block (p, h2, h3, ul, ol, blockquote, hr) gets the same inline breakout style the figures and
tables use. Blocks are styled one by one (not wrapped in a div) so the theme's `.prose > * + *`
spacing still applies. Usage: from widen import widen; html = widen(html)"""
import re

WIDE = 'width:min(1100px, calc(100vw - 32px));max-width:none;margin-left:calc(50% - min(550px, calc(50vw - 16px)))'
BLOCKS = ('p', 'h2', 'h3', 'h4', 'ul', 'ol', 'blockquote', 'hr')
VOID = {'hr', 'br', 'img', 'input', 'meta', 'link', 'source', 'wbr'}


def widen(html):
    out, depth, pos = [], 0, 0
    for m in re.finditer(r'<(/?)([a-zA-Z0-9]+)([^>]*)>', html):
        closing, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        out.append(html[pos:m.start()])
        piece = m.group(0)
        if closing:
            depth -= 1
        else:
            if depth == 0 and tag in BLOCKS and 'style=' not in attrs:
                self_close = attrs.rstrip().endswith('/')
                a = attrs.rstrip()[:-1].rstrip() if self_close else attrs
                piece = f'<{m.group(2)}{a} style="{WIDE}"' + (' />' if self_close else '>')
            if tag not in VOID and not attrs.rstrip().endswith('/'):
                depth += 1
        out.append(piece)
        pos = m.end()
    out.append(html[pos:])
    assert depth == 0, f'unbalanced html (depth {depth})'
    return ''.join(out)
