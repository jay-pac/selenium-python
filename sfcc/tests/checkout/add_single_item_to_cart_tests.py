from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest
import time


class AddSingleItemToCartTests(unittest.TestCase):

    def tests_addtocart(self):
        """Test Scenario: 
        1. Add single item from PDP
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

        # add_cart_btn = self.driver.find_element(By.ID, 'add-to-cart')
        # action = ActionChains(self.driver)
        #
        # action.move_to_element(add_cart_btn)
        # action.click(add_cart_btn).perform()
        #
        # cart_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        # cart_link.click()
        #
        # checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        # checkout_btn.click()

        # email = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login"]//*[@type="email"]')
        # email.send_keys("generalOne@user.com")
        #
        # pwd = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login"]//*[@type="password"]')
        # pwd.send_keys("Generalone19!")
        #
        # login_btn = self.driver.find_element(By.NAME, 'dwfrm_login_login')
        # login_btn.click()

        # checkout_continue_btn = self.driver.find_element(By.NAME, 'dwfrm_singleshipping_save')
        # checkout_continue_btn.click()
        #
        # cvv_num = self.driver.find_element(By.CSS_SELECTOR, 'input[class="input-text   required"]')
        # cvv_num.send_keys('111')
        #
        # place_order_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[name="dwfrm_billing_save"]')
        # place_order_btn.click()

        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)



