import pytest
from PageObject import MainPage, LogInPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Tests.fixtures import WebDriverSetup
from PageObject.helpers import Helpers

class TestLogIn(WebDriverSetup):

    test_data = {"correct_username":"MrTester","nonexistent_username":"nonexistentusername",
                "correct_password":"test0TEST.","incorrect_password":"wrongpassword"}

    # @pytest.mark.smoke
    def test_login_correct(self, test_setup):

        # SETUP #

        driver = test_setup
        h = Helpers(driver)
        test_data = self.test_data
        main_page = MainPage.MainPage(driver)
        login_page = LogInPage.LogInPage(driver)

        # TEST #

        driver.get("https://www.demoblaze.com")
        login_page.log_in(test_data['correct_username'], test_data['correct_password'])

        ## VERIFY USER LOGGED IN ##

        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(main_page.USERNAME_IN_MENU,"Welcome"))
        cookies = driver.get_cookies()
        assert cookies[0]['name'] == 'tokenp_'
        element = h.get_element(main_page.USERNAME_IN_MENU)
        assert element.text == f"Welcome {test_data['correct_username']}"
        h.click_element(main_page.LOG_OUT)
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(main_page.LOG_IN,"Log in"))
        element = h.get_element(main_page.LOG_IN)
        assert element.text == "Log in"
        cookies = driver.get_cookies()
        assert cookies[0]['name'] != 'tokenp_'

    @pytest.mark.smoke
    def test_login_incorrect_password(self, test_setup):
        
        # SETUP #

        driver = test_setup
        h = Helpers(driver)
        test_data = self.test_data
        main_page = MainPage.MainPage(driver)
        login_page = LogInPage.LogInPage(driver)

        # TEST #

        driver.get("https://www.demoblaze.com")
        login_page.log_in(test_data['correct_username'], test_data['incorrect_password'])
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "Wrong password."
        alert.accept()

        ## VERIFY USER ISN'T LOGGED IN ##

        element = h.get_element(main_page.LOG_IN)
        assert element.text == "Log in"
        h.click_element(login_page.CLOSE_BUTTON)
        cookies = driver.get_cookies()
        assert cookies[0]['name'] != 'tokenp_'
    
    def test_nonexistent_user(self, test_setup):

        # SETUP #

        driver = test_setup
        test_data = self.test_data
        login_page = LogInPage.LogInPage(driver)

        # TEST #

        driver.get("https://www.demoblaze.com")
        login_page.log_in(test_data['nonexistent_username'], test_data['incorrect_password'])
        WebDriverWait(driver,10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "User does not exist."
        alert.accept()
        cookies = driver.get_cookies()
        assert cookies[0]['name'] != 'tokenp_'
        