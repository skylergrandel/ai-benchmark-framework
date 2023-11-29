import unittest

def test(code):
    # Load the code as a module
    exec(code, globals())

    class TestCountVowelsFunction(unittest.TestCase):
        def test_empty_string(self):
            self.assertEqual(count_vowels(''), 0)

        def test_no_vowels(self):
            self.assertEqual(count_vowels('bcdfg'), 0)

        def test_mixed_case(self):
            self.assertEqual(count_vowels('Apple'), 2)

        def test_consecutive_vowels(self):
            self.assertEqual(count_vowels('queue'), 4)

    suite = unittest.TestSuite()
    suite.addTest(TestCountVowelsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
