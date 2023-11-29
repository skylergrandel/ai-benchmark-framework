import unittest

def test(code):
    exec(code, globals())

    class TestMajorityElementFunction(unittest.TestCase):
        def test_regular_case(self):
            self.assertEqual(majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]), 4)

        def test_single_element(self):
            self.assertEqual(majority_element([1]), 1)

        def test_all_same_elements(self):
            self.assertEqual(majority_element([2, 2, 2]), 2)

    suite = unittest.TestSuite()
    suite.addTest(TestMajorityElementFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
