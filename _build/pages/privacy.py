"""Privacy page. The analytics section follows lib.GA_ID, so it stays accurate."""
import lib

SLUG = 'privacy'
MODIFIED = '2026-11-02'


def build(data):
    if lib.GA_ID:
        analytics = f'''
    <h2 id="analytics">Analytics and cookies</h2>
    <p>If you choose "Allow" on the cookie banner, the site uses Google Analytics to count visits and see which pages and buttons are used. Google Analytics sets cookies and records things like the pages you view, your approximate location, and your device and browser. It isn't used to identify you. If you choose "No thanks", or make no choice, Google Analytics doesn't load and no analytics cookies are set.</p>
    <p>Google processes this data on the site's behalf. See {lib.ext('https://policies.google.com/technologies/partner-sites', "how Google uses information from sites that use its services")}.</p>
    <p>You can change your choice at any time: <button type="button" class="linkish" data-consent-reset>change cookie settings</button>.</p>
'''
    else:
        analytics = '''
    <h2 id="analytics">Analytics and cookies</h2>
    <p>The site doesn't set cookies or use analytics that track you. Cloudflare, which hosts the site, keeps short-lived server logs to deliver pages and protect the site from attacks.</p>
'''
    body = f'''
    <p>This site is run by the owner of the domain name {lib.NAME}. This page explains what data the site collects and why.</p>
{analytics}
    <h2 id="form">Contact and offer form</h2>
    <p>The "Make an offer" button and the contact links open a Google Form. The details you enter are stored in Google Forms and used only to reply to your enquiry. They aren't sold or shared with anyone else, and other people who fill in the form can't see your answers.</p>

    <h2 id="hosting">Hosting</h2>
    <p>The site is served by Cloudflare. Like any website host, Cloudflare processes your IP address to deliver pages and block attacks. See {lib.ext('https://www.cloudflare.com/privacypolicy/', "Cloudflare's privacy policy")}.</p>

    <h2 id="other-websites">Other websites</h2>
    <p>This site links to other websites, which have their own privacy policies. We aren't responsible for how those websites collect or use your data.</p>

    <h2 id="rights">Your rights</h2>
    <p>Under UK data protection law you can ask to see, correct or delete data held about you. To do this, use the {lib.form_link('contact form')} and say your message is about privacy. You can also complain to the {lib.ext('https://ico.org.uk/make-a-complaint/', "Information Commissioner's Office")}.</p>
'''
    html = lib.plain(SLUG, f'Privacy – {lib.NAME}', f'What data {lib.NAME} collects, why, and your choices.',
                     'Privacy', MODIFIED, body, 'privacy', robots='noindex, follow')
    return SLUG, html
