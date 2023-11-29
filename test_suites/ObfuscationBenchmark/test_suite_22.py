import unittest

def test(code):
    exec(code, globals())

    class TestAverageOfListFunction(unittest.TestCase):
        def test_regular_list(self):
            self.assertEqual(average_of_list([1, 2, 3, 4]), 2.5)

        def test_empty_list(self):
            self.assertEqual(average_of_list([]), 0)

        def test_single_element(self):
            self.assertEqual(average_of_list([10]), 10)

    suite = unittest.TestSuite()
    suite.addTest(TestAverageOfListFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
