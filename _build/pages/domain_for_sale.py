"""The domain sale page."""
import lib

SLUG = 'domain-for-sale'
TITLE = 'Totterdown.com Domain for Sale'
DESC = ('Totterdown.com is for sale: the exact-match .com for Totterdown, Bristol. '
        'Suits an estate agent, local business or publisher. Make an offer.')
OG_DESC = 'The exact-match .com domain for Totterdown, Bristol. Make an offer.'


def build(data):
    graph = [{'@type': 'WebPage', '@id': f'{lib.SITE}/{SLUG}/#webpage', 'url': f'{lib.SITE}/{SLUG}/', 'name': TITLE,
              'description': DESC, 'isPartOf': {'@type': 'WebSite', '@id': f'{lib.SITE}/#website', 'name': lib.NAME, 'url': f'{lib.SITE}/'},
              'primaryImageOfPage': f'{lib.SITE}/img/og-sale.png', 'inLanguage': 'en-GB'}]
    ext = ' target="_blank" rel="nofollow noopener"' if lib.OFFER_URL else ''
    html = lib.head(TITLE, DESC, SLUG, OG_DESC, og_type='website', graph=graph, image='/img/og-sale.png',
                    image_alt='Totterdown.com – domain name for sale', source='domain_for_sale') + f'''<body>
  <main class="page">
    {lib.terrace()}
    <h1>
      <span class="label"><span class="dot" aria-hidden="true"></span> Domain name for sale</span>
      <span class="domain">Totterdown<span class="tld">.com</span></span>
    </h1>

    <p class="intro"><strong>A working local site, not just a name.</strong> The exact-match .com for Totterdown, the Bristol neighbourhood known for its coloured houses, England's steepest street and the city's oldest arts trail, with the sourced guides on this site available alongside it. A fit for an estate agent, local business, community group or publisher.</p>

    <a class="btn" id="offer" data-lead="offer_button" href="{lib.offer_href()}"{ext}>Make an offer</a>
    <p class="small">No price is listed. Payment goes through Escrow.com, which holds the buyer's money until the domain has been transferred, so the buyer is protected.</p>

    <section class="included" aria-labelledby="included-title">
      <h2 id="included-title" class="guides-title">What can be included</h2>
      <ul>
        <li><strong>The domain</strong> Totterdown.com</li>
        <li><strong>{len(lib.GUIDES)} sourced guides</strong> to Totterdown, every figure linked to its source</li>
        <li><strong>The site itself:</strong> pages, illustrations and the build system that checks every page</li>
      </ul>
    </section>

    <section class="guides-section" aria-labelledby="guides-title">
      <h2 id="guides-title" class="guides-title">Guides on this site</h2>
      <nav class="guides" aria-label="Guides">
{lib.guide_cards()}
      </nav>
    </section>
  </main>

{lib.footer('    <p>Totterdown.com is offered for sale as a domain name only.</p>' + chr(10))}</body>
</html>
'''
    return SLUG, html
