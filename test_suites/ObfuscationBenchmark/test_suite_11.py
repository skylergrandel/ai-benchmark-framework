import unittest

def test(code):
    exec(code, globals())

    class TestBinaryToDecimalFunction(unittest.TestCase):
        def test_simple_binary(self):
            self.assertEqual(binary_to_decimal('101'), 5)

        def test_complex_binary(self):
            self.assertEqual(binary_to_decimal('11010'), 26)

        def test_zero(self):
            self.assertEqual(binary_to_decimal('0'), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestBinaryToDecimalFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
