from selenium.webdriver.common.by import By

class PageSecure:

    H2_MSG = (By.TAG_NAME, 'h2')

    def __init__(self, driver):
        self.driver = driver

    def get_h2_msg(self):
        return self.driver.find_element(*self.H2_MSG)

    def text_msg(self):
        return self.get_h2_msg().text
