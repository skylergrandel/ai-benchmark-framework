def test(code):
    # Define the local scope for executing the code
    local_scope = {}
    exec(code, globals(), local_scope)

    # Retrieve the function from the local scope
    three_sum_zero = local_scope.get('three_sum_zero')

    # Helper function to compare results
    def are_results_same(actual, expected):
        return sorted(map(sorted, actual)) == sorted(map(sorted, expected))

    # All test cases to be executed
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([1, 2, 3], []),
        ([], []),
    ]

    # Run test cases
    for nums, expected in test_cases:
        try:
            result = three_sum_zero(nums)
            if not are_results_same(result, expected):
                print(f"Test failed: Input {nums} expected {expected} but got {result}")
                return 0  # Test failed
        except Exception as e:
            print(f"An exception occurred during testing: {e}")
            return 0  # Test failed due to exception

    return 1  # All tests passed
