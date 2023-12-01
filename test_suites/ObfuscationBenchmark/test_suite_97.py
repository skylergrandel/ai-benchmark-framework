'''
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
'''

def test(code):
    # Define local dictionary to execute code within
    local_variables = {}
    exec(code, globals(), local_variables)
    bubble_sort = local_variables['bubble_sort']

    # Test cases to validate that the implementation works correctly
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([], [])
    ]

    # Loop through each test case and check if the result matches expected output
    for input_list, expected_result in test_cases:
        sorted_list = bubble_sort(input_list.copy())  # Make a copy to avoid mutating the original list
        if sorted_list != expected_result:
            return 0  # Return 0 if any of the test cases fail

    return 1  # All test cases passed
