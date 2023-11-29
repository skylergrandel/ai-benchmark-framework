import unittest

def test(code):
    exec(code, globals())

    class TestGenerateParenthesesFunction(unittest.TestCase):
        def test_n_is_3(self):
            expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
            result = generate_parentheses(3)
            self.assertEqual(sorted(result), sorted(expected))

        def test_n_is_1(self):
            self.assertEqual(generate_parentheses(1), ['()'])

        def test_n_is_0(self):
            self.assertEqual(generate_parentheses(0), [''])

    suite = unittest.TestSuite()
    suite.addTest(TestGenerateParenthesesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
