#!/usr/bin/env python3
"""Build every page, and sitemap.xml, from _build/pages/*.py into site/.

    python3 _build/build.py           write the pages
    python3 _build/build.py --check   fail if any committed file differs from a fresh build
"""
import difflib
import importlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

import lib  # noqa: E402

NOT_INDEXED = {'404', 'privacy'}


def out_path(slug):
    if slug == '':
        return os.path.join(lib.OUT, 'index.html')
    if slug == '404':
        return os.path.join(lib.OUT, '404.html')
    return os.path.join(lib.OUT, slug, 'index.html')


def modified(mod):
    if hasattr(mod, 'META'):
        return mod.META['modified']
    return getattr(mod, 'MODIFIED', None)


def sitemap(entries):
    newest = max(d for _, d in entries if d)
    rows = []
    for slug, d in sorted(entries, key=lambda e: (e[0] != '', e[0])):
        rows.append(f'  <url>\n    <loc>{lib.url_for(slug)}</loc>\n    <lastmod>{d or newest}</lastmod>\n  </url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(rows) + '\n</urlset>\n')


def main():
    check = '--check' in sys.argv
    files = {}
    entries = []
    for name in sorted(os.listdir(os.path.join(ROOT, 'pages'))):
        if not name.endswith('.py') or name.startswith('_'):
            continue
        mod = importlib.import_module('pages.' + name[:-3])
        slug, html = mod.build({})
        files[out_path(slug)] = html
        if slug not in NOT_INDEXED:
            entries.append((slug, modified(mod)))
    files[os.path.join(lib.OUT, 'sitemap.xml')] = sitemap(entries)

    stale = []
    for path, text in files.items():
        rel = os.path.relpath(path, os.path.dirname(ROOT))
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if check:
            if old != text:
                stale.append(rel)
                diff = difflib.unified_diff(old.splitlines(), text.splitlines(), f'{rel} (committed)', f'{rel} (built)', lineterm='', n=0)
                print('\n'.join(list(diff)[:20]))
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(('updated ' if old != text else 'unchanged ') + rel)
    if check:
        if stale:
            print('Out of date: ' + ', '.join(stale) + '. Run python3 _build/build.py')
            sys.exit(1)
        print('All generated files match a fresh build.')


if __name__ == '__main__':
    main()
