"""404 page. Cloudflare Pages serves site/404.html for any missing URL."""
import lib

SLUG = '404'


def build(data):
    html = lib.head(f'Page not found – {lib.NAME}', '', SLUG, robots='noindex', source='not_found') + f'''<body>
  <main class="page hub">
    {lib.terrace()}
    <span class="label"><span class="dot" aria-hidden="true"></span> Page not found</span>
    <h1>Lost on the hill?</h1>
    <p class="intro">This page doesn't exist. Try one of the guides instead.</p>
    <div class="guides-section">
      <nav class="guides" aria-label="Guides">
{lib.guide_cards()}
      </nav>
    </div>
  </main>

{lib.footer()}</body>
</html>
'''
    return SLUG, html
