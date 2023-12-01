def test(code):
    # Execute the provided code string
    local_vars = {}
    exec(code, globals(), local_vars)
    
    # Extract the function from the local variables created by exec
    nth_ugly_number = local_vars.get("nth_ugly_number")
    if not nth_ugly_number:
        # If the function is not defined, return failure code (0)
        return 0
    
    # Test cases dictionary where key is the input and value is the expected output
    test_cases = {
        1: 1,
        10: 12,
        100: 1536,
        # Add more test cases as necessary
    }
    
    # Run all tests
    all_tests_passed = True
    for input_n, expected_output in test_cases.items():
        result = nth_ugly_number(input_n)
        if result != expected_output:
            all_tests_passed = False
            break  # A single failure means the entire test suite fails
    
    # Return result code: 1 for success, 0 for failure
    return 1 if all_tests_passed else 0
