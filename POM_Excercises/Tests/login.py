from selenium import webdriver
import unittest
from POM_Excercises.Pages.loginPage import LoginPage
from POM_Excercises.Pages.homePage import HomePage
from selenium.webdriver import ActionChains

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.action = ActionChains
        cls.driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login1(self):
        driver = self.driver
        action = self.action
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()

        home_page = HomePage(driver,action)
        home_page.verify_welcome_text()
        home_page.click_welcome_button()
        home_page.click_logout_button()

    def test_login2(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login_page = LoginPage(driver)
        login_page.enter_username("lala")
        login_page.enter_password("koala")
        login_page.click_login_button()
        login_page.invalid_credentials_check()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()