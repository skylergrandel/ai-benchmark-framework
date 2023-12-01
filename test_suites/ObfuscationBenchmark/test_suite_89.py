def test(code):
    # Define a local function to act as the global count_pairs_with_difference function
    local_variables = {}
    exec(code, local_variables)
    count_pairs_with_difference = local_variables['count_pairs_with_difference']
    
    # Define the test cases as tuples of input arguments and expected output
    test_cases = [
        ([1, 5, 3, 4, 2], 3),  # Regular case: Pairs (1, 3), (3, 5), (2, 4)
        ([1, 7, 11], 0),       # No pairs
        ([], 0),               # Empty list
    ]

    # Run test cases
    for nums, expected in test_cases:
        result = count_pairs_with_difference(nums)
        if result != expected:
            return 0  # Test failed
            
    return 1  # All tests passed
