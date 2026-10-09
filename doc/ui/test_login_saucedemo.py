import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('class_setup')
class TestLogin:

    @pytest.fixture
    def class_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')

    def test_login_correcto(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        assert self.driver.find_element(By.XPATH, "//div[@class='app_logo']").text == 'Swag Labs'
        self.driver.quit()

    def test_login_incorrecto_sin_user_sin_pass(self):
        self.driver.find_element(By.ID, 'login-button').click()
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == 'Epic sadface: Username is required'
        self.driver.quit()

    def test_login_incorrecto_con_user_sin_pass(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'login-button').click()
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == 'Epic sadface: Password is required'
        self.driver.quit()

    @pytest.mark.parametrize('user, pwd', [('pepe', 'secret_sauce'), ('standard_user', 'pepe'), ('pepe', 'pepe')])
    def test_login_incorrecto(self, user, pwd):
        self.driver.find_element(By.ID, 'user-name').send_keys(user)
        self.driver.find_element(By.ID, 'password').send_keys(pwd)
        self.driver.find_element(By.ID, 'login-button').click()
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == 'Epic sadface: Username and password do not match any user in this service'
        self.driver.quit()
