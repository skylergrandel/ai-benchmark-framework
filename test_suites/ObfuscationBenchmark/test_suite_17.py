import unittest

def test(code):
    exec(code, globals())

    class TestSumEvenInRangeFunction(unittest.TestCase):
        def test_regular_range(self):
            self.assertEqual(sum_even_in_range(1, 10), 30)  # 2 + 4 + 6 + 8 + 10

        def test_negative_range(self):
            self.assertEqual(sum_even_in_range(-4, 2), -2)  # -4 + -2 + 0 + 2

        def test_single_even_number(self):
            self.assertEqual(sum_even_in_range(4, 4), 4)

        def test_no_even_numbers(self):
            self.assertEqual(sum_even_in_range(1, 1), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestSumEvenInRangeFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
