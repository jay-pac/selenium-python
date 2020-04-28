from selenium.webdriver.common.by import By
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import pytest

@pytest.mark.usefixtures("setup")
class TestGuestCheckout():

    def test_guest_checkout(self):
        """Test Scenario: 
        1. Add single Stock glassware from PDP
        2. Click on Add To Cart button
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        5. Checkout As Guest
        6. Place order to complete 
        """
        pdp = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)

        pdp.addToCart()
        pdp.clickMiniCart()

        checkout.checkoutAsGuest()

        checkout.shippingAddress(
            'John', 'Smith', '3100 Neal Street', 'Austin', 'TX', '78702', '512-555-5555')

        checkout.shippingBtn()

        checkout.guestPayment('4847189499632248', 'John Smith', '111')

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
