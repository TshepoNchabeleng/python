from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto("https://unsplash.com/images", timeout= 60000)

search_input = page.locator('input[name="searchKeyword"]')
search_input.fill("Open path POV")
search_input.press("Enter")
#page.get_by_role("button", title="Search Unsplash", exact=False).click()
#page.locator('.button-ns_esx resetBtn-aZVYwi').click()

filter_button = page.get_by_role("button", name='Filters')
filter_button.click()
page.locator('html').press('End')

page.get_by_role("button", name='Free').click()
page.get_by_role("button", name='Apply').click()

page.wait_for_selector('div[role="dialog"]', state="hidden")

photo_selector_text = 'figure a[href*="/photos/"]'
page.wait_for_selector(photo_selector_text, state="visible")
photo_links = page.locator(photo_selector_text).all()

num_photos = len(photo_links)
print(f"found {num_photos} photos.")

def next_btn ():
    page.keyboard.press("ArrowRight")
    print("Next button pressed")


last_url = page.url

for i in range(min(3, num_photos)):
    try:
        current_photos = page.locator(photo_selector_text)
        current_photos.nth(i).scroll_into_view_if_needed()
        current_photos.nth(i).click()

        download_selector = 'a[title="Download free"], a[href*="download=true"]'

        page.wait_for_selector(download_selector, state = "visible", timeout=60000)
    
        with page.expect_download() as download_info:
            page.locator(download_selector).first.click()

        download = download_info.value
        path = f"./{download.suggested_filename}"
        download.save_as(path)
        print(f"Downloaded ({i+1}/3): {download.suggested_filename}")

        if page.locator('div[role="dialog"]').is_visible():
            page.keyboard.press("Escape")
        else:
            page.go_back()
            page.wait_for_selector(photo_selector_text)

    except Exception as e:
        print(f"Skipping index {i} due to error: {e}")
        page.goto("https://unsplash.com/s/photos/dog")

page.wait_for_timeout(5000)

browser.close()
playwright.stop()