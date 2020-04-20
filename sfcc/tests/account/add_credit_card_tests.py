from sfcc.pages.account.saved_credit_card_page import SavedCreditCardPage
from sfcc.pages.account.account_page import AccountPage
from sfcc.pages.login.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestAddCreditCard():

    # TODO: Need to add more tests for adding multiple cc to a single account
    def tests_add_credit_card(self):
        self.lp = LoginPage(self.driver)
        self.ap = AccountPage(self.driver)
        self.sccp = SavedCreditCardPage(self.driver)

        self.lp.login('qa2004151252@yeti.com', 'T3ster#!@')
        self.ap.clickSavedCCLink()
        self.sccp.clickAddCCBtn()
        self.sccp.enterCCNickName()
        self.sccp.enterCardNumber()
        self.sccp.enterName()
        self.sccp.selectMonth()
        self.sccp.selectYear()
        self.sccp.enterCCV()
        self.sccp.clickApplyBtn()
        assert self.sccp.verifySavedCC() == 'DEFAULT CARD - QA AUTOMATION'

    def tests_add_mc_cc(self):
        self.ap.clickSavedCCLink()
        self.sccp.clickAddCardLink()
        self.sccp.enterCCNickName('QA MasterCard')
        self.sccp.enterCardNumber('5424180279791773')
        self.sccp.enterName()
        self.sccp.selectMonth()
        self.sccp.selectYear()
        self.sccp.enterCCV()
        self.sccp.clickApplyBtn()
        assert self.sccp.verifySavedCC() == 'QA MASTERCARD'

    def tearDown(self):
        self.sccp.clickRemoveLink()
        self.sccp.clickDeleteModal()
        self.driver.quit()