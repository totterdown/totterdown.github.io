"""Parks and green spaces in and near Totterdown."""
from lib import page

META = {
    'slug': 'parks-in-totterdown',
    'title': "Parks Near Totterdown: Perrett's Park, Victoria Park & More",
    'desc': "Parks and green spaces near Totterdown, Bristol: Perrett's Park views, Victoria Park's water maze, Windmill Hill City Farm, Arnos Vale and the New Cut.",
    'og_desc': "Perrett's Park, Victoria Park, Windmill Hill City Farm, Arnos Vale and the New Cut: green spaces around Totterdown.",
    'crumb': 'Parks and green spaces',
    'h1': 'Parks and green spaces near Totterdown',
    'published': '2026-11-02',
    'modified': '2026-11-02',
}

BODY = r'''    <p class="meta">Updated 2 November 2026. Opening times change, so check before you visit. <a href="/about/">How we check facts</a>.</p>
    <p>Totterdown's own streets are tightly packed terraces, but some of south Bristol's best green spaces are within a short walk, several of them with views back across the city.</p>

    <section class="summary" aria-label="Quick answer">
      <h2>Quick answer</h2>
      <ul>
        <li><strong>Best view:</strong> Perrett's Park, a popular spot to watch the Balloon Fiesta's mass ascents in August. [[perretts]]</li>
        <li><strong>Next door:</strong> Victoria Park in Windmill Hill, with views over Totterdown and the city, and a water maze from 1984. [[vb_windmill]] [[vicpark]]</li>
        <li><strong>With children:</strong> Windmill Hill City Farm, free to enter, with a café open every day. [[farm_visit]] [[farm_contact]]</li>
        <li><strong>For a quiet walk:</strong> Arnos Vale, a Victorian garden cemetery on the Bath Road. [[arnos]]</li>
      </ul>
    </section>

    <nav class="toc" aria-label="Contents">
      <ol>
        <li><a href="#perretts">Perrett's Park</a></li>
        <li><a href="#victoria">Victoria Park</a></li>
        <li><a href="#farm">Windmill Hill City Farm</a></li>
        <li><a href="#arnos">Arnos Vale</a></li>
        <li><a href="#river">The New Cut</a></li>
        <li><a href="#community">Community growing</a></li>
        <li><a href="#sources">Sources</a></li>
      </ol>
    </nav>

    <h2 id="perretts">Why is Perrett's Park worth visiting?</h2>
    <ul>
      <li><strong>The view:</strong> on the edge of Totterdown, Windmill Hill and Knowle, its slopes look out over the city, and it's a popular place to watch the Bristol International Balloon Fiesta's mass ascents in August. [[perretts]]</li>
      <li><strong>Looked after locally:</strong> a community group, the Community of Perrett's Park, holds an annual picnic to raise money for the park. [[perretts]]</li>
    </ul>

    <h2 id="victoria">What is the water maze in Victoria Park?</h2>
    <ul>
      <li><strong>The park:</strong> Victoria Park, next to Totterdown in Windmill Hill, was laid out in the 1880s and has views over Totterdown and central Bristol. [[vicpark_pg]] [[vb_windmill]]</li>
      <li><strong>The water maze:</strong> built in 1984, its pattern copies a carved roof boss in St Mary Redcliffe church, and it sits on the line of an old pipe that carried spring water from Knowle to Redcliffe. [[vicpark]]</li>
      <li><strong>Is it running?</strong> A local petition says the maze has had no water flowing through it for years. [[maze_petition]]</li>
    </ul>

    <h2 id="farm">Is Windmill Hill City Farm free?</h2>
    <p>Yes. Entry is free, though the farm is a charity and asks for donations. [[farm_visit]] It opened in 1976 on derelict ground, and its café is open seven days a week. [[farm_history]] [[farm_contact]] It's in Bedminster, a short walk west of Totterdown.</p>

    <h2 id="arnos">Can you walk around Arnos Vale Cemetery?</h2>
    <p>Yes. Arnos Vale is a Victorian garden cemetery on the Bath Road, on the edge of Totterdown, with its first burial in 1839. Bristol City Council took ownership in 2003, and a charitable trust looks after it. It's still a working cemetery, so be respectful of funerals. [[arnos]] [[arnos_visit]]</p>

    <h2 id="river">Where can you walk by the river near Totterdown?</h2>
    <p>The Avon New Cut runs from Totterdown towards Cumberland Basin, with the brick-paved Chocolate Path on its north bank. [[newcut]] The Friends of the Avon New Cut publish circular walks around it. [[franc_walks]]</p>

    <h2 id="community">Where are Totterdown's community gardens?</h2>
    <ul>
      <li><strong>TRESA's community space</strong> on Park Street hosts events such as an apple pressing in September 2025. [[tresa_space]] [[tresa_events]]</li>
      <li><strong>Front gardens:</strong> the residents' association runs annual Front Garden Awards, giving out more than 260 in one year. [[tresa_gardens]]</li>
      <li><strong>Garden festival:</strong> TRESA lists a garden festival among Totterdown's events through the year. [[tresa_events]] See <a href="/whats-on-in-totterdown/">what's on</a>.</li>
    </ul>
'''


def build(data):
    return META['slug'], page(body=BODY, source=__name__.split('.')[-1], **META)
