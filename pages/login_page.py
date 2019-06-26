from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_substring = 'login'
        assert login_substring in self.url, 'login link not contains "{}" substring'.format(login_substring)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "login e-mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_ACCEPT_BUTTON), "login accept button is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOTTEN_PASS_LINK), "login link for forgotten password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "registration e-mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_REPEATED_PASSWORD), "registration repeated password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_ACCEPT_BUTTON), "registration accept button is not presented"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password1.send_keys(password)
        register_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_REPEATED_PASSWORD)
        register_password2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_ACCEPT_BUTTON).click()