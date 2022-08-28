from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.keywordsClass import KeyClass


class LoginPage(KeyClass):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    add_backpack = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    remove_backpack = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    cart_count = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def __init__(self, driver):
        super().__init__(driver)

    def title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        self.do_send_keys(self.username, username)
        self.do_send_keys(self.password, password)
        self.click_element(self.login_button)

    def add_to_cart(self):
        self.is_visible(self.add_backpack)
        print("Add to cart available")
        self.click_element(self.add_backpack)
        print("Add to cart success")

    def add_to_cart_success(self):
        count = self.get_text(self.cart_count)
        return count

    def change_to_remove_button(self):
        remove = self.is_visible(self.remove_backpack)
        print("Remove button available")
        return remove

