def test(code):
    # Define the local scope where the code will be executed
    local_scope = {}

    # Execute the provided code string in the local scope
    exec(code, local_scope)
    
    # Assert helper function, it checks if the condition is True.
    # If not, it returns 0 indicating a test failure.
    def assert_equal(actual, expected):
        return actual == expected

    # Define test cases as tuples of parameters and the expected result
    test_cases = [
        ((12, 8), 4),
        ((13, 7), 1),
        ((0, 5), 5),
        ((14, 28), 14),
        ((10, 0), 10),
    ]

    # Loop over the test cases and test each one
    for params, expected in test_cases:
        # Call the gcd function from the local scope with the parameters
        result = local_scope['gcd'](*params)
        # If the result doesn't match the expected output, return 0
        if not assert_equal(result, expected):
            return 0

    # If all tests pass, return 1
    return 1
