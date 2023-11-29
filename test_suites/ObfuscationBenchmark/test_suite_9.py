import unittest

def test(code):
    exec(code, globals())

    class TestAreAnagramsFunction(unittest.TestCase):
        def test_anagrams(self):
            self.assertTrue(are_anagrams('listen', 'silent'))

        def test_not_anagrams(self):
            self.assertFalse(are_anagrams('hello', 'world'))

        def test_different_lengths(self):
            self.assertFalse(are_anagrams('abc', 'abcd'))

    suite = unittest.TestSuite()
    suite.addTest(TestAreAnagramsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
