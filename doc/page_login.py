from selenium.webdriver.common.by import By

class PageLogin:

    INPUT_USERNAME = (By.ID, 'username')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN =   (By.TAG_NAME, 'button')

    def __init__(self, driver):
        self.driver = driver

    def get_input_username(self):
        return self.driver.find_element(*self.INPUT_USERNAME)

    def get_input_password(self):
        return self.driver.find_element(*self.INPUT_PASSWORD)

    def get_button_login(self):
        return self.driver.find_element(*self.BUTTON_LOGIN)

    def write_username(self, username):
        self.get_input_username().send_keys(username)

    def write_password(self, password):
        self.get_input_password().send_keys(password)

    def click_login(self):
        self.get_button_login().click()
