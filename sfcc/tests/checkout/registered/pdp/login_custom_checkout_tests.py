# TODO: Add a Timestamp to the custom text
# TODO: Wait for element to clickable
# TODO: Unable to select the 'customize' button unless scroll into view.
# TODO: Add Assertions to test
from selenium.webdriver.common.by import By
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import pytest


@pytest.mark.usefixtures("setup")
class TestCustomItemCheckout():

    def tests_custom_check_out(self):
        """Test Scenario: 
        1. Add single Custom Text glassware from PDP
        2. Click on Add To Cart button
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        5. Sign in as test user
        6. Place order to complete 
        """

        custom = CustomizePage(self.driver)
        pdp = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)

        pdp.pdpSwatches('Black')

        custom.pdpClickCustomButton()
        custom.customModal()
        custom.addCustomSwatches('color-seafoam')
        custom.selectCustomText()
        custom.selectCustomMono()
        custom.selectCustomDesign()
        custom.clickApproval()
        custom.addNumQtyField()
        custom.clickIncrementButton()
        custom.clickAddToCart()

        pdp.clickMiniCart()

        checkout.signIn('jason.pacitti@yeti.com', 'tester123')
        checkout.shippingBtn()
        checkout.accountPayment('111')

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
