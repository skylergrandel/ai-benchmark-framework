def test(code):
    exec(code, globals())

    def run_test_case(test_input, expected_output):
        result = product_except_max(test_input)
        return result == expected_output

    # Define test cases as tuples of (input, expected_output)
    test_cases = [
        ([1, 2, 3, 4], 6),            # Regular case
        ([3, 3, 3, 1], 1),            # With duplicates of the max
        ([5], 5),                     # Single element list
        ([], 1),                      # Empty list should return 1 (no elements to multiply)
        ([-1, -2, -3, 0], 0),         # Contains zero
        ([-3, -2, -1], 6),            # All negative values
        ([3, 3, 2, 2], 12),           # Multiple max values not at the beginning/end
    ]

    for test_input, expected_output in test_cases:
        if not run_test_case(test_input, expected_output):
            return 0  # Return 0 if a test has failed
    
    return 1  # Return 1 if all tests have passed
