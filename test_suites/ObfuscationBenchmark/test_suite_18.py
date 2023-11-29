import unittest

def test(code):
    exec(code, globals())

    class TestIsPerfectSquareFunction(unittest.TestCase):
        def test_perfect_square(self):
            self.assertTrue(is_perfect_square(16))

        def test_non_perfect_square(self):
            self.assertFalse(is_perfect_square(14))

        def test_zero(self):
            self.assertTrue(is_perfect_square(0))

        def test_negative_number(self):
            self.assertFalse(is_perfect_square(-4))

    suite = unittest.TestSuite()
    suite.addTest(TestIsPerfectSquareFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
