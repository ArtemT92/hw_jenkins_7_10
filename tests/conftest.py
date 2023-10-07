import pytest
import os

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config



from utils import attach

PROJECT_ROOT_PATH = os.path.dirname(__file__)
print(PROJECT_ROOT_PATH)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )




@pytest.fixture(scope='function', autouse=True)
def browser_managment(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
