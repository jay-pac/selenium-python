from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime


class SignUpPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _customer_fn = 'dwfrm_profile_customer_firstname'
    _customer_ln = 'dwfrm_profile_customer_lastname'
    _customer_email = 'dwfrm_profile_customer_email'
    _confirm_email = 'dwfrm_profile_customer_emailconfirm'
    _customer_pwd = '//form[contains(@id,"RegistrationForm")]//input[contains(@id,"profile_login_password_")]'
    _confirm_pwd = '//form[contains(@id,"RegistrationForm")]//input[contains(@id,"profile_login_passwordconfirm_")]'
    _form_sign_in = 'dwfrm_profile_confirm'
    _invalid_pwd_message = '//div[contains(@class, "form-row")]//span[contains(@id, "dwfrm_profile_login_password_")]'

    def enterFirstName(self):
        fn = self.driver.find_element(By.ID, self._customer_fn)
        fn.send_keys('QA')

    def enterLastName(self):
        ln = self.driver.find_element(By.ID, self._customer_ln)
        ln.send_keys('Tester')

    def enterEmail(self):
        timestamp = datetime.now().strftime('%y%m%d%H%M')
        self.email_address = f'qa{timestamp}@yeti.com'
        email_field = self.driver.find_element(By.ID, self._customer_email)
        email_field.send_keys(self.email_address)

    def confirmEmail(self):
        email_field = self.driver.find_element(By.ID, self._confirm_email)
        email_field.send_keys(self.email_address)
        print(self.email_address)

    def enterPassword(self):
        self.pwd = 'T3ster#!@'
        pwd_field = self.driver.find_element(By.XPATH, self._customer_pwd)
        pwd_field.send_keys(self.pwd)

    def confirmPassword(self):
        pwd_field = self.driver.find_element(By.XPATH, self._confirm_pwd)
        pwd_field.send_keys(self.pwd)

    def enterInvalidPassword(self):
        self.invalid_pwd = 'tester00'
        pwd_field = self.driver.find_element(By.XPATH, self._customer_pwd)
        pwd_field.send_keys(self.invalid_pwd)

    def confirmInvalidPassword(self):
        pwd_field = self.driver.find_element(By.XPATH, self._confirm_pwd)
        pwd_field.send_keys(self.invalid_pwd)

    def verifyPwdError(self):
        error_message = self.driver.find_element(By.XPATH, self._invalid_pwd_message).text
        return error_message

    def clickSignUpBtn(self):
        signup_btn = self.driver.find_element(By.NAME, self._form_sign_in)
        signup_btn.click()