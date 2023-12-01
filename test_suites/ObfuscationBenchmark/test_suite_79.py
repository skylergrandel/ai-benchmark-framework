def test(solution_code):
    # Define a success flag to keep track of whether all tests pass
    success = True
    
    # Execute solution code in the global environment
    global_env = {}
    local_env = {}
    exec(solution_code, global_env, local_env)
    
    # Retrieve the testable function from the local environment
    three_sum_exists = local_env.get("three_sum_exists")
    
    # Helper function to run individual tests
    def run_test(test_case, expected):
        nonlocal success
        result = three_sum_exists(*test_case)
        if result != expected:
            print(f"Test failed for input {test_case}: expected {expected}, got {result}")
            success = False
    
    # Test Cases
    test_cases = [
        (([1, 2, 3, 4, 5], 9), True),   # Regular case, 1 + 3 + 5 = 9
        (([1, 2, 4, 8], 6), False),     # No solution case
        (([-1, -2, -3, -4, 0], -6), True)   # Negative numbers, -1 + -2 + -3 = -6
    ]
    
    # Run all tests
    for test_case, expected in test_cases:
        run_test(test_case, expected)
    
    # Return 1 if all tests passed, 0 otherwise
    return 1 if success else 0
