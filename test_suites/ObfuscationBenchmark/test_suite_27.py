def test(code):
    # Load the code as a module
    exec(code, globals())

    # Helper function to run a test case
    def run_test(input_list, expected_output):
        try:
            result = product_except_self(input_list)
            return result == expected_output
        except Exception as e:
            print(f"Test failed with exception: {e}")
            return False

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),              # Testing a regular list
        ([0, 1, 2, 3, 4], [24, 0, 0, 0, 0]),         # Testing a list with zero
        ([5], [1])                                   # Testing a list with one element
    ]

    # Running the test cases
    for input_list, expected_output in test_cases:
        if not run_test(input_list, expected_output):
            return 0  # Test failed

    return 1  # All tests passed
