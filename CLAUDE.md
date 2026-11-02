# Totterdown.com

Sourced guides to Totterdown, Bristol, plus a domain-for-sale page. Published by Cloudflare Pages from `site/`.

## Ground rules

- Never put the owner's name, email, phone or address in any page, file or commit. The site is "run by the owner of the domain name".
- Commit as `Totterdown.com <noreply@totterdown.com>` (set with `git config user.name` / `user.email` in this repo).
- Never commit valuation, price or offer notes. They live outside this repo.
- Every figure on a guide links to a source in `_build/data/sources.json`. If sources disagree, give the range and name each one. Never invent a figure; write "not published" instead.

## Workflow

- Pages are generated: edit `_build/pages/*.py` (and `_build/lib.py` for the shared template), never `site/**/*.html`.
- Before every commit: `python3 _build/build.py` then `python3 _build/check.py`. Commit only when it says "no problems" (warnings about OFFER_URL or GA_ID are expected until those are set).
- Changing a guide's content: update its `modified` date and the "Updated" line in the body.
- Changing CSS or JS: bump `ASSET_VERSION` in `_build/lib.py`.
