def test_solution(code):
    # Executing the provided code within a local scope
    local_vars = {}
    exec(code, local_vars)
    first_n_fibonacci = local_vars['first_n_fibonacci']
    
    # Helper function to test
    def check_fibonacci(n, expected):
        try:
            result = first_n_fibonacci(n)
            return result == expected
        except Exception as e:
            print(f"Test failed with exception: {e}")
            return False
    
    # Define a list of test cases as tuples: (input, expected_output)
    test_cases = [
        (5, [0, 1, 1, 2, 3]),
        (1, [0]),
        (0, []),
    ]
    
    # Perform tests
    all_tests_passed = True
    for n, expected in test_cases:
        if not check_fibonacci(n, expected):
            all_tests_passed = False
            print(f"Test failed for n={n}, expected {expected}")
    
    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_passed else 0

