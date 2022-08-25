from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.keywordsClass import BaseClass


class Login(BaseClass):
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        self.do_send_keys(self.username, username)
        self.do_send_keys(self.password, password)
        self.click_element(self.login_button)
