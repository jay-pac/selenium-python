from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


class AddressBookPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _address_book_link = '//a[contains(text(),"Address book")]'
    _manage_address = '//a[contains(text(),"manage addresses")]'
    _address_button = '//a[@class="button-primary section-header-note address-create"]'
    _address_nickname = 'dwfrm_profile_address_addressid'
    _address_fn = 'dwfrm_profile_address_firstname'
    _address_ln = 'dwfrm_profile_address_lastname'
    _address_1 = 'dwfrm_profile_address_address1'
    _address_city = 'dwfrm_profile_address_city'
    _address_state = 'dwfrm_profile_address_states_state'
    _address_zip = 'dwfrm_profile_address_postal'
    _address_phone = 'dwfrm_profile_address_phone'
    _save_address = 'dwfrm_profile_address_save'
    _edit_address = '//a[@class="address-edit"]'
    _remove_address = '//a[@class="address-delete delete"]'

    # Add Address methods
    def clickAddressLink(self):
        self.driver.find_element(By.XPATH, self._address_book_link).click()

    def clickManageAddress(self):
        self.driver.find_element(By.XPATH, self._manage_address).click()

    def clickAddressBtn(self):
        address_btn = self.driver.find_element(By.XPATH, self._address_button)
        address_btn.click()

    # Address Form
    def enterAddressNickname(self, nickname='QA Automation'):
        nickname_field = self.driver.find_element(By.ID, self._address_nickname)
        nickname_field.send_keys(nickname)

    def enterFirstName(self, fn='Jason'):
        fn_field = self.driver.find_element(By.ID, self._address_fn)
        fn_field.send_keys(fn)

    def enterLastName(self, ln='Pacitti'):
        ln_field = self.driver.find_element(By.ID, self._address_ln)
        ln_field.send_keys(ln)

    def enterAddress(self, address='7601 Southwest Pkwy'):
        address_field = self.driver.find_element(By.ID, self._address_1)
        address_field.send_keys(address)

    def enterCity(self, city='Austin'):
        city_field = self.driver.find_element(By.ID, self._address_city)
        city_field.send_keys(city)

    def selectState(self, state='TX'):
        select_state = Select(self.driver.find_element(By.ID, self._address_state))
        select_state.select_by_value(state)

    def enterZip(self, zip=78735):
        zip_code = self.driver.find_element(By.ID, self._address_zip)
        zip_code.send_keys(zip)

    def enterPhone(self, phone='5125551234'):
        phone_num = self.driver.find_element(By.ID, self._address_phone)
        phone_num.send_keys(phone)

    def clickSaveButton(self):
        save_btn = self.driver.find_element(By.NAME, self._save_address)
        save_btn.click()

    def clickEditLink(self):
        edit_link = self.driver.find_element(By.XPATH, '//a[@class="address-edit"]')
        edit_link.click()

    def clickRemoveLink(self):
        remove_link = self.driver.find_element(By.XPATH, '//a[@class="address-delete delete"]')
        remove_link.click()

    def clickDeleteModal(self):
        delete_btn = self.driver.find_element(By.XPATH, '//button[@class="button-primary apply"]')
        delete_btn.click()

    def verifyAddressCreate(self):
        address = self.driver.find_element(By.XPATH, '//div[@class="mini-address-title"]').text
        return address
