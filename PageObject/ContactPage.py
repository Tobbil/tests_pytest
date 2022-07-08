import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage

class ContactPage(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.CONTACT_EMAIL = (By.ID, "recipient-email")
        self.CONTACT_NAME = (By.ID, "recipient-name")
        self.CONTACT_MESSAGE = (By.ID, "message-text")
        self.CONTACT_SEND_BUTTON = (By.CSS_SELECTOR, "#exampleModal button.btn.btn-primary")

    def fill_contact_fields(self, test_data):

        timeout = time.time() + 10

        element = self.get_element(self.CONTACT_EMAIL)
        while element.get_attribute("value") == "" and time.time() < timeout:
            element.send_keys(test_data["email"])
        
        element = self.get_element(self.CONTACT_NAME)
        while element.get_attribute("value") == "" and time.time() < timeout:
            element.send_keys(test_data["name"])

        element = self.get_element(self.CONTACT_MESSAGE)
        while element.get_attribute("value") == "" and time.time() < timeout:
            element.send_keys(test_data["message"])