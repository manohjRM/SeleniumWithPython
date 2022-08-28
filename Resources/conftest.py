import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def launch_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    # request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()


@pytest.mark.usefixtures("launch_browser")
class BaseTest:
    pass
