def test(code):
    local_vars = {}
    exec(code, globals(), local_vars)
    third_max = local_vars['third_max']

    # Test cases
    tests = [
        ([2, 2, 3, 1], 1),
        ([1, 2], 2),
        ([-1, -2, -3, -4], -2),
        ([3, 3, 4, 3, 4, 4, 5, 5], 4),
        ([2], 2),
        ([1, 2, 2, 5], 1)
    ]

    passed_all_tests = 1
    for i, (nums, expected) in enumerate(tests):
        result = third_max(nums)
        if result != expected:
            passed_all_tests = 0
            print(f"Test case {i+1} failed: third_max({nums}) = {result}, expected {expected}")
            break

    return passed_all_tests
