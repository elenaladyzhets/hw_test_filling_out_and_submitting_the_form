import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import os
import warnings



@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def setup_browser():
    warnings.filterwarnings("ignore", category=UserWarning, module="selenium.webdriver.remote.remote_connection")
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    if not all([selenoid_login, selenoid_pass, selenoid_url]):
        raise ValueError("Не заданы переменные окружения SELENOID_LOGIN, SELENOID_PASS или SELENOID_URL")

    executor_url = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options,
        keep_alive=True
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()