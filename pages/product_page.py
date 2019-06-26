from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        self.click_to_add_to_cart_button()
        self.solve_quiz_and_get_code()
        self.alert_success_addition_present()
        self.equal_product_name_and_added_product(product_name)
        self.equal_total_cart_and_product_price(product_price)

    def click_to_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), 'product page no add to cart button presented'
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def alert_success_addition_present(self):
        success_addition_phrase_en_gb = 'has been added to your basket'
        assert 'en-gb' == self.browser.find_element(*ProductPageLocators.LANG_EN_GB).get_attribute('lang'), 'current page language is not "en-gb"'
        assert success_addition_phrase_en_gb in self.browser.find_elements(*ProductPageLocators.SUCCESS_ADDITION_ALERT)[0].text,\
            'success addition alert not contain phrase "{}"'.format(success_addition_phrase_en_gb)

    def equal_product_name_and_added_product(self, product_name):
        product_name_in_success_alert = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_ADDITION_ALERT)[0].text
        assert product_name == product_name_in_success_alert, 'choosen: "{}" not equal added: "{}"'.format(product_name, product_name_in_success_alert)

    def equal_total_cart_and_product_price(self, product_price):
        assert product_price == self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text, 'product price and price in alert message not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDITION_ALERT), 'Success message is presented, but should not be'

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDITION_ALERT), 'Success message is presented, but should not be'