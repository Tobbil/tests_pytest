from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    MENU_PHONES = (By.LINK_TEXT, "Phones")
    PRICE_IN_LIST = (By.CSS_SELECTOR, "#tbodyid h5")
    PRICE_IN_ITEM_PAGE = (By.CSS_SELECTOR, "#tbodyid h3")
    PHONE_NAME_IN_LIST = (By.CSS_SELECTOR, "#tbodyid a.hrefch")
    PHONE_NAME_IN_ITEM_PAGE = (By.CSS_SELECTOR, "#tbodyid h2")
    DESCRIPTION_IN_ITEM_PAGE = (By.CSS_SELECTOR, "#more-information p")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#tbodyid a.btn.btn-success.btn-lg")
    GO_TO_CART = (By.CSS_SELECTOR, "#cartur")
    CART = (By.CLASS_NAME, "table-responsive")
    CART_CHILDREN = (By.ID, "tbodyid")
    CART_TOTAL = (By.XPATH, "//*[@id='totalp']")
    TABLE = (By.CLASS_NAME, "success") 
    PLACE_ORDER_BUTTON = (By.CLASS_NAME, "btn.btn-success")

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass