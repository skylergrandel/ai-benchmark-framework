def test(solution_code):
    # Define a function within this scope to execute the passed code
    def custom_sort(nums):
        exec(solution_code)
        return locals()['custom_sort'](nums)

    # Define the test cases
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
        ([], []),
        ([7], [7])
    ]

    # Run test cases
    for input_list, expected in test_cases:
        if custom_sort(input_list) != expected:
            return 0

    # If all tests passed
    return 1
