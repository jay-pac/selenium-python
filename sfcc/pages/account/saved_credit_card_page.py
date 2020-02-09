from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SavedCreditCardPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _cc_view_all = '//a[contains(text(),"view all")]'
    _cc_add_cc = '//a[@class="section-header-note add-card button-primary"]'
    _cc_nickname = 'dwfrm_paymentinstruments_creditcards_newcreditcard_nickname'
    _cc_cardnumber = 'c-cardnumber'
    _cc_name = 'c-cardname'
    _cc_month = 'c-exmth'
    _cc_year = 'c-exyr'
    _cc_cvv = 'lbl-c-cvv'
    _cc_apply = 'applyBtn'
    _remove_cc = '//button[@class="button-text delete"]'
    _saved_cc = '//h3[@class="proxima-nova-rg-bold"]'
    _delete_cc = '//button[@class="button-primary apply"]'
    _add_cc_link = '//a[@class="section-header-note add-card add-credit-card"]'

    def clickAddCCBtn(self):
        add_cc_btn = self.driver.find_element(By.XPATH, self._cc_add_cc)
        add_cc_btn.click()

    def enterCCNickName(self, nickname='QA Automation'):
        nickname_field = self.driver.find_element(By.ID, self._cc_nickname)
        nickname_field.send_keys(nickname)

    def enterCardNumber(self, cc='4847189499632248'):
        self.driver.switch_to.frame(self.driver.find_element(By.ID, 'paymetric-credit-card'))
        cc_num = self.driver.find_element(By.ID, self._cc_cardnumber)
        cc_num.send_keys(cc)

    def enterName(self, name='QA Tester'):
        full_name = self.driver.find_element(By.ID, self._cc_name)
        full_name.send_keys(name)

    def selectMonth(self, month='7'):
        select_month = Select(self.driver.find_element(By.ID, self._cc_month))
        select_month.select_by_value(month)

    def selectYear(self, year='2029'):
        select_year = Select(self.driver.find_element(By.ID, self._cc_year))
        select_year.select_by_value(year)

    def enterCCV(self, cvv='111'):
        self.driver.execute_script("document.getElementById('c-cvv').value = '111'")

    def clickApplyBtn(self):
        self.driver.switch_to.default_content()
        self.driver.execute_script('document.getElementById("applyBtn").click();')

    def verifySavedCC(self):
        saved_cc = self.driver.find_element(By.XPATH, self._saved_cc).text
        return saved_cc

    def clickRemoveLink(self):
        remove_link = self.driver.find_element(By.XPATH, self._remove_cc)
        remove_link.click()

    def clickDeleteModal(self):
        delete_btn = self.driver.find_element(By.XPATH, self._delete_cc)
        delete_btn.click()

    def clickAddCardLink(self):
        add_card = self.driver.find_element(By.XPATH, self._add_cc_link)
        add_card.click()