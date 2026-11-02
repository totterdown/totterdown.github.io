# Totterdown.com

Sourced guides to Totterdown, Bristol, and the sale page for the domain.

- `site/` is the published website. GitHub Pages serves this folder through `.github/workflows/pages.yml`, which runs `_build/check.py` first and won't publish if it fails.
- `_build/` is the page builder. It is never published.

## GitHub Pages settings

| Setting | Value |
|---|---|
| Settings → Pages → Source | GitHub Actions |
| Custom domain | `totterdown.com` (also in `site/CNAME`) |
| Enforce HTTPS | On, once the certificate is issued |

GitHub Pages ignores `site/_headers`. To send the security headers, put the domain behind Cloudflare's proxy and add them there as a Response Header Transform Rule. `site/404.html` is served for missing pages.

## Before launch

1. Set `OFFER_URL` in `_build/lib.py` to the Google Form link (from the domain's own Google account, with response summaries turned off).
2. Optional: set `GA_ID` to a GA4 measurement ID. Analytics loads only after a visitor accepts the cookie banner, and the privacy page updates itself. Mark `generate_lead` as a key event in GA4.
3. Rebuild and check: `python3 _build/build.py && python3 _build/check.py`.

See `_build/README.md` for day-to-day editing.
