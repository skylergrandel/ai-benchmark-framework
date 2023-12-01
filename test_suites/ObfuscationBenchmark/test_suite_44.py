def test(code):
    # Execute the code solution provided as a string
    exec(code, globals())

    # Test cases to check the majority_element function
    test_cases = [
        ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4),
        ([1], 1),
        ([2, 2, 2], 2),
    ]

    # Variable to keep track of test results
    all_tests_passed = True

    # Loop through the test cases and check the function's answer
    for input_list, expected_output in test_cases:
        # Call the provided majority_element function with the current test case input
        actual_output = majority_element(input_list)

        # Check if the actual_output matches the expected_output
        if actual_output != expected_output:
            # If there is a mismatch, set the variable to False and break the loop
            all_tests_passed = False
            break

    # Return 1 if all tests passed, otherwise return 0
    return 1 if all_tests_passed else 0
