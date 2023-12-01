def test(code):
    exec(code)

    try:
        # Define test cases
        test_cases = [
            (([2, 7, 11, 15], 9), [0, 1]),
            (([1, 2, 3], 6), None),
            (([1], 1), None),
        ]

        # Run test cases
        for inputs, expected in test_cases:
            nums, target = inputs
            actual = two_sum_indices(nums, target)
            if expected is not None:
                # Check if the actual indices sorted matches the expected ones
                if sorted(actual) != expected:
                    return 0
            else:
                # Check if actual is None when expected is None
                if actual is not None:
                    return 0

    except Exception as e:
        print(f"An error occurred during testing: {e}")
        return 0

    # If all tests pass
    return 1