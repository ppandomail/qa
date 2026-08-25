import pytest
from selenium import webdriver
from page_login import PageLogin
from page_secure import PageSecure
from pyaml_env import parse_config

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

@pytest.fixture
def class_setup(driver):
    page_login = PageLogin(driver)
    page_secure = PageSecure(driver)
    return page_login, page_secure

class TestLogin:

    data_login = parse_config('data_login.yaml')
    
    def test_login(self, class_setup):
        page_login, page_secure = class_setup
        page_login.write_username(self.data_login['username'])
        page_login.write_password(self.data_login['password'])
        page_login.click_login()
        assert page_secure.text_msg() == self.data_login['expected']
