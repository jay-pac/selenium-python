from selenium import webdriver
from sfcc.pages.account.address_book_page import AddressBookPage
from sfcc.pages.login.login_page import LoginPage
import unittest


class AddAddressTests(unittest.TestCase):

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
        self.adp = AddressBookPage(self.driver)

        self.lp.login('yabba_dabba@yeti.com', 'Tester123')

    def tests_add_address(self):
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
        self.adp.verifyAddressCreate()
        # assert self.adp.verifyAddressCreate() == 'QA AUTOMATION'

    def tearDown(self):
        self.adp.clickRemoveLink()
        self.adp.clickDeleteModal()
        self.driver.quit()