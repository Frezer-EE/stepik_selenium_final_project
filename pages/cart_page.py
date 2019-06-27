from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):


    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_NOT_EMPTY), 'cart is not empty'

    def should_be_empty_cart_message(self):
        assert 'Your basket is empty' == self.browser.find_element(*CartPageLocators.CART_EMPTY_MESSAGE).text.split('.')[0],\
            'cart empty message is not present'