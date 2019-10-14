from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import unittest

class GuestCheckoutTest(unittest.TestCase):

    def setUp(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        # base_url = 'https://www.yeti.com/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        self.driver.maximize_window()

        try:
            # splash = self.driver.find_element_by_xpath('//*[@id="bx-element-1025412-TYHGubV"]/button')
            # splash.click()
            splash = self.driver.find_element(By.CSS_SELECTOR, '#bx-element-1063655-tmuokvD > button')
            splash.click()
        except:
            pass
        
    def tests_guest_checkout(self):

        add_cart_btn = self.driver.find_element(By.ID, 'add-to-cart')
        action = ActionChains(self.driver)
        
        action.move_to_element(add_cart_btn)
        action.click(add_cart_btn).perform()

        cart_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
        cart_link.click()

        checkout_btn = self.driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()

        # Guest Checkout section -- This will be a class method for this test
        checkout_guest_btn = self.driver.find_element_by_name('dwfrm_login_unregistered')
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
        place_order_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[name="dwfrm_billing_save"]')
        place_order_btn.click()
        time.sleep(10)

        el = self.driver.find_element(By.TAG_NAME, 'h1')
        assert el.text == "Thanks for your order"
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    