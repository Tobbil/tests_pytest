import sys
import os
# sys.path.append(sys.path[0] + "/...")
# sys.path.append(os.getcwd())
 
from unittest import TestLoader, TestSuite, TextTestRunner
from test_AddToCart import TestAddToCart
from test_SendMessage import TestSendMessage
from test_SignUp import TestSignUp
from test_LogIn import TestLogIn

import testtools as testtools
 
if __name__ == "__main__":
 
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(TestAddToCart),
        test_loader.loadTestsFromTestCase(TestSendMessage),
        test_loader.loadTestsFromTestCase(TestSignUp),
        test_loader.loadTestsFromTestCase(TestLogIn)
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
 
    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    # parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    # parallel_suite.run(testtools.StreamResult())
    #     self.driver.set_page_load_timeout(30))