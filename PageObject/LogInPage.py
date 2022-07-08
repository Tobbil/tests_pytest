import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage

class LogInPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.USERNAME = (By.ID, "loginusername")
        self.PASSWORD = (By.ID, "loginpassword")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal button.btn.btn-primary")

    def fill_username_and_password(self,test_data):

        timeout = time.time() + 10

        element = self.get_element(self.USERNAME)
        while element.get_attribute("value") == "" and time.time() < timeout:
            element.send_keys(test_data["username"])

        element = self.get_element(self.PASSWORD)
        while element.get_attribute("value") == "" and time.time() < timeout:
            element.send_keys(test_data["password"])