import unittest

def test(code):
    exec(code, globals())

    class TestLetterCombinationsFunction(unittest.TestCase):
        def test_regular_case(self):
            expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
            self.assertEqual(sorted(letter_combinations('23')), sorted(expected))

        def test_empty_string(self):
            self.assertEqual(letter_combinations(''), [])

        def test_single_digit(self):
            expected = ['w', 'x', 'y', 'z']
            self.assertEqual(sorted(letter_combinations('9')), sorted(expected))

    suite = unittest.TestSuite()
    suite.addTest(TestLetterCombinationsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
