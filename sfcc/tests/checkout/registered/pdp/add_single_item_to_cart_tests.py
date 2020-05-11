from selenium.webdriver.common.by import By
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import pytest

@pytest.mark.usefixtures("setup")
class TestAddSingleItemToCart():

    def tests_addtocart(self):
        """Test Scenario: 
        1. Add single Stock glassware from PDP
        2. Click on Add To Cart button
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        5. Sign in as test user
        6. Place order to complete 
        """
        pdp = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)
        # Quantity field action is not working
        # pdp.pdpQuantityField()
        pdp.addToCart()
        pdp.clickMiniCart()

        checkout.shippingBtn()
        checkout.clickVerifyAddress()
        checkout.accountPayment('111')

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)



