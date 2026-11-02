# Page builder

Every page in `site/` is generated from a module in `pages/`, so the header,
footer, navigation, structured data and sources list stay in step.

| Page | Built from |
|---|---|
| `/` | `pages/home.py` |
| `/totterdown-parking-scheme/` | `pages/totterdown_parking_scheme.py` |
| `/vale-street/` | `pages/vale_street.py` |
| `/totterdown-history/` | `pages/totterdown_history.py` |
| `/totterdown-arts-trail/` | `pages/totterdown_arts_trail.py` |
| `/living-in-totterdown/` | `pages/living_in_totterdown.py` |
| `/things-to-do-in-totterdown/` | `pages/things_to_do_in_totterdown.py` |
| `/domain-for-sale/` | `pages/domain_for_sale.py` |
| `/about/` | `pages/about.py` |
| `/privacy/` | `pages/privacy.py` |
| `/404.html` | `pages/not_found.py` |
| `/sitemap.xml` | `build.py`, from each page's `modified` date |

Generated pages carry a comment at the top saying so. Edit the source, not the HTML.

## Common jobs

```sh
python3 _build/build.py          # rebuild every page and the sitemap
python3 _build/check.py          # check every page (links, citations, sitemap, nav, titles, stale builds)
```

- **Cite a source:** add it once to `data/sources.json` as
  `{"label": "...", "links": [["site.com", "https://..."]]}`, then write
  `[[source_key]]` in a page. Numbers and the sources list are generated in
  order of first use.
- **Update a guide:** edit its module, change `modified` in `META` and the
  "Updated" line, then rebuild. The sitemap picks up the new date.
- **New guide:** copy a guide module, give it a new `slug`, add it to `NAV`
  and `GUIDES` in `lib.py`, then rebuild.
- **Change the stylesheet or script:** bump `ASSET_VERSION` in `lib.py`.
- **Log a correction:** add it to the corrections list in `pages/about.py`.

Before committing, run both commands. `check.py` also fails if a generated
page no longer matches a fresh build.
