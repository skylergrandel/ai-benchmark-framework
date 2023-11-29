import unittest

def test(code):
    exec(code, globals())

    class TestSumOfListFunction(unittest.TestCase):
        def test_regular_list(self):
            self.assertEqual(sum_of_list([1, 2, 3, 4]), 10)

        def test_empty_list(self):
            self.assertEqual(sum_of_list([]), 0)

        def test_single_element(self):
            self.assertEqual(sum_of_list([5]), 5)

    suite = unittest.TestSuite()
    suite.addTest(TestSumOfListFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
