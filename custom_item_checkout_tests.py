# TODO: Add a Timestamp to the custom text
# TODO: Wait for element to clickable
# TODO: Unable to select the 'customize' button unless scroll into view.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest

class CustomItemCheckoutTest(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(base_url)
    
    def tests_custom_check_out(self):
        try:
            splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass
        
        self.driver.find_element_by_id("add-customization").click()

        try:
            self.driver.switch_to.frame(self.driver.find_element_by_css_selector('iframe[data-ycs="customizer"]'))
        except NoSuchElementException:
            return False
        
        self.driver.find_element_by_css_selector('[data-yti="add-text"]').click()
        self.driver.find_element_by_id('design-text').send_keys('AUTOMATION TEST')
        self.driver.find_element_by_css_selector('[data-yti="preview-approve"]').click()
        add_to_cart_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-yti="add-to-cart"]')))
        add_to_cart_btn.click()

    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
    unittest.main()