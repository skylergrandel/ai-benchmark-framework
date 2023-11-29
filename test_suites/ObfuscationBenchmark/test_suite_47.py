import unittest

def test(code):
    exec(code, globals())

    class TestMinCharsForPalindromeFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(min_chars_for_palindrome('abca'), 1)  # Adding 'b' at the end makes it a palindrome

        def test_already_palindrome(self):
            self.assertEqual(min_chars_for_palindrome('racecar'), 0)

        def test_empty_string(self):
            self.assertEqual(min_chars_for_palindrome(''), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestMinCharsForPalindromeFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
