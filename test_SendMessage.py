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

class TestSendMessage(WebDriverSetup):

    test_data = {"email":"tester@gmail.com","name":"Mr Tester","message":"Hello!"}

    def test_send_message(self):

        driver = self.driver
        test_data = self.test_data
        main_page = page.MainPage(driver)
        contact_page = page.ContactPage(driver)
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/")
        main_page.click_contact_link()
        element = contact_page.get_contact_email_field()
        element.send_keys(test_data["email"])
        self.assertEqual(test_data["email"],element.get_attribute("value")) # VERIFY IF INPUT IS CORRECT
        element = contact_page.get_contact_name_field()
        element.send_keys(test_data["name"])
        self.assertEqual(test_data["name"],element.get_attribute("value"))
        element = contact_page.get_contact_message_field()
        element.send_keys(test_data["message"])
        self.assertEqual(test_data["message"],element.get_attribute("value"))
        time.sleep(1)
        contact_page.click_send_button()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()

if __name__ == "__main__":
    unittest.main()