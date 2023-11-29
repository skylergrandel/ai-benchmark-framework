import unittest

def test(code):
    exec(code, globals())

    class TestLongestConsecutiveFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)  # Sequence is 1, 2, 3, 4

        def test_with_duplicates(self):
            self.assertEqual(longest_consecutive([1, 2, 2, 3]), 3)

        def test_empty_array(self):
            self.assertEqual(longest_consecutive([]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestLongestConsecutiveFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
