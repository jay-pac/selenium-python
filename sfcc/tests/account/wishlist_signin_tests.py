from sfcc.pages.wishlist_page import WishListPage
import pytest


@pytest.mark.usefixtures("setup")
class TestWishlistSignin():

    def tests_wishlist_signin(self):
        wlp = WishListPage(self.driver)

        drinkware_clp = 'https://development-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware'
        self.driver.get(drinkware_clp)
        # TODO: Add wishlist button to Category_page
        wlp.clickWishListBtn()
        wlp.enterEmailAddress('jason.pacitti@yeti.com')
        wlp.enterPassword('T3ster#!')
        wlp.clickContinueButton()

        assert wlp.verifyAccountWishlist() == 'MY WISHLIST'
