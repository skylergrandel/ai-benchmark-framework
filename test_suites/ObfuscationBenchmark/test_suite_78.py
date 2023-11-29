import unittest

def test(code):
    exec(code, globals())

    class TestMatchPatternFunction(unittest.TestCase):
        def test_regular_case(self):
            strings = ['apple', 'apply', 'tuple', 'poplar']
            pattern = 'a?pl?'
            self.assertEqual(sorted(match_pattern(strings, pattern)), ['apple', 'apply'])

        def test_no_match(self):
            self.assertEqual(match_pattern(['cat', 'dog', 'bird'], 'f?sh'), [])

        def test_exact_match(self):
            self.assertEqual(match_pattern(['hello', 'hallo', 'hxllo'], 'hello'), ['hello'])

    suite = unittest.TestSuite()
    suite.addTest(TestMatchPatternFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
