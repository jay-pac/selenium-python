from sfcc.pages.account.sign_up_page import SignUpPage
import pytest


@pytest.mark.usefixtures("setup")
class TestAccountCreation():

    def tests_create_account(self):
        signup = SignUpPage(self.driver)

        signup.enterFirstName()
        signup.enterLastName()
        signup.enterEmail()
        signup.confirmEmail()
        signup.enterPassword()
        signup.confirmPassword()
        signup.clickSignUpBtn()
