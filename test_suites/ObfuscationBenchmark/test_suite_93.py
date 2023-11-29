import unittest

def test(code):
    exec(code, globals())

    class TestEvaluateExpressionFunction(unittest.TestCase):
        def test_simple_addition(self):
            self.assertEqual(evaluate_expression('2+3'), 5)

        def test_mixed_operations(self):
            self.assertEqual(evaluate_expression('2+3*4-1'), 13)

        def test_single_number(self):
            self.assertEqual(evaluate_expression('10'), 10)

    suite = unittest.TestSuite()
    suite.addTest(TestEvaluateExpressionFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
