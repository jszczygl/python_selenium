import unittest
from Python_with_selenium.Package1.TC_LoginTest import LoginTest
from Python_with_selenium.Package1.TC_SignupTest import SignupTest

from Python_with_selenium.Package2.TC_PaymentTest import PaymentTest
from Python_with_selenium.Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#run all tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating test suites

sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

# unittest.TextTestRunner().run(sanityTestSuite)
# unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)