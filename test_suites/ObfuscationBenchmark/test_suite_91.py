import unittest

def test(code):
    exec(code, globals())

    class TestSumBetweenLargestFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(sum_between_largest([2, 7, 1, 8, 2, 8, 1]), 1)  # Sum between the first two '8's

        def test_single_occurrence_of_max(self):
            self.assertEqual(sum_between_largest([5, 2, 4, 3, 1]), 9)  # Sum between '5's

        def test_no_elements_between(self):
            self.assertEqual(sum_between_largest([10, 1, 10]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestSumBetweenLargestFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
