import unittest

def setUpModule():  #will be executed before any calss or method present in the test calss
    print("setup module")

def tearDownModule():   #will be executed after everything presnt in the test class
    print("trardown module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):  #being executed before every test
        print("this is setup login method")

    @classmethod
    def tearDown(self): #being executed after every test
        print("teardown logout")

    @classmethod
    def setUpClass(cls):    #being executed before all tests
        print("setup class SETUP")

    @classmethod
    def tearDownClass(cls): #being executed after all tests
        print("tardown class TEARDOWN")

    def test_1(self):
        print("1")

    def test_2(self):
        print("2")

    def test_3(self):
        print("3")

    def test_4(self):
        print("4")

if __name__ == "__main__":
    unittest.main()