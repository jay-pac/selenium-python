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
        add_to_cart_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-yti="add-to-cart"]')))
        add_to_cart_btn.click()
        time.sleep(10)
        
        self.driver.switch_to.default_content()
        cart_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        cart_link.click()

        checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()

        # Guest Checkout section -- This will be a class method for this test
        checkout_guest_btn = self.driver.find_element(By.XPATH, '//div[@class="desktop-guest-checkout"]//a[@name="dwfrm_login_unregistered"]')
        # checkout_guest_btn = self.driver.find_element_by_name('dwfrm_login_unregistered')
        checkout_guest_btn.click()

        # Checkout: Shipping Address form
        fn = self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_firstName')
        fn.send_keys('John')

        ln = self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_lastName')
        ln.send_keys('Smith')

        address_1 = self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_address1')
        address_1.send_keys('3100 Neal Street')

        city = self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_city')
        city.send_keys('Austin')

        select_state = Select(self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_states_state'))
        select_state.select_by_value('TX')

        zip_code = self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_postal')
        zip_code.send_keys('78702')

        phone = self.driver.find_element_by_id('dwfrm_singleshipping_shippingAddress_addressFields_phone')
        phone.send_keys('512-555-5555')

        email = self.driver.find_element_by_id('dwfrm_singleshipping_profile_email')
        email.send_keys('jason.pacitti@yeti.com')

        shipping_continue_btn = self.driver.find_element_by_name('dwfrm_singleshipping_save')
        shipping_continue_btn.click()
        # Checkout: Payment form
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_css_selector('iframe[id="paymetric-credit-card"]'))
        except NoSuchElementException:
            return False

        cc_num = self.driver.find_element(By.ID, 'c-cardnumber')
        cc_num.send_keys('4847189499632248')

        name_on_card = self.driver.find_element(By.ID, 'c-cardname')
        name_on_card.send_keys('John Smith')

        select_exp_month = Select(self.driver.find_element_by_id('c-exmth'))
        select_exp_month.select_by_value('1')

        select_exp_year = Select(self.driver.find_element_by_id('c-exyr'))
        select_exp_year.select_by_value('2028')

        cvv_num = self.driver.find_element_by_id('c-cvv')
        cvv_num.send_keys('111')

        self.driver.switch_to.default_content()

        place_order_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'button[name="dwfrm_billing_save"]')))
        place_order_btn.click()

        try:
            order_number = self.driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
            print(order_number)
        except NoSuchElementException:
            return False

    def tearDown(self):
        self.driver.quit()
    
        
if __name__ == '__main__':
    unittest.main()