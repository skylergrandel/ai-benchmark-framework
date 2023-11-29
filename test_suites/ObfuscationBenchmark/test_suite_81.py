import unittest

def test(code):
    exec(code, globals())

    class TestLongestPalindromicSubstringFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(longest_palindromic_substring('babad'), 'bab')  # 'aba' is also a valid answer

        def test_single_char(self):
            self.assertEqual(longest_palindromic_substring('a'), 'a')

        def test_no_palindrome(self):
            self.assertEqual(longest_palindromic_substring('abc'), 'a')

    suite = unittest.TestSuite()
    suite.addTest(TestLongestPalindromicSubstringFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
