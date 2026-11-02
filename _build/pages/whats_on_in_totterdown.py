"""What's on in Totterdown through the year."""
from lib import page

META = {
    'slug': 'whats-on-in-totterdown',
    'title': "What's On in Totterdown: Events Through the Year",
    'desc': "What's on in Totterdown, Bristol, month by month: the Vale Street egg roll, garden festival, Balloon Fiesta views, apple pressing and the arts trail.",
    'og_desc': "Totterdown's year: the Easter egg roll, garden festival, Balloon Fiesta views, apple pressing and the arts trail.",
    'crumb': "What's on",
    'h1': "What's on in Totterdown",
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Community events are run by volunteers and dates change, so check with the organisers. Know of an event we've missed? Tell us through the <a href="/about/#contact">contact form</a>. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown has a busy calendar for a small neighbourhood, much of it run by residents. The residents' association TRESA says there are events all year round. [[tresa_events]]</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Next up:</strong> the Totterdown Arts Trail, Saturday 14 and Sunday 15 November 2026, free. [[tat_faq]] [[tat_home]]</li>
        <li><strong>Spring:</strong> egg rolling down Vale Street on Easter Sunday; in 2027 that's 28 March. [[egg_itv]]</li>
        <li><strong>August:</strong> the Balloon Fiesta's mass ascents, seen from Perrett's Park. [[perretts]]</li>
        <li><strong>Every year:</strong> a garden festival and TRESA's Front Garden Awards. [[tresa_events]] [[tresa_gardens]]</li>
        <li><strong>Autumn:</strong> TRESA's community apple pressing, held in September 2025. [[tresa_events]]</li>
      </ul>
    </section>

    <h2 id="calendar">Totterdown events calendar</h2>
    <div class="table-wrap"><table>
      <caption>Regular events in and around Totterdown</caption>
      <thead><tr><th>When</th><th>Event</th></tr></thead>
      <tbody>
        <tr><td>Easter Sunday</td><td><a href="/vale-street/#eggs">Vale Street egg rolling</a>: hard-boiled eggs raced down England's steepest residential street [[egg_itv]] [[egg_b247]]</td></tr>
        <tr><td>Yearly, date varies</td><td>Garden festival, listed by TRESA among Totterdown's events; 2027 date not yet published [[tresa_events]]</td></tr>
        <tr><td>Yearly</td><td>TRESA Front Garden Awards [[tresa_gardens]]</td></tr>
        <tr><td>Yearly</td><td>Community of Perrett's Park annual picnic, raising money for the park [[perretts]]</td></tr>
        <tr><td>August</td><td>Bristol International Balloon Fiesta: watch the mass ascents from Perrett's Park [[perretts]]</td></tr>
        <tr><td>September</td><td>Apple pressing at TRESA's community space on Park Street (21 September in 2025) [[tresa_events]] [[tresa_space]]</td></tr>
        <tr><td>November</td><td><a href="/totterdown-arts-trail/">Totterdown Arts Trail</a>: 14 and 15 November in 2026 [[tat_faq]]</td></tr>
        <tr><td>Through the year</td><td>TRESA public meetings on local issues, such as the meeting on 17 May 2026 about the Liveable Neighbourhood and parking [[tresa_may26]]</td></tr>
      </tbody>
    </table></div>

    <h2 id="weekly">What's on every week?</h2>
    <ul>
      <li><strong>Live music:</strong> the Thunderbolt and the Oxford both host live music. [[vb_locals]] [[wiki_totterdown]]</li>
      <li><strong>Live sport:</strong> the Star &amp; Dove and the New Found Out. [[vb_locals]] More in <a href="/food-and-drink-in-totterdown/">where to eat and drink</a>.</li>
      <li><strong>Community halls:</strong> The Harbour, a former Methodist church bought by a local church in 2024, offers three halls for local groups, arts and cultural events. [[harbour]]</li>
    </ul>

    <h2 id="news">Where can you find out what's happening in Totterdown?</h2>
    <ul>
      <li><strong>TRESA</strong> publishes news, events and its newsletter, Talk of Totterdown. [[tresa_events]] [[tresa]]</li>
      <li><strong>The arts trail</strong> posts its dates and map on its own website. [[tat_home]]</li>
    </ul>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
