import unittest

def test(code):
    exec(code, globals())

    class TestGCDFunction(unittest.TestCase):
        def test_common_case(self):
            self.assertEqual(gcd(12, 8), 4)

        def test_prime_numbers(self):
            self.assertEqual(gcd(13, 7), 1)

        def test_zero(self):
            self.assertEqual(gcd(0, 5), 5)

    suite = unittest.TestSuite()
    suite.addTest(TestGCDFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
