# TODO: Add a Timestamp to the custom text
# TODO: Wait for element to clickable
# TODO: Unable to select the 'customize' button unless scroll into view.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import unittest
import time

class CustomItemCheckoutTest(unittest.TestCase):

    def setUp(self):
        # base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        base_url = 'https://www.yeti.com/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(base_url)
        self.driver.maximize_window()
        
        try:
            splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass
    
    def tests_custom_check_out(self):
        add_custom_btn = self.driver.find_element_by_id("add-customization")
        action = ActionChains(self.driver)
        action.move_to_element(add_custom_btn)
        action.click(add_custom_btn).perform()

        try:
            self.driver.switch_to.frame(self.driver.find_element_by_css_selector('iframe[data-ycs="customizer"]'))
        except NoSuchElementException:
            return False
        
        self.driver.find_element_by_css_selector('[data-yti="add-text"]').click()
        self.driver.find_element_by_id('design-text').send_keys('AUTOMATION TEST')
        self.driver.find_element_by_css_selector('[data-yti="preview-approve"]').click()
        add_to_cart_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-yti="add-to-cart"]')))
        add_to_cart_btn.click()
        time.sleep(10)
        self.driver.switch_to.default_content()
        ## Nothing wrong with the locator.  Need to switch back focus to main window from iframe.  Which isn't working @ the moment. Shit.
        # cart_link = self.driver.find_element_by_xpath('/div[@class="mini-cart"]//a[@class="mini-cart-link"]')
        cart_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        cart_link.click()

    def tearDown(self):
        self.driver.quit()
    
        
if __name__ == '__main__':
    unittest.main()