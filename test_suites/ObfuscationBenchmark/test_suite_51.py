import unittest

def test(code):
    exec(code, globals())

    class TestWordBreakFunction(unittest.TestCase):
        def test_can_segment(self):
            dictionary = {'apple', 'pen', 'applepen', 'pine', 'pineapple'}
            self.assertTrue(word_break('pineapplepenapple', dictionary))

        def test_cannot_segment(self):
            dictionary = {'cats', 'dog', 'sand', 'and', 'cat'}
            self.assertFalse(word_break('catsandog', dictionary))

    suite = unittest.TestSuite()
    suite.addTest(TestWordBreakFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
