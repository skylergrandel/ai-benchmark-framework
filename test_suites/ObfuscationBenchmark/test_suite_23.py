import unittest

def test(code):
    exec(code, globals())

    class TestLongestNonRepeatingSubstringFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(longest_non_repeating_substring('abcabcbb'), 'abc')

        def test_no_repetition(self):
            self.assertEqual(longest_non_repeating_substring('abcdef'), 'abcdef')

        def test_empty_string(self):
            self.assertEqual(longest_non_repeating_substring(''), '')

        def test_repeating_characters(self):
            self.assertEqual(longest_non_repeating_substring('bbbbb'), 'b')

    suite = unittest.TestSuite()
    suite.addTest(TestLongestNonRepeatingSubstringFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
