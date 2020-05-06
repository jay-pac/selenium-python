from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest


class GuestStockCheckoutTest(unittest.TestCase):

    def tests_guest_stock_checkout(self):
        """Use for Volume Testing"""
        x = 1
        while x <= 10:
            base_url = 'https://Storefront:Yeti2017@development-na-yeti.demandware.net/s/Yeti_US/en_US'
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get(base_url)

            cookie = {
                'domain': 'development-na-yeti.demandware.net',
                'httpOnly': False,
                'name': 'consent-accepted',
                'path': '/',
                'secure': False,
                'value': 'true'}
            self.driver.add_cookie(cookie)
            self.driver.refresh()

            self.driver.maximize_window()

            self.pdp = ProductPage(self.driver)
            self.checkout = CheckoutPage(self.driver)

            self.driver.get(f'{base_url}/drinkware/rambler-20-oz-tumbler/YRAM20.html')
            self.pdp.addToCart()
            self.pdp.clickMiniCart()
            self.checkout.checkoutAsGuest()

            self.checkout.shippingAddress(
                'John', 'Smith', '617 W 6th St', 'Austin', 'TX', '78701', '512-555-5555')

            self.checkout.enterEmail()

            self.checkout.shippingBtn()
            self.checkout.clickVerifyAddress()

            self.checkout.guestPayment('4847189499632248', 'John Smith', '111')

            order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
            print(order_number)

            self.driver.quit()

            x += 1

