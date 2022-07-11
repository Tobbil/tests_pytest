from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

def handle_exceptions(driver, object):

        try:
            element = driver.find_element(*object)

        except (StaleElementReferenceException, NoSuchElementException):
            element = WebDriverWait(driver,5).until(EC.presence_of_element_located(object))
            
        return element

def send_keys_to_elem(driver, object, test_data):

    element = handle_exceptions(driver, object)
    timeout = time.time() + 10

    while element.get_attribute("value") == "" and time.time() < timeout:
        element.send_keys(test_data)

def click_element(driver, object):

        element = handle_exceptions(driver, object)
        element.click()

def get_element(driver, object):

    return handle_exceptions(driver, object)

