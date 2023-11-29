import unittest

def test(code):
    exec(code, globals())

    class TestMultiplyBinaryFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(multiply_binary('1010', '1011'), '1101110')

        def test_single_digit(self):
            self.assertEqual(multiply_binary('1', '0'), '0')

        def test_different_lengths(self):
            self.assertEqual(multiply_binary('11', '1'), '11')

    suite = unittest.TestSuite()
    suite.addTest(TestMultiplyBinaryFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
