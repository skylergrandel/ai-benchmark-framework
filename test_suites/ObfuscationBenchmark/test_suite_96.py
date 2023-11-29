import unittest

def test(code):
    exec(code, globals())

    class TestSmallerElementsRightFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(smaller_elements_right([5, 2, 6, 1]), [2, 1, 1, 0])

        def test_all_same_elements(self):
            self.assertEqual(smaller_elements_right([4, 4, 4, 4]), [0, 0, 0, 0])

        def test_empty_list(self):
            self.assertEqual(smaller_elements_right([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestSmallerElementsRightFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
