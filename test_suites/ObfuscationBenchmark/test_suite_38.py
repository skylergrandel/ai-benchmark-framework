import unittest

def test(code):
    exec(code, globals())

    class TestShiftCharactersFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(shift_characters('abcd'), 'bcde')
            self.assertEqual(shift_characters('xyz'), 'yza')

        def test_empty_string(self):
            self.assertEqual(shift_characters(''), '')

        def test_string_with_uppercase(self):
            self.assertEqual(shift_characters('Hello'), 'Ifmmp')  # Assuming case sensitivity

    suite = unittest.TestSuite()
    suite.addTest(TestShiftCharactersFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
