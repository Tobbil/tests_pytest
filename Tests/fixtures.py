import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pytest

class WebDriverSetup:

    driver_service = Service(os.path.join(os.getcwd(), "chromedriver"))
    
    @pytest.fixture
    def test_setup(self):

        driver = webdriver.Chrome(service=self.driver_service)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.close()
        driver.quit()

        