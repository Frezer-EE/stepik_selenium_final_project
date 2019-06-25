from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math

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
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDITION_ALERT), 'no success addition alert presented'

    def equal_product_name_and_added_product(self, product_name):
        assert product_name in self.browser.find_elements(*ProductPageLocators.SUCCESS_ADDITION_ALERT)[0].text, \
            'choosen product name: "{}" and name in added alert message not equal'.format(product_name)

    def equal_total_cart_and_product_price(self, product_price):
        assert product_price == self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text, 'product price and price in alert message not equal'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")