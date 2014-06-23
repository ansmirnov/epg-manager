__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

import re

HTML_ESCAPE = {
    '&amp;': ' ',
    '&lt;': '<',
    '&gt;': '>',
    '&nbsp;': ' ',
}

def clean(html):
    html = re.sub(r'\<[^>]*\>', '', html)
    for s, r in HTML_ESCAPE.items():
        html = html.replace(s, r)
    return html