from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.login.login_page import LoginPage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.category_page import CategoryPage
import unittest


class MasterOrderTests(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)

        cookie = {
            'domain': 'staging-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}

        self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.pdp = ProductPage(self.driver)
        self.checkout = CheckoutPage(self.driver)
        self.custom = CustomizePage(self.driver)
        self.clp = CategoryPage(self.driver)

        self.lp.login('jason.pacitti@yeti.com', 'tester123')

    def tests_createMixedOrder(self):
        product_urls = [
            '/drinkware/rambler-12-oz-bottle/YRAM12.html',
            '/drinkware/rambler-36-oz-bottle/YRAM36.html',
            '/drinkware/rambler-24-oz-mug/YRAM24.html']
        for product_url in product_urls:
            self.driver.get('https://staging-na-yeti.demandware.net/s/Yeti_US/en_US' + product_url)
            self.custom.pdpClickCustomButton()
            self.custom.customModal()

        cart_url = 'https://staging-na-yeti.demandware.net/s/Yeti_US/en_US/cart'
        self.driver.get(cart_url)
        self.checkout.checkoutBtn()
        self.checkout.shippingBtn()
        self.checkout.accountPayment('111')
        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)

    def tests_clp_custom_checkout(self):
        clp_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware'
        self.driver.get(clp_url)
        self.clp.clpSwatches()
        self.clp.clickCustomizeBtn()
        self.custom.customModal()
        self.pdp.clickMiniCart()

        # self.checkout.checkoutBtn()
        self.checkout.shippingBtn()
        self.checkout.accountPayment('111')
        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)

    def tearDown(self):
        self.driver.quit()