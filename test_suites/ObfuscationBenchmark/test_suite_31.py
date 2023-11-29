import unittest

def test(code):
    exec(code, globals())

    class TestLongestConsecutiveSequenceFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4)  # Sequence is 1, 2, 3, 4

        def test_no_consecutive_sequence(self):
            self.assertEqual(longest_consecutive_sequence([10, 5, 6, 9]), 2)  # Longest is either 5, 6 or 9, 10

        def test_single_element(self):
            self.assertEqual(longest_consecutive_sequence([7]), 1)

        def test_empty_list(self):
            self.assertEqual(longest_consecutive_sequence([]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestLongestConsecutiveSequenceFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
