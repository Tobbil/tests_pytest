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
        driver.get("https://www.demoblaze.com/")
        main_page.click_element(main_page.LOG_IN)
        login_page.fill_username_and_password(test_data)
        time.sleep(1)
        login_page.click_element(login_page.LOGIN_BUTTON)
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(main_page.USERNAME_IN_MENU,"Welcome"))
        element = main_page.get_element(main_page.USERNAME_IN_MENU)
        self.assertEqual(element.text,f"Welcome {test_data['username']}")
        main_page.click_element(main_page.LOG_OUT)
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(main_page.LOG_IN,"Log in"))
        element = self.driver.find_element(*main_page.LOG_IN)
        self.assertEqual(element.text,"Log in")
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()