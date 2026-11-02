"""Totterdown Arts Trail 2026."""
from lib import page

META = {
    'slug': 'totterdown-arts-trail',
    'title': 'Totterdown Arts Trail 2026: Dates, Times & What to Expect',
    'desc': "Totterdown Arts Trail 2026 runs on 14 and 15 November: opening times, this year's theme, how the front-room trail works and tips for visiting.",
    'og_desc': "Dates, times and tips for the Totterdown Arts Trail, Bristol's longest-running arts trail, on 14 and 15 November 2026.",
    'crumb': 'Totterdown Arts Trail',
    'h1': 'Totterdown Arts Trail 2026',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Dates and times are from the organisers; check their site before you go. <a href="/about/">How we check facts</a>.</p>
    <p>The Totterdown Arts Trail, first known as the Front Room arts trail, opens local homes and community venues to visitors for one weekend each November, with artists showing and selling their work. It's described as Bristol's oldest arts trail. [[tat_secret]] [[tat_creatives]]</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Dates:</strong> Saturday 14 November 2026, 11am to 6pm, and Sunday 15 November 2026, 11am to 5pm. [[tat_faq]]</li>
        <li><strong>Cost:</strong> free to attend. [[tat_home]]</li>
        <li><strong>Theme:</strong> "Homegrown". [[tat_home]]</li>
        <li><strong>History:</strong> held every November since 2001; it marked 25 years in 2025. [[tat_2014]] [[tat_25]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#when">When is the arts trail?</a></li>
        <li><a href="#how">How does it work?</a></li>
        <li><a href="#history">How long has it been running?</a></li>
        <li><a href="#tips">Tips for visiting</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="when">When is the Totterdown Arts Trail 2026?</h2>
    <div class="table-wrap"><table>
      <caption>Totterdown Arts Trail 2026 opening times</caption>
      <thead><tr><th>Day</th><th>Opening hours</th></tr></thead>
      <tbody>
        <tr><td>Saturday 14 November 2026</td><td>11am to 6pm</td></tr>
        <tr><td>Sunday 15 November 2026</td><td>11am to 5pm</td></tr>
      </tbody>
    </table></div>
    <p>Source: the organisers' FAQ. [[tat_faq]]</p>

    <h2 id="how">How does the Totterdown Arts Trail work?</h2>
    <ul>
      <li><strong>Front rooms:</strong> artists show their work in local homes and community venues, so you walk from house to house. [[tat_creatives]]</li>
      <li><strong>Map:</strong> printed booklets and maps go out to community venues and houses one to two weeks before the trail. [[tat_home]]</li>
      <li><strong>More than art:</strong> the organisers promise entertainment, food and activities for all ages. [[tat_home]]</li>
      <li><strong>Exhibiting:</strong> artist spaces for 2026 are full. [[tat_home]] Applications for 2027 will be announced on the organisers' site.</li>
    </ul>

    <h2 id="history">How long has the arts trail been running?</h2>
    <p>The trail has been held every November since 2001. [[tat_2014]] By 2014 it regularly hosted more than 180 artists. [[tat_2014]] It celebrated its 25th anniversary in November 2025. [[tat_25]] [[tat_secret]]</p>

    <h2 id="tips">Tips for visiting</h2>
    <ul>
      <li><strong>Wear good shoes:</strong> Totterdown is built on a steep hill, and <a href="/vale-street/">Vale Street</a> is England's steepest residential street.</li>
      <li><strong>Getting there:</strong> it's a short walk uphill from Bristol Temple Meads station. [[walk_temple]]</li>
      <li><strong>Make a day of it:</strong> see <a href="/things-to-do-in-totterdown/">things to do in Totterdown</a> for pubs and walks nearby.</li>
    </ul>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
