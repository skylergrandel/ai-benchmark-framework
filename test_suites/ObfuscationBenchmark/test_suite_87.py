import unittest

def test(code):
    exec(code, globals())

    class TestThreeSumZeroFunction(unittest.TestCase):
        def test_regular_case(self):
            nums = [-1, 0, 1, 2, -1, -4]
            expected = [[-1, -1, 2], [-1, 0, 1]]
            result = three_sum_zero(nums)
            self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

        def test_no_solution(self):
            self.assertEqual(three_sum_zero([1, 2, 3]), [])

        def test_empty_list(self):
            self.assertEqual(three_sum_zero([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestThreeSumZeroFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
