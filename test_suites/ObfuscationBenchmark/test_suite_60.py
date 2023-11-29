import unittest

def test(code):
    exec(code, globals())

    class TestSumOfOthersFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(sum_of_others([1, 2, 3]), [5, 4, 3])  # 2+3, 1+3, 1+2

        def test_single_element(self):
            self.assertEqual(sum_of_others([7]), [0])

        def test_empty_list(self):
            self.assertEqual(sum_of_others([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestSumOfOthersFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
