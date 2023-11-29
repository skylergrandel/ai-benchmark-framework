import unittest

def test(code):
    exec(code, globals())

    class TestIsPalindromeFunction(unittest.TestCase):
        def test_empty_string(self):
            self.assertTrue(is_palindrome(''))

        def test_single_character(self):
            self.assertTrue(is_palindrome('a'))

        def test_palindrome(self):
            self.assertTrue(is_palindrome('racecar'))

        def test_not_palindrome(self):
            self.assertFalse(is_palindrome('hello'))

    suite = unittest.TestSuite()
    suite.addTest(TestIsPalindromeFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
