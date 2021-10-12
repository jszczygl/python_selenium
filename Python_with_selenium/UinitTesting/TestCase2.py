import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        self.driver.close()

    def test_BING(self):
        self.driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
        self.driver.get("https://bing.com")
        print(self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()