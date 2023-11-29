import unittest

def test(code):
    exec(code, globals())

    class TestIsRotationFunction(unittest.TestCase):
        def test_valid_rotation(self):
            self.assertTrue(is_rotation('abcde', 'deabc'))

        def test_invalid_rotation(self):
            self.assertFalse(is_rotation('abcde', 'edcba'))

        def test_different_lengths(self):
            self.assertFalse(is_rotation('abc', 'abcd'))

        def test_empty_strings(self):
            self.assertTrue(is_rotation('', ''))

    suite = unittest.TestSuite()
    suite.addTest(TestIsRotationFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
