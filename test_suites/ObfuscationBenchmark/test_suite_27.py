import unittest

def test(code):
    exec(code, globals())

    class TestProductExceptSelfFunction(unittest.TestCase):
        def test_regular_list(self):
            self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

        def test_list_with_zero(self):
            self.assertEqual(product_except_self([0, 1, 2, 3, 4]), [24, 0, 0, 0, 0])

        def test_list_with_one_element(self):
            self.assertEqual(product_except_self([5]), [1])

    suite = unittest.TestSuite()
    suite.addTest(TestProductExceptSelfFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
