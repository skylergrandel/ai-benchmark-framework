import unittest

def test(code):
    exec(code, globals())

    class TestDigitalRootFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(digital_root(942), 6)  # 9 + 4 + 2 = 15, then 1 + 5 = 6

        def test_single_digit(self):
            self.assertEqual(digital_root(5), 5)

        def test_large_number(self):
            self.assertEqual(digital_root(132189), 6)

    suite = unittest.TestSuite()
    suite.addTest(TestDigitalRootFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
