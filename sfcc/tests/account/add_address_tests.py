from sfcc.pages.account.address_book_page import AddressBookPage
from sfcc.pages.login.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestAddAddress():

    def tests_add_address(self):
        self.lp = LoginPage(self.driver)
        self.adp = AddressBookPage(self.driver)

        self.lp.login('qa2004151252@yeti.com', 'T3ster#!@')

        self.adp.clickAddressLink()
        self.adp.clickAddressBtn()
        self.adp.enterAddressNickname()
        self.adp.enterFirstName()
        self.adp.enterLastName()
        self.adp.enterAddress()
        self.adp.enterCity()
        self.adp.selectState()
        self.adp.enterZip()
        self.adp.enterPhone()
        self.adp.clickSaveButton()
        assert self.adp.verifyAddressCreate() == 'QA AUTOMATION'

    # This is no longer needed.  I will need to add either another add it to existing conftest or create a new one
    # def tearDown(self):
    #     self.adp.clickRemoveLink()
    #     self.adp.clickDeleteModal()
    #     self.driver.quit()