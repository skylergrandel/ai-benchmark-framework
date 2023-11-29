import unittest

def test(code):
    exec(code, globals())

    class TestReverseListFunction(unittest.TestCase):
        def test_empty_list(self):
            self.assertEqual(reverse_list([]), [])

        def test_single_element(self):
            self.assertEqual(reverse_list([1]), [1])

        def test_multiple_elements(self):
            self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])

    suite = unittest.TestSuite()
    suite.addTest(TestReverseListFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
