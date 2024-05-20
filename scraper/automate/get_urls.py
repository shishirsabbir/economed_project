# imports
from playwright.sync_api import sync_playwright


# launch browser
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.goto('https://www.praxisdienst.com/')
    page.wait_for_timeout(1500)

    type_url_list = []

    if page.locator('css=div.c-header__modal--enabled').count():
        discipline_block = page.locator('css=#TargetgroupForm')

        btns = discipline_block.locator('css=button[name="targetgroupid"]').all()
        
        for btn in btns:
            print(btn.get_attribute('data-redirect'))

    
    browser.close()