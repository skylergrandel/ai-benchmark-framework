import unittest

def test(code):
    exec(code, globals())

    class TestSecondLargestFunction(unittest.TestCase):
        def test_regular_list(self):
            self.assertEqual(second_largest([1, 3, 4, 5]), 4)

        def test_list_with_duplicates(self):
            self.assertEqual(second_largest([1, 5, 5, 6, 6]), 5)

        def test_sorted_list(self):
            self.assertEqual(second_largest([1, 2, 3, 4, 5]), 4)

        def test_reverse_sorted_list(self):
            self.assertEqual(second_largest([5, 4, 3, 2, 1]), 4)

    suite = unittest.TestSuite()
    suite.addTest(TestSecondLargestFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
