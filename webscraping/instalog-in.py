import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

env_path= r'C:\Users\lebak\Documents\python\sensitive.env'
load_dotenv(dotenv_path = env_path)
ig_password = os.environ.get('PASSWORD')
ig_code = os.environ.get('AUTH_PIN')

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://www.instagram.com/', timeout = 100000)

try:
    page.get_by_role("button", name="Allow all cookies").click(timeout=10000)
except:
    pass #if cookies banner does not show up

page.locator('input[name="username"]').fill("tshepo_nchabeleng7")
page.locator('input[name="password"]').fill(ig_password)
page.get_by_role("button", name="Log in", exact=True).click()

try:
    page.locator('input[name="verificationCode"]').fill(ig_code)
    page.get_by_role("button", name="Confirm", exact=True).click()
except:
    pass

page.wait_for_timeout(30000)

browser.close()
playwright.stop()