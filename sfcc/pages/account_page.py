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


