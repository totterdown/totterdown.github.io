#!/usr/bin/env python3
"""Site-wide checks for every page in site/.

    python3 _build/check.py

Checks: JSON-LD parses; internal links, anchors and assets exist; citations
match the sources list and are numbered in order; tables are wrapped; every
page uses the current asset version, the same navigation and the footer note;
one H1 per page; titles are 60 characters or fewer and descriptions 155 or
fewer; indexable pages have a canonical tag and are in sitemap.xml; external
links open in a new tab with rel="nofollow noopener"; generated pages match a
fresh build.
"""
import glob
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import lib  # noqa: E402

os.chdir(lib.OUT)
pages = sorted(glob.glob('*.html') + glob.glob('*/index.html'))
ids = {p: set(re.findall(r'id="([^"]+)"', open(p, encoding='utf-8').read())) for p in pages}
sitemap = open('sitemap.xml', encoding='utf-8').read()
NOT_INDEXED = {'404.html', 'privacy/index.html'}
problems = []
warnings = []


def target(url):
    url = url.split('#')[0].split('?')[0]
    if '.' in os.path.basename(url.rstrip('/')):
        return url[1:]
    return 'index.html' if url == '/' else url.strip('/') + '/index.html'


expected_nav = [(h, html.unescape(l)) for h, l in lib.NAV]
for p in pages:
    s = open(p, encoding='utf-8').read()
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            json.loads(block)
        except ValueError as e:
            problems.append(f'{p}: JSON-LD does not parse ({e})')
    for ref in re.findall(r'(?:href|src|srcset)="([^"]+)"', s):
        if ref.startswith('#'):
            if ref[1:] not in ids[p]:
                problems.append(f'{p}: missing anchor {ref}')
        elif ref.startswith('/') and not ref.startswith('//'):
            t = target(ref)
            if not os.path.exists(t):
                problems.append(f'{p}: broken link {ref}')
            elif '#' in ref and ref.split('#')[1] not in ids.get(t, set()):
                problems.append(f'{p}: missing anchor {ref}')
    for tag in re.findall(r'<a [^>]*href="https?://[^"]+"[^>]*>', s):
        if 'target="_blank"' not in tag or 'nofollow' not in tag or 'noopener' not in tag:
            problems.append(f'{p}: external link without target="_blank" rel="nofollow noopener": {tag}')
    cited = set(re.findall(r'href="#s(\d+)"', s))
    listed = re.findall(r'<li id="s(\d+)"', s)
    if listed and cited != set(listed):
        problems.append(f'{p}: citations and sources differ {sorted(cited ^ set(listed))}')
    if listed and [int(x) for x in listed] != list(range(1, len(listed) + 1)):
        problems.append(f'{p}: sources not numbered 1..n')
    if s.count('<table') != s.count('<div class="table-wrap"><table'):
        problems.append(f'{p}: table without table-wrap')
    if f'/css/site.css?v={lib.ASSET_VERSION}"' not in s:
        problems.append(f'{p}: stylesheet version is not v={lib.ASSET_VERSION}')
    if s.count('<h1') != 1:
        problems.append(f'{p}: has {s.count("<h1")} H1 headings')
    if 'external websites</a> linked from this site' not in s:
        problems.append(f'{p}: missing the external websites footer note')
    nav = re.search(r'<nav class="topnav".*?</nav>', s, re.S)
    if nav:
        found = [(h, html.unescape(l)) for h, l in re.findall(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', nav.group(0))]
        if found != expected_nav:
            problems.append(f'{p}: navigation differs from lib.NAV')
    title = html.unescape(re.search(r'<title>(.*?)</title>', s).group(1))
    if len(title) > 60:
        problems.append(f'{p}: title is {len(title)} characters')
    desc = re.search(r'<meta name="description" content="([^"]*)"', s)
    if desc and len(html.unescape(desc.group(1))) > 155:
        problems.append(f'{p}: description is {len(html.unescape(desc.group(1)))} characters')
    if p not in NOT_INDEXED:
        url = lib.SITE + '/' + ('' if p == 'index.html' else p[:-len('index.html')])
        if f'<loc>{url}</loc>' not in sitemap:
            problems.append(f'{p}: not in sitemap.xml')
        if f'<link rel="canonical" href="{url}">' not in s:
            problems.append(f'{p}: canonical tag missing or wrong')
        if not desc:
            problems.append(f'{p}: no meta description')

if not lib.OFFER_URL:
    warnings.append('OFFER_URL in _build/lib.py is empty: the "Make an offer" button points at /about/#contact until the Google Form link is added.')
if not lib.GA_ID:
    warnings.append('GA_ID in _build/lib.py is empty: no analytics are loaded.')

build = subprocess.run([sys.executable, os.path.join(ROOT, 'build.py'), '--check'], capture_output=True, text=True)
if build.returncode:
    problems.append('generated pages are out of date:\n' + build.stdout)

for w in warnings:
    print('warning: ' + w)
if problems:
    print('\n'.join(problems))
    sys.exit(1)
print(f'{len(pages)} pages checked, no problems.')
