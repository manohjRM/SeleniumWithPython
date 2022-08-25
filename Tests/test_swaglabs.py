import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages import pageObjects
import pytest

Driver = None


def test_launch_browser():
    global Driver
    Driver = webdriver.Chrome(ChromeDriverManager().install())
    Driver.get("https://www.saucedemo.com/")
    Driver.implicitly_wait(10)
    loginPage = pageObjects.Login(Driver)
    loginPage.login("standard_user", "secret_sauce")
    print("\n")
    print(Driver.title)
    time.sleep(5)
    Driver.close()
