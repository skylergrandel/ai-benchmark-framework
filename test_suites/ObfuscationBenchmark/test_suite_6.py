import unittest

def test(code):
    exec(code, globals())

    class TestRomanToIntFunction(unittest.TestCase):
        def test_single_digit(self):
            self.assertEqual(roman_to_int('I'), 1)

        def test_complex_numeral(self):
            self.assertEqual(roman_to_int('MMXVII'), 2017)

        def test_invalid_input(self):
            self.assertEqual(roman_to_int('MMMM'), 4000)  # Assuming handling for invalid cases

    suite = unittest.TestSuite()
    suite.addTest(TestRomanToIntFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
