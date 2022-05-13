from element import BasePageElement
from locators import MainPageLocators
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

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_menu_phones(self):
        
        try:
            element = self.driver.find_element(*MainPageLocators.MENU_PHONES)
            element.click()

        except StaleElementReferenceException:
            element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located(MainPageLocators.MENU_PHONES))
            element.click()

        except NoSuchElementException:
            element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located(MainPageLocators.MENU_PHONES))
            element.click()

    def go_to_price(self):

        try:
            element = self.driver.find_element(*MainPageLocators.PRICE_IN_LIST)

        except (StaleElementReferenceException, NoSuchElementException): # bez "*" przed MainPageLocators bo ma być nieunpackowany!
            element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located(MainPageLocators.PRICE_IN_LIST))

        # except NoSuchElementException:
        #     element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located(MainPageLocators.PRICE_IN_LIST))
            
        return element




class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source