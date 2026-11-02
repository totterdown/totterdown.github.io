"""Vale Street, Totterdown: England's steepest residential street."""
from lib import page

META = {
    'slug': 'vale-street',
    'title': "Vale Street, Bristol: England's Steepest Street",
    'desc': "Vale Street in Totterdown, Bristol: how steep it is, why Ordnance Survey named it England's steepest street, the Easter egg roll and how to visit.",
    'og_desc': "How steep Vale Street is, who measured it, the Easter egg roll and how to visit England's steepest residential street.",
    'crumb': 'Vale Street',
    'h1': "Vale Street: England's steepest residential street",
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Every figure links to its source. <a href="/about/">How we check facts</a>.</p>
    <p>Vale Street is a short residential street of terraced houses in Totterdown, on the hillside above Bristol Temple Meads. In 2019 it was reported as England's steepest residential street, and it's best known for an Easter egg-rolling race down the hill.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Title:</strong> Ordnance Survey named Vale Street England's steepest street in 2019. [[vale_itv]] [[vale_secret]]</li>
        <li><strong>Gradient:</strong> an average of about 21.8%, according to Ordnance Survey figures reported by Bristol24/7. [[vale_cadbury]] Some reports describe it as 22 degrees, which would be far steeper; the percentage is the figure to use.</li>
        <li><strong>Britain and the world:</strong> Ffordd Pen Llech in Harlech, Wales, is often cited as steeper, and Baldwin Street in Dunedin, New Zealand, holds the Guinness world record. [[ffordd]]</li>
        <li><strong>Egg rolling:</strong> residents race hard-boiled eggs down the street every Easter Sunday. [[egg_itv]] [[egg_b247]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#how-steep">How steep is Vale Street?</a></li>
        <li><a href="#compare">How does it compare with other steep streets?</a></li>
        <li><a href="#eggs">The Vale Street Easter egg roll</a></li>
        <li><a href="#living">What's it like to live on?</a></li>
        <li><a href="#visit">How to visit</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="how-steep">How steep is Vale Street?</h2>
    <p>Ordnance Survey's figures, reported by Bristol24/7 in February 2026, give Vale Street an average gradient of 21.8%. [[vale_cadbury]] That means the road climbs about 22 metres for every 100 metres you travel along it. Dangerous Roads gives a maximum gradient of 25.6%. [[vale_roads]]</p>
    <p><strong>Percent or degrees?</strong> Several reports, including ITV's 2019 coverage, describe the street as about 22 degrees. [[vale_itv]] A 22% gradient is roughly 12 degrees; a 22-degree slope would be a gradient of about 40%, steeper than the world's steepest street. The percentage figure is the consistent one.</p>

    <h2 id="compare">Is Vale Street the steepest street in Britain?</h2>
    <p>No: the claim is for England. In Wales, Ffordd Pen Llech in Harlech was listed by Guinness World Records as the world's steepest street until 2020, when the title went back to Baldwin Street in Dunedin, New Zealand, after a change in how it was measured. [[ffordd]]</p>
    <div class="table-wrap"><table>
      <caption>Steep streets compared</caption>
      <thead><tr><th>Street</th><th>Where</th><th>Claim</th></tr></thead>
      <tbody>
        <tr><td>Vale Street</td><td>Totterdown, Bristol</td><td>England's steepest residential street (Ordnance Survey, 2019) [[vale_itv]]</td></tr>
        <tr><td>Ffordd Pen Llech</td><td>Harlech, Wales</td><td>World's steepest street (Guinness) until 2020 [[ffordd]]</td></tr>
        <tr><td>Baldwin Street</td><td>Dunedin, New Zealand</td><td>World's steepest street (Guinness) since 2020 [[ffordd]]</td></tr>
      </tbody>
    </table></div>

    <h2 id="eggs">When is the Vale Street egg rolling?</h2>
    <p>On Easter Sunday, people gather at the top of Vale Street and roll hard-boiled eggs down to the bottom. [[egg_itv]]</p>
    <ul>
      <li><strong>How long it's run:</strong> ITV described the gathering in 2024 as more than 30 years old; Bristol24/7 put it at 25 years, with only the pandemic stopping it. [[egg_itv]] [[egg_b247]]</li>
      <li><strong>Next date:</strong> Easter Sunday 2027 is 28 March. Check local listings nearer the time for the start time.</li>
    </ul>

    <h2 id="living">What is it like to live on Vale Street?</h2>
    <ul>
      <li><strong>Parking:</strong> residents park their cars sideways, across the slope, so they don't roll away. [[vale_park]]</li>
      <li><strong>On screen:</strong> in February 2026 a Cadbury advert was filmed on the street, with a temporary Cadbury shopfront built for the shoot. [[vale_cadbury]]</li>
    </ul>

    <h2 id="visit">How do you get to Vale Street?</h2>
    <p>Vale Street is in Totterdown, a short walk uphill from Bristol Temple Meads station. Visit Bristol's walking route from the station passes through Totterdown's colourful streets. [[walk_temple]] It's a residential street, so keep noise down and don't block driveways or doors.</p>
    <p>Nearby: <a href="/things-to-do-in-totterdown/">things to do in Totterdown</a> and <a href="/totterdown-history/">the history of the area</a>.</p>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
