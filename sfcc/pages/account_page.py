from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time
from datetime import datetime


class AccountPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _customer_fn = 'dwfrm_profile_customer_firstname'
    _customer_ln = 'dwfrm_profile_customer_lastname'
    _customer_email = 'dwfrm_profile_customer_email'
    _confirm_email = 'dwfrm_profile_customer_emailconfirm'
    _customer_psw = '//form[contains(@id,"RegistrationForm")]//input[contains(@id,"profile_login_password_")]'
    _confirm_psw = '//form[contains(@id,"RegistrationForm")]//input[contains(@id,"profile_login_passwordconfirm_")]'
    _form_sign_in = 'dwfrm_profile_confirm'
    _manage_address = '//a[contains(text(),"manage addresses")]'
    _address_button = '//a[@class="button-primary section-header-note address-create"]'
    _address_nickname = 'dwfrm_profile_address_addressid'
    _address_fn = 'dwfrm_profile_address_firstname'
    _address_ln = 'dwfrm_profile_address_lastname'
    _address_1 = 'dwfrm_profile_address_address1'
    _address_city = 'dwfrm_profile_address_city'
    _address_state = 'dwfrm_profile_address_states_state_chosen'
    _address_zip = 'dwfrm_profile_address_postal'
    _address_phone = 'dwfrm_profile_address_phone'
    _save_address = 'dwfrm_profile_address_save'

    def enterFirstName(self):
        fn = self.driver.find_element(By.ID, self._customer_fn)
        fn.send_keys('Fred')

    def enterLastName(self):
        ln = self.driver.find_element(By.ID, self._customer_ln)
        ln.send_keys('Flintstone')

    def enterEmail(self):
        # running into error when attempting to store the email value in the confirm email method.
        timestamp = datetime.now().strftime('%y%m%d%H%M')
        email = self.driver.find_element(By.ID, self._customer_email)
        email.send_keys(f'qa{timestamp}@yeti.com')

    def confirmEmail(self):
        timestamp = datetime.now().strftime('%y%m%d%H%M')
        email = self.driver.find_element(By.ID, self._confirm_email)
        email.send_keys(f'qa{timestamp}@yeti.com')

    def enterPassword(self):
        psw = self.driver.find_element(By.XPATH, self._customer_psw)
        psw.send_keys('Tester123')

    def confirmPassword(self):
        psw = self.driver.find_element(By.XPATH, self._confirm_psw)
        psw.send_keys('Tester123')

    def clickSignUpBtn(self):
        signup_btn = self.driver.find_element(By.NAME, self._form_sign_in)
        signup_btn.click()

    # Add Address methods
    def clickManageAddress(self):
        pass

    def clickAddBtn(self):
        pass
    # Address Form
    def enterAddressNicname(self):
        pass

    def enterFirstName(self):
        pass

    def enterLastName(self):
        pass

    def enterAddress(self):
        pass

    def enterCity(self):
        pass

    def selectState(self):
        pass

    def enterZip(self):
        pass

    def enterPhone(self):
        pass

    def clickSaveButton(self):
        pass
