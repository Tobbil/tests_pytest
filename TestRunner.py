
from unittest import TestLoader, TestSuite, TextTestRunner
from test_AddToCart import TestAddToCart
from test_SendMessage import TestSendMessage
from test_SignUp import TestSignUp
from test_LogIn import TestLogIn
 
if __name__ == "__main__":
 
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(TestAddToCart),
        test_loader.loadTestsFromTestCase(TestSendMessage),
        test_loader.loadTestsFromTestCase(TestSignUp),
        test_loader.loadTestsFromTestCase(TestLogIn)
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)