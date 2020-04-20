from selenium.webdriver.common.by import By
from datetime import datetime


class WishListPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _add_wishlist = '//a[@class="add-btn "][@data-master-sku="YRAMCOLSTER"]'
    _email_field = '//div[contains(@id, "dialog-container")]//input[contains(@id,"dwfrm_login_username_")]'
    _pwd_field = '//div[contains(@id, "dialog-container")]//input[contains(@id,"dwfrm_login_password_")]'
    _continue_btn = '//div[@id="dialog-container"]//button[@class="button-primary wishlist-dialog-container__button wishlist-login__continue"]'
    _no_checkbox = 'modal_new_user_true'
    _yes_checkbox = 'modal_new_user_false'
    _wishlist_text = '//h1[@class="wishlist-title text-left"]'

    _first_name = '//div[@id="dialog-container"]//input[@id="dwfrm_profile_customer_firstname"]'
    _last_name = '//div[@id="dialog-container"]//input[@id="dwfrm_profile_customer_lastname"]'
    _register_email = '//div[@id="dialog-container"]//input[@id="dwfrm_profile_customer_email"]'
    _register_pwd = '//div[@class="wishlist-register"]//input[contains(@id, "dwfrm_profile_wishlistregister_password_")]'
    _register_continue = '//div[@class="wishlist-register"]//button[@class="button-primary wishlist-dialog-container__button no-margin"]'
    _remove_link = 'dwfrm_wishlist_items_i2_deleteItem'

    _pwd_error_message = '//span[contains(@id, "dwfrm_profile_wishlistregister_password_")]'

    def clickWishListBtn(self):
        wishlist_btn = self.driver.find_element(By.XPATH, self._add_wishlist)
        wishlist_btn.click()

    def enterEmailAddress(self, username):
        email = self.driver.find_element(By.XPATH, self._email_field)
        email.send_keys(username)

    def enterPassword(self, password):
        pwd = self.driver.find_element(By.XPATH, self._pwd_field)
        pwd.send_keys(password)

    def clickYesCheckbox(self):
        yes_checkbox = self.driver.find_element(By.ID, self._yes_checkbox)
        yes_checkbox.click()

    def clickNoCheckbox(self):
        self.driver.execute_script('document.getElementById("modal_new_user_true").click();')

    def clickContinueButton(self):
        continue_btn = self.driver.find_element(By.XPATH, self._continue_btn)
        continue_btn.click()

    def enterFirstName(self, firstname='QA'):
        fn = self.driver.find_element(By.XPATH, self._first_name)
        fn.send_keys(firstname)

    def enterLastName(self, lastname='Automation'):
        fn = self.driver.find_element(By.XPATH, self._last_name)
        fn.send_keys(lastname)

    def enterRegisterEmail(self):
        timestamp = datetime.now().strftime('%y%m%d%H%M')
        email_address = f'qa{timestamp}@yeti.com'
        email_field = self.driver.find_element(By.XPATH, self._register_email)
        email_field.send_keys(email_address)
        print(email_address)

    def enterRegisterPwd(self):
        pwd = self.driver.find_element(By.XPATH, self._register_pwd)
        pwd.send_keys('T3ster#!@')

    def enterInvalidPwd(self):
        pwd = self.driver.find_element(By.XPATH, self._register_pwd)
        pwd.send_keys('tester123')

    def clickRegisterContinue(self):
        continue_btn = self.driver.find_element(By.XPATH, self._register_continue)
        continue_btn.click()

    def verifyAccountWishlist(self):
        wishlist_page_text = self.driver.find_element(By.XPATH, self._wishlist_text).text
        return wishlist_page_text

    def verifyInvalidPwd(self):
        error_message = self.driver.find_element(By.XPATH, self._pwd_error_message).text
        return error_message

    def removeWishListItem(self):
        remove = self.driver.find_element(By.NAME, self._remove_link)
        remove.click()


