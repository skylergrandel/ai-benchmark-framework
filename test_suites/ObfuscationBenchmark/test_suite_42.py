import unittest

def test(code):
    exec(code, globals())

    class TestCustomSortFunction(unittest.TestCase):
        def test_regular_list(self):
            self.assertEqual(custom_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

        def test_empty_list(self):
            self.assertEqual(custom_sort([]), [])

        def test_single_element(self):
            self.assertEqual(custom_sort([7]), [7])

    suite = unittest.TestSuite()
    suite.addTest(TestCustomSortFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
