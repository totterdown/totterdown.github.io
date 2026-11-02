"""Homepage: guide hub."""
import lib

SLUG = ''
TITLE = 'Totterdown, Bristol: Guides to History, Homes & Events'
DESC = ("Sourced guides to Totterdown, Bristol: Vale Street, local history, the arts trail, "
        "the residents' parking scheme, house prices and things to do.")
OG_DESC = 'Sourced guides to Totterdown in Bristol: Vale Street, history, the arts trail, parking, living here and things to do.'


def build(data):
    graph = [
        lib.ORG,
        {'@type': 'WebSite', '@id': f'{lib.SITE}/#website', 'name': lib.NAME, 'url': f'{lib.SITE}/',
         'publisher': {'@id': f'{lib.SITE}/#organization'}, 'inLanguage': 'en-GB'},
        {'@type': 'CollectionPage', '@id': f'{lib.SITE}/#webpage', 'url': f'{lib.SITE}/', 'name': TITLE,
         'description': DESC, 'isPartOf': {'@id': f'{lib.SITE}/#website'},
         'about': {'@type': 'Place', 'name': 'Totterdown, Bristol',
                   'containedInPlace': {'@type': 'City', 'name': 'Bristol'}},
         'primaryImageOfPage': f'{lib.SITE}/img/og.png', 'inLanguage': 'en-GB'},
    ]
    html = lib.head(TITLE, DESC, SLUG, OG_DESC, og_type='website', graph=graph, source='home') + f'''<body>
  <main class="page hub">
    {lib.terrace()}
    <span class="label"><span class="dot" aria-hidden="true"></span> Guides to a Bristol neighbourhood</span>
    <h1>Totterdown, Bristol</h1>

    <p class="intro">Plain, sourced guides to the hillside neighbourhood above Temple Meads: its steep streets and coloured houses, its history, what's on, and what's changing.</p>

    <a class="news" href="/totterdown-parking-scheme/"><strong>Residents' parking:</strong> the council's survey on a Totterdown scheme closes on 5 November 2026. See what's proposed</a>

    <section class="guides-section" aria-labelledby="guides-title">
      <h2 id="guides-title" class="guides-title">Guides</h2>
      <nav class="guides" aria-label="Guides">
{lib.guide_cards()}
      </nav>
    </section>

    <section class="hub-about" aria-labelledby="what-title">
      <h2 id="what-title">What is Totterdown?</h2>
      <p>Totterdown is a neighbourhood in south Bristol, on the steep hill above the River Avon and Temple Meads station, in the city's Windmill Hill ward. In short:</p>
      <ul>
        <li>It was built in late Victorian times to house railway workers, and many of its terraces are now painted in bright colours. <a href="/totterdown-history/#victorian">History</a></li>
        <li>Vale Street, with an average gradient of about 21.8%, was named England's steepest residential street by Ordnance Survey in 2019. <a href="/vale-street/">Vale Street</a></li>
        <li>More than 500 homes and businesses were demolished from about 1968 for a ring road that was never built. <a href="/totterdown-history/#road">The lost road</a></li>
        <li>Homes sold for an average of £374,399 in the year to early 2026. <a href="/living-in-totterdown/#prices">House prices</a></li>
        <li>The Totterdown Arts Trail, held since 2001, returns on 14 and 15 November 2026. <a href="/totterdown-arts-trail/">Arts trail</a></li>
      </ul>
      <p>Each figure is sourced on the linked guide.</p>
    </section>
  </main>

{lib.footer()}</body>
</html>
'''
    return SLUG, html
