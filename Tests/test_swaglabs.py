from Pages.pageObjects import LoginPage

from Resources.conftest import BaseTest, launch_browser


class TestLoginPage(BaseTest):

    def test_swag_labs(self):
        self.swag_labs = LoginPage(self.driver)
        self.swag_labs.get_title("Swag Labs")

    def test_login_swag_labs(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.get_title("Swag Labs")
        print("\n" + self.driver.title)

    def test_add_to_cart(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.add_to_cart()

    def test_shopping_cart_count(self):
        self.loginPage = LoginPage(self.driver)
        count = self.loginPage.add_to_cart_success()
        assert count == "1"
        print("One item add to cart successfully")

    def test_remove_button_presence(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.change_to_remove_button() == 1
