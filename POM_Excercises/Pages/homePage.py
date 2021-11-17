class HomePage():

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

        self.welcome_field_id = "welcome"
        self.logout_button_link = "Logout"
        self.admin_tab_id = "menu_admin_viewAdminModule"
        self.user_management_menu_id="menu_admin_UserManagement"
        self.user_tab_button_id="menu_admin_viewSystemUsers"

    def navigate_to_users_page(self):
        elem = self.driver.find_element_by_id(self.admin_tab_id)
        self.action.move_to_element(elem).perform()
        elem1 = self.driver.find_element_by_id(self.user_management_menu_id)
        self.action.move_to_element(elem1).perform()
        self.driver.find_element_by_id(self.user_tab_button_id).click()

    def verify_welcome_text(self):
        status = self.driver.find_element_by_id(self.welcome_field_id).is_displayed()
        assert status

    def click_welcome_button(self):
        self.driver.find_element_by_id(self.welcome_field_id).click()

    def click_logout_button(self):
        self.driver.find_element_by_link_text(self.logout_button_link).click()
