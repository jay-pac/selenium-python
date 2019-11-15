from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.login.login_page import LoginPage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest
import time


class MixOrderTests(unittest.TestCase):

    def tests_addtocart(self):
        """Test Scenario: 
        1. Add single item from PDP
        2. Click on Add To Cart button
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        5. Sign in as test user
        6. Place order to complete 
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.maximize_window()
        lp = LoginPage(driver)
        pdp = ProductPage(driver)
        checkout = CheckoutPage(driver)
        lp.login('generalOne@user.com', 'Generalone19!')

        product_urls = [
            '/hard-coolers/roadie-20-cooler/YR20.html',
            '/drinkware/rambler-36-oz-bottle/YRAM36.html',
            '/drinkware/rambler-half-gallon-jug/YRAMHALFJUG.html']
        x = 1
        while x <= 5:
            for product_url in product_urls:
                driver.get('https://staging-na-yeti.demandware.net/s/Yeti_US/en_US' + product_url)
                pdp.addToCart()
            
            # pdp.clickMiniCart()
            # checkout.miniCartCheckoutBtn()
            cart_url = 'https://staging-na-yeti.demandware.net/s/Yeti_US/en_US/cart'
            driver.get(cart_url)
            checkout.shippingBtn()
            checkout.accountPayment('111')
            order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
            print(order_number)

            x += 1
    
