import unittest

def test(code):
    exec(code, globals())

    class TestIsValidPalindromeFunction(unittest.TestCase):
        def test_valid_palindrome(self):
            self.assertTrue(is_valid_palindrome('A man, a plan, a canal: Panama'))

        def test_invalid_palindrome(self):
            self.assertFalse(is_valid_palindrome('race a car'))

        def test_empty_string(self):
            self.assertTrue(is_valid_palindrome(''))

    suite = unittest.TestSuite()
    suite.addTest(TestIsValidPalindromeFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
