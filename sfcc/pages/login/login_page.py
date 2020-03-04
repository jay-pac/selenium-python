from selenium.webdriver.common.by import By


class LoginPage():

    # defining a constructor
    # Provide driver instance
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _email_field = '//*[@id="dwfrm_login"]//*[@type="email"]'
    _password_field = '//*[@id="dwfrm_login"]//*[@type="password"]'
    _loginbutton = 'dwfrm_login_login'

    def login(self, username, password):
        email = self.driver.find_element(By.XPATH, self._email_field)
        email.send_keys(username)

        pwd = self.driver.find_element(By.XPATH, self._password_field)
        pwd.send_keys(password)

        self.driver.execute_script("document.getElementsByName('dwfrm_login_login')[0].click()")