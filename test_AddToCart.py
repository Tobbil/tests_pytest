import sys
import time
import unittest
import os
from WebDriverSetup import WebDriverSetup
from PageObject import page
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(WebDriverSetup):

    test_data = {"name":"Mr Test","country":"Norway","city":"Tromsø",
                "card":"4376232127005830","month":"May","year":"2022"}
        
    def test_add_to_cart(self):
        driver = self.driver
        test_data = self.test_data
        driver.implicitly_wait(10)
        driver.get("https://www.demoblaze.com/")
        main_page = page.MainPage(driver)
        cart_page = page.CartPage(driver)
        checkout_page = page.CheckoutPage(driver)
        main_page.click_menu_phones()
        element = main_page.get_price_in_list()
        self.assertEqual("$360",element.text)
        element = main_page.get_phone_name_in_list()
        self.assertEqual("Samsung galaxy s6",element.text)
        element = main_page.get_phone_name_in_list()
        element.click()
        element = main_page.get_price_in_item_page()
        price_add_to_cart_trimmed = element.text.replace(" *includes tax","")
        self.assertEqual("$360",price_add_to_cart_trimmed)
        element = main_page.get_phone_name_in_item_page()
        self.assertEqual("Samsung galaxy s6",element.text)
        element = main_page.get_description_in_item_page()
        self.assertNotEqual("",element.text)
        self.assertNotEqual(" ",element.text)
        element = main_page.get_add_to_cart_button()
        self.assertEqual("Add to cart",element.text)
        element.click()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        self.assertEqual("Product added",message)
        alert.accept()
        element = main_page.get_go_to_cart()
        element.click()
        self.assertTrue(cart_page.test_cart_content())
        element = cart_page.get_cart_total()
        self.assertIn(element.text,"$360")
        element = cart_page.get_price_in_table()
        self.assertIn(element.text,"$360")
        element = cart_page.get_phone_name_in_table()
        self.assertEqual("Samsung galaxy s6",element.text)
        # tu test dla delete

        # tu test dla delete
        element = cart_page.get_place_order_button()
        self.assertEqual("Place Order",element.text)
        element.click()
        element = checkout_page.get_total_in_checkout()
        price_checkout_trimmed = element.text.replace("Total: ","")
        self.assertEqual(price_checkout_trimmed,"360")
        checkout_elements = checkout_page.get_checkout_form()
        checkout_elements[0].send_keys(test_data["name"])
        checkout_elements[1].send_keys(test_data["country"])
        checkout_elements[2].send_keys(test_data["city"])
        checkout_elements[3].send_keys(test_data["card"])
        checkout_elements[4].send_keys(test_data["month"])
        checkout_elements[5].send_keys(test_data["year"])
        time.sleep(1)
        element = checkout_page.get_submit_purchase()
        element.click()
        # tu assert danych w alercie
        
        # tu assert danych w alercie
        element = checkout_page.get_OK_button_purchase()
        element.click()

if __name__ == "__main__":
    unittest.main()