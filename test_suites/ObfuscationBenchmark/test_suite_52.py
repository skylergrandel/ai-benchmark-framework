import unittest

def test(code):
    exec(code, globals())

    class TestCountUniqueBSTsFunction(unittest.TestCase):
        def test_small_n(self):
            self.assertEqual(count_unique_bsts(3), 5)  # There are 5 unique BSTs for n=3

        def test_n_is_1(self):
            self.assertEqual(count_unique_bsts(1), 1)

        def test_n_is_0(self):
            self.assertEqual(count_unique_bsts(0), 1)  # Empty tree is counted as 1

    suite = unittest.TestSuite()
    suite.addTest(TestCountUniqueBSTsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
