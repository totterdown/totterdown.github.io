"""Living in Totterdown: house prices, schools, transport."""
from lib import page

META = {
    'slug': 'living-in-totterdown',
    'title': 'Living in Totterdown, Bristol: Prices, Schools & Transport',
    'desc': 'Moving to Totterdown, Bristol: house prices and rents, GPs, libraries, schools, getting to Temple Meads, safety, parking and the Clean Air Zone.',
    'og_desc': 'House prices, schools, transport, parking and the Clean Air Zone for anyone thinking of moving to Totterdown, Bristol.',
    'crumb': 'Living in Totterdown',
    'h1': 'Living in Totterdown',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Every figure links to its source. Prices and ratings change, so check the source before you decide. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown is a neighbourhood of Victorian terraces on a steep hill in south Bristol, mostly in the BS4 postcode with some streets in BS3, a short walk from Temple Meads station. This guide covers the practical side of living here.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>House prices:</strong> homes in Totterdown sold for an average of £374,399 over the year to early 2026, 5% more than the year before. [[rightmove]]</li>
        <li><strong>Renting:</strong> example listings in 2026 asked about £1,100 a month for a one-bed flat and £1,500 for a two-bed; there's no published average for Totterdown. [[rent_1bed]] [[rent_2bed]]</li>
        <li><strong>Council ward:</strong> Totterdown is in Windmill Hill ward, home to an estimated 14,104 people in mid-2024. [[ward_wiki]] [[ward_2024]]</li>
        <li><strong>Getting about:</strong> Temple Meads station is at the foot of the hill, within walking distance. [[walk_temple]]</li>
        <li><strong>Parking:</strong> a residents' parking scheme is proposed; the council's survey closes on 5 November 2026. <a href="/totterdown-parking-scheme/">Details</a></li>
        <li><strong>Clean Air Zone:</strong> Totterdown is outside Bristol's zone, which starts at the Three Lamps junction. [[caz_tresa]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#prices">How much are houses in Totterdown?</a></li>
        <li><a href="#area">Where is Totterdown?</a></li>
        <li><a href="#rent">Renting in Totterdown</a></li>
        <li><a href="#services">GPs, libraries and halls</a></li>
        <li><a href="#schools">Schools</a></li>
        <li><a href="#transport">Getting around</a></li>
        <li><a href="#safety">Is Totterdown safe?</a></li>
        <li><a href="#caz">Is Totterdown in the Clean Air Zone?</a></li>
        <li><a href="#changes">What's changing nearby?</a></li>
        <li><a href="#community">Community</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="prices">How much are houses in Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Average sold prices in Totterdown, Rightmove (HM Land Registry data), February 2026</caption>
      <thead><tr><th>Measure</th><th>Figure</th></tr></thead>
      <tbody>
        <tr><td>Average sold price, last 12 months</td><td>£374,399</td></tr>
        <tr><td>Change on previous year</td><td>+5%</td></tr>
        <tr><td>2023 peak average</td><td>£365,128</td></tr>
      </tbody>
    </table></div>
    <p>Most homes in Totterdown are terraced houses, so the average reflects a mix of terrace sizes. Check recent sales on your street before making an offer. [[rightmove]]</p>

    <h2 id="rent">How much does it cost to rent in Totterdown?</h2>
    <p>No organisation publishes an average rent for Totterdown alone. As examples, a one-bed flat was listed at £1,100 a month and a two-bed flat at £1,500 a month in 2026. [[rent_1bed]] [[rent_2bed]] Compare several current listings before you agree a rent.</p>

    <h2 id="area">Where is Totterdown, and which ward is it in?</h2>
    <ul>
      <li><strong>Location:</strong> south of the River Avon, above Temple Meads, where the A4 Bath Road and the A37 Wells Road split at Three Lamps. [[three_lamps]]</li>
      <li><strong>Postcodes and boundary:</strong> Totterdown has no official boundary. The residents' association TRESA notes that postcode, ward and parish boundaries all differ, and addresses fall in both BS3 and BS4. [[where_tresa]]</li>
      <li><strong>Ward:</strong> since 2016, Totterdown has been part of Windmill Hill ward, with the south-eastern part of Bedminster and the Ravenhill Road area of Lower Knowle. [[ward_wiki]]</li>
      <li><strong>Population:</strong> the ward had 13,958 residents at the 2021 Census and an estimated 14,104 in mid-2024. Neither figure is for Totterdown alone. [[ward_2021]] [[ward_2024]]</li>
    </ul>

    <h2 id="services">Where are the nearest GPs and libraries?</h2>
    <div class="table-wrap"><table>
      <caption>Local services near Totterdown</caption>
      <thead><tr><th>Service</th><th>Where</th></tr></thead>
      <tbody>
        <tr><td>Wells Road Surgery (GP)</td><td>233 Wells Road, Knowle [[gp_wells]]</td></tr>
        <tr><td>Priory Surgery (GP)</td><td>326 Wells Road, Knowle [[gp_priory]]</td></tr>
        <tr><td>Knowle Library</td><td>Broad Walk, Knowle [[lib_knowle]]</td></tr>
        <tr><td>Bedminster Library</td><td>Bedminster Parade [[lib_bedminster]]</td></tr>
        <tr><td>Wick Road Library</td><td>Wick Road, Brislington [[lib_wick]]</td></tr>
        <tr><td>The Harbour (community halls)</td><td>A former Methodist church in Totterdown with three halls for local groups [[harbour]]</td></tr>
      </tbody>
    </table></div>
    <p>Which GP practice you can register with depends on your address. Use the NHS website to find practices that cover your postcode and are accepting new patients. [[nhs_gp]]</p>

    <h2 id="schools">What schools are in Totterdown?</h2>
    <p>Hillcrest Primary School on Cemetery Road is Totterdown's own primary school, rated Good at its January 2022 inspection. [[hillcrest]] There's no secondary school in Totterdown. See <a href="/schools-in-totterdown/">schools in and near Totterdown</a> for primary and secondary options and how places are given.</p>

    <h2 id="transport">How do you get around from Totterdown?</h2>
    <ul>
      <li><strong>Train:</strong> Bristol Temple Meads is at the bottom of the hill. Visit Bristol's walking route from the station runs through Totterdown's colourful streets and over the New Cut. [[walk_temple]]</li>
      <li><strong>Bus:</strong> the 512 runs from Totterdown via Windmill Hill, Bedminster and Redcliffe to the city centre. Check the current timetable before you travel. [[bus512]]</li>
      <li><strong>Roads:</strong> the A4 Bath Road and the A37 Wells Road meet at Three Lamps, at the edge of Totterdown. [[three_lamps]]</li>
      <li><strong>Hills:</strong> many streets are steep. <a href="/vale-street/">Vale Street</a> has an average gradient of about 21.8%. [[vale_cadbury]]</li>
    </ul>
    <p>More in <a href="/getting-around-totterdown/">getting to and around Totterdown</a>.</p>

    <h2 id="safety">Is Totterdown a safe place to live?</h2>
    <p>No source publishes a crime rate for Totterdown as a whole. For one example, StreetCheck counted 57 crimes within half a mile of Bath Road, Totterdown, in October 2025 and rated the level "medium". [[streetcheck]] For a street you're thinking of moving to, look up its postcode on the police.uk crime map, which shows recorded crime month by month. [[police_uk]]</p>

    <h2 id="caz">Is Totterdown in the Clean Air Zone?</h2>
    <p>No. Bristol's Clean Air Zone has been running since 28 November 2022. [[caz_council]] Totterdown sits just outside it: the boundary starts at the Three Lamps junction, so drivers coming in on the Bath Road can turn onto the Wells Road without entering the zone. [[caz_tresa]]</p>
    <ul>
      <li><strong>Charge:</strong> £9 a day for non-compliant private cars; fully electric vehicles don't pay. [[caz_council]]</li>
      <li><strong>Possible rise:</strong> the council has considered raising some charges to £14 a day. [[caz_14]] Check the council's checker before you drive in.</li>
    </ul>

    <h2 id="changes">What is changing near Totterdown?</h2>
    <ul>
      <li><strong>Residents' parking and Liveable Neighbourhood:</strong> both are being consulted on or designed now. <a href="/totterdown-parking-scheme/">Read the guide</a>.</li>
      <li><strong>Temple Island:</strong> Bristol City Council approved Legal &amp; General's £350m Temple Island scheme, with 520 homes, offices, a hotel and shops, in April 2026. [[temple_island]] Objectors argued the towers would block views of Totterdown's coloured houses from the city. [[temple_views]]</li>
    </ul>

    <h2 id="community">Community groups</h2>
    <ul>
      <li><strong>TRESA</strong> (Totterdown Residents' Environmental and Social Action) holds public meetings on planning, transport and local issues. [[tresa]]</li>
      <li><strong>Arts trail:</strong> the <a href="/totterdown-arts-trail/">Totterdown Arts Trail</a> opens homes to visitors every November.</li>
      <li><strong>Events:</strong> see <a href="/whats-on-in-totterdown/">what's on in Totterdown</a> through the year.</li>
    </ul>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
