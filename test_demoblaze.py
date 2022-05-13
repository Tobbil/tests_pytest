import time
import unittest
import os
import sys
import page
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


class TestDemoblazeAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver"))
        self.driver.get("https://www.demoblaze.com/")
        
    def test_add_to_cart(self):
        driver = self.driver
        main_page = page.MainPage(driver)
        main_page.click_menu_phones()
        element = main_page.go_to_price()
        self.assertEqual("$360",element.text)
        price = element.text
        print(price)
        # elem = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbodyid a.hrefch")))
        # self.assertEqual("Samsung galaxy s6",elem.text,"assert FAILED")
        # elem.click()
        # elem = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbodyid h2")))
        # self.assertEqual("Samsung galaxy s6",elem.text,"assert FAILED")
        # elem = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbodyid h3")))
        # price_add_to_cart_trimmed = elem.text.replace(" *includes tax","")
        # self.assertEqual(price,price_add_to_cart_trimmed,"assert FAILED")
        # elem = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#more-information p")))
        # self.assertNotEqual("",elem.text)
        # self.assertNotEqual(" ",elem.text)
        # elem = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tbodyid a.btn.btn-success.btn-lg")))
        # elem.click()
        # time.sleep(3)
        # WebDriverWait(driver, 3).until(EC.alert_is_present())
        # alert = driver.switch_to.alert
        # msg = alert.text
        # self.assertEqual("Product added",msg)
        # print(f"Alert shows the following message: {msg}")
        # alert.accept()
        # elem = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartur")))
        # elem.click()

        time.sleep(10)
        #elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pane h1"))).text
        



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()