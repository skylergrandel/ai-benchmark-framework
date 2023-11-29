import unittest

def test(code):
    exec(code, globals())

    class TestShiftCharactersVowelsAndConsonantsFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(shift_characters_vowels_and_consonants('hello'), 'jinnp')

        def test_string_with_all_vowels(self):
            self.assertEqual(shift_characters_vowels_and_consonants('aeiou'), 'eioua')

        def test_string_with_all_consonants(self):
            self.assertEqual(shift_characters_vowels_and_consonants('bcdfg'), 'cdehi')

    suite = unittest.TestSuite()
    suite.addTest(TestShiftCharactersVowelsAndConsonantsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
