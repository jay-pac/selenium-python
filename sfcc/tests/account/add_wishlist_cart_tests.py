from selenium.webdriver.common.by import By
from sfcc.pages.product_page import ProductPage
from sfcc.pages.login.login_page import LoginPage
from sfcc.pages.checkout_page import CheckoutPage
from sfcc.pages.account.my_wishlist_page import MyWishListPage
from sfcc.pages.account.account_page import AccountPage
import pytest


@pytest.mark.usefixtures("setup")
class TestAddWishListCart():

    def tests_add_wishlist_cart(self):
        lp = LoginPage(self.driver)
        pdp = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)
        mwlp = MyWishListPage(self.driver)
        ap = AccountPage(self.driver)

        lp.login('yabba_dabba@yeti.com', 'T3ster#!')
        ap.clickMyWishListLink()
        mwlp.clickAddToCart()

        pdp.clickMiniCart()

        checkout.shippingBtn()
        checkout.accountPayment('111')

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)
