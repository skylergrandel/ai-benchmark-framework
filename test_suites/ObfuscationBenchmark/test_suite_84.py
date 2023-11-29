import unittest

def test(code):
    exec(code, globals())

    class TestCountAbcSequencesFunction(unittest.TestCase):
        def test_contains_sequences(self):
            self.assertEqual(count_abc_sequences('abcabcabc'), 3)

        def test_no_sequences(self):
            self.assertEqual(count_abc_sequences('ababab'), 0)

        def test_intermixed_sequence(self):
            self.assertEqual(count_abc_sequences('aabcbcabcc'), 2)

    suite = unittest.TestSuite()
    suite.addTest(TestCountAbcSequencesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
