import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager' #для неспешного ДемоКуа
   # driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield
    browser.quit()