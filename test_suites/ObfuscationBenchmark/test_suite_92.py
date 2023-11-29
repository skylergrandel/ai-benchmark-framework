import unittest

def test(code):
    exec(code, globals())

    class TestMostFrequentWordFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(most_frequent_word('the cat chased the rat and the cat escaped'), 'the')

        def test_tie_case(self):
            self.assertEqual(most_frequent_word('red blue green red blue'), 'red')

        def test_single_word(self):
            self.assertEqual(most_frequent_word('hello'), 'hello')

    suite = unittest.TestSuite()
    suite.addTest(TestMostFrequentWordFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
