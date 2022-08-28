import time

from Pages.pageObjects import Login
import pytest

from Resources.conftest import BaseTest, launch_browser


class TestLoginPage(BaseTest):

    def test_login_swag_labs(self):
        self.loginPage = Login(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.get_title("Swag Labs")
        print("\n"+self.driver.title)
