import time
import unittest
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleUseCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/users/perfectson/Documents/Testing/Selenium boilerplate/Selenium-Python-Boilerplate/tests/chromedriver")
#djksajdkasjd
    def test_google_use_case(self):
        driver = self.driver
        driver.get("https://www.google.com/maps")
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Doonbeg")
        time.sleep(0.5)
        elem = driver.find_element(By.ID, "searchbox-searchbutton")
        elem.click()
        time.sleep(0.5)
        elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.DUwDvf.fontHeadlineLarge"))).text
        self.assertEqual("Doonbeg",elem,"Not equal")
        print(f"'Doonbeg' is in the searchbox.")
        time.sleep(1)
        elem = driver.find_element(By.CSS_SELECTOR, "button.S9kvJb")
        elem.click()
        elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sb_ifc52 > input")))
        aria_label = elem.get_attribute("aria-label")
        self.assertIn("Doonbeg",aria_label,"Not in field")
        print(f"'Doonbeg' is in '{aria_label}'.")
        time.sleep(3)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()