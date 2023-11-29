import unittest

def test(code):
    exec(code, globals())

    class TestIsValidNumberFunction(unittest.TestCase):
        def test_valid_number(self):
            self.assertTrue(is_valid_number('10'))
            self.assertTrue(is_valid_number('-10.5'))

        def test_invalid_number(self):
            self.assertFalse(is_valid_number('a10'))
            self.assertFalse(is_valid_number('10a'))

        def test_edge_cases(self):
            self.assertFalse(is_valid_number(''))
            self.assertTrue(is_valid_number('0'))

    suite = unittest.TestSuite()
    suite.addTest(TestIsValidNumberFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
