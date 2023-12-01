def test(solution_code):
    # First, define the filter_even_numbers function from the input string
    local_vars = {}
    exec(solution_code, globals(), local_vars)
    filter_even_numbers = local_vars['filter_even_numbers']

    # Define test cases as a list of tuples (input, expected_output)
    test_cases = [
        ([1, 2, 3, 4], [2, 4]),
        ([2, 4, 6], [2, 4, 6]),
        ([1, 3, 5], []),
        ([], []),
        ([0, -2, -3, -4], [0, -2, -4]),
    ]

    # Run test cases
    for input_list, expected_output in test_cases:
        result = filter_even_numbers(input_list)
        if result != expected_output:
            return 0  # Test failed

    return 1  # All tests passed

