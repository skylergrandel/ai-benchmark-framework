import unittest

def test(code):
    exec(code, globals())

    class TestFirstNPrimesFunction(unittest.TestCase):
        def test_small_n(self):
            self.assertEqual(first_n_primes(5), [2, 3, 5, 7, 11])

        def test_n_is_one(self):
            self.assertEqual(first_n_primes(1), [2])

        def test_n_is_zero(self):
            self.assertEqual(first_n_primes(0), [])

    suite = unittest.TestSuite()
    suite.addTest(TestFirstNPrimesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
