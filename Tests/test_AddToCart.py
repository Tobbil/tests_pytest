import sys
import time
import unittest
import os
from datetime import date
from WebDriverSetup import WebDriverSetup
from PageObject import MainPage, CartPage, LogInPage, SignUpPage, ContactPage, CheckoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
from PageObject.helpers import Helpers


class TestAddToCart(WebDriverSetup):

    test_data = {"name":"Mr Test","country":"Norway","city":"Tromsø",
                "card":"4376232127005830","month":"May","year":"2022"}
        
    def test_add_to_cart(self):
        
        driver = self.driver
        test_data = self.test_data
        h = Helpers(driver)
        driver.get("https://www.demoblaze.com/")
        main_page = MainPage.MainPage(driver)
        cart_page = CartPage.CartPage(driver)
        checkout_page = CheckoutPage.CheckoutPage(driver)
        h.click_element(main_page.MENU_PHONES)
        element = h.get_element(main_page.PRICE_IN_LIST)
        self.assertEqual("$360",element.text)
        element = h.get_element(main_page.PHONE_NAME_IN_LIST)
        self.assertEqual("Samsung galaxy s6",element.text)
        h.click_element(main_page.PHONE_NAME_IN_LIST)
        element = h.get_element(main_page.PRICE_IN_ITEM_PAGE)
        price_add_to_cart_trimmed = element.text.replace(" *includes tax","")
        self.assertEqual("$360",price_add_to_cart_trimmed)
        element = h.get_element(main_page.PHONE_NAME_IN_ITEM_PAGE)
        self.assertEqual("Samsung galaxy s6",element.text)
        element = h.get_element(main_page.DESCRIPTION_IN_ITEM_PAGE)
        self.assertNotEqual("",element.text)
        self.assertNotEqual(" ",element.text)
        element = h.get_element(main_page.ADD_TO_CART_BUTTON)
        self.assertEqual("Add to cart",element.text)
        element.click()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        self.assertEqual("Product added",message)
        alert.accept()
        h.click_element(main_page.GO_TO_CART)
        self.assertTrue(cart_page.test_cart_content())
        element = h.get_element(cart_page.CART_TOTAL)
        self.assertIn(element.text,"$360")
        element = cart_page.get_price_in_table()
        self.assertIn(element.text,"$360")
        element = cart_page.get_phone_name_in_table()
        self.assertEqual("Samsung galaxy s6",element.text)
        element = h.get_element(cart_page.PLACE_ORDER_BUTTON)
        self.assertEqual("Place Order",element.text)
        element.click()
        element = checkout_page.get_total_in_checkout()
        self.assertEqual(element,"360")
        checkout_page.fill_checkout_form(test_data)
        time.sleep(1)
        h.click_element(checkout_page.CHECKOUT_SUBMIT_BUTTON)
        element = h.get_element(checkout_page.CHECKOUT_CONFIRMATION).text.split("\n")
        amount = element[1]
        card_number = element[2]
        name = element[3]
        date_today = date.today().strftime('%d/%m/%Y')
        if date_today[3] == "0":
            date_today = date_today[:3] + date_today[4:]
        self.assertEqual("Amount: 360 USD",amount)
        self.assertEqual(f"Card Number: {test_data['card']}",card_number)
        self.assertEqual(f"Name: {test_data['name']}",name)
        time.sleep(1.5)
        # self.assertEqual(f"Date: {date_today}",current_date) # BUG - wrong month.
        h.click_element(checkout_page.CHECKOUT_OK_BUTTON)

if __name__ == "__main__":
    unittest.main()