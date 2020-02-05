from selenium import webdriver
from sfcc.pages.login.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
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

        self.lp = LoginPage(self.driver)

    def tests_login(self):
        self.lp.login('generalOne@user.com', 'Generalone19!')

        assert 'My Account Home' in self.driver.title

    def tearDown(self):
        self.driver.quit()