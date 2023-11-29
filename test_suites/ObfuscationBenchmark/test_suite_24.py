import unittest

def test(code):
    exec(code, globals())

    class TestFirstNFibonacciFunction(unittest.TestCase):
        def test_small_n(self):
            self.assertEqual(first_n_fibonacci(5), [0, 1, 1, 2, 3])

        def test_n_is_one(self):
            self.assertEqual(first_n_fibonacci(1), [0])

        def test_n_is_zero(self):
            self.assertEqual(first_n_fibonacci(0), [])

    suite = unittest.TestSuite()
    suite.addTest(TestFirstNFibonacciFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
