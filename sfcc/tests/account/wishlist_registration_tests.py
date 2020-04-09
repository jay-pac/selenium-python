from sfcc.pages.wishlist_page import WishListPage
import pytest
import time


@pytest.mark.usefixtures()
class TestWishListRegistration():

    def tests_wishlist_registration(self):
        wlp = WishListPage()
        wlp.clickWishListBtn()
        time.sleep(5)
