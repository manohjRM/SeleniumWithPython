import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Pages.keywordsClass import KeyClass


@pytest.fixture(scope='class')
def launch_browser(request):
    driver = KeyClass.driver_chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("launch_browser")
class BaseTest:
    pass
