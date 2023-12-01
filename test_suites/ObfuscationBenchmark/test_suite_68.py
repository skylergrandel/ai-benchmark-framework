def test(code):
    # Execute the code to define the max_sum_non_adjacent function
    exec(code, globals())

    # Helper function to run an individual test case
    def run_test_case(test_input, expected_result):
        try:
            result = max_sum_non_adjacent(test_input)
            return result == expected_result
        except:
            # If there is an exception, the test case fails
            return False

    # Set up test cases
    test_cases = [
        ([3, 2, 7, 10], 13),
        ([-1, -2, -3], -1),
        ([], 0),
    ]

    # Run tests
    all_tests_passed = all(run_test_case(test_input, expected_result) for test_input, expected_result in test_cases)

    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_passed else 0