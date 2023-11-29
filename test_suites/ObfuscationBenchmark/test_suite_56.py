import unittest

def test(code):
    exec(code, globals())

    class TestZeroSumPairsFunction(unittest.TestCase):
        def test_regular_case(self):
            expected = [(-3, 3), (-2, 2), (-1, 1)]
            result = zero_sum_pairs([-3, -2, -1, 0, 1, 2, 3])
            for pair in expected:
                self.assertIn(pair, result)
            self.assertEqual(len(result), len(expected))

        def test_no_zero_sum_pairs(self):
            self.assertEqual(zero_sum_pairs([1, 2, 3]), [])

        def test_empty_list(self):
            self.assertEqual(zero_sum_pairs([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestZeroSumPairsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
