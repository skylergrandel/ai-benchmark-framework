import unittest

def test(code):
    exec(code, globals())

    class TestThreeSumExistsFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertTrue(three_sum_exists([1, 2, 3, 4, 5], 9))  # 1 + 3 + 5 = 9

        def test_no_solution(self):
            self.assertFalse(three_sum_exists([1, 2, 4, 8], 6))

        def test_negative_numbers(self):
            self.assertTrue(three_sum_exists([-1, -2, -3, -4, 0], -6))

    suite = unittest.TestSuite()
    suite.addTest(TestThreeSumExistsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
