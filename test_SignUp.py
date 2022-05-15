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

class TestSignUp(WebDriverSetup):

    test_data = {"username":"MrTester","password":"test0TEST."}

    def test_sign_up(self):

        driver = self.driver
        test_data = self.test_data
        main_page = page.MainPage(driver)
        signup_page = page.SignUpPage(driver)
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/")
        main_page.click_signup_link()
        element = signup_page.get_username_field()
        element.send_keys(test_data["username"])
        element = signup_page.get_password_field()
        element.send_keys(test_data["password"])
        time.sleep(1)
        signup_page.click_signup_button()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Alert message: {alert.text}")
        alert.accept()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()