import unittest

def test(code):
    exec(code, globals())

    class TestSmallestMissingPositiveFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(smallest_missing_positive([3, 4, -1, 1]), 2)

        def test_all_negative(self):
            self.assertEqual(smallest_missing_positive([-1, -2, -3]), 1)

        def test_sequential_numbers(self):
            self.assertEqual(smallest_missing_positive([1, 2, 0]), 3)

    suite = unittest.TestSuite()
    suite.addTest(TestSmallestMissingPositiveFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
