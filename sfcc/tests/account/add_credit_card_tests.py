from selenium import webdriver
from sfcc.pages.account.saved_credit_card_page import SavedCreditCardPage
from sfcc.pages.account.account_page import AccountPage
from sfcc.pages.login.login_page import LoginPage
import unittest


class AddCreditCardTests(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(base_url)

        cookie = {
            'domain': 'staging-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.ap = AccountPage(self.driver)
        self.sccp = SavedCreditCardPage(self.driver)

        self.lp.login('yabba_dabba@yeti.com', 'Tester123')

    # TODO: Need to add more tests for adding multiple cc to a single account
    def tests_add_credit_card(self):
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

    def tearDown(self):
        self.sccp.clickRemoveLink()
        self.sccp.clickDeleteModal()
        self.driver.quit()