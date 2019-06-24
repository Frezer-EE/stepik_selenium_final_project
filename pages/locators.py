from selenium.webdriver.common.by import By


class MainPageLocators(object):

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):

    LOGIN_EMAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_ACCEPT_BUTTON = (By.NAME, 'login_submit')
    LOGIN_FORGOTTEN_PASS_LINK = (By.TAG_NAME, 'p')

    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_REPEATED_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTER_ACCEPT_BUTTON = (By.NAME, 'registration_submit')