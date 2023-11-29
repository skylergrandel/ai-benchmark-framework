import unittest

def test(code):
    exec(code, globals())

    class TestOddOccurrencesFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(sorted(odd_occurrences([20, 15, 20, 16, 15, 15, 16])), [15, 15])

        def test_no_odd_occurrences(self):
            self.assertEqual(odd_occurrences([10, 10, 20, 20]), [])

        def test_single_element(self):
            self.assertEqual(odd_occurrences([7]), [7])

    suite = unittest.TestSuite()
    suite.addTest(TestOddOccurrencesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
