from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from sfcc.pages.product_page import ProductPage
import time
import unittest


class GuestCheckoutTest(unittest.TestCase):

    def tests_guest_checkout(self):
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)
        driver.maximize_window()


        try:
            splash = driver.find_element(By.CSS_SELECTOR, '#bx-element-1063655-tmuokvD > button')
            splash.click()
        except:
            pass

        pdp = ProductPage(driver)
        pdp.addToCart()
        pdp.clickMiniCart()

        checkout_btn = driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
        checkout_btn.click()

        # Guest Checkout section -- This will be a class method for this test
        checkout_guest_btn = driver.find_element(By.XPATH,
                                                      '//div[@class="desktop-guest-checkout"]//a[@name="dwfrm_login_unregistered"]')
        # checkout_guest_btn = driver.find_element_by_name('dwfrm_login_unregistered')
        checkout_guest_btn.click()

        # Checkout: Shipping Address form
        fn = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_firstName')
        fn.send_keys('John')

        ln = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_lastName')
        ln.send_keys('Smith')

        address_1 = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_address1')
        address_1.send_keys('3100 Neal Street')

        city = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_city')
        city.send_keys('Austin')

        select_state = Select(
            driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_states_state'))
        select_state.select_by_value('TX')

        zip_code = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_postal')
        zip_code.send_keys('78702')

        phone = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_phone')
        phone.send_keys('512-555-5555')

        email = driver.find_element(By.ID, 'dwfrm_singleshipping_profile_email')
        email.send_keys('jason.pacitti@yeti.com')

        shipping_continue_btn = driver.find_element(By.NAME, 'dwfrm_singleshipping_save')
        shipping_continue_btn.click()
        # Checkout: Payment form
        try:
            driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'iframe[id="paymetric-credit-card"]'))
        except NoSuchElementException:
            return False

        cc_num = driver.find_element(By.ID, 'c-cardnumber')
        cc_num.send_keys('4847189499632248')

        name_on_card = driver.find_element(By.ID, 'c-cardname')
        name_on_card.send_keys('John Smith')

        select_exp_month = Select(driver.find_element(By.ID, 'c-exmth'))
        select_exp_month.select_by_value('1')

        select_exp_year = Select(driver.find_element(By.ID, 'c-exyr'))
        select_exp_year.select_by_value('2028')

        cvv_num = driver.find_element(By.ID, 'c-cvv')
        cvv_num.send_keys('111')

        driver.switch_to.default_content()

        place_order_btn = WebDriverWait(driver, 20, poll_frequency=1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="dwfrm_billing_save"]')))
        place_order_btn.click()

        try:
            order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
            print(order_number)
        except NoSuchElementException:
            return False
    
    

#     def setUp(self):
#         base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html'
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(10)
#         driver.get(base_url)
#         driver.maximize_window()
# 
#         try:
#             splash = driver.find_element(By.CSS_SELECTOR, '#bx-element-1063655-tmuokvD > button')
#             splash.click()
#         except:
#             pass
# 
#     def tests_guest_checkout(self):
# 
#         add_cart_btn = driver.find_element(By.ID, 'add-to-cart')
#         action = ActionChains(driver)
# 
#         action.move_to_element(add_cart_btn)
#         action.click(add_cart_btn).perform()
# 
#         cart_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="mini-cart"]//a[@class="mini-cart-link"]')))
#         cart_link.click()
# 
#         checkout_btn = driver.find_element(By.NAME, 'dwfrm_cart_checkoutCart')
#         checkout_btn.click()
# 
#         # Guest Checkout section -- This will be a class method for this test
#         checkout_guest_btn = driver.find_element(By.XPATH, '//div[@class="desktop-guest-checkout"]//a[@name="dwfrm_login_unregistered"]')
#         # checkout_guest_btn = driver.find_element_by_name('dwfrm_login_unregistered')
#         checkout_guest_btn.click()
# 
#         # Checkout: Shipping Address form
#         fn = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_firstName')
#         fn.send_keys('John')
# 
#         ln = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_lastName')
#         ln.send_keys('Smith')
# 
#         address_1 = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_address1')
#         address_1.send_keys('3100 Neal Street')
# 
#         city = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_city')
#         city.send_keys('Austin')
# 
#         select_state = Select(driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_states_state'))
#         select_state.select_by_value('TX')
# 
#         zip_code = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_postal')
#         zip_code.send_keys('78702')
# 
#         phone = driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_phone')
#         phone.send_keys('512-555-5555')
# 
#         email = driver.find_element(By.ID, 'dwfrm_singleshipping_profile_email')
#         email.send_keys('jason.pacitti@yeti.com')
# 
#         shipping_continue_btn = driver.find_element(By.NAME, 'dwfrm_singleshipping_save')
#         shipping_continue_btn.click()
#         # Checkout: Payment form
#         try:
#             driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'iframe[id="paymetric-credit-card"]'))
#         except NoSuchElementException:
#             return False
# 
#         cc_num = driver.find_element(By.ID, 'c-cardnumber')
#         cc_num.send_keys('4847189499632248')
# 
#         name_on_card = driver.find_element(By.ID, 'c-cardname')
#         name_on_card.send_keys('John Smith')
# 
#         select_exp_month = Select(driver.find_element(By.ID, 'c-exmth'))
#         select_exp_month.select_by_value('1')
# 
#         select_exp_year = Select(driver.find_element(By.ID, 'c-exyr'))
#         select_exp_year.select_by_value('2028')
# 
#         cvv_num = driver.find_element(By.ID, 'c-cvv')
#         cvv_num.send_keys('111')
# 
#         driver.switch_to.default_content()
# 
#         place_order_btn = WebDriverWait(driver, 20, poll_frequency=1).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="dwfrm_billing_save"]')))
#         place_order_btn.click()
# 
#         try:
#             order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
#             print(order_number)
#         except NoSuchElementException:
#             return False
# 
#     def tearDown(self):
#         driver.quit()
# 
# 
# if __name__ == '__main__':
#     unittest.main()