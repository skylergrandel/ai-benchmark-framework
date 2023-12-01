def test(code):
    # Define the longest_consecutive function in the global scope by executing the code.
    exec(code, globals())

    # Helper function to check the result of the test case
    def check_test_case(sequence, expected):
        result = longest_consecutive(sequence)
        return result == expected

    # List of test cases, each case is a tuple (input, expected_output)
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),  # Sequence is 1, 2, 3, 4
        ([1, 2, 2, 3], 3),            # With duplicates
        ([], 0),                      # Empty array
        # Add more test cases if needed
    ]

    # Run each test case and collect results
    test_results = [check_test_case(case[0], case[1]) for case in test_cases]

    # Return 1 if all test cases pass, 0 otherwise
    return 1 if all(test_results) else 0
