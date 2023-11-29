import unittest

def test(code):
    exec(code, globals())

    class TestFourSumFunction(unittest.TestCase):
        def test_regular_case(self):
            nums = [1, 0, -1, 0, -2, 2]
            target = 0
            expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
            result = four_sum(nums, target)
            self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

        def test_no_solution(self):
            self.assertEqual(four_sum([1, 2, 3, 4], 10), [])

        def test_empty_array(self):
            self.assertEqual(four_sum([], 0), [])

    suite = unittest.TestSuite()
    suite.addTest(TestFourSumFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
