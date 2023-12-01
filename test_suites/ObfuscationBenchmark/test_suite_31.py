def test(solution_code):
    # Define a dictionary to serve as local namespace for exec.
    local_vars = {}
    # Execute the solution code within the local namespace.
    exec(solution_code, globals(), local_vars)

    # Retrieve the function from the local namespace after execution.
    longest_consecutive_sequence = local_vars.get('longest_consecutive_sequence')

    # Define the test cases.
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),  # Sequence is 1, 2, 3, 4
        ([10, 5, 6, 9], 2),           # Longest is either 5, 6 or 9, 10
        ([7], 1),                     # Single element.
        ([], 0)                       # Empty list.
    ]

    # Perform the tests.
    all_tests_passed = True
    for numbers, expected in test_cases:
        # Check if the function is present.
        if not callable(longest_consecutive_sequence):
            all_tests_passed = False
            break

        result = longest_consecutive_sequence(numbers)
        if result != expected:
            # If a result doesn't match the expected output, fail the test.
            all_tests_passed = False
            break

    # Return 1 if all tests pass, 0 otherwise.
    return 1 if all_tests_passed else 0
