from selenium.webdriver.common.by import By


class AccountPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _account_dash_link = '//a[contains(text(),"Account dashboard")]'
    _profile_link = '//a[contains(text(),"Profile")]'
    _address_book_link = '//a[contains(text(),"Address book")]'
    _saved_cc_link = '//a[contains(text(),"Saved credit cards")]'
    _order_history_link = '//a[contains(text(),"Order history")]'
    _my_wishlist_link = '//a[contains(text(),"My Wishlist")]'
    _product_regist_link = '//a[contains(text(),"Product registration")]'
    _logout_button = '//button[@class="button-primary log-out-button"]'

    _faq_link = '//a[@class="service-link"][contains(text(),"FAQ")]'
    _help_link = '//a[@class="service-link"][contains(text(),"Help")]'
    _contact_link = '//a[@class="service-link"][contains(text(),"Contact")]'

    _order_history_viewall_link = '//div[@class="data-box data-box-orders"]//a[contains(text(),"view all")]'
    _profile_edit_link = '//a[contains(text(),"Edit")]'
    _cc_viewall_link = '//div[@class="data-box-info"]//a[contains(text(),"view all")]'
    _address_manage_link = '//a[contains(text(),"manage addresses")]'

    # My Account - Left Navigation Links
    def clickAccountDashLink(self):
        account_dash_link = self.driver.find_element(By.XPATH, self._account_dash_link)
        account_dash_link.click()

    def clickProfileLink(self):
        profile_link = self.driver.find_element(By.XPATH, self._profile_link)
        profile_link.click()

    def clickAddressLink(self):
        address_link = self.driver.find_element(By.XPATH, self._address_book_link)
        address_link.click()

    def clickSavedCCLink(self):
        saved_cc_link = self.driver.find_element(By.XPATH, self._saved_cc_link)
        saved_cc_link.click()

    def clickOrderHistoryLink(self):
        orderhistory_link = self.driver.find_element(By.XPATH, self._order_history_link)
        orderhistory_link.click()

    def clickMyWishListLink(self):
        my_wishlist_link = self.driver.find_element(By.XPATH, self._my_wishlist_link)
        my_wishlist_link.click()

    def clickProductRegistLink(self):
        product_regist_link = self.driver.find_element(By.XPATH, self._product_regist_link)
        product_regist_link.click()

    def clickLogoutBtn(self):
        logout_btn = self.driver.find_element(By.XPATH, self._logout_button)
        logout_btn.click()

    # Customer Support -  Left Navigation
    def clickFaqLink(self):
        faq_link = self.driver.find_element(By.XPATH, self._faq_link)
        faq_link.click()

    def clickHelpLink(self):
        help_link = self.driver.find_element(By.XPATH, self._help_link)
        help_link.click()

    def clickContactLink(self):
        contact_link = self.driver.find_element(By.XPATH, self._contact_link)
        contact_link.click()

    # Account Overview - Section Links
    def clickOrderHistoryViewAll(self):
        order_history_viewall = self.driver.find_element(By.XPATH, self._order_history_viewall_link)
        order_history_viewall.click()

    def clickProfileEdit(self):
        profile_edit = self.driver.find_element(By.XPATH, self._profile_edit_link)
        profile_edit.click()

    def clickCCViewAll(self):
        cc_viewall = self.driver.find_element(By.XPATH, self._cc_viewall_link)
        cc_viewall.click()

    def clickManageAddress(self):
        manage_address = self.driver.find_element(By.XPATH, self._address_manage_link)
        manage_address.click()

