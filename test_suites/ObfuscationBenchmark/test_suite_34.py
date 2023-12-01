def test(solution_code):
    # Define a local scope to execute the solution code
    local_scope = {}
    
    # Execute the solution code in the local scope
    exec(solution_code, local_scope)
    
    # Retrieve the running_sum function from the local scope
    running_sum = local_scope.get('running_sum')
    
    # Check if running_sum is a callable function
    if not callable(running_sum):
        return 0
    
    # Test cases to validate the running_sum function
    test_cases = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([5], [5]),
        ([], []),
    ]
    
    # Run the test cases
    for nums, expected in test_cases:
        try:
            result = running_sum(nums)
            assert result == expected
        except AssertionError:
            return 0
    
    # If all tests pass, return 1
    return 1
