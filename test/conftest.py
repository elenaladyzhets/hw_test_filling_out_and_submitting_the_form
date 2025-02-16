import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.with_(window_width=1920, window_height=1080)
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    driver_options = webdriver.ChromeOptions()
   # driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield
    browser.quit()