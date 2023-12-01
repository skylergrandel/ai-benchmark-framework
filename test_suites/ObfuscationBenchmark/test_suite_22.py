def test(code):
    # Define a simple helper function to execute tests and catch exceptions
    def execute_test(test_case, expected):
        try:
            result = average_of_list(test_case)
            assert result == expected, f"Expected {expected}, got {result}"
        except Exception as e:
            print(f"Test failed with exception: {e}")
            return False
        return True

    # Execute the provided code which should define the 'average_of_list' function
    exec(code, globals())

    # List of test cases as tuples (input list, expected result)
    test_cases = [
        ([1, 2, 3, 4], 2.5),
        ([], 0), # if the empty list should return 0 by problem's definition
        ([10], 10),
    ]

    # Run the tests
    all_tests_passed = True
    for test_case in test_cases:
        if not execute_test(*test_case):
            all_tests_passed = False
            break

    # Return 1 for success, 0 for failure
    return 1 if all_tests_passed else 0