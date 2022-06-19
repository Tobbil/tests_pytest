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
    CONTACT = (By.LINK_TEXT, "Contact")
    SIGN_UP = (By.ID, "signin2")
    LOG_IN = (By.ID, "login2")
    LOG_OUT = (By.ID, "logout2")
    USERNAME_IN_MENU = (By.ID, "nameofuser")

class CartPageLocators(object):

    CART = (By.CLASS_NAME, "table-responsive")
    CART_CHILDREN = (By.ID, "tbodyid")
    CART_TOTAL = (By.XPATH, "//*[@id='totalp']")
    TABLE = (By.CLASS_NAME, "success") 
    PLACE_ORDER_BUTTON = (By.CLASS_NAME, "btn.btn-success")

class CheckoutPageLocators(object):

    CHECKOUT_TOTAL = (By.CSS_SELECTOR, "#orderModal #totalm")
    CHECKOUT_FORM_NAME = (By.CSS_SELECTOR, "#orderModal #name")
    CHECKOUT_FORM_COUNTRY = (By.CSS_SELECTOR, "#orderModal #country")
    CHECKOUT_FORM_CITY = (By.CSS_SELECTOR, "#orderModal #city")
    CHECKOUT_FORM_CARD = (By.CSS_SELECTOR, "#orderModal #card")
    CHECKOUT_FORM_MONTH = (By.CSS_SELECTOR, "#orderModal #month")
    CHECKOUT_FORM_YEAR = (By.CSS_SELECTOR, "#orderModal #year")
    CHECKOUT_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#orderModal button.btn.btn-primary")
    CHECKOUT_CONFIRMATION = (By.CSS_SELECTOR, "p.lead.text-muted")
    CHECKOUT_OK_BUTTON = (By.CSS_SELECTOR, "button.confirm.btn.btn-lg.btn-primary")

class ContactPageLocators(object):
    
    CONTACT_EMAIL = (By.ID, "recipient-email")
    CONTACT_NAME = (By.ID, "recipient-name")
    CONTACT_MESSAGE = (By.ID, "message-text")
    CONTACT_SEND_BUTTON = (By.CSS_SELECTOR, "#exampleModal button.btn.btn-primary")

class SignUpPageLocators(object):

    USERNAME = (By.ID, "sign-username")
    PASSWORD = (By.ID, "sign-password")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#signInModal button.btn.btn-primary")

class LogInPageLocators(object):

    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal button.btn.btn-primary")   