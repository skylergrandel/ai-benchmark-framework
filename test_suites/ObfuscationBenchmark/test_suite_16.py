import unittest

def test(code):
    exec(code, globals())

    class TestIntToBinaryFunction(unittest.TestCase):
        def test_regular_number(self):
            self.assertEqual(int_to_binary(5), '101')

        def test_zero(self):
            self.assertEqual(int_to_binary(0), '0')

        def test_large_number(self):
            self.assertEqual(int_to_binary(1023), '1111111111')

    suite = unittest.TestSuite()
    suite.addTest(TestIntToBinaryFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
