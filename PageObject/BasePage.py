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
            element = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(object))
            
        return element

    def click_element(self, object):

        element = self.handle_exceptions(object)
        element.click()

    def get_element(self, object):

        return self.handle_exceptions(object)