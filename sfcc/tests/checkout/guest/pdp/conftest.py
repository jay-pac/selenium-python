from selenium import webdriver
import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--env_name", action="store", default="dev-us"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver is not an option")

    env_name = request.config.getoption("env_name")
    if env_name == "dev-us":
        driver.get('https://Storefront:Yeti2017@development-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html')
        cookie = {
            'domain': 'development-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        driver.add_cookie(cookie)
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(10)

    elif env_name == 'stg-us':
        driver.get('https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html')
        cookie = {
            'domain': 'staging-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        driver.add_cookie(cookie)
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(10)

    elif env_name == 'prod-us':
        driver.get('https://www.yeti.com/en_US/drinkware/rambler-20-oz-tumbler/YRAM20.html')
        cookie = {
            'domain': 'www.yeti.com',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        driver.add_cookie(cookie)
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.close()
