# imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep as wait_for


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('start-maximized')
chrome_options.add_argument(r"--user-data-dir=C:\Users\shishirsabbir\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"--profile-directory=Profile 1")
chrome_options.add_argument('--ignore-certificate-errors')

service = Service(executable_path='./webdriver/chromedriver.exe')


# initialize chrome
def run_driver(driver_service=service, driver_option=chrome_options):
    return webdriver.Chrome(service=driver_service, options=driver_option)


# click using action
def click_action(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)

    ActionChains(driver).move_to_element(element).pause(1).click().perform()
    wait_for(1)

