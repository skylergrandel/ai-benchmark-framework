def test(code):
    exec(code, globals())  # Execute the provided solution code to define rearrange_odd_even

    # Test cases with expected results
    test_cases = [
        ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]),
        ([1, 3, 5], [1, 3, 5]),
        ([2, 4, 6], [2, 4, 6]),
        ([], [])
    ]
    
    all_tests_passed = True  # Variable to track if all tests are passing

    for nums, expected in test_cases:
        try:
            result = rearrange_odd_even(nums)  # Call the provided rearrange_odd_even function
            # Check if result matches expected output
            if result != expected:
                all_tests_passed = False  # Set to False if any test fails
                print(f"Test Failed: Input {nums} expected {expected} but got {result}")
        except Exception as e:
            all_tests_passed = False  # Set to False if the function raises an exception
            print(f"Test Raised Exception: Input {nums} raised {e}")

    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_passed else 0