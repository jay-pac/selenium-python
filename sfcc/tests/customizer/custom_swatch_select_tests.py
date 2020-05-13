from selenium.webdriver.common.by import By
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import pytest


@pytest.mark.usefixtures("setup")
class TestCustomSwatchSelect():

    def tests_select_swatch(self):
        pdp = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)
        custom = CustomizePage(self.driver)

        pdp.pdpSwatches('Black')

        custom.pdpClickCustomButton()
        custom.customModal()
        custom.addCustomSwatches('color-seafoam')
        custom.selectCustomMono()
        custom.clickApproval()
        custom.clickAddToCart()

        pdp.clickMiniCart()
        checkout.shippingBtn()
        checkout.clickVerifyAddress()
        checkout.accountPayment('111')

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
