# imports
from playwright.sync_api import sync_playwright


# launching chrome
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    # page.evaluate()
    page.goto('https://www.praxisdienst.com/')
    page.wait_for_timeout(1500)
    # print(page.title())

    # check popup exists or not
    # print(page.locator('css=div.c-header__modal--enabled').count())
    # print(page.locator('css=div.c-header__infobar-right').count())

    discipline_block = page.locator('css=#TargetgroupForm')
    # btns = discipline_block.locator('css=button[name="targetgroupid"]').all()
    # print(btns)

    btn = discipline_block.locator('css=button[name="targetgroupid"]').nth(2)
    print(btn.get_attribute('data-redirect'))

    browser.close()