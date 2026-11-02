"""A self-guided walk around Totterdown's sights."""
from lib import page

def osm(query):
    from urllib.parse import quote
    url = 'https://www.openstreetmap.org/search?query=' + quote(query)
    return f'<a class="map" href="{url}" target="_blank" rel="nofollow noopener">Map</a>'


META = {
    'slug': 'totterdown-walk',
    'title': 'Totterdown Walk: 10 Sights on a Self-Guided Route',
    'desc': "A self-guided walk around Totterdown, Bristol: ten sights from Totterdown Bridge and Three Lamps to Vale Street, the coloured houses and Perrett's Park.",
    'og_desc': 'Ten sights on a self-guided walk around Totterdown, Bristol, from the river to the top of the hill.',
    'crumb': 'Totterdown walk',
    'h1': 'A self-guided Totterdown walk',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Totterdown is very steep, so wear good shoes and take your time. Most stops are on residential streets: keep noise down and don't block doors. <a href="/about/">How we check facts</a>.</p>
    <p>These ten sights run roughly from the river at the bottom of the hill to the top, so you can link them into a walk from Temple Meads station. Each has a map link to help you plan your own route.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Start:</strong> Bristol Temple Meads, at the foot of the hill. [[walk_temple]]</li>
        <li><strong>Highlights:</strong> the Three Lamps signpost, the coloured terraces and Vale Street, England's steepest residential street. [[three_lamps]] [[richmond]] [[vale_itv]]</li>
        <li><strong>Finish:</strong> the view from Perrett's Park, or a drink on the Wells Road on the way back down. [[perretts]] [[vb_locals]]</li>
        <li><strong>Ready-made routes:</strong> Visit Bristol, TRESA and the Friends of the Avon New Cut all publish walks that pass through or near Totterdown. [[walk_temple]] [[relig_walk]] [[franc_walks]]</li>
      </ul>
    </section>

    <h2 id="route">The ten sights</h2>
    <ol class="stops">
      <li id="stop-1"><strong>Bristol Temple Meads.</strong> The station is the natural starting point; Visit Bristol's walk from here crosses the New Cut and climbs into Totterdown. [[walk_temple]] __MAP_TEMPLE__</li>
      <li id="stop-2"><strong>Totterdown Bridge.</strong> The bridge over the Avon at the foot of the hill was built in 1888. [[bridge]] __MAP_BRIDGE__</li>
      <li id="stop-3"><strong>The Thunderbolt, 124 Bath Road.</strong> A Grade II listed turnpike tollhouse from about 1840, now a music pub. [[turnpike]] __MAP_THUNDERBOLT__</li>
      <li id="stop-4"><strong>Three Lamps.</strong> The Grade II* listed cast-iron signpost where the Bath Road and the Wells Road part, its arms pointing to Bath and Wells. [[three_lamps]] __MAP_THREELAMPS__</li>
      <li id="stop-5"><strong>The lost middle of Totterdown.</strong> Around Three Lamps stood the streets cleared from about 1968 for a road that was never built. [[cable]] [[roads_wiki]] <a href="/totterdown-history/#road">The full story</a>.</li>
      <li id="stop-6"><strong>Bristol Jamia Mosque, Green Street.</strong> Bristol's first mosque, in a former church bought in 1968. [[mosque]] __MAP_MOSQUE__</li>
      <li id="stop-7"><strong>Richmond Street.</strong> One of the best-known rows of coloured houses, with more than 70 homes, most of them brightly painted. [[richmond]] __MAP_RICHMOND__</li>
      <li id="stop-8"><strong>Vale Street.</strong> England's steepest residential street, home to the Easter egg roll, and briefly to Banksy's "Aachoo!!". [[vale_itv]] [[banksy_removed]] <a href="/vale-street/">Vale Street guide</a>. __MAP_VALE__</li>
      <li id="stop-9"><strong>The Wells Road and Oxford Street.</strong> Totterdown's two shopping streets, with cafés, Farrows' fish and chips, the Bruhaha brewpub and the Carouse wine bar. [[farrows]] [[bruhaha_b247]] [[carouse]] <a href="/food-and-drink-in-totterdown/">Where to eat</a>. __MAP_WELLS__</li>
      <li id="stop-10"><strong>Perrett's Park.</strong> Finish with one of the best views of the city, especially at Balloon Fiesta time in August. [[perretts]] __MAP_PERRETTS__</li>
    </ol>

    <h2 id="extend">How can you extend the walk?</h2>
    <ul>
      <li><strong>Arnos Vale Cemetery:</strong> a Victorian garden cemetery further along the Bath Road. [[arnos]] <a href="/parks-in-totterdown/#arnos">More</a>.</li>
      <li><strong>Religious buildings:</strong> TRESA's walk visits Totterdown's churches, chapels and mosque. [[relig_walk]]</li>
      <li><strong>The river:</strong> the Friends of the Avon New Cut publish circular walks along the New Cut. [[franc_walks]]</li>
      <li><strong>On the arts trail weekend</strong> you can go inside artists' homes along the way: 14 and 15 November in 2026. [[tat_faq]] <a href="/totterdown-arts-trail/">Arts trail guide</a>.</li>
    </ul>
'''

MAPS = {
    '__MAP_TEMPLE__': 'Bristol Temple Meads',
    '__MAP_BRIDGE__': 'Totterdown Bridge, Bristol',
    '__MAP_THUNDERBOLT__': '124 Bath Road, Bristol',
    '__MAP_THREELAMPS__': 'Three Lamps, Totterdown, Bristol',
    '__MAP_MOSQUE__': 'Bristol Jamia Mosque',
    '__MAP_RICHMOND__': 'Richmond Street, Totterdown, Bristol',
    '__MAP_VALE__': 'Vale Street, Totterdown, Bristol',
    '__MAP_WELLS__': 'Wells Road, Totterdown, Bristol',
    '__MAP_PERRETTS__': "Perrett's Park, Bristol",
}


def build(data):
    body = BODY
    for token, query in MAPS.items():
        body = body.replace(token, osm(query))
    return META['slug'], page(body=body, source=__name__.split('.')[-1], **META)
