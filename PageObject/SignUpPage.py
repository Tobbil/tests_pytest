import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.helpers import Helpers

class SignUpPage:

    def __init__(self,driver):
        global h
        h = Helpers(driver)
        self.driver = driver
        self.USERNAME = (By.ID, "sign-username")
        self.PASSWORD = (By.ID, "sign-password")
        self.SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#signInModal button.btn.btn-primary")

    def fill_username_and_password(self,test_data):

        h.send_keys_to_elem(self.USERNAME,test_data["username"])
        h.send_keys_to_elem(self.PASSWORD,test_data["password"])