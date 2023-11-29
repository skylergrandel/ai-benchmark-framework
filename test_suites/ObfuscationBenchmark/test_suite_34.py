import unittest

def test(code):
    exec(code, globals())

    class TestRunningSumFunction(unittest.TestCase):
        def test_regular_array(self):
            self.assertEqual(running_sum([1, 2, 3, 4]), [1, 3, 6, 10])  # 1, 1+2, 1+2+3, 1+2+3+4

        def test_single_element(self):
            self.assertEqual(running_sum([5]), [5])

        def test_empty_array(self):
            self.assertEqual(running_sum([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestRunningSumFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
