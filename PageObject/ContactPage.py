import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage
from PageObject import helpers as h

class ContactPage(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.CONTACT_EMAIL = (By.ID, "recipient-email")
        self.CONTACT_NAME = (By.ID, "recipient-name")
        self.CONTACT_MESSAGE = (By.ID, "message-text")
        self.CONTACT_SEND_BUTTON = (By.CSS_SELECTOR, "#exampleModal button.btn.btn-primary")

    def fill_contact_fields(self, test_data):

        # timeout = time.time() + 10

        h.send_keys_to_elem(self.driver,self.CONTACT_EMAIL,test_data["email"])
        h.send_keys_to_elem(self.driver,self.CONTACT_NAME,test_data["name"])
        h.send_keys_to_elem(self.driver,self.CONTACT_MESSAGE,test_data["message"])