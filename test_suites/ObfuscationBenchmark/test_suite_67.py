import unittest

def test(code):
    exec(code, globals())

    class TestMinStepsToAnagramFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(min_steps_to_anagram('anagram', 'mangaar'), 0)

        def test_different_lengths(self):
            self.assertEqual(min_steps_to_anagram('friend', 'finder'), 2)

        def test_completely_different(self):
            self.assertEqual(min_steps_to_anagram('hello', 'world'), 4)

    suite = unittest.TestSuite()
    suite.addTest(TestMinStepsToAnagramFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
