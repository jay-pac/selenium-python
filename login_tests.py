# TODO:  Need to find unqiue locator for Homepage Splash page / Modal popup
# TODO: Add Assertions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest
import time


class LoginTests(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        self.driver.maximize_window()
        
        try:
            splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass

    def tests_login(self):
        email = self.driver.find_element_by_xpath('//*[@id="dwfrm_login"]//*[@type="email"]')
        email.send_keys("generalOne@user.com")

        pwd = self.driver.find_element_by_xpath('//*[@id="dwfrm_login"]//*[@type="password"]')
        pwd.send_keys("Generalone19!")
        login_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'dwfrm_login_login')))
        login_btn.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
