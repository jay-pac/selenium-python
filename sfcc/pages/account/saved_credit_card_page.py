

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

