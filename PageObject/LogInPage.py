import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.helpers import Helpers
from PageObject.MainPage import MainPage

class LogInPage:

    def __init__(self, driver):
        self.h = Helpers(driver)
        self.driver = driver
        self.main_page = MainPage(driver)
        self.USERNAME = (By.ID, "loginusername")
        self.PASSWORD = (By.ID, "loginpassword")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal button.btn.btn-primary")
        self.CLOSE_BUTTON = (By.CSS_SELECTOR, "#logInModal button.btn.btn-secondary")
        self.LOGIN_MODAL_TITLE = (By.ID, "logInModalLabel")

    def fill_username_and_password(self, username, password):

        self.h.send_keys_to_elem(self.USERNAME,username)
        self.h.send_keys_to_elem(self.PASSWORD,password)

    def log_in(self, username, password):

        self.h.click_element(self.main_page.LOG_IN)
        self.fill_username_and_password(username, password)
        self.h.click_element(self.LOGIN_BUTTON)

        