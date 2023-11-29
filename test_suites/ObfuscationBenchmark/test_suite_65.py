import unittest

def test(code):
    exec(code, globals())

    class TestLongestValidParenthesesFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(longest_valid_parentheses('(()'), 2)

        def test_complex_case(self):
            self.assertEqual(longest_valid_parentheses(')()())'), 4)

        def test_empty_string(self):
            self.assertEqual(longest_valid_parentheses(''), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestLongestValidParenthesesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
