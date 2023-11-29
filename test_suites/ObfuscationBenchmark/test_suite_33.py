import unittest

def test(code):
    exec(code, globals())

    class TestLongestWordFunction(unittest.TestCase):
        def test_regular_sentence(self):
            self.assertEqual(longest_word('I love programming in Python'), 'programming')

        def test_sentence_with_tie(self):
            self.assertEqual(longest_word('The quick brown fox'), 'quick')  # 'quick' and 'brown' tie, 'quick' is first

        def test_empty_string(self):
            self.assertEqual(longest_word(''), '')

    suite = unittest.TestSuite()
    suite.addTest(TestLongestWordFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
