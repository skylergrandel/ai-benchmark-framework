import unittest

def test(code):
    exec(code, globals())

    class TestMaxDifferenceFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(max_difference([2, 3, 10, 6, 4, 8, 1]), 8)

        def test_no_difference(self):
            self.assertEqual(max_difference([7, 7, 7, 7]), 0)

        def test_empty_array(self):
            self.assertEqual(max_difference([]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestMaxDifferenceFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
