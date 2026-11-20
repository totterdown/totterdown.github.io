"""Getting to and around Totterdown."""
from lib import page

META = {
    'slug': 'getting-around-totterdown',
    'title': 'Getting to Totterdown: Train, Bus, Bike & Parking',
    'desc': 'How to get to Totterdown, Bristol: walking from Temple Meads, buses on the Wells Road and Bath Road, cycling, driving, the Clean Air Zone and parking.',
    'og_desc': 'Walking from Temple Meads, buses, cycling, driving and parking in Totterdown, Bristol.',
    'crumb': 'Getting around',
    'h1': 'Getting to and around Totterdown',
    'published': '2026-11-02',
    'modified': '2026-11-20',
}

BODY = r'''    <p class="meta">Updated 20 November 2026. Bus routes and timetables change, so check the operator before you travel. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown sits on the hill directly above Bristol Temple Meads, so most visitors arrive on foot from the station. Two main roads frame it: the A4 Bath Road along the bottom of the hill and the A37 Wells Road climbing up it, meeting at Three Lamps. [[three_lamps]]</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>By train:</strong> walk up from Bristol Temple Meads; Visit Bristol's walking route from the station runs through Totterdown's colourful streets. [[walk_temple]]</li>
        <li><strong>By bus:</strong> services stop on both the Wells Road and the Bath Road, including the local 512 to the city centre. [[bus_localities]] [[bus_bathroad]] [[bus512]]</li>
        <li><strong>By car:</strong> Totterdown is just outside Bristol's Clean Air Zone, which starts at Three Lamps. [[caz_tresa]]</li>
        <li><strong>Parking:</strong> a residents' parking scheme is proposed; see <a href="/totterdown-parking-scheme/">the parking guide</a>.</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#train">By train</a></li>
        <li><a href="#bus">By bus</a></li>
        <li><a href="#bike">By bike and on foot</a></li>
        <li><a href="#car">By car</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="train">How do you get to Totterdown from Temple Meads?</h2>
    <p class="answer">To get to Totterdown from Bristol Temple Meads, walk up the hill from the station: Totterdown sits directly above it, and Visit Bristol's walking route crosses the New Cut and climbs into its streets. [[walk_temple]]</p>
    <ul>
      <li><strong>On foot:</strong> Temple Meads is at the foot of the hill. Visit Bristol's walking route from the station crosses the New Cut and climbs through Totterdown's streets. [[walk_temple]] Expect steep hills; <a href="/vale-street/">Vale Street</a> has an average gradient of about 21.8%. [[vale_cadbury]]</li>
      <li><strong>New entrances:</strong> Temple Meads' new Eastern Entrance has opened. [[nr_regen]] A Southern Gateway, with a new pedestrian route into the station over the River Avon, received planning permission in January 2026. [[southern_gateway]] [[sg_weca]] [[sg_permission]] We haven't seen an opening date.</li>
    </ul>

    <h2 id="bus">Which buses go to Totterdown?</h2>
    <p class="answer">Buses serve Totterdown on both its main roads: the local 512 runs to the city centre via Windmill Hill, Bedminster and Redcliffe, the 376a uses the Wells Road, and First routes including the 1, 39 and 43 run along the Bath Road. [[bus512]] [[bus_376a]] [[bus_bathroad]]</p>
    <div class="table-wrap"><table>
      <caption>Buses serving Totterdown</caption>
      <thead><tr><th>Road</th><th>Services</th></tr></thead>
      <tbody>
        <tr><td>Local</td><td>512: Totterdown to Windmill Hill, Bedminster, Redcliffe and the city centre [[bus512]]</td></tr>
        <tr><td>Wells Road</td><td>Services including the 376a between Bristol Bus Station and Wells, via Temple Meads, Redcliffe, Totterdown and Knowle [[bus_376a]]</td></tr>
        <tr><td>Bath Road</td><td>First services 1, 39, 43, 522 and X39, which First listed as affected by a Bath Road closure in Totterdown in April 2026 [[bus_bathroad]]</td></tr>
      </tbody>
    </table></div>
    <p>For every service and stop, see bustimes.org's page for Totterdown, or the First Bus app for live times. [[bus_localities]]</p>

    <h2 id="bike">Can you cycle or walk from Totterdown into the city?</h2>
    <p class="answer">Yes: from Totterdown you can walk or cycle into central Bristol along the Avon New Cut, where the brick-surfaced Chocolate Path on the north bank leads towards the Harbourside. [[newcut]]</p>
    <ul>
      <li><strong>The New Cut:</strong> the Avon New Cut runs from Totterdown towards Cumberland Basin. On its north bank, the brick-surfaced Chocolate Path is a walking and cycling route towards the Harbourside. [[newcut]]</li>
      <li><strong>Circular walks:</strong> the Friends of the Avon New Cut publish circular walks along the river. [[franc_walks]]</li>
      <li><strong>Bath Road:</strong> the shared pavement for walking and cycling beside the four-lane Bath Road, near the roundabout south of Temple Meads, has been criticised as poor. [[bathrd_cycle]]</li>
    </ul>

    <h2 id="car">What should drivers know about Totterdown?</h2>
    <p class="answer">Drivers should know that Totterdown is just outside Bristol's Clean Air Zone, which starts at the Three Lamps junction, that it has no residents' parking scheme yet, and that some streets are steep enough for residents to park sideways. [[caz_tresa]] [[rps_consult]] [[vale_park]]</p>
    <ul>
      <li><strong>Clean Air Zone:</strong> the zone's boundary starts at the Three Lamps junction, so you can drive in on the Bath Road and turn onto the Wells Road without entering it. [[caz_tresa]] Non-compliant private cars pay £9 a day inside the zone; fully electric vehicles don't pay. [[caz_council]]</li>
      <li><strong>Parking:</strong> Totterdown has no residents' parking scheme yet. The council consulted on one in autumn 2026; the survey closed on 5 November and no decision has been published. [[rps_consult]] <a href="/totterdown-parking-scheme/">What's proposed</a>.</li>
      <li><strong>Hills:</strong> on Vale Street residents park sideways across the slope. [[vale_park]]</li>
      <li><strong>Roadworks:</strong> First Bus warned of a Bath Road closure in Totterdown from 25 April 2026; check for current closures before you drive. [[bus_bathroad]]</li>
    </ul>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
