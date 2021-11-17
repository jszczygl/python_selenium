from selenium import webdriver
from POM_Excercises.Pages.loginPage import LoginPage
from POM_Excercises.Pages.homePage import HomePage
from POM_Excercises.Pages.usersPage import UsersPage
from selenium.webdriver import ActionChains

import unittest
import time


class UsersActions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        login_page = LoginPage(cls.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        action = ActionChains(cls.driver)
        home_page = HomePage(cls.driver, action)
        home_page.verify_welcome_text()

    def test_add_search_delete_user(self):
        driver = self.driver
        action = ActionChains(driver)
        home_page = HomePage(driver, action)
        users_page = UsersPage(driver)

        home_page.navigate_to_users_page()
        users_page.verify_users_page()
        users_page.click_add_new_user()
        users_page.enter_text_into_username_field("newuser5")
        users_page.enter_text_into_fullname_field("David Morris")
        users_page.select_user_role("ESS")
        users_page.select_user_status("Enabled")
        users_page.enter_text_into_password_field("newUser123")
        users_page.enter_text_into_conf_password_field("newUser123")
        time.sleep(2)
        users_page.click_save_new_user()

        users_page.find_user_by_username("newuser5")
        users_page.verify_user_in_table("newuser5")
        users_page.delete_searched_user()

        users_page.verify_if_user_was_deleted("newuser5")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()