import unittest

def test(code):
    exec(code, globals())

    class TestThirdMaxFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(third_max([2, 2, 3, 1]), 1)

        def test_no_third_max(self):
            self.assertEqual(third_max([1, 2]), 2)

        def test_with_negative_numbers(self):
            self.assertEqual(third_max([-1, -2, -3, -4]), -2)

    suite = unittest.TestSuite()
    suite.addTest(TestThirdMaxFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
