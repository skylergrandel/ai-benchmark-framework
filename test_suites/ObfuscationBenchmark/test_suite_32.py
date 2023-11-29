import unittest

def test(code):
    exec(code, globals())

    class TestMostFrequentCharacterFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(most_frequent_character('abracadabra'), 'a')

        def test_all_unique_characters(self):
            self.assertEqual(most_frequent_character('abcdefg'), 'a')

        def test_empty_string(self):
            self.assertEqual(most_frequent_character(''), '')

        def test_tie_case(self):
            self.assertEqual(most_frequent_character('abbccc'), 'b')  # 'b' and 'c' tie, but 'b' appears first

    suite = unittest.TestSuite()
    suite.addTest(TestMostFrequentCharacterFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
