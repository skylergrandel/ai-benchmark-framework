import unittest

def test(code):
    exec(code, globals())

    class TestIsPrimeFunction(unittest.TestCase):
        def test_prime_number(self):
            self.assertTrue(is_prime(7))

        def test_non_prime_number(self):
            self.assertFalse(is_prime(10))

        def test_one(self):
            self.assertFalse(is_prime(1))

        def test_two(self):
            self.assertTrue(is_prime(2))

    suite = unittest.TestSuite()
    suite.addTest(TestIsPrimeFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
