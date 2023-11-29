import unittest

def test(code):
    exec(code, globals())

    class TestLongestSubstringWithoutRepeatingFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(longest_substring_without_repeating('abcabcbb'), 3)  # 'abc'

        def test_one_char_repeating(self):
            self.assertEqual(longest_substring_without_repeating('bbbbb'), 1)  # 'b'

        def test_empty_string(self):
            self.assertEqual(longest_substring_without_repeating(''), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestLongestSubstringWithoutRepeatingFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
