from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, 'login url not contains "login" substring'

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