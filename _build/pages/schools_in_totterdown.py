"""Schools in and near Totterdown."""
from lib import page

META = {
    'slug': 'schools-in-totterdown',
    'title': 'Schools in Totterdown, Bristol: Primary & Secondary',
    'desc': 'Schools in and near Totterdown, Bristol: Hillcrest, Victoria Park, St Mary Redcliffe and Temple, the Oasis academies, Ofsted ratings and admissions.',
    'og_desc': 'Primary and secondary schools serving Totterdown, Bristol, their Ofsted ratings and how places are given.',
    'crumb': 'Schools',
    'h1': 'Schools in and near Totterdown',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Ofsted ratings, catchments and admission rules change every year, so check each school and the council before you apply. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown has one primary school of its own, with more in neighbouring Windmill Hill and Knowle. There's no secondary school in Totterdown, so older children travel to schools nearby. Ofsted now publishes report cards instead of single-word grades for new inspections, so the ratings below are from each school's last graded or ungraded inspection.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Primary in Totterdown:</strong> Hillcrest Primary School, Cemetery Road, rated Good in January 2022. [[hillcrest]]</li>
        <li><strong>Primary next door:</strong> Victoria Park Primary School in Windmill Hill, which remained Good after an inspection in January 2022. [[vpps_ofsted]] [[vpps_gias]]</li>
        <li><strong>Secondary:</strong> none in Totterdown. Schools nearby include St Mary Redcliffe and Temple, Oasis Academy Brislington and Oasis Academy Temple Quarter. [[smrt]] [[oab]] [[oatq]]</li>
        <li><strong>Applying:</strong> places at most state schools in the city are allocated through Bristol City Council. [[admissions]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#primary">Primary schools</a></li>
        <li><a href="#secondary">Secondary schools</a></li>
        <li><a href="#admissions">How school places are given</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="primary">Which primary schools serve Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Primary schools in and next to Totterdown</caption>
      <thead><tr><th>School</th><th>Details</th></tr></thead>
      <tbody>
        <tr><td>Hillcrest Primary School, Cemetery Road, Totterdown</td><td>Community school for ages 4 to 11. Rated Good at its January 2022 inspection. [[hillcrest]]</td></tr>
        <tr><td>Victoria Park Primary School, Atlas Road, Windmill Hill</td><td>Academy in the Amplify Education trust. An ungraded inspection in January 2022 found it remained Good. [[vpps_gias]] [[vpps_ofsted]]</td></tr>
      </tbody>
    </table></div>

    <h2 id="secondary">Which secondary schools are near Totterdown?</h2>
    <div class="table-wrap"><table>
      <caption>Secondary schools near Totterdown</caption>
      <thead><tr><th>School</th><th>Details</th></tr></thead>
      <tbody>
        <tr><td>St Mary Redcliffe and Temple School, Redcliffe</td><td>Church of England voluntary aided school for ages 11 to 18, with about 1,780 pupils. Admissions use faith criteria as well as distance. Listed as Outstanding by Eduscope. [[smrt]] [[eduscope]]</td></tr>
        <tr><td>Oasis Academy Brislington, Hungerford Road</td><td>Academy that has been at or above capacity, so distance matters. [[oab]]</td></tr>
        <tr><td>Oasis Academy Temple Quarter, Spring Street</td><td>A small secondary school of about 280 pupils; places are allocated by Bristol City Council using its oversubscription criteria. [[oatq]]</td></tr>
      </tbody>
    </table></div>
    <p>Which secondary school a Totterdown address is likely to get can change from year to year with the number of applicants. Check each school's admissions policy and the council's allocation figures before relying on any school.</p>

    <h2 id="admissions">How are school places given in Bristol?</h2>
    <ul>
      <li><strong>One application:</strong> you apply to Bristol City Council and list your preferred schools; the council publishes how places were allocated each year. [[admissions]]</li>
      <li><strong>Oversubscription:</strong> when a school has more applicants than places, it uses its published criteria, typically children in care first, then siblings, then distance. [[oab]]</li>
      <li><strong>Faith schools</strong> such as St Mary Redcliffe and Temple also give priority on religious criteria. [[smrt]]</li>
    </ul>
    <p>Moving here? See <a href="/living-in-totterdown/">living in Totterdown</a> for house prices, rents and local services.</p>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
