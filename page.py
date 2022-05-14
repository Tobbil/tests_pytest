from element import BasePageElement
from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def handle_exceptions(self,object):

        try:
            element = self.driver.find_element(*object)

        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located(object))
            
        return element        

    def click_menu_phones(self):
        
        element = self.handle_exceptions(MainPageLocators.MENU_PHONES)
        element.click()

    def test_price_in_list(self):

        return self.handle_exceptions(MainPageLocators.PRICE_IN_LIST)


    def test_phone_name_in_list(self):

        return self.handle_exceptions(MainPageLocators.PHONE_NAME_IN_LIST)
 

    def test_price_in_item_page(self):

        return self.handle_exceptions(MainPageLocators.PRICE_IN_ITEM_PAGE)
 

    def test_phone_name_in_item_page(self):
        
        return self.handle_exceptions(MainPageLocators.PHONE_NAME_IN_ITEM_PAGE)

    def test_description_in_item_page(self):

        return self.handle_exceptions(MainPageLocators.DESCRIPTION_IN_ITEM_PAGE)

    def test_add_to_cart_button(self):

        return self.handle_exceptions(MainPageLocators.ADD_TO_CART_BUTTON)

    def test_go_to_cart(self):

        return self.handle_exceptions(MainPageLocators.GO_TO_CART)

    def test_cart_content(self):

        parent_element = self.handle_exceptions(MainPageLocators.CART)
        element_list = parent_element.find_elements(*MainPageLocators.CART_CHILDREN)
        print(f"Items in cart: {len(element_list)}")
        return len(element_list) == 1

    def test_cart_total(self):

        while True:

            element = self.handle_exceptions(MainPageLocators.CART_TOTAL)
            if len(element.text) > 0:
                break

        return element

    def test_price_in_table(self):

        element = self.handle_exceptions(MainPageLocators.TABLE)
        element_list = element.find_elements(By.TAG_NAME, "td")
        for i in element_list:
            text = i.text
            if text.isnumeric():
                element = i

        return element 

    def test_phone_name_in_table(self):

        element = self.handle_exceptions(MainPageLocators.TABLE)
        element_list = element.find_elements(By.TAG_NAME, "td")

        return element_list[1]    
  
    def test_place_order_button(self):

        element = self.handle_exceptions(MainPageLocators.PLACE_ORDER_BUTTON)

        return element


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source