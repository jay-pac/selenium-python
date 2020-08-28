from sfcc.pages.login.login_page import LoginPage
import pytest
import unittest


@pytest.mark.usefixtures("setup")
class TestLogin(unittest.TestCase):

    def tests_login(self):
        lp = LoginPage(self.driver)
        lp.login('jason.pacitti@yeti.com', 'T3ster@!')

        assert 'My Account Home' in self.driver.title
