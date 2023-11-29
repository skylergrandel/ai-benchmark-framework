import unittest

def test(code):
    exec(code, globals())

    class TestLookAndSayFunction(unittest.TestCase):
        def test_initial_numbers(self):
            self.assertEqual(look_and_say(1), '1')
            self.assertEqual(look_and_say(2), '11')
            self.assertEqual(look_and_say(3), '21')
            self.assertEqual(look_and_say(4), '1211')
            self.assertEqual(look_and_say(5), '111221')

        def test_higher_number(self):
            # Testing for a higher number in the sequence for correctness
            self.assertEqual(look_and_say(6), '312211')

    suite = unittest.TestSuite()
    suite.addTest(TestLookAndSayFunction())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
