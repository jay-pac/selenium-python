# TODO: Add a Timestamp to the custom text
# TODO: Wait for element to clickable
# TODO: Unable to select the 'customize' button unless scroll into view.
# TODO: Add Assertions to test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
import unittest
import time


class CustomItemCheckoutTest(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(base_url)
        self.driver.maximize_window()
        
        try:
            splash = self.driver.find_element(By.XPATH, '//*[@id="bx-element-1025412-TYHGubV"]/button')
            splash.click()
        except:
            pass
    
    def tests_custom_check_out(self):
        add_custom_btn = self.driver.find_element(By.ID, "add-customization")
        action = ActionChains(self.driver)
        action.move_to_element(add_custom_btn)
        action.click(add_custom_btn).perform()

        try:
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'iframe[data-ycs="customizer"]'))
        except NoSuchElementException:
            return False
        
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="add-text"]').click()
        self.driver.find_element(By.ID, 'design-text').send_keys('AUTOMATION TEST')
        self.driver.find_element(By.CSS_SELECTOR, '[data-yti="preview-approve"]').click()
        add_to_cart_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-yti="add-to-cart"]')))
        add_to_cart_btn.click()
        
        self.driver.switch_to.default_content()
        cart_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        cart_link.click()

        checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()
        
        email = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login"]//*[@type="email"]')
        email.send_keys("generalOne@user.com")

        pwd = self.driver.find_element(By.XPATH, '//*[@id="dwfrm_login"]//*[@type="password"]')
        pwd.send_keys("Generalone19!")

        login_btn = self.driver.find_element(By.NAME, 'dwfrm_login_login')
        login_btn.click()

        checkout_continue_btn = self.driver.find_element(By.NAME, 'dwfrm_singleshipping_save')
        checkout_continue_btn.click()
        
        cvv_num = self.driver.find_element(By.CSS_SELECTOR, 'input[class="input-text   required"]')
        cvv_num.send_keys('111')

        place_order_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[name="dwfrm_billing_save"]')
        place_order_btn.click()

        order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
        print(order_number)

    def tearDown(self):
        self.driver.quit()
    
        
if __name__ == '__main__':
    unittest.main()