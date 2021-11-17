import unittest

class LoginTest(unittest.TestCase):
    def test_login1(self):
        print("login1")
        self.assertTrue(True)

    def test_login2(self):
        print("login2")
        self.assertTrue(True)

    def test_login3(self):
        print("login3")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()