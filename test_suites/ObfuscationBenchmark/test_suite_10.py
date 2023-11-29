import unittest

def test(code):
    exec(code, globals())

    class TestFibonacciFunction(unittest.TestCase):
        def test_base_cases(self):
            self.assertEqual(fibonacci(0), 0)
            self.assertEqual(fibonacci(1), 1)

        def test_fibonacci_sequence(self):
            self.assertEqual(fibonacci(5), 5)
            self.assertEqual(fibonacci(10), 55)

    suite = unittest.TestSuite()
    suite.addTest(TestFibonacciFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
