import unittest

def test(code):
    exec(code, globals())

    class TestLongestConsecutiveCharFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(longest_consecutive_char('aabbbccccddd'), 4)  # 'cccc'

        def test_single_character(self):
            self.assertEqual(longest_consecutive_char('a'), 1)

        def test_alternating_characters(self):
            self.assertEqual(longest_consecutive_char('ababab'), 1)

        def test_empty_string(self):
            self.assertEqual(longest_consecutive_char(''), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestLongestConsecutiveCharFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
