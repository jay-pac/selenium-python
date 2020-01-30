from selenium import webdriver
from sfcc.pages.account_page import AccountPage
import unittest


class AccountCreationTests(unittest.TestCase):

    def tests_create_account(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(base_url)

        cookie = {
            'domain': 'staging-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        driver.add_cookie(cookie)
        driver.refresh()

        driver.maximize_window()

        account = AccountPage(driver)

        account.enterFirstName()
        account.enterLastName()
        account.enterEmail()
        account.confirmEmail()
        account.enterPassword()
        account.confirmPassword()
        account.clickSignUpBtn()

