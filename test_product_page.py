import pytest
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from selenium import webdriver
import time

"""
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
"""

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'])
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()

def test_guest_cant_see_success_message_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_cart_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_dissapeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_cart_button()
    page.should_be_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_empty_cart_message()

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

@pytest.mark.login
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.link = self.product_page.url
        self.product_page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.register_new_user(str(time.time()) + '@fakemail.org', 'fake_user')
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_cart()