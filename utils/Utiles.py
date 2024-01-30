import os
import pytest
from config.configurar_browser import BrowserConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    driver = BrowserConfig(browser).select_browser()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://wikipedia.org")
    request.cls.driver = driver
    yield
    driver.quit()
    print("Test Completed")