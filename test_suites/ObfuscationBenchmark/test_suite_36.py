import unittest

def test(code):
    exec(code, globals())

    class TestRandomizeListFunction(unittest.TestCase):
        def test_regular_list(self):
            original_list = [1, 2, 3, 4, 5]
            randomized_list = randomize_list(original_list.copy())
            self.assertNotEqual(original_list, randomized_list)
            self.assertEqual(sorted(original_list), sorted(randomized_list))

        def test_empty_list(self):
            self.assertEqual(randomize_list([]), [])

        def test_single_element_list(self):
            self.assertEqual(randomize_list([1]), [1])

    suite = unittest.TestSuite()
    suite.addTest(TestRandomizeListFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
