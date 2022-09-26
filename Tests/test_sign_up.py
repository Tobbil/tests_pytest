from PageObject import MainPage, CartPage, LogInPage, SignUpPage, ContactPage, CheckoutPage
from Tests.fixtures import WebDriverSetup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from PageObject.helpers import Helpers

class TestSignUp(WebDriverSetup):

    test_data = {"username":"MrTester","password":"test0TEST."}

    def test_sign_up_user_exists(self, test_setup):
        
        # SETUP #

        driver = test_setup
        h = Helpers(driver)
        test_data = self.test_data
        main_page = MainPage.MainPage(driver)
        signup_page = SignUpPage.SignUpPage(driver)

        # TEST #

        driver.get("https://www.demoblaze.com/")
        h.click_element(main_page.SIGN_UP)
        signup_page.fill_username_and_password(test_data)
        h.click_element(signup_page.SIGN_UP_BUTTON)
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "This user already exist."
        alert.accept()