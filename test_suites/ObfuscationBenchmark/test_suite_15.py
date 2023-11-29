import unittest

def test(code):
    exec(code, globals())

    class TestReverseStringsFunction(unittest.TestCase):
        def test_regular_strings(self):
            self.assertEqual(reverse_strings(['abc', 'def', 'ghi']), ['cba', 'fed', 'ihg'])

        def test_empty_string(self):
            self.assertEqual(reverse_strings(['', 'abc']), ['', 'cba'])

        def test_single_character_strings(self):
            self.assertEqual(reverse_strings(['a', 'b', 'c']), ['a', 'b', 'c'])

    suite = unittest.TestSuite()
    suite.addTest(TestReverseStringsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
