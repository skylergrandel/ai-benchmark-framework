import unittest

def test(code):
    exec(code, globals())

    class TestNextClosestTimeFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(next_closest_time('19:34'), '19:39')

        def test_end_of_day(self):
            self.assertEqual(next_closest_time('23:59'), '22:22')

        def test_single_digit_repeated(self):
            self.assertEqual(next_closest_time('11:11'), '11:11')

    suite = unittest.TestSuite()
    suite.addTest(TestNextClosestTimeFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
