import unittest

def test(code):
    exec(code, globals())

    class TestBubbleSortFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])

        def test_already_sorted(self):
            self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

        def test_empty_list(self):
            self.assertEqual(bubble_sort([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestBubbleSortFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
