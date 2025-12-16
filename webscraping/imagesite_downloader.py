from playwright.sync_api import sync_playwright as sp
import bs4

playwright = sp().start()
browser = playwright.firefox.launch(headless = False, slow_mo=50)
page = browser.new_page()
page.goto('https://www.pexels.com/')

if page.is_visible('#__next > header > div.HeroHeader_content__Pbldf.Flex_flex__3z447.Flex_flex-direction-column__olKIE.spacing_noMargin__F5u9R'):
    page

print(page.title())
browser.close()