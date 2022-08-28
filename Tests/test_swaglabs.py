import time

from Pages.pageObjects import Login
import pytest

from Resources.conftest import BaseTest


class TestLoginPage:

    def test_login_swag_labs(self, launch_browser):
        self.loginPage = Login(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        assert self.driver.title == "Swag Labs"
        print("\n")
        print(self.Driver.title)
        time.sleep(5)
