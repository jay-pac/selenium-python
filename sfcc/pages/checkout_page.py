from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from datetime import datetime
import time


class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _checkout = 'dwfrm_cart_checkoutCart'
    _mini_checkout = '//div[@class="mini-cart-opened"]//a[@class="button-primary full-width mini-cart-link-checkout"][contains(text(),"Check out")]'
    _email_field = '//*[@id="dwfrm_login"]//*[@type="email"]'
    _pwd_field = '//*[@id="dwfrm_login"]//*[@type="password"]'
    _login = 'dwfrm_login_login'
    _guest_checkout = '//div[@class="desktop-guest-checkout"]//a[@name="dwfrm_login_unregistered"]'
    _first_name = 'dwfrm_singleshipping_shippingAddress_addressFields_firstName'
    _last_name = 'dwfrm_singleshipping_shippingAddress_addressFields_lastName'
    _address = 'dwfrm_singleshipping_shippingAddress_addressFields_address1'
    _city = 'dwfrm_singleshipping_shippingAddress_addressFields_city'
    _state = 'dwfrm_singleshipping_shippingAddress_addressFields_states_state'
    _zip_code = 'dwfrm_singleshipping_shippingAddress_addressFields_postal'
    _phone_num = 'dwfrm_singleshipping_shippingAddress_addressFields_phone'
    _email = 'dwfrm_singleshipping_profile_email'
    _continue = 'dwfrm_singleshipping_save'
    _cc_num = 'c-cardnumber'
    _cc_name = 'c-cardname'
    _cc_month = 'c-exmth'
    _cc_year = 'c-exyr'
    _cvv = 'c-cvv'
    _place_order = 'button[name="dwfrm_billing_save"]'
    _cvv_registered = 'input[class="input-text   required"]'
    _customer_pwd = '//input[contains(@id, "dwfrm_singleshipping_profile_password_")]'
    _invalid_pwd_message = '//div[contains(@class, "dwfrm_singleshipping_profile_password_")]//span[contains(@id, "dwfrm_singleshipping_profile_password_")]'

    def checkoutBtn(self):
        checkout_btn = self.driver.find_element(By.NAME, self._checkout)
        checkout_btn.click()

    def miniCartCheckoutBtn(self):
        checkout_btn = self.driver.find_element(By.XPATH, self._mini_checkout)
        checkout_btn.click()

    def signIn(self, username, password):
        email = self.driver.find_element(By.XPATH, self._email_field)
        email.send_keys(username)

        pwd = self.driver.find_element(By.XPATH, self._pwd_field)
        pwd.send_keys(password)

        login_btn = self.driver.find_element(By.NAME, self._login)
        login_btn.click()

    def checkoutAsGuest(self):
        checkout_guest_btn = self.driver.find_element(By.XPATH, self._guest_checkout)
        checkout_guest_btn.click()

    def shippingAddress(self, firstname, lastname, add1, city, state, zip, phone):
        fn = self.driver.find_element(By.ID, self._first_name)
        fn.send_keys(firstname)

        ln = self.driver.find_element(By.ID, self._last_name)
        ln.send_keys(lastname)

        address_1 = self.driver.find_element(By.ID, self._address)
        address_1.send_keys(add1)

        city_field = self.driver.find_element(By.ID, self._city)
        city_field.send_keys(city)

        select_state = Select(
            self.driver.find_element(By.ID, self._state))
        select_state.select_by_value(state)

        zip_code = self.driver.find_element(By.ID, self._zip_code)
        zip_code.send_keys(zip)

        phone_field = self.driver.find_element(By.ID, self._phone_num)
        phone_field.send_keys(phone)

    def enterEmail(self):
        timestamp = datetime.now().strftime('%y%m%d%H%M')
        self.email_address = f'qa{timestamp}@yeti.com'
        email_field = self.driver.find_element(By.ID, self._email)
        email_field.send_keys(self.email_address)

    def enterPassword(self):
        self.pwd = 'T3ster#!@'
        pwd_field = self.driver.find_element(By.XPATH, self._customer_pwd)
        pwd_field.send_keys(self.pwd)

    def enterInvalidPassword(self):
        self.invalid_pwd = 'Tester123'
        pwd_field = self.driver.find_element(By.XPATH, self._customer_pwd)
        pwd_field.send_keys(self.invalid_pwd)

    def verifyPwdError(self):
        error_message = self.driver.find_element(By.XPATH, self._invalid_pwd_message).text
        return error_message

    def shippingBtn(self):
        shipping_continue_btn = self.driver.find_element(By.NAME, self._continue)
        shipping_continue_btn.click()

    def billing(self):
        pass

    def guestPayment(self, cc_num, name, cvv):
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, 'iframe[id="paymetric-credit-card"]'))
        except NoSuchElementException:
            return False

        cc_num_field = self.driver.find_element(By.ID, self._cc_num)
        cc_num_field.send_keys(cc_num)

        name_on_card = self.driver.find_element(By.ID, self._cc_name)
        name_on_card.send_keys(name)

        select_exp_month = Select(self.driver.find_element(By.ID, self._cc_month))
        select_exp_month.select_by_value('1')

        select_exp_year = Select(self.driver.find_element(By.ID, self._cc_year))
        select_exp_year.select_by_value('2028')

        cvv_num = self.driver.find_element(By.ID, self._cvv)
        cvv_num.send_keys(cvv)

        self.driver.switch_to.default_content()

        time.sleep(5)
        place_order_btn = self.driver.find_element(By.CSS_SELECTOR, self._place_order)
        place_order_btn.click()

    def accountPayment(self, cvv):
        cvv_num = self.driver.find_element(By.CSS_SELECTOR, self._cvv_registered)
        cvv_num.send_keys(cvv)

        place_order_btn = self.driver.find_element(By.CSS_SELECTOR, self._place_order)
        place_order_btn.click()
