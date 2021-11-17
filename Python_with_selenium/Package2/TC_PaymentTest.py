import unittest

class PaymentTest(unittest.TestCase):
    def test_payment1(self):
        print("payment1")
        self.assertTrue(True)

    def test_payment2(self):
        print("payment2")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()