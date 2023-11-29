import unittest

def test(code):
    exec(code, globals())

    class TestClimbStairsFunction(unittest.TestCase):
        def test_small_n(self):
            self.assertEqual(climb_stairs(3), 3)  # 1+1+1, 1+2, 2+1

        def test_larger_n(self):
            self.assertEqual(climb_stairs(5), 8)  # Different ways to climb 5 stairs

    suite = unittest.TestSuite()
    suite.addTest(TestClimbStairsFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
