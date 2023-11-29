import unittest

def test(code):
    exec(code, globals())

    class TestReverseStringKeepWordsOrderFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(reverse_string_keep_words_order('Hello World'), 'olleH dlroW')

        def test_single_word(self):
            self.assertEqual(reverse_string_keep_words_order('Python'), 'nohtyP')

        def test_empty_string(self):
            self.assertEqual(reverse_string_keep_words_order(''), '')

    suite = unittest.TestSuite()
    suite.addTest(TestReverseStringKeepWordsOrderFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
