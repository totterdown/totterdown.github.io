"""Things to do in Totterdown."""
from lib import page

META = {
    'slug': 'things-to-do-in-totterdown',
    'title': 'Things to Do in Totterdown, Bristol: Houses, Pubs & Walks',
    'desc': "Things to do in Totterdown, Bristol: the coloured houses, Vale Street, historic pubs, Arnos Vale Cemetery and the November arts trail.",
    'og_desc': 'The coloured houses, Vale Street, historic pubs, Arnos Vale Cemetery and the arts trail: a visitor guide to Totterdown.',
    'crumb': 'Things to do',
    'h1': 'Things to do in Totterdown',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Opening hours change, so check with each place before you go. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown is small enough to walk around in an afternoon, but steep enough that you'll feel it. Here's what's worth seeing, starting from Temple Meads station at the bottom of the hill.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>See:</strong> the coloured terraces, including Richmond Street, and <a href="/vale-street/">Vale Street</a>, England's steepest residential street. [[richmond]] [[vale_itv]]</li>
        <li><strong>Drink:</strong> the Thunderbolt, a former tollhouse, plus the Shakespeare and the Star &amp; Dove. [[turnpike]] [[camra_shakes]] [[camra_star]]</li>
        <li><strong>Walk:</strong> Arnos Vale, a Victorian garden cemetery on the Bath Road. [[arnos]]</li>
        <li><strong>Time it:</strong> the <a href="/totterdown-arts-trail/">arts trail</a> on 14 and 15 November 2026, or the Vale Street egg roll on Easter Sunday. [[tat_faq]] [[egg_itv]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#houses">The coloured houses</a></li>
        <li><a href="#vale">Vale Street</a></li>
        <li><a href="#pubs">Pubs</a></li>
        <li><a href="#arnos">Arnos Vale Cemetery</a></li>
        <li><a href="#landmarks">Landmarks on the way</a></li>
        <li><a href="#events">Events through the year</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="houses">Where are Totterdown's coloured houses?</h2>
    <p>The painted Victorian terraces on the hillside are visible from Temple Meads and much of the city centre. [[colour_secret]] Richmond Street is one of the best known, with more than 70 houses, most of them brightly painted. [[richmond]] Visit Bristol's walk from Temple Meads takes you through these streets. [[walk_temple]]</p>

    <h2 id="vale">Can you visit Vale Street?</h2>
    <p>Yes. It's a public residential street, and Ordnance Survey named it England's steepest in 2019. [[vale_itv]] Please respect residents' homes. <a href="/vale-street/">Read our Vale Street guide</a>.</p>

    <h2 id="pubs">What are the best pubs in Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Totterdown pubs</caption>
      <thead><tr><th>Pub</th><th>Why go</th></tr></thead>
      <tbody>
        <tr><td>The Thunderbolt, 124 Bath Road</td><td>A Grade II listed former turnpike tollhouse from about 1840, known for live music [[turnpike]] [[camra_thunder]]</td></tr>
        <tr><td>The Shakespeare, 1 Henry Street</td><td>A traditional local [[camra_shakes]]</td></tr>
        <tr><td>Star &amp; Dove, St Luke's Road</td><td>A pub and dining room in the heart of Totterdown [[camra_star]]</td></tr>
      </tbody>
    </table></div>

    <h2 id="arnos">Is Arnos Vale Cemetery worth visiting?</h2>
    <p>Arnos Vale is a Victorian garden cemetery on the Bath Road, on the edge of Totterdown. Its first burial was in 1839. [[arnos]] [[arnos_visit]]</p>
    <ul>
      <li><strong>Design:</strong> it was laid out in the style of a Greek necropolis, influenced by Père Lachaise in Paris. [[arnos_visit]]</li>
      <li><strong>Rescued:</strong> after decades of decline, Bristol City Council took ownership in 2003 and a charitable trust was set up to restore it. [[arnos]]</li>
      <li><strong>Still working:</strong> it's still an active cemetery, so be respectful of services. [[arnos]]</li>
    </ul>

    <h2 id="landmarks">What landmarks can you see on the way?</h2>
    <ul>
      <li><strong>Three Lamps:</strong> the Grade II* listed signpost pointing to Bath and Wells, at the top of Bath Road. [[three_lamps]]</li>
      <li><strong>Bristol Jamia Mosque:</strong> on Green Street, the first mosque in Bristol, in a former church. [[mosque]]</li>
      <li><strong>Totterdown Bridge:</strong> the 1888 bridge over the Avon at the foot of the hill. [[bridge]]</li>
    </ul>
    <p>The stories behind them are in <a href="/totterdown-history/">our history of Totterdown</a>.</p>

    <h2 id="events">What's on in Totterdown through the year?</h2>
    <div class="table-wrap"><table>
      <caption>Regular events</caption>
      <thead><tr><th>When</th><th>Event</th></tr></thead>
      <tbody>
        <tr><td>Easter Sunday</td><td>Vale Street egg rolling [[egg_itv]]</td></tr>
        <tr><td>November</td><td>Totterdown Arts Trail, 14 and 15 November in 2026 [[tat_faq]]</td></tr>
      </tbody>
    </table></div>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
