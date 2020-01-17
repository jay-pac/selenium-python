# TODO:  Need to find unqiue locator for Homepage Splash page / Modal popup
# TODO: Add Assertions
from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.login.login_page import LoginPage

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest
import time


class LoginTests(unittest.TestCase):

    def tests_login(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
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

        lp = LoginPage(driver)
        lp.login('generalOne@user.com', 'Generalone19!')



