import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage

class CheckoutPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.CHECKOUT_TOTAL = (By.CSS_SELECTOR, "#orderModal #totalm")
        self.CHECKOUT_FORM_NAME = (By.CSS_SELECTOR, "#orderModal #name")
        self.CHECKOUT_FORM_COUNTRY = (By.CSS_SELECTOR, "#orderModal #country")
        self.CHECKOUT_FORM_CITY = (By.CSS_SELECTOR, "#orderModal #city")
        self.CHECKOUT_FORM_CARD = (By.CSS_SELECTOR, "#orderModal #card")
        self.CHECKOUT_FORM_MONTH = (By.CSS_SELECTOR, "#orderModal #month")
        self.CHECKOUT_FORM_YEAR = (By.CSS_SELECTOR, "#orderModal #year")
        self.CHECKOUT_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#orderModal button.btn.btn-primary")
        self.CHECKOUT_CONFIRMATION = (By.CSS_SELECTOR, "p.lead.text-muted")
        self.CHECKOUT_OK_BUTTON = (By.CSS_SELECTOR, "button.confirm.btn.btn-lg.btn-primary")

    def get_total_in_checkout(self):

        timeout = time.time() + 10  

        while time.time() < timeout:

            element = self.handle_exceptions(self.CHECKOUT_TOTAL)
            if len(element.text) > 0:
                break

        return element

    def fill_checkout_form(self, test_data):
        
        timeout = time.time() + 10

        checkout_name = self.handle_exceptions(self.CHECKOUT_FORM_NAME)
        while checkout_name.get_attribute("value") == "" and time.time() < timeout:
            checkout_name.send_keys(test_data["name"])
        checkout_country = self.handle_exceptions(self.CHECKOUT_FORM_COUNTRY)
        while checkout_country.get_attribute("value") == "" and time.time() < timeout:
            checkout_country.send_keys(test_data["country"])
        checkout_city = self.handle_exceptions(self.CHECKOUT_FORM_CITY)
        while checkout_city.get_attribute("value") == "" and time.time() < timeout:
            checkout_city.send_keys(test_data["city"])
        checkout_card = self.handle_exceptions(self.CHECKOUT_FORM_CARD)
        while checkout_card.get_attribute("value") == "" and time.time() < timeout:
            checkout_card.send_keys(test_data["card"])
        checkout_month = self.handle_exceptions(self.CHECKOUT_FORM_MONTH)
        while checkout_month.get_attribute("value") == "" and time.time() < timeout:
            checkout_month.send_keys(test_data["month"])
        checkout_year = self.handle_exceptions(self.CHECKOUT_FORM_YEAR)
        while checkout_year.get_attribute("value") == "" and time.time() < timeout:
            checkout_year.send_keys(test_data["year"])