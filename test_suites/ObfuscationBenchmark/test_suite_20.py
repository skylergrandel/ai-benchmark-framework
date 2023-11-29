import unittest

def test(code):
    exec(code, globals())

    class TestRepeatCharactersFunction(unittest.TestCase):
        def test_regular_string(self):
            self.assertEqual(repeat_characters('abc'), 'aabbcc')

        def test_empty_string(self):
            self.assertEqual(repeat_characters(''), '')

        def test_string_with_spaces(self):
            self.assertEqual(repeat_characters('hello world'), 'hheelllloo  wwoorrlldd')

    suite = unittest.TestSuite()
    suite.addTest(TestRepeatCharactersFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
