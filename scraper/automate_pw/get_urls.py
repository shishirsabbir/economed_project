# imports
from playwright.sync_api import sync_playwright


# launch browser
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    page = browser.new_page()
    # page.set_viewport_size({'width': 1366, 'height': 768})
    # page.evaluate('() => {document.body.style.zoom = .75}')
    page.goto('https://www.praxisdienst.com/en/Veterinary/')
    page.wait_for_timeout(1500)

    type_url_list = []

    if page.locator('css=div.c-header__modal--enabled').count():
        discipline_block = page.locator('css=#TargetgroupForm')

        btns = discipline_block.locator('css=button[name="targetgroupid"]').all()
        
        for btn in btns:
            print(btn.get_attribute('data-redirect'))

    
    page.wait_for_timeout(3000)

    
    browser.close()