import unittest

def test(code):
    exec(code, globals())

    class TestCanJumpToEndFunction(unittest.TestCase):
        def test_possible_to_reach_end(self):
            self.assertTrue(can_jump_to_end([2, 3, 1, 1, 4]))

        def test_impossible_to_reach_end(self):
            self.assertFalse(can_jump_to_end([3, 2, 1, 0, 4]))

        def test_single_element(self):
            self.assertTrue(can_jump_to_end([0]))

    suite = unittest.TestSuite()
    suite.addTest(TestCanJumpToEndFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
