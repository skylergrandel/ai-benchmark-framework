import unittest

def test(code):
    exec(code, globals())

    class TestReplaceWithGreatestOnRightFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(replace_with_greatest_on_right([17, 18, 5, 4, 6, 1]), [18, 6, 6, 6, 1, -1])

        def test_single_element(self):
            self.assertEqual(replace_with_greatest_on_right([2]), [-1])

        def test_empty_list(self):
            self.assertEqual(replace_with_greatest_on_right([]), [])

    suite = unittest.TestSuite()
    suite.addTest(TestReplaceWithGreatestOnRightFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
