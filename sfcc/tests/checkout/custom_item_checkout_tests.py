from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest


class CustomItemCheckoutTest(unittest.TestCase):

    def tests_custom_check_out(self):
        """Test Scenario: 
        1. Add single Custom Text glassware from PDP
        2. Click on Add To Cart button
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        5. Checkout as Guest
        6. Place order to complete 
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)

        cookie = {
            'domain': 'staging-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        driver.add_cookie(cookie)
        driver.refresh()

        driver.maximize_window()

        custom = CustomizePage(driver)
        pdp = ProductPage(driver)
        checkout = CheckoutPage(driver)

        custom.pdpClickCustomButton()
        custom.customModal()
        custom.selectCustomMono()
        custom.clickApproval()
        custom.clickAddToCart()

        pdp.clickMiniCart()
        checkout.checkoutAsGuest()

        checkout.shippingAddress(
            'John', 'Smith', '3100 Neal Street', 'Austin', 'TX', '78702', '512-555-5555', 'jason.pacitti@yeti.com')

        checkout.shippingBtn()

        checkout.guestPayment('4847189499632248', 'John Smith', '111')

        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)