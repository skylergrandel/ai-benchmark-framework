import unittest

def test(code):
    exec(code, globals())

    class TestMaxProductFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(max_product([10, 3, 5, 6, 2]), 60)  # 10 * 6

        def test_negative_numbers(self):
            self.assertEqual(max_product([-1, -3, -5, 2, 4]), 20)  # -5 * -4

        def test_single_element(self):
            with self.assertRaises(ValueError):
                max_product([5])

    suite = unittest.TestSuite()
    suite.addTest(TestMaxProductFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
