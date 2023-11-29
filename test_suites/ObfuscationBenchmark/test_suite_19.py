import unittest

def test(code):
    exec(code, globals())

    class TestMaxTripletProductFunction(unittest.TestCase):
        def test_positive_numbers(self):
            self.assertEqual(max_triplet_product([1, 2, 3, 4]), 24)  # 2 * 3 * 4

        def test_including_negative_numbers(self):
            self.assertEqual(max_triplet_product([-10, -10, 1, 3, 2]), 300)  # -10 * -10 * 3

        def test_all_negative_numbers(self):
            self.assertEqual(max_triplet_product([-1, -2, -3, -4]), -6)  # -1 * -2 * -3

    suite = unittest.TestSuite()
    suite.addTest(TestMaxTripletProductFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
