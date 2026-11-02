"""Where to eat and drink in Totterdown."""
from lib import page

META = {
    'slug': 'food-and-drink-in-totterdown',
    'title': 'Totterdown Pubs, Cafés & Restaurants: Where to Eat',
    'desc': "Where to eat and drink in Totterdown, Bristol, street by street: pubs, the Bruhaha brewpub, Sundial Kitchen, Laura's Pizzas, Farrows, Florence and more.",
    'og_desc': "Pubs, a brewpub, a wine bar, cafés, bakeries, pizza and fish and chips: where to eat and drink in Totterdown, Bristol.",
    'crumb': 'Food and drink',
    'h1': 'Where to eat and drink in Totterdown',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Places open, close and change their hours, so check before you go. Nobody pays to be included. Spotted somewhere missing or closed? Tell us through the <a href="/about/#contact">contact form</a>. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown's food and drink is clustered in three places: the Wells Road, which climbs the hill from Three Lamps; Oxford Street, a smaller row of shops near the top; and a handful of corner pubs and cafés on the side streets in between.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Brunch:</strong> The Sundial Kitchen on William Street, a small vegetarian café; book ahead at weekends. [[sundial_brunch]] [[sundial_open]]</li>
        <li><strong>Pizza:</strong> Laura's Pizzas (Neapolitan, takeaway and delivery), A Cappella on the Wells Road, or Florence on Oxford Street. [[lauras]] [[vb_locals]] [[florence_review]]</li>
        <li><strong>Fish and chips:</strong> Farrows, 146 Wells Road, a Good Food Award winner in 2020 and 2021. [[farrows]] [[farrows_fsa]]</li>
        <li><strong>A drink:</strong> the Oxford, the Shakespeare, the Star &amp; Dove, the New Found Out and the Thunderbolt; Bruhaha brews its own beer, and Carouse is a wine bar and shop. [[vb_locals]] [[bruhaha_b247]] [[carouse]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#pubs">Pubs</a></li>
        <li><a href="#bars">Brewpub, wine and cocktails</a></li>
        <li><a href="#cafes">Cafés, brunch and bakeries</a></li>
        <li><a href="#dinner">Restaurants and takeaways</a></li>
        <li><a href="#streets">Street by street</a></li>
        <li><a href="#families">With children</a></li>
        <li><a href="#arts-trail">During the arts trail</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="pubs">What are the best pubs in Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Totterdown pubs</caption>
      <thead><tr><th>Pub</th><th>Known for</th></tr></thead>
      <tbody>
        <tr><td>The Oxford, Oxford Street</td><td>A locals' favourite for its Sunday roast, plus live music and open mic nights [[vb_locals]] [[wiki_totterdown]] [[oxford_fsa]]</td></tr>
        <tr><td>The Shakespeare, 1 Henry Street</td><td>Cider, local art on the walls and a walled beer garden [[vb_locals]] [[b365]] [[camra_shakes]]</td></tr>
        <tr><td>Star &amp; Dove, St Luke's Road</td><td>Food and live sport, under new management [[vb_locals]] [[star_reopen]] [[camra_star]]</td></tr>
        <tr><td>The New Found Out, 60 Green Street</td><td>Live sport; reopened in October 2021 after a refurbishment [[vb_locals]] [[newfound]]</td></tr>
        <tr><td>The Thunderbolt, 124 Bath Road</td><td>Live music in a Grade II listed former tollhouse [[vb_locals]] [[turnpike]]</td></tr>
      </tbody>
    </table></div>
    <p><strong>Is the Thunderbolt closing?</strong> The freehold has been put up for sale after 18 years under the same landlord, but Bristol24/7 reported it would keep trading and hosting live events until a sale completes. [[thunder_sale]]</p>

    <h2 id="bars">Where can you get local beer, wine or a cocktail?</h2>
    <ul>
      <li><strong>Bruhaha, 156–158 Wells Road:</strong> a brewpub that started as a home brewery in 2019 and opened here in October 2023. [[bruhaha_b247]] Its beers include Three Lamps, an IPA, TotterDowner, a bitter, and Rusty Robot, a porter. [[bruhaha_camra]]</li>
      <li><strong>Carouse, 32 Oxford Street:</strong> a wine shop and bar with more than 200 wines and simple food, opened in 2025 in the former Little Kitchen Cookery School. [[carouse]] [[carouse_inf]]</li>
      <li><strong>BANK, 107 Wells Road:</strong> coffee by day, cocktails and craft beer by night. [[bank_b247]] [[bank_hardens]]</li>
      <li><strong>Smokebox, 172 Wells Road:</strong> smoked barbecue with cocktails, in the former Southside Bar &amp; Kitchen. [[smokebox]] [[bristol_sauce]]</li>
    </ul>

    <h2 id="cafes">Where are the best cafés in Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Cafés, brunch and bakeries</caption>
      <thead><tr><th>Café</th><th>Why go</th></tr></thead>
      <tbody>
        <tr><td>The Sundial Kitchen, 1 William Street</td><td>A small vegetarian café opposite the Shakespeare, popular for brunch, with live music and film nights upstairs. Open on selected days only, so check before you go [[sundial_brunch]] [[sundial_open]] [[sundial_fsa]]</td></tr>
        <tr><td>Totterdown Canteen, 141 Wells Road</td><td>A traditional café for a fry-up [[vb_locals]] [[canteen]]</td></tr>
        <tr><td>Fox &amp; West, 172 Wells Road</td><td>Deli, café and greengrocer that buys as locally as it can [[foxwest]]</td></tr>
        <tr><td>BANK, 107 Wells Road</td><td>Speciality coffee during the day [[bank_b247]]</td></tr>
        <tr><td>The Bakehouse, 118 Oxford Street</td><td>Bakery and café [[bakehouse]]</td></tr>
      </tbody>
    </table></div>

    <h2 id="dinner">Where can you eat dinner in Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Restaurants and takeaways</caption>
      <thead><tr><th>Place</th><th>Food</th></tr></thead>
      <tbody>
        <tr><td>Laura's Pizzas, 1 William Street</td><td>Neapolitan pizza with slow-proved dough, for takeaway and delivery on Wednesday to Saturday evenings [[lauras]]</td></tr>
        <tr><td>A Cappella, 184C Wells Road</td><td>Award-winning pizzeria, café and trattoria [[vb_locals]] [[acappella]] [[tat_food]]</td></tr>
        <tr><td>Florence, Oxford Street</td><td>Good-value Italian in a small, colourful room; also does takeaway [[b365]] [[florence_review]] [[florence_fsa]]</td></tr>
        <tr><td>Farrows, 146 Wells Road</td><td>Fish and chips; Good Food Award winner in 2020 and 2021 [[farrows]] [[farrows_fsa]]</td></tr>
        <tr><td>Truffled of Totterdown, 152 Wells Road</td><td>Bring-your-own-bottle bistro and supper club, with Sunday roasts by reservation [[truffled]]</td></tr>
        <tr><td>Smokebox, 172 Wells Road</td><td>Smoked barbecue [[smokebox]] [[bristol_sauce]]</td></tr>
        <tr><td>Al Waha, 147 Wells Road</td><td>Indian food [[tat_food]] [[alwaha_fsa]]</td></tr>
        <tr><td>Asia Garden, 29 Oxford Street</td><td>Chinese takeaway [[asia_garden]]</td></tr>
        <tr><td>Star &amp; Dove, St Luke's Road</td><td>Pub food [[star_reopen]]</td></tr>
      </tbody>
    </table></div>

    <h2 id="streets">Food and drink in Totterdown, street by street</h2>
    <ul>
      <li><strong>Wells Road:</strong> BANK (107), Totterdown Canteen (141), Farrows (146), Al Waha (147), Truffled of Totterdown (152), Bruhaha (156–158), Fox &amp; West and Smokebox (172) and A Cappella (184C).</li>
      <li><strong>Oxford Street:</strong> the Oxford, Florence, Carouse (32), Asia Garden (29) and The Bakehouse (118).</li>
      <li><strong>Side streets:</strong> the Sundial Kitchen and Laura's Pizzas (1 William Street), the Shakespeare (1 Henry Street), the New Found Out (60 Green Street) and the Star &amp; Dove (St Luke's Road).</li>
      <li><strong>Bath Road:</strong> the Thunderbolt (124).</li>
    </ul>
    <p>Addresses are from the sources in each table above.</p>

    <h2 id="families">Where can you eat with children in Totterdown?</h2>
    <ul>
      <li><strong>Tots &amp; Teapots, Wells Road:</strong> a play café with sessions for young children, food and party bookings. [[tots]]</li>
      <li><strong>Windmill Hill City Farm:</strong> a short walk away, with a café open every day and free entry to the farm. [[farm_contact]] [[farm_visit]] See <a href="/parks-in-totterdown/#farm">parks and green spaces</a>.</li>
    </ul>

    <h2 id="arts-trail">Where to eat during the Totterdown Arts Trail</h2>
    <p>Many local venues open specially or run pop-ups during the <a href="/totterdown-arts-trail/">arts trail weekend</a>, which is on 14 and 15 November in 2026. The organisers publish a food and drink list on their website, and the printed trail map is available in local businesses. [[tat_food]] [[tat_secret]]</p>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
