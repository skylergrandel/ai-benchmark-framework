def test(code):
    # Create a local scope and execute the code in it
    local_scope = {}
    exec(code, local_scope)

    # Define the test cases: input data and expected output
    test_cases = [
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([2], [-1]),
        ([], [])
    ]

    # Try to find 'replace_with_greatest_on_right' in the local scope
    if 'replace_with_greatest_on_right' not in local_scope:
        print("Function 'replace_with_greatest_on_right' is not defined.")
        return 0

    # Run each test case
    for nums, expected in test_cases:
        try:
            # Call the function with the current test case input
            result = local_scope['replace_with_greatest_on_right'](nums.copy())
        except Exception as e:
            # If an exception is raised, the test fails
            print(f"Test with input {nums} raised an exception: {e}")
            return 0
        if result != expected:
            # If the output is not as expected, print an error message and return 0
            print(f"Test failed with input {nums}. Expected {expected}, but got {result}.")
            return 0
    
    # If all tests pass, return 1
    return 1
