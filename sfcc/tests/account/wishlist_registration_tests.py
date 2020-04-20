from sfcc.pages.wishlist_page import WishListPage
import pytest


@pytest.mark.usefixtures("setup")
class TestWishListRegistration():

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.wlp = WishListPage(self.driver)
        self.drinkware_clp = 'https://development-na-yeti.demandware.net/s/Yeti_US/drinkware'
        self.driver.get(self.drinkware_clp)

    @pytest.mark.run(order=2)
    def tests_wishlist_registration(self):
        # TODO: Add wishlist button to Category_page
        self.wlp.clickWishListBtn()
        self.wlp.clickNoCheckbox()
        self.wlp.clickContinueButton()
        self.wlp.enterFirstName()
        self.wlp.enterLastName()

        self.wlp.enterRegisterEmail()
        self.wlp.enterRegisterPwd()
        self.wlp.clickRegisterContinue()

        assert self.wlp.verifyAccountWishlist() == 'MY WISHLIST'

    @pytest.mark.run(order=1)
    def tests_wishlist_invalid_pwd(self):
        self.wlp.clickWishListBtn()
        self.wlp.clickNoCheckbox()
        self.wlp.clickContinueButton()
        self.wlp.enterFirstName()
        self.wlp.enterLastName()
        self.wlp.enterRegisterEmail()
        self.wlp.enterInvalidPwd()
        self.wlp.clickRegisterContinue()

        assert self.wlp.verifyInvalidPwd() == 'OOPS! PLEASE ENTER A VALID NEW PASSWORD'



