import unittest

def test(code):
    exec(code, globals())

    class TestMergeSortedListsFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

        def test_one_empty_list(self):
            self.assertEqual(merge_sorted_lists([], [1, 2, 3]), [1, 2, 3])

        def test_both_empty_lists(self):
            self.assertEqual(merge_sorted_lists([], []), [])

    suite = unittest.TestSuite()
    suite.addTest(TestMergeSortedListsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
