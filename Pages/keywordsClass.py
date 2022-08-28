from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ecs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class KeyClass:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def driver_chrome():
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def click_element(self, by_loc):
        WebDriverWait(self.driver, 10).until(ecs.visibility_of_element_located(by_loc)).click()

    def do_send_keys(self, by_loc, text):
        WebDriverWait(self.driver, 10).until(ecs.visibility_of_element_located(by_loc)).send_keys(text)

    def is_visible(self, by_loc):
        element = WebDriverWait(self.driver, 10).until(ecs.visibility_of_element_located(by_loc))
        return bool(element)

    def get_text(self, by_loc):
        ele = WebDriverWait(self.driver, 10).until(ecs.visibility_of_element_located(by_loc))
        return ele.text

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ecs.title_is(title))
        return self.driver.title
