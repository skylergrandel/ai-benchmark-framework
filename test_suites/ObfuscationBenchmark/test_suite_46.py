import unittest

def test(code):
    exec(code, globals())

    class TestNthUglyNumberFunction(unittest.TestCase):
        def test_small_n(self):
            self.assertEqual(nth_ugly_number(1), 1)
            self.assertEqual(nth_ugly_number(10), 12)

        def test_large_n(self):
            self.assertEqual(nth_ugly_number(100), 1536)

    suite = unittest.TestSuite()
    suite.addTest(TestNthUglyNumberFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
