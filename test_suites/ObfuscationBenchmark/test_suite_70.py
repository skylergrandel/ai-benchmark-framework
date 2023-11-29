import unittest

def test(code):
    exec(code, globals())

    class TestMostFrequentStringFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(most_frequent_string(['apple', 'banana', 'apple', 'apple', 'orange']), 'apple')

        def test_tie_case(self):
            self.assertEqual(most_frequent_string(['red', 'green', 'blue', 'red', 'blue']), 'red')

        def test_single_string(self):
            self.assertEqual(most_frequent_string(['only']), 'only')

    suite = unittest.TestSuite()
    suite.addTest(TestMostFrequentStringFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
