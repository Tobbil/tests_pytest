import time
from PageObject.locators import ContactPageLocators, LogInPageLocators, MainPageLocators, CartPageLocators, CheckoutPageLocators, SignUpPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:

    def handle_exceptions(self, object):

        try:
            element = self.driver.find_element(*object)

        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located(object))
            
        return element

    def click_element(self, object):

        element = self.handle_exceptions(object)
        element.click()

    def get_element(self, object):

        return self.handle_exceptions(object)

class MainPage(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.MENU_PHONES = MainPageLocators.MENU_PHONES
        self.PRICE_IN_LIST = MainPageLocators.PRICE_IN_LIST
        self.PHONE_NAME_IN_LIST = MainPageLocators.PHONE_NAME_IN_LIST
        self.PRICE_IN_ITEM_PAGE = MainPageLocators.PRICE_IN_ITEM_PAGE
        self.PHONE_NAME_IN_ITEM_PAGE = MainPageLocators.PHONE_NAME_IN_ITEM_PAGE
        self.DESCRIPTION_IN_ITEM_PAGE = MainPageLocators.DESCRIPTION_IN_ITEM_PAGE
        self.ADD_TO_CART_BUTTON = MainPageLocators.ADD_TO_CART_BUTTON
        self.GO_TO_CART = MainPageLocators.GO_TO_CART
        self.CONTACT = MainPageLocators.CONTACT
        self.SIGN_UP = MainPageLocators.SIGN_UP
        self.LOG_IN = MainPageLocators.LOG_IN
        self.LOG_OUT = MainPageLocators.LOG_OUT
        self.USERNAME_IN_MENU = MainPageLocators.USERNAME_IN_MENU

class CartPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.CART = CartPageLocators.CART
        self.CART_CHILDREN = CartPageLocators.CART_CHILDREN
        self.CART_TOTAL = CartPageLocators.CART_TOTAL
        self.TABLE = CartPageLocators.TABLE
        self.PLACE_ORDER_BUTTON = CartPageLocators.PLACE_ORDER_BUTTON

    def test_cart_content(self):

        parent_element = self.handle_exceptions(self.CART)
        element_list = parent_element.find_elements(*self.CART_CHILDREN)
        print(f"Items in cart: {len(element_list)}")
        return len(element_list) == 1

    def get_cart_total(self):

        timeout = time.time() + 10  

        while time.time() < timeout:

            element = self.handle_exceptions(self.CART_TOTAL)
            if len(element.text) > 0:
                break

        return element

    def get_price_in_table(self):

        element = self.handle_exceptions(self.TABLE)
        element_list = element.find_elements(By.TAG_NAME, "td")
        for i in element_list:
            text = i.text
            if text.isnumeric():
                element = i

        return element 

    def get_phone_name_in_table(self):

        element = self.handle_exceptions(self.TABLE)
        element_list = element.find_elements(By.TAG_NAME, "td")

        return element_list[1]    
  
    def get_place_order_button(self):

        element = self.handle_exceptions(self.PLACE_ORDER_BUTTON)

        return element

class CheckoutPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.CHECKOUT_TOTAL = CheckoutPageLocators.CHECKOUT_TOTAL
        self.CHECKOUT_FORM_NAME = CheckoutPageLocators.CHECKOUT_FORM_NAME
        self.CHECKOUT_FORM_COUNTRY = CheckoutPageLocators.CHECKOUT_FORM_COUNTRY
        self.CHECKOUT_FORM_CITY = CheckoutPageLocators.CHECKOUT_FORM_CITY
        self.CHECKOUT_FORM_CARD = CheckoutPageLocators.CHECKOUT_FORM_CARD
        self.CHECKOUT_FORM_MONTH = CheckoutPageLocators.CHECKOUT_FORM_MONTH
        self.CHECKOUT_FORM_YEAR = CheckoutPageLocators.CHECKOUT_FORM_YEAR
        self.CHECKOUT_SUBMIT_BUTTON = CheckoutPageLocators.CHECKOUT_SUBMIT_BUTTON
        self.CHECKOUT_CONFIRMATION = CheckoutPageLocators.CHECKOUT_CONFIRMATION
        self.CHECKOUT_OK_BUTTON = CheckoutPageLocators.CHECKOUT_OK_BUTTON

    def get_total_in_checkout(self):

        timeout = time.time() + 10  

        while time.time() < timeout:

            element = self.handle_exceptions(self.CHECKOUT_TOTAL)
            if len(element.text) > 0:
                break

        return element

    def fill_checkout_form(self, test_data):
        
        checkout_name = self.handle_exceptions(self.CHECKOUT_FORM_NAME)
        while checkout_name.get_attribute("value") == "":
            checkout_name.send_keys(test_data["name"])
        checkout_country = self.handle_exceptions(self.CHECKOUT_FORM_COUNTRY)
        while checkout_country.get_attribute("value") == "":
            checkout_country.send_keys(test_data["country"])
        checkout_city = self.handle_exceptions(self.CHECKOUT_FORM_CITY)
        while checkout_city.get_attribute("value") == "":
            checkout_city.send_keys(test_data["city"])
        checkout_card = self.handle_exceptions(self.CHECKOUT_FORM_CARD)
        while checkout_card.get_attribute("value") == "":
            checkout_card.send_keys(test_data["card"])
        checkout_month = self.handle_exceptions(self.CHECKOUT_FORM_MONTH)
        while checkout_month.get_attribute("value") == "":
            checkout_month.send_keys(test_data["month"])
        checkout_year = self.handle_exceptions(self.CHECKOUT_FORM_YEAR)
        while checkout_year.get_attribute("value") == "":
            checkout_year.send_keys(test_data["year"])

class ContactPage(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.CONTACT_EMAIL = ContactPageLocators.CONTACT_EMAIL
        self.CONTACT_NAME = ContactPageLocators.CONTACT_NAME
        self.CONTACT_MESSAGE = ContactPageLocators.CONTACT_MESSAGE
        self.CONTACT_SEND_BUTTON = ContactPageLocators.CONTACT_SEND_BUTTON

    def fill_contact_fields(self, test_data):

        element = self.get_element(self.CONTACT_EMAIL)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["email"])
        
        element = self.get_element(self.CONTACT_NAME)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["name"])

        element = self.get_element(self.CONTACT_MESSAGE)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["message"])

class SignUpPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.USERNAME = SignUpPageLocators.USERNAME
        self.PASSWORD = SignUpPageLocators.PASSWORD
        self.SIGN_UP_BUTTON = SignUpPageLocators.SIGN_UP_BUTTON

    def fill_username_and_password(self,test_data):

        element = self.get_element(self.USERNAME)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["username"])
        
        element = self.get_element(self.PASSWORD)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["password"])

class LogInPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.USERNAME = LogInPageLocators.USERNAME
        self.PASSWORD = LogInPageLocators.PASSWORD
        self.LOGIN_BUTTON = LogInPageLocators.LOGIN_BUTTON

    def fill_username_and_password(self,test_data):

        element = self.get_element(self.USERNAME)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["username"])

        element = self.get_element(self.PASSWORD)
        while element.get_attribute("value") == "":
            element.send_keys(test_data["password"])

