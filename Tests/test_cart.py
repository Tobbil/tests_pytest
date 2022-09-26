import time
import pytest
from datetime import date
from PageObject import MainPage, CartPage, LogInPage, SignUpPage, ContactPage, CheckoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver.chrome.service import Service
from PageObject.helpers import Helpers
from Tests.fixtures import WebDriverSetup

class TestCart(WebDriverSetup):

    test_data = {"name":"Mr Test","country":"Norway","city":"Tromsø",
                "card":"4376232127005830","month":"May","year":"2022"}
    
    @pytest.mark.xfail(condition=True, reason="Expected fail - KNOWN BUG: Wrong month.")
    def test_add_to_cart_and_checkout(self, test_setup):
        
        # SETUP #

        driver = test_setup
        test_data = self.test_data
        h = Helpers(driver)
        driver.get("https://www.demoblaze.com/")
        main_page = MainPage.MainPage(driver)
        cart_page = CartPage.CartPage(driver)
        checkout_page = CheckoutPage.CheckoutPage(driver)

        # TEST #

        ## ADD PRODUCT ##

        h.click_element(main_page.MENU_PHONES)
        element = h.get_element(main_page.PRICE_IN_LIST)
        assert "$360" == element.text
        element = h.get_element(main_page.PHONE_NAME_IN_LIST)
        assert "Samsung galaxy s6" == element.text
        h.click_element(main_page.PHONE_NAME_IN_LIST)
        element = h.get_element(main_page.PRICE_IN_ITEM_PAGE)
        price_add_to_cart_trimmed = element.text.replace(" *includes tax","")
        assert "$360" == price_add_to_cart_trimmed
        element = h.get_element(main_page.PHONE_NAME_IN_ITEM_PAGE)
        assert "Samsung galaxy s6" == element.text
        element = h.get_element(main_page.DESCRIPTION_IN_ITEM_PAGE)
        assert "" != element.text
        assert " " != element.text
        element = h.get_element(main_page.ADD_TO_CART_BUTTON)
        assert "Add to cart" == element.text
        element.click()
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        message = alert.text
        assert "Product added" == message
        alert.accept()

        ## VERIFY CART ##

        h.click_element(main_page.GO_TO_CART)
        assert cart_page.test_cart_content() == True
        element = h.get_element(cart_page.CART_TOTAL)
        assert element.text in "$360"
        element = cart_page.get_price_in_table()
        assert element.text in "$360"
        element = cart_page.get_phone_name_in_table()
        assert "Samsung galaxy s6" == element.text
        element = h.get_element(cart_page.PLACE_ORDER_BUTTON)
        assert "Place Order" == element.text
        element.click()

        ## TEST CHECKOUT ##

        element = checkout_page.get_total_in_checkout()
        assert element == "360"
        checkout_page.fill_checkout_form(test_data)
        time.sleep(1)
        h.click_element(checkout_page.CHECKOUT_SUBMIT_BUTTON)
        element = h.get_element(checkout_page.CHECKOUT_CONFIRMATION).text.split("\n")
        print(element)
        id_num, amount, card_number, name, date_checkout = element
        date_today = date.today().strftime('%d/%m/%Y')

        # ADJUST DATE FORMAT
        if date_today[3] == "0":
            date_today = date_today[:3] + date_today[4:]

        assert "Amount: 360 USD" == amount
        assert f"Card Number: {test_data['card']}" == card_number
        assert f"Name: {test_data['name']}" == name

        time.sleep(1.5)
        assert f"Date: {date_today}" == date_checkout # BUG - wrong month.
        h.click_element(checkout_page.CHECKOUT_OK_BUTTON)
