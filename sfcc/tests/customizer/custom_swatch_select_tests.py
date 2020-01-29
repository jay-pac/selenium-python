from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.login.login_page import LoginPage
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest


class CustomSwatchSelectTests(unittest.TestCase):

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

        self.lp.login('jason.pacitti@yeti.com', 'tester123')