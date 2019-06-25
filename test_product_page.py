from .pages.product_page import ProductPage
from selenium import webdriver

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 5)
    page.open()
    page.add_product_to_cart()