from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.login.login_page import LoginPage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
from sfcc.pages.customize_page import CustomizePage
import unittest


class MixOrderTests(unittest.TestCase):

    def tests_addtocart(self):
        """Test Scenario:
        1. Login
        2. Add 2 Custom Text Glasseware products to Cart
        3. Add Stock product to Cart
        4. Navigate on Checkout button
        5. Place order to complete
        6. Repeats Steps 2-6
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
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

        lp = LoginPage(driver)
        pdp = ProductPage(driver)
        checkout = CheckoutPage(driver)
        custom = CustomizePage(driver)

        lp.login('qa2005121119@yeti.com', 'T3ster#!')

        custom_product_urls = [
            '/drinkware/rambler-12-oz-bottle/YRAM12.html',
            '/drinkware/rambler-14-oz-mug/YRAM24.html']

        for product_url in custom_product_urls:
            driver.get('https://staging-na-yeti.demandware.net/s/Yeti_US/en_US' + product_url)
            custom.pdpClickCustomButton()
            custom.customModal()
            custom.selectCustomMono()
            custom.clickApproval()
            custom.clickAddToCart()

        stock_product_urls = [
            '/drinkware/rambler-12-oz-bottle/YRAM12.html',
            '/drinkware/rambler-14-oz-mug/YRAM24.html']

        for product_url in stock_product_urls:
            driver.get('https://staging-na-yeti.demandware.net/s/Yeti_US/en_US' + product_url)
            pdp.addToCart()

        # driver.get('https://staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html')
        # pdp.pdpSwatches()
        # time.sleep(5)
        # pdp.addToCart()

        cart_url = 'https://staging-na-yeti.demandware.net/s/Yeti_US/en_US/cart'
        driver.get(cart_url)
        checkout.checkoutBtn()
        checkout.shippingBtn()
        checkout.clickVerifyAddress()
        checkout.accountPayment('111')
        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
