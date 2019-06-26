from selenium.webdriver.common.by import By


class MainPageLocators(object):

    pass

class LoginPageLocators(object):

    LOGIN_EMAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_ACCEPT_BUTTON = (By.NAME, 'login_submit')
    LOGIN_FORGOTTEN_PASS_LINK = (By.TAG_NAME, 'p')

    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_REPEATED_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTER_ACCEPT_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators(object):

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    LANG_EN_GB = (By.XPATH, '//html')
    SUCCESS_ADDITION_ALERT = (By.CSS_SELECTOR, '.alert-success')
    PRODUCT_NAME_ADDITION_ALERT = (By.CSS_SELECTOR, '.alert-success strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')

class BasePageLocators(object):

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//a[text()="View basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):

    CART_NOT_EMPTY = (By.CLASS_NAME, 'basket-title')
    CART_EMPTY_MESSAGE = (By.TAG_NAME, 'p')