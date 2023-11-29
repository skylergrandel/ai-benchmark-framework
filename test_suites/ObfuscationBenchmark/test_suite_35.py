import unittest

def test(code):
    exec(code, globals())

    class TestHasDuplicatesFunction(unittest.TestCase):
        def test_with_duplicates(self):
            self.assertTrue(has_duplicates('programming'))

        def test_no_duplicates(self):
            self.assertFalse(has_duplicates('python'))

        def test_empty_string(self):
            self.assertFalse(has_duplicates(''))

    suite = unittest.TestSuite()
    suite.addTest(TestHasDuplicatesFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
