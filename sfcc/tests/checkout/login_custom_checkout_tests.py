# TODO: Add a Timestamp to the custom text
# TODO: Wait for element to clickable
# TODO: Unable to select the 'customize' button unless scroll into view.
# TODO: Add Assertions to test
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        5. Sign in as test user
        6. Place order to complete 
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
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

        pdp.pdpSwatches('Black')
        custom.pdpClickCustomButton()
        custom.customModal()
        pdp.clickMiniCart()

        checkout.signIn('jason.pacitti@yeti.com', 'tester123')
        checkout.shippingBtn()
        checkout.accountPayment('111')

        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
