import unittest

def test(code):
    exec(code, globals())

    class TestListPrimesFunction(unittest.TestCase):
        def test_range_with_primes(self):
            self.assertEqual(list_primes(10, 20), [11, 13, 17, 19])

        def test_range_without_primes(self):
            self.assertEqual(list_primes(22, 25), [])

        def test_single_prime_number(self):
            self.assertEqual(list_primes(13, 13), [13])

        def test_negative_range(self):
            self.assertEqual(list_primes(-10, 2), [2])

    suite = unittest.TestSuite()
    suite.addTest(TestListPrimesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
