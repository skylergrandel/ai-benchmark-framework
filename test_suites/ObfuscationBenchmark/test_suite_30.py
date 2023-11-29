import unittest

def test(code):
    exec(code, globals())

    class TestCapitalizeWordsFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(capitalize_words('hello world'), 'Hello World')

        def test_mixed_case_string(self):
            self.assertEqual(capitalize_words('hELLo wORld'), 'Hello World')

        def test_single_word(self):
            self.assertEqual(capitalize_words('python'), 'Python')

        def test_empty_string(self):
            self.assertEqual(capitalize_words(''), '')

    suite = unittest.TestSuite()
    suite.addTest(TestCapitalizeWordsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
