from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest


class CustomItemCheckoutTest(unittest.TestCase):

    def tests_custom_check_out(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.maximize_window()

        try:
            splash = driver.find_element(By.CSS_SELECTOR, '#bx-element-1063655-tmuokvD > button')
            splash.click()
        except:
            pass
        custom = CustomizePage(driver)
        custom.customModal()

        pdp = ProductPage(driver)
        pdp.addToCart()
        pdp.clickMiniCart()

        checkout = CheckoutPage(driver)
        checkout.checkoutAsGuest()

        checkout.shippingAddress(
            'John', 'Smith', '3100 Neal Street', 'Austin', 'TX', '78702', '512-555-5555', 'jason.pacitti@yeti.com')

        checkout.shippingBtn()

        checkout.guestPayment('4847189499632248', 'John Smith', '111')

        try:
            order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
            print(order_number)
        except NoSuchElementException:
            return False
