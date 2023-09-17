import pytest
from selene import browser
import os

PROJECT_ROOT_PATH = os.path.dirname(__file__)
print(PROJECT_ROOT_PATH)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 900
    browser.config.window_height = 800

    yield

    browser.quit()
