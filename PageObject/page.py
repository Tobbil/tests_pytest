from lib2to3.pgen2 import driver
from re import S
import sys
import time
from element import BasePageElement
from locators import ContactPageLocators, MainPageLocators, CartPageLocators, CheckoutPageLocators
from selenium import webdriver
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

    def click_menu_phones(self):
        
        element = self.handle_exceptions(self.MENU_PHONES)
        element.click()

    def get_price_in_list(self):

        return self.handle_exceptions(self.PRICE_IN_LIST)


    def get_phone_name_in_list(self):

        return self.handle_exceptions(self.PHONE_NAME_IN_LIST)
 

    def get_price_in_item_page(self):

        return self.handle_exceptions(self.PRICE_IN_ITEM_PAGE)
 

    def get_phone_name_in_item_page(self):
        
        return self.handle_exceptions(self.PHONE_NAME_IN_ITEM_PAGE)

    def get_description_in_item_page(self):

        return self.handle_exceptions(self.DESCRIPTION_IN_ITEM_PAGE)

    def get_add_to_cart_button(self):

        return self.handle_exceptions(self.ADD_TO_CART_BUTTON)

    def get_go_to_cart(self):

        return self.handle_exceptions(self.GO_TO_CART)

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
        self.CHECKOUT_OK_BUTTON = CheckoutPageLocators.CHECKOUT_OK_BUTTON

    def get_total_in_checkout(self):

        timeout = time.time() + 10  

        while time.time() < timeout:

            element = self.handle_exceptions(self.CHECKOUT_TOTAL)
            if len(element.text) > 0:
                break

        return element

    def get_checkout_form(self):
        
        checkout_name = self.handle_exceptions(self.CHECKOUT_FORM_NAME)
        checkout_country = self.handle_exceptions(self.CHECKOUT_FORM_COUNTRY)
        checkout_city = self.handle_exceptions(self.CHECKOUT_FORM_CITY)
        checkout_card = self.handle_exceptions(self.CHECKOUT_FORM_CARD)
        checkout_month = self.handle_exceptions(self.CHECKOUT_FORM_MONTH)
        checkout_year = self.handle_exceptions(self.CHECKOUT_FORM_YEAR)

        return checkout_name, checkout_country, checkout_city, checkout_card, checkout_month, checkout_year
        
    def get_submit_purchase(self):

        return self.handle_exceptions(self.CHECKOUT_SUBMIT_BUTTON)

    def get_OK_button_purchase(self):

        return self.handle_exceptions(self.CHECKOUT_OK_BUTTON)

class ContactPage(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.CONTACT = ContactPageLocators.CONTACT
        self.CONTACT_EMAIL = ContactPageLocators.CONTACT_EMAIL
        self.CONTACT_NAME = ContactPageLocators.CONTACT_NAME
        self.CONTACT_MESSAGE = ContactPageLocators.CONTACT_MESSAGE
        self.CONTACT_SEND_BUTTON = ContactPageLocators.CONTACT_SEND_BUTTON

    def click_contact_link(self):

        element = self.handle_exceptions(self.CONTACT)
        element.click()

    def get_contact_email_field(self):

        return self.handle_exceptions(self.CONTACT_EMAIL)

    def get_contact_name_field(self):

        return self.handle_exceptions(self.CONTACT_NAME)
        
    def get_contact_message_field(self):

        return self.handle_exceptions(self.CONTACT_MESSAGE)

    def click_send_button(self):

        element = self.handle_exceptions(self.CONTACT_SEND_BUTTON)
        element.click()