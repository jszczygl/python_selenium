import unittest

class App(unittest.TestCase):
    @unittest.SkipTest  #skip current test
    def test_1(self):
        print("1")

    @unittest.skip("skipping because it's not rdy")
    def test_2(self):
        print("2")

    @unittest.skipIf(1==1, "skipping because cond is true")
    def test_3(self):
        print("3")

    def test_4(self):
        print("4")


if __name__ == "__main__":
    unittest.main()