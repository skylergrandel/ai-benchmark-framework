import unittest

def test(code):
    exec(code, globals())

    class TestFilterEvenNumbersFunction(unittest.TestCase):
        def test_mixed_list(self):
            self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])

        def test_all_even(self):
            self.assertEqual(filter_even_numbers([2, 4, 6]), [2, 4, 6])

        def test_no_even(self):
            self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestFilterEvenNumbersFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
