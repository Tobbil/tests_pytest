import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage
from PageObject import helpers as h

class LogInPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.USERNAME = (By.ID, "loginusername")
        self.PASSWORD = (By.ID, "loginpassword")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal button.btn.btn-primary")

    def fill_username_and_password(self,test_data):

        h.send_keys_to_elem(self.driver,self.USERNAME,test_data["username"])
        h.send_keys_to_elem(self.driver,self.PASSWORD,test_data["password"])

        