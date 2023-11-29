import unittest

def test(code):
    exec(code, globals())

    class TestTwoSumIndicesFunction(unittest.TestCase):
        def test_regular_case(self):
            nums = [2, 7, 11, 15]
            target = 9
            self.assertEqual(sorted(two_sum_indices(nums, target)), [0, 1])  # nums[0] + nums[1] = 9

        def test_no_solution(self):
            self.assertIsNone(two_sum_indices([1, 2, 3], 6))

        def test_single_element(self):
            self.assertIsNone(two_sum_indices([1], 1))

    suite = unittest.TestSuite()
    suite.addTest(TestTwoSumIndicesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
