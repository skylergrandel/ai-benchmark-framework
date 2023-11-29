import unittest

def test(code):
    exec(code, globals())

    class TestTrapRainWaterFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

        def test_flat_surface(self):
            self.assertEqual(trap_rain_water([1, 1, 1, 1]), 0)

        def test_increasing_heights(self):
            self.assertEqual(trap_rain_water([1, 2, 3, 4]), 0)

    suite = unittest.TestSuite()
    suite.addTest(TestTrapRainWaterFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
