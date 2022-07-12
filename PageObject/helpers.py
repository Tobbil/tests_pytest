from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

class Helpers():

    def __init__(self, driver):

        self.driver = driver
        
    def handle_exceptions(self, object):

            try:
                element = self.driver.find_element(*object)

            except (StaleElementReferenceException, NoSuchElementException):
                element = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(object))
                
            return element

    def send_keys_to_elem(self, object, test_data):

        element = self.handle_exceptions(object)
        timeout = time.time() + 10

        while element.get_attribute("value") == "" and time.time() < timeout:
            element.send_keys(test_data)

    def click_element(self, object):

            element = self.handle_exceptions(object)
            element.click()

    def get_element(self, object):

        return self.handle_exceptions(object)

