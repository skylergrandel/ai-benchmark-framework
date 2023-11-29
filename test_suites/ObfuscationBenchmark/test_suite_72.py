import unittest

def test(code):
    exec(code, globals())

    class TestRemoveVowelsFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(remove_vowels('Hello World'), 'Hll Wrld')

        def test_string_with_all_vowels(self):
            self.assertEqual(remove_vowels('AEIOUaeiou'), '')

        def test_empty_string(self):
            self.assertEqual(remove_vowels(''), '')

    suite = unittest.TestSuite()
    suite.addTest(TestRemoveVowelsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
