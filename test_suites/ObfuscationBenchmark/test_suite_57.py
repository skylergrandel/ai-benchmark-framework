def test(solution_code):
    # Inject the solution code into the global namespace
    exec(solution_code, globals())

    # Define test cases
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # The LIS is [2, 3, 7, 101]
        ([3, 2, 1], 1),                      # The LIS is [3] or [2] or [1]
        ([], 0),                             # No elements, no subsequences
        # More test cases can be added here
    ]

    # Run tests
    for nums, expected in test_cases:
        if length_of_lis(nums) != expected:
            return 0 # Test failed

    return 1 # All tests passed
