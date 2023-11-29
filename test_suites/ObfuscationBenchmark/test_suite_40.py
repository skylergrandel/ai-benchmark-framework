import unittest

def test(code):
    exec(code, globals())

    class TestIsValidIPv4Function(unittest.TestCase):
        def test_valid_ipv4(self):
            self.assertTrue(is_valid_ipv4('192.168.1.1'))
            self.assertTrue(is_valid_ipv4('255.255.255.255'))

        def test_invalid_ipv4(self):
            self.assertFalse(is_valid_ipv4('256.256.256.256'))
            self.assertFalse(is_valid_ipv4('192.168.1'))
            self.assertFalse(is_valid_ipv4('192.168.1.1.1'))

        def test_empty_string(self):
            self.assertFalse(is_valid_ipv4(''))

    suite = unittest.TestSuite()
    suite.addTest(TestIsValidIPv4Function())
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return 1 if result.wasSuccessful() else 0
