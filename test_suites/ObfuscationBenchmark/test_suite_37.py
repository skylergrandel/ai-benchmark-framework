import unittest

def test(code):
    exec(code, globals())

    class TestValidParenthesesFunction(unittest.TestCase):
        def test_valid_parentheses(self):
            self.assertTrue(valid_parentheses('()'))
            self.assertTrue(valid_parentheses('()[]{}'))

        def test_invalid_parentheses(self):
            self.assertFalse(valid_parentheses('(]'))
            self.assertFalse(valid_parentheses('([)]'))

        def test_empty_string(self):
            self.assertTrue(valid_parentheses(''))

    suite = unittest.TestSuite()
    suite.addTest(TestValidParenthesesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
