from selenium import webdriver
from sfcc.pages.account.sign_up_page import SignUpPage
import unittest


class AccountCreationTests(unittest.TestCase):

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

        self.signup = SignUpPage(self.driver)

    def tests_create_account(self):
        self.signup.enterFirstName()
        self.signup.enterLastName()
        self.signup.enterEmail()
        self.signup.confirmEmail()
        self.signup.enterPassword()
        self.signup.confirmPassword()
        self.signup.clickSignUpBtn()

    def tearDown(self):
        self.driver.quit()


