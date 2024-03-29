from selenium.webdriver.common.by import By
from sfcc.pages.category_page import CategoryPage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import pytest


@pytest.mark.usefixtures("setup")
class TestClpAddStockCheckout():

    def tests_add_to_cart(self):
        """Test Scenario:
        1. Navigate to Category Landing Page
        2. Add Stock Glassware to cart
        3. Click on add to cart button
        4. Click on Checkout button
        6. Place order to complete
        """
        
        pdp = ProductPage(self.driver)
        clp = CategoryPage(self.driver)
        checkout = CheckoutPage(self.driver)
        
        clp.clpSwatches()
        clp.clickAddToCartBtn()
        pdp.clickMiniCart() # Need to remove mini cart actions from Product page class.  Need to create a new page class for it

        checkout.shippingBtn()
        checkout.clickVerifyAddress()
        checkout.accountPayment('111')
        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)


