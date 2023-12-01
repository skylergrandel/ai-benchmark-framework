def test(solution_code):
    # Execute the given solution code string
    local_vars = {}
    exec(solution_code, local_vars)

    # Retrieve the max_product function from local variables
    max_product = local_vars.get('max_product')
    if not max_product:
        print("No max_product function found.")
        return 0

    # Define a simple test case wrapper
    def run_test_case(case, expected, error=False):
        try:
            result = max_product(case)
            if error:
                print(f"Expected an error for input {case}, but got result {result}")
                return False
            return result == expected
        except ValueError as e:
            if error:
                return True
            else:
                print(f"Unexpected exception for input {case}: {e}")
                return False
        except Exception as e:
            print(f"Unexpected exception for input {case}: {e}")
            return False

    # Test cases
    test_cases = [
        ([10, 3, 5, 6, 2], 60),
        ([-1, -3, -5, 2, 4], 20),
    ]
    
    error_cases = [
        ([], ValueError),
        ([5], ValueError),
    ]

    # Run regular test cases
    for case, expected in test_cases:
        if not run_test_case(case, expected):
            print(f"Test failed for input {case} with expected output {expected}")
            return 0

    # Run error test cases
    for case, exc in error_cases:
        if not run_test_case(case, None, error=True):
            print(f"Test failed - expected an exception for input {case}, but it did not occur.")
            return 0

    # If all tests pass
    print("All tests passed.")
    return 1
