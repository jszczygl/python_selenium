
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_field_id = "txtUsername"
        self.password_field_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalid_credentials_xpath = "//*[contains(text(), 'Invalid credentials')]"

    def enter_username(self, text):
        self.driver.find_element_by_id(self.username_field_id).clear()
        self.driver.find_element_by_id(self.username_field_id).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element_by_id(self.password_field_id).clear()
        self.driver.find_element_by_id(self.password_field_id).send_keys(text)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def invalid_credentials_check(self):
        status = self.driver.find_element_by_xpath(self.invalid_credentials_xpath).is_displayed()
        assert status
