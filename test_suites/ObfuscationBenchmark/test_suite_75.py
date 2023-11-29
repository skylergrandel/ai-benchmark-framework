import unittest

def test(code):
    exec(code, globals())

    class TestProductExceptMaxFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(product_except_max([1, 2, 3, 4]), 6)  # 1 * 2 * 3

        def test_with_duplicates_of_max(self):
            self.assertEqual(product_except_max([3, 3, 3, 1]), 1)  # 1

        def test_single_element(self):
            self.assertEqual(product_except_max([5]), 5)

    suite = unittest.TestSuite()
    suite.addTest(TestProductExceptMaxFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
