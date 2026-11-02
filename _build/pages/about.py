"""About page: fact checking, corrections, external links, reuse."""
import lib

SLUG = 'about'
MODIFIED = '2026-11-02'


def build(data):
    body = f'''
    <p>{lib.NAME} publishes plain, sourced guides to Totterdown, a neighbourhood in south Bristol: its streets, history, events and the local changes that affect people who live and visit here.</p>

    <h2 id="facts">How we check facts</h2>
    <ul>
      <li>Every figure and date links to its source, listed at the end of each page.</li>
      <li>We use official sources where we can: Bristol City Council, Historic England, Ofsted and HM Land Registry data. Where we cite local news or community groups, it's because they're the best record available, and we say who reported a figure.</li>
      <li>Where sources disagree, such as on how steep Vale Street is or how many homes were demolished in the 1970s, we give the range and name each source.</li>
      <li>Each page shows the date it was last updated. Prices, dates and council plans change, so check the source before you rely on a detail.</li>
      <li>We don't copy text or images from other sites. The illustrations on this site are our own work.</li>
      <li>Some figures contain public sector information licensed under the {lib.ext('https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/', 'Open Government Licence v3.0')}.</li>
    </ul>

    <h2 id="contact">Corrections and contact</h2>
    <p>If you spot something wrong or out of date, tell us through the {lib.form_link('contact form')} and say which page and figure it's about. We fix confirmed errors and update the page date. The same form is used for enquiries about buying the domain and for privacy requests.</p>

    <h2 id="corrections-log">Corrections log</h2>
    <p>No corrections yet. Each confirmed correction will be listed here with its date and page.</p>

    <h2 id="reuse">Using our illustrations</h2>
    <p>You're free to reuse the illustrations on this site, including commercially, under the {lib.ext('https://creativecommons.org/licenses/by/4.0/', 'Creative Commons Attribution 4.0 licence (CC BY 4.0)')}. Credit {lib.NAME} and link to the page the image appears on.</p>
    <p>The written guides aren't covered by that licence, but you're welcome to quote short passages with a link to the page.</p>

    <h2 id="external-links">Links to other websites</h2>
    <p>Our guides link to other websites so you can check where each figure comes from. We don't control those websites and aren't responsible for their content, accuracy, availability or privacy practices. A link isn't an endorsement of the website, its owner or anything it sells. Check the original source before you rely on a figure.</p>

    <h2 id="independent">Independence</h2>
    <p>The guides are independent. They aren't sponsored by, or connected with, Bristol City Council, any estate agent, business or community group mentioned on the site.</p>

    <h2 id="domain">The domain name</h2>
    <p>The domain name {lib.NAME} is <a href="/domain-for-sale/">for sale</a>.</p>
'''
    graph = [{'@type': 'AboutPage', '@id': f'{lib.SITE}/about/#webpage', 'url': f'{lib.SITE}/about/',
              'name': f'About {lib.NAME}', 'isPartOf': {'@type': 'WebSite', '@id': f'{lib.SITE}/#website', 'name': lib.NAME, 'url': f'{lib.SITE}/'},
              'publisher': {'@id': f'{lib.SITE}/#organization'}, 'inLanguage': 'en-GB'}]
    html = lib.plain(SLUG, f'About {lib.NAME}: How We Check Facts',
                     f'How {lib.NAME} sources and checks its guides to Totterdown, Bristol, how to report a correction, and the corrections log.',
                     'About this site', MODIFIED, body, 'about',
                     og_desc='How we source and check our guides to Totterdown, Bristol, and how to report a correction.', graph=graph)
    return SLUG, html
