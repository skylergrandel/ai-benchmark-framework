import unittest

def test(code):
    exec(code, globals())

    class TestRearrangeOddEvenFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(rearrange_odd_even([1, 2, 3, 4, 5, 6]), [1, 3, 5, 2, 4, 6])

        def test_all_odd(self):
            self.assertEqual(rearrange_odd_even([1, 3, 5]), [1, 3, 5])

        def test_all_even(self):
            self.assertEqual(rearrange_odd_even([2, 4, 6]), [2, 4, 6])

        def test_empty_list(self):
            self.assertEqual(rearrange_odd_even([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestRearrangeOddEvenFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
