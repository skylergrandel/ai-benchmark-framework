import unittest

def test(code):
    exec(code, globals())

    class TestPrimesLessThanFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(primes_less_than(10), [2, 3, 5, 7])

        def test_no_primes(self):
            self.assertEqual(primes_less_than(2), [])

        def test_single_prime(self):
            self.assertEqual(primes_less_than(3), [2])

    suite = unittest.TestSuite()
    suite.addTest(TestPrimesLessThanFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
