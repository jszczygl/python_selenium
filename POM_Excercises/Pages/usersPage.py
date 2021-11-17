import time
from selenium.webdriver.support.ui import Select

class UsersPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_new_user_button_id = "btnAdd"
        self.system_users_tab_name_xpath="//*[contains(text(), 'System Users')]"
        self.user_name_field_id="systemUser_userName"
        self.user_role_select_menu_id="systemUser_userType"
        self.user_full_name_field_id="systemUser_employeeName_empName"
        self.status_field_id="systemUser_status"
        self.password_field_id="systemUser_password"
        self.password_conf_field_id="systemUser_confirmPassword"
        self.save_user_button_id="btnSave"
        self.search_user_field_id="searchSystemUser_userName"
        self.search_button_id="searchBtn"
        self.first_record_in_table_xpath="//*[@id='resultTable']/tbody/tr/td[2]/a"
        self.first_record_in_table_checkbox_id="ohrmList_chkSelectRecord_61"
        self.delete_user_button_id="btnDelete"
        self.no_records_in_table_msg_xpath="//*[@id='resultTable']/tbody/tr/td"

    def verify_if_user_was_deleted(self, text):
        self.driver.find_element_by_id(self.search_user_field_id).send_keys(text)
        self.driver.find_element_by_id(self.search_button_id).click()
        msg = self.driver.find_element_by_xpath(self.no_records_in_table_msg_xpath).text
        assert msg == "No Records Found"

    def delete_searched_user(self):
        self.driver.find_element_by_id(self.first_record_in_table_checkbox_id).click()
        self.driver.find_element_by_id(self.delete_user_button_id).click()
        self.driver.switch_to.alert.accept()

    def verify_user_in_table(self, text):
        user = self.driver.find_element_by_xpath(self.first_record_in_table_xpath).text
        assert text == user

    def find_user_by_username(self, text):
        self.driver.find_element_by_id(self.search_user_field_id).send_keys(text)
        time.sleep(1)
        self.driver.find_element_by_id(self.search_button_id).click()

    def click_save_new_user(self):
        self.driver.find_element_by_id(self.save_user_button_id).is_enabled()
        self.driver.find_element_by_id(self.save_user_button_id).click()

    def enter_text_into_password_field(self, text):
        self.driver.find_element_by_id(self.password_field_id).send_keys(text)

    def enter_text_into_conf_password_field(self, text):
        self.driver.find_element_by_id(self.password_conf_field_id).send_keys(text)

    def select_user_status(self, status):
        drop1 = Select(self.driver.find_element_by_id(self.status_field_id))
        drop1.select_by_visible_text(status)

    def enter_text_into_fullname_field(self, text):
        self.driver.find_element_by_id(self.user_full_name_field_id).send_keys(text)

    def select_user_role(self, role):
        drop = Select(self.driver.find_element_by_id(self.user_role_select_menu_id))
        drop.select_by_visible_text(role)

    def click_add_new_user(self):
        self.driver.find_element_by_id(self.add_new_user_button_id).click()

    def enter_text_into_username_field(self, text):
        self.driver.find_element_by_id(self.user_name_field_id).send_keys(text)

    def verify_users_page(self):
        status = self.driver.find_element_by_xpath(self.system_users_tab_name_xpath).is_displayed()
        assert status


