from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    MENU_PHONES = (By.LINK_TEXT, "Phones")
    PRICE_IN_LIST = (By.CSS_SELECTOR, "#tbodyid h5")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass