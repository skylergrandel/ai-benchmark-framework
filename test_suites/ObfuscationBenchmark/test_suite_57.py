import unittest

def test(code):
    exec(code, globals())

    class TestLengthOfLISFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)  # The sequence [2, 3, 7, 101]

        def test_decreasing_sequence(self):
            self.assertEqual(length_of_lis([3, 2, 1]), 1)

        def test_empty_array(self):
            self.assertEqual(length_of_lis([]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestLengthOfLISFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
