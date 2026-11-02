# Totterdown.com

Sourced guides to Totterdown, Bristol, and the sale page for the domain.

- `site/` is the published website. Cloudflare Pages serves this folder.
- `_build/` is the page builder. It is never published.

## Cloudflare Pages settings

| Setting | Value |
|---|---|
| Framework preset | None |
| Build command | *(blank)* |
| Build output directory | `site` |
| Production branch | `main` |

`site/_headers` sets the security headers. `site/404.html` is served for missing pages.

## Before launch

1. Set `OFFER_URL` in `_build/lib.py` to the Google Form link (from the domain's own Google account, with response summaries turned off).
2. Optional: set `GA_ID` to a GA4 measurement ID. Analytics loads only after a visitor accepts the cookie banner, and the privacy page updates itself. Mark `generate_lead` as a key event in GA4.
3. Rebuild and check: `python3 _build/build.py && python3 _build/check.py`.

See `_build/README.md` for day-to-day editing.
