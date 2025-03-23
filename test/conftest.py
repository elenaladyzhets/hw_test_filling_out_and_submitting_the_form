import pytest, os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import warnings


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    warnings.simplefilter("ignore", UserWarning)
    warnings.simplefilter("ignore", PendingDeprecationWarning)

    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    url = os.getenv('URL')

    # Проверка значений переменных окружения
    print(f"LOGIN: {login}, PASSWORD: {password}, URL: {url}")

    # Проверьте, что URL не равен 'none'
    if url == 'none':
        raise ValueError("URL is not correctly set in the environment variables.")

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}/wd/hub",
        options=options)

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()