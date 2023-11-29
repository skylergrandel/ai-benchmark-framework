import unittest

def test(code):
    exec(code, globals())

    class TestSumWithNeighborsFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(sum_with_neighbors([1, 2, 3, 4]), [3, 6, 9, 7])

        def test_single_element(self):
            self.assertEqual(sum_with_neighbors([5]), [5])

        def test_empty_list(self):
            self.assertEqual(sum_with_neighbors([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestSumWithNeighborsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
