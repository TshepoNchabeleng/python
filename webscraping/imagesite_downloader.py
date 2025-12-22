from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto("https://unsplash.com/images")

search_input = page.locator('input[name="searchKeyword"]')
search_input.fill("Dog")
search_input.press("Enter")
#page.get_by_role("button", title="Search Unsplash", exact=False).click()
#page.locator('.button-ns_esx resetBtn-aZVYwi').click()

filter_button = page.get_by_role("button", name='Filters')
filter_button.click()
page.locator('html').press('End')

page.get_by_role("button", name='Free').click()
page.get_by_role("button", name='Apply').click()

photo_links = page.locator('a[href*="/photos/"]').all()

def next_btn ():
    page.keyboard.press("ArrowRight")
    print("Next button pressed")


for i in range(3):
    photo_links[i].click()

    download_button = page.locator('a:has-text("Download free")').first

    try:
        download_button.wait_for(state="visible", timeout=10000)

        with page.expect_download() as download_info:
            download_button.click()

            download = download_info.value
            download.save_as(f"./{download.suggested_filename}")
            next_btn()
            print(f"Downloaded: {download.suggested_filename}")
    except Exception as e:
        print(f"Could not find download button: {e}")


"""
for i in range(10):
    download_button.click()
    next_button.click()
"""

page.wait_for_timeout(5000)

browser.close()
playwright.stop()