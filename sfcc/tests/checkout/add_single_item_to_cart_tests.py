from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest


class AddSingleItemToCartTests(unittest.TestCase):

    def tests_addtocart(self):
        """Test Scenario: 
        1. Add single Stock glassware from PDP
        2. Click on Add To Cart button
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        5. Sign in as test user
        6. Place order to complete 
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.maximize_window()

        try:
            splash = driver.find_element(By.XPATH, '//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass

        pdp = ProductPage(driver)
        pdp.addToCart()
        pdp.clickMiniCart()

        checkout = CheckoutPage(driver)
        checkout.signIn('generalOne@user.com', 'Generalone19!')
        checkout.shippingBtn()
        checkout.accountPayment('111')

        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)



