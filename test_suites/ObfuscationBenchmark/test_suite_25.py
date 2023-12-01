def test(code):
    # Define a helper function to dynamically execute the code and define the climb_stairs function in the local scope
    local_vars = {}
    exec(code, globals(), local_vars)
    climb_stairs = local_vars['climb_stairs']

    # Define a list of test cases (input, expected output)
    test_cases = [
        (3, 3),  # 1+1+1, 1+2, 2+1
        (5, 8),  # Different ways to climb 5 stairs
        # Add more test cases if necessary
    ]

    # Run each test case
    for n, expected in test_cases:
        # Compute the actual result
        result = climb_stairs(n)
        # Compare it with the expected result
        if result != expected:
            # If any test fails, return 0
            return 0

    # If all tests passed, return 1
    return 1

