import time
import unittest
import os
import sys
from PageObject import page
from WebDriverSetup import WebDriverSetup
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class TestLogIn(WebDriverSetup):

    test_data = {"username":"MrTester","password":"test0TEST."}

    def test_login(self):

        driver = self.driver
        test_data = self.test_data
        main_page = page.MainPage(driver)
        login_page = page.LogInPage(driver)
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/")
        main_page.click_login_link()
        element = login_page.get_username_field()
        element.send_keys(test_data["username"])
        self.assertEqual(test_data["username"],element.get_attribute("value"))
        element = login_page.get_password_field()
        element.send_keys(test_data["password"])
        self.assertEqual(test_data["password"],element.get_attribute("value"))
        time.sleep(1)
        login_page.click_login_button()
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(page.MainPageLocators.USERNAME_IN_MENU,"Welcome"))
        element = main_page.get_username_in_menu()
        self.assertEqual(element.text,f"Welcome {test_data['username']}")
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()