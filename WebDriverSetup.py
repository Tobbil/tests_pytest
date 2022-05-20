import unittest
import os
import sys
from selenium import webdriver

class WebDriverSetup(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver"))
        self.driver.implicitly_wait(10)

    def tearDown(self):

        self.driver.close()
        self.driver.quit()