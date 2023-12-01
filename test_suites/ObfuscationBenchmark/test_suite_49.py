'''
def first_missing_positive(nums):
    # Sample solution for the first_missing_positive function
    if not nums:
        return 1
    nums = [num for num in nums if num > 0]
    nums.sort()
    smallest = 1
    for num in nums:
        if num == smallest:
            smallest += 1
    return smallest
'''

def test(code):
    # Execute the provided code
    exec(code, globals())

    # Define test cases
    test_cases = [
        ([3, 4, -1, 1], 2),
        ([-1, -2, -3], 1),
        ([1, 2, 0], 3),
        ([1, 2, 3], 4),
        ([], 1),
        ([7, 8, 9, 11, 12], 1)
    ]
    
    # Run the test cases
    for nums, expected_output in test_cases:
        try:
            output = first_missing_positive(nums)
            assert output == expected_output, f"Test case first_missing_positive({nums}) failed: expected {expected_output}, got {output}"
        except AssertionError as e:
            print(e)
            return 0

    # All tests passed
    return 1