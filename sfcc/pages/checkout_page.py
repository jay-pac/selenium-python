from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

    def signIn(self, username, password):
        pass

    def checkoutAsGuest(self):
        checkout_guest_btn = self.driver.find_element(By.XPATH,
                                                 '//div[@class="desktop-guest-checkout"]//a[@name="dwfrm_login_unregistered"]')
        checkout_guest_btn.click()

    def shippingAddress(self, firstname, lastname, add1, city, state, zip, phone, email):
        fn = self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_firstName')
        fn.send_keys(firstname)

        ln = self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_lastName')
        ln.send_keys(lastname)

        address_1 = self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_address1')
        address_1.send_keys(add1)

        city_field = self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_city')
        city_field.send_keys(city)

        select_state = Select(
            self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_states_state'))
        select_state.select_by_value(state)

        zip_code = self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_postal')
        zip_code.send_keys(zip)

        phone_field = self.driver.find_element(By.ID, 'dwfrm_singleshipping_shippingAddress_addressFields_phone')
        phone_field.send_keys(phone)

        email_field = self.driver.find_element(By.ID, 'dwfrm_singleshipping_profile_email')
        email_field.send_keys(email)

        shipping_continue_btn = self.driver.find_element(By.NAME, 'dwfrm_singleshipping_save')
        shipping_continue_btn.click()

    def billing(self):
        pass

    def payment(self, cc_num, name, cvv):
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'iframe[id="paymetric-credit-card"]'))
        except NoSuchElementException:
            return False

        cc_num_field = self.driver.find_element(By.ID, 'c-cardnumber')
        cc_num_field.send_keys(cc_num)

        name_on_card = self.driver.find_element(By.ID, 'c-cardname')
        name_on_card.send_keys(name)

        select_exp_month = Select(self.driver.find_element(By.ID, 'c-exmth'))
        select_exp_month.select_by_value('1')

        select_exp_year = Select(self.driver.find_element(By.ID, 'c-exyr'))
        select_exp_year.select_by_value('2028')

        cvv_num = self.driver.find_element(By.ID, 'c-cvv')
        cvv_num.send_keys(cvv)

        self.driver.switch_to.default_content()

        place_order_btn = WebDriverWait(self.driver, 20, poll_frequency=1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="dwfrm_billing_save"]')))
        place_order_btn.click()
