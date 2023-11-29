import unittest

def test(code):
    exec(code, globals())

    class TestTwoSumFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(sorted(two_sum([2, 7, 11, 15], 9)), [0, 1])  # 2 + 7 = 9

        def test_case_with_negative_numbers(self):
            self.assertEqual(sorted(two_sum([-1, -2, -3, -4, -5], -8)), [2, 4])  # -3 + -5 = -8

        def test_no_solution(self):
            with self.assertRaises(ValueError):
                two_sum([1, 2, 3], 6)

    suite = unittest.TestSuite()
    suite.addTest(TestTwoSumFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
