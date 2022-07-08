import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage

class MainPage(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.MENU_PHONES = (By.LINK_TEXT, "Phones")
        self.PRICE_IN_LIST = (By.CSS_SELECTOR, "#tbodyid h5")
        self.PHONE_NAME_IN_LIST = (By.CSS_SELECTOR, "#tbodyid h4")
        self.PRICE_IN_ITEM_PAGE = (By.CLASS_NAME, "price-container")
        self.PHONE_NAME_IN_ITEM_PAGE = (By.CSS_SELECTOR, "#tbodyid h2")
        self.DESCRIPTION_IN_ITEM_PAGE = (By.CSS_SELECTOR, "#more-information p")
        self.ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#tbodyid a.btn.btn-success.btn-lg")
        self.GO_TO_CART = (By.CSS_SELECTOR, "#cartur")
        self.CONTACT = (By.LINK_TEXT, "Contact")
        self.SIGN_UP = (By.ID, "signin2")
        self.LOG_IN = (By.ID, "login2")
        self.LOG_OUT = (By.ID, "logout2")
        self.USERNAME_IN_MENU = (By.ID, "nameofuser")