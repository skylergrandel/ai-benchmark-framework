import unittest

def test(code):
    exec(code, globals())

    class TestPrimeFactorsFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(sorted(prime_factors(60)), [2, 2, 3, 5])

        def test_prime_number(self):
            self.assertEqual(prime_factors(13), [13])

        def test_one(self):
            self.assertEqual(prime_factors(1), [])

    suite = unittest.TestSuite()
    suite.addTest(TestPrimeFactorsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
