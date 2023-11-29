import unittest

def test(code):
    exec(code, globals())

    class TestFirstNonRepeatingCharFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(first_non_repeating_char('swiss'), 'w')

        def test_all_repeating(self):
            self.assertIsNone(first_non_repeating_char('aabbcc'))

        def test_empty_string(self):
            self.assertIsNone(first_non_repeating_char(''))

    suite = unittest.TestSuite()
    suite.addTest(TestFirstNonRepeatingCharFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
