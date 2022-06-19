import time
import unittest
import os
import sys
from PageObject import page
from WebDriverSetup import WebDriverSetup
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
        driver.get("https://www.demoblaze.com/")
        main_page.click_element(main_page.CONTACT)
        contact_page.fill_contact_fields(test_data)
        time.sleep(1)
        contact_page.click_element(contact_page.CONTACT_SEND_BUTTON)
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertEqual("Thanks for the message!!",alert.text)
        time.sleep(1)
        alert.accept()

if __name__ == "__main__":
    unittest.main()