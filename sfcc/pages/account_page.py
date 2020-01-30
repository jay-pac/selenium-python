from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    _edit_address = '//a[@class="address-edit"]'
    _remove_address = '//a[@class="address-delete delete"]'

    _cc_view_all = '//a[contains(text(),"view all")]'
    _cc_add_cc = '//a[@class="section-header-note add-card button-primary"]'
    _cc_nickname = 'dwfrm_paymentinstruments_creditcards_newcreditcard_nickname'
    _cc_cardnumber = 'c-cardnumber'
    _cc_name = 'c-cardname'
    _cc_month = 'c-exmth'
    _cc_year = 'c-exyr'
    _cc_cvv = 'lbl-c-cvv'
    _cc_apply = 'applyBtn'

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
    def clickAddressLink(self):
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Address book")]').click()

    def clickManageAddress(self):
        self.driver.find_element(By.XPATH, self._manage_address).click()

    def clickAddressBtn(self):
        address_btn = self.driver.find_element(By.ID, self._address_button)
        address_btn.click()

    # Address Form
    def enterAddressNickname(self):
        nickname_field = self.driver.find_element(By.ID, self._address_nickname)
        nickname_field.send_keys('')
    # TODO:  Need to add a separate page class for account > create address
    def enterFirstName(self):
        fn_field = self.driver.find_element(By.ID, self._address_fn)
        fn_field.send_keys('')

    def enterLastName(self):
        ln_field = self.driver.find_element(By.ID, self._address_ln)
        ln_field.send_keys('')

    def enterAddress(self):
        address_field = self.driver.find_element(By.ID, self._address_1)
        address_field.send_keys('')

    def enterCity(self):
        city_field = self.driver.find_element(By.ID, self._address_city)
        city_field.send_keys('')

    def selectState(self, state='TX'):
        select_state = Select(self.driver.find_element(By.ID, self._address_state))
        select_state.select_by_value(state)

    def enterZip(self, zip=78701):
        zip_code = self.driver.find_element(By.ID, self._address_zip)
        zip_code.send_keys(zip)

    def enterPhone(self):
        phone_num = self.driver.find_element(By.ID, self._address_phone)
        phone_num.send_keys('5125551234')

    def clickSaveButton(self):
        save_btn = self.driver.find_element(By.ID, self._save_address)
        save_btn.click()
