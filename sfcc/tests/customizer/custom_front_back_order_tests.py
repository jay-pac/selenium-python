from selenium.webdriver.common.by import By
from sfcc.pages.customize_page import CustomizePage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import pytest


@pytest.mark.usefixtures("setup")
class TestCustomOrderFrontBackOrder():

    def tests_custom_front_back(self):
        pdp = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)
        custom = CustomizePage(self.driver)

        pdp.pdpSwatches('Black')

        custom.pdpClickCustomButton()
        custom.customModal()
        # custom.selectCustomMono()
        custom.selectCustomText()
        # custom.selectCustomLogo()
        custom.clickBackDesign()
        custom.selectCustomMono()
        custom.clickApproval()
        custom.clickAddToCart()
        custom.clickConfirmButton()

        pdp.clickMiniCart()
        checkout.shippingBtn()
        checkout.clickVerifyAddress()
        checkout.accountPayment('111')

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)