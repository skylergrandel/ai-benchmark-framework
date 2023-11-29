import unittest

def test(code):
    # Load the code as a module
    exec(code, globals())

    class TestSquareListFunction(unittest.TestCase):
        def test_empty_list(self):
            self.assertEqual(square_list([]), [])

        def test_single_element(self):
            self.assertEqual(square_list([2]), [4])

        def test_multiple_elements(self):
            self.assertEqual(square_list([1, 2, 3]), [1, 4, 9])

        def test_negative_elements(self):
            self.assertEqual(square_list([-1, -2]), [1, 4])

    suite = unittest.TestSuite()
    suite.addTest(TestSquareListFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
