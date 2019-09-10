from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class LoginTests(unittest.TestCase):

    def setUp(self):
        auth_url = "xxxxx"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(auth_url)
        try:
            # element is dynamic need to update locator
            splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass

    def tests_login(self):

        # sign_in_link = self.driver.find_element_by_xpath('//a[@class="header-utility-link header-banner-login"]')
        # sign_in_link.click()
        email = self.driver.find_element_by_xpath('//*[@id="dwfrm_login"]//*[@type="email"]')
        email.send_keys("xxxxx")

        pwd = self.driver.find_element_by_xpath('//*[@id="dwfrm_login"]//*[@type="password"]')
        pwd.send_keys("xxxxx")
        time.sleep(10)
        login_btn = self.driver.find_element_by_name('dwfrm_login_login')
        login_btn.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
