def test(solution_code):
    # Define a local scope to execute the solution in
    local_scope = {}
    exec(solution_code, globals(), local_scope)
    longest_non_repeating_substring = local_scope['longest_non_repeating_substring']

    # List of test cases: each tuple contains the input string and the expected output
    test_cases = [
        ('abcabcbb', 'abc'),
        ('abcdef', 'abcdef'),
        ('', ''),
        ('bbbbb', 'b'),
        # Add more test cases if necessary
    ]

    # Iterating through the test cases and applying the function
    for test_input, expected_output in test_cases:
        actual_output = longest_non_repeating_substring(test_input)
        if actual_output != expected_output:
            # If any test fails, return 0
            return 0

    # If all tests pass, return 1
    return 1
