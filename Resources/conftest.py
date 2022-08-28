import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Pages.keywordsClass import KeyClass
from Resources.readProperties import ReadConfig


@pytest.fixture(scope='class')
def launch_browser(request):
    driver = KeyClass.driver_chrome()
    url = "https://www.saucedemo.com/"
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("launch_browser")
class BaseTest:
    pass
