from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class SingleItemAddToCartTests(unittest.TestCase):

    def setUp(self):
        auth_url = 'xxxxx'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(auth_url)
        try:
            # element is dynamic need to update locator
            splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass

        try:
            cookie = self.driver.find_element_by_xpath('//button[@class="close-mat"]')
            cookie.click()
        except:
            pass

    def tests_add_to_cart(self):
        add_to_cart_btn = self.driver.find_element_by_id('add-to-cart')
        add_to_cart_btn.click()
        time.sleep(10)

        cart_icon = self.driver.find_element_by_xpath('//div[@class="mini-cart"]//div[@class="mini-cart-quantity"][contains(text(),"1")]')
        cart_icon.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()