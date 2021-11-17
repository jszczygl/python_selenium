import unittest
from selenium import webdriver

class App(unittest.TestCase):
    def test_1(self):
        driver = webdriver.Chrome('C:/Users/Kuba/PycharmProjects/python_selenium/Drivers/chromedriver.exe')
        driver.get("https://www.google.com")
        title = driver.title

        #assertEqual and assertNotEqual
        self.assertEqual("Google", title, "webpage title is not correct")
        self.assertNotEqual("Gooogle", title)

        #assertTrue and assertFalse
        self.assertTrue("Google"==title)
        self.assertFalse("Gooogle" == title)

        #asserisNone and assertIsNotNone
        self.assertIsNone(None)
        self.assertIsNotNone(driver)

        #assertIn and assertNotIn
        list=["python", "apple", "banana"]
        self.assertIn("python", list)
        self.assertNotIn("jajo", list)

        #assertGreater, assertGreaterEqual, assertLess, assertLessEqual
        self.assertGreater(2, 1)
        self.assertGreaterEqual(2, 2)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 1)

        driver.close()



if __name__ == "__main__":
    unittest.main()