from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.category_page import CategoryPage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
from sfcc.pages.customize_page import CustomizePage
import unittest


class ClpAddStockCheckout(unittest.TestCase):

    def tests_add_to_cart(self):
        """Test Scenario:
        1. Navigate to Category Landing Page
        2. Add Stock Glassware to cart
        3. Click on add to cart button
        4. Click on Checkout button
        6. Place order to complete
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware'
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

        pdp = ProductPage(driver)
        clp = CategoryPage(driver)
        checkout = CheckoutPage(driver)
        custom = CustomizePage(driver)

        clp.clpSwatches()
        clp.clickCustomizeBtn()
        custom.customModal()
        custom.selectCustomMono()
        custom.clickApproval()
        custom.clickAddToCart()
        pdp.clickMiniCart()  # Need to remove mini cart actions from Product page class.  Need to create a new page class for it

        checkout.signIn('jason.pacitti011420@yeti.com', 'Tester456!')
        checkout.shippingBtn()
        checkout.accountPayment('111')
        order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)