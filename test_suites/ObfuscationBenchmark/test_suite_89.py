import unittest

def test(code):
    exec(code, globals())

    class TestCountPairsWithDifferenceFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(count_pairs_with_difference([1, 5, 3, 4, 2]), 3)  # Pairs: (1, 3), (3, 5), (2, 4)

        def test_no_pairs(self):
            self.assertEqual(count_pairs_with_difference([1, 7, 11]), 0)

        def test_empty_list(self):
            self.assertEqual(count_pairs_with_difference([]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestCountPairsWithDifferenceFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
