import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def launch_browser(request):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("launch_browser")
class BaseTest:
    pass
