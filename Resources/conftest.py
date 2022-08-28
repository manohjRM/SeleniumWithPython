import pytest

from Pages.keywordsClass import KeyClass
from Resources.readProperties import ReadConfig


@pytest.fixture(params=["Chrome", "Firefox"], scope='class')
def launch_browser(request):
    if request.param == "Chrome":
        driver = KeyClass.driver_chrome()
    if request.param == "Firefox":
        driver = KeyClass.driver_firefox()
    url = "https://www.saucedemo.com/"
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("launch_browser")
class BaseTest:
    pass
