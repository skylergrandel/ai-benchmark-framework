import unittest

def test(code):
    exec(code, globals())

    class TestAddBinaryFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(add_binary('1010', '1011'), '10101')

        def test_single_digit(self):
            self.assertEqual(add_binary('1', '0'), '1')

        def test_different_lengths(self):
            self.assertEqual(add_binary('11', '1'), '100')

    suite = unittest.TestSuite()
    suite.addTest(TestAddBinaryFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
