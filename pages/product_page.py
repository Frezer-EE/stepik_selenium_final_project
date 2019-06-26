from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time

class ProductPage(BasePage):

    def add_product_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        #time.sleep(2)
        self.click_to_add_to_cart_button()
        #time.sleep(1)
        self.solve_quiz_and_get_code()
        #time.sleep(2)
        self.alert_success_addition_present()
        #time.sleep(2)
        self.equal_product_name_and_added_product(product_name)
        #time.sleep(2)
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