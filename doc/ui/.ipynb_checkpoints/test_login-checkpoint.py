import pytest
from selenium import webdriver
from 'ui/page_login' import PageLogin
from 'ui/page_secure' import PageSecure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/login')
    yield driver
    driver.quit()

@pytest.fixture
def class_setup(driver):
    page_login = PageLogin(driver)
    page_secure = PageSecure(driver)
    return page_login, page_secure

class TestLogin:
    
    def test_login(self, class_setup):
        page_login, page_secure = class_setup
        page_login.write_username('tomsmith')
        page_login.write_password('SuperSecretPassword!')
        page_login.click_login()
        assert page_secure.text_msg() == 'Secure Area'
