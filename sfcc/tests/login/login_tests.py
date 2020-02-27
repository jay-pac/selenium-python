from sfcc.pages.login.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestLogin():

    def tests_login(self):
        lp = LoginPage(self.driver)
        lp.login('jason.pacitti@yeti.com', 'T3ster#!')

        assert 'My Account Home' in self.driver.title
