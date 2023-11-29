import unittest

def test(code):
    exec(code, globals())

    class TestProductExceptSelfFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])  # Product of all except self

        def test_single_element(self):
            self.assertEqual(product_except_self([5]), [1])

        def test_empty_list(self):
            self.assertEqual(product_except_self([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestProductExceptSelfFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
