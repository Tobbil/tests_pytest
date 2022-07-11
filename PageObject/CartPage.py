import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasePage
from PageObject import helpers as h

class CartPage(BasePage):

    def __init__(self,driver):

        self.driver = driver
        self.CART = (By.CLASS_NAME, "table-responsive")
        self.CART_CHILDREN = (By.ID, "tbodyid")
        self.CART_TOTAL = (By.XPATH, "//*[@id='totalp']")
        self.TABLE = (By.CLASS_NAME, "success") 
        self.PLACE_ORDER_BUTTON = (By.CLASS_NAME, "btn.btn-success")

    def test_cart_content(self):

        parent_element = h.get_element(self.driver, self.CART)
        element_list = parent_element.find_elements(*self.CART_CHILDREN)
        print(f"Items in cart: {len(element_list)}")
        return len(element_list) == 1

    def get_cart_total(self):

        timeout = time.time() + 10  

        while time.time() < timeout:

            element = h.get_element(self.driver, self.CART_TOTAL)
            if len(element.text) > 0:
                break

        return element

    def get_price_in_table(self):

        element = h.get_element(self.driver, self.TABLE)
        element_list = element.find_elements(By.TAG_NAME, "td")
        for i in element_list:
            text = i.text
            if text.isnumeric():
                element = i

        return element 

    def get_phone_name_in_table(self):

        element = h.get_element(self.driver, self.TABLE)
        element_list = element.find_elements(By.TAG_NAME, "td")

        return element_list[1]