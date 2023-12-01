def test(code):
    # Execute the provided code
    exec(code, globals())

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], [3, 6, 9, 7]),
        ([5], [5]),
        ([], []),
    ]

    # Function to run all test cases
    def run_tests():
        for input_list, expected_output in test_cases:
            # Check if 'sum_with_neighbors' function exists
            if 'sum_with_neighbors' not in globals():
                return 0

            # Run the function and compare the output with the expected output
            result = globals()['sum_with_neighbors'](input_list)
            if result != expected_output:
                return 0

        return 1

    # Run the tests and return the result
    return run_tests()