import unittest

def test(code):
    exec(code, globals())

    class TestBinaryNumbersFunction(unittest.TestCase):
        def test_n_is_2(self):
            self.assertEqual(binary_numbers(2), ['00', '01', '10', '11'])

        def test_n_is_3(self):
            expected = ['000', '001', '010', '011', '100', '101', '110', '111']
            self.assertEqual(binary_numbers(3), expected)

        def test_n_is_1(self):
            self.assertEqual(binary_numbers(1), ['0', '1'])

    suite = unittest.TestSuite()
    suite.addTest(TestBinaryNumbersFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
