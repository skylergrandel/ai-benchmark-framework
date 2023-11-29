import unittest

def test(code):
    exec(code, globals())

    class TestMaxSumNonAdjacentFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(max_sum_non_adjacent([3, 2, 7, 10]), 13)  # Choose 3 and 10

        def test_all_negative(self):
            self.assertEqual(max_sum_non_adjacent([-1, -2, -3]), -1)

        def test_empty_list(self):
            self.assertEqual(max_sum_non_adjacent([]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestMaxSumNonAdjacentFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
