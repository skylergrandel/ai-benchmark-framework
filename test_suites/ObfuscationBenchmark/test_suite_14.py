def test(code):
    # Execute the code string to define sum_of_list function in the global scope
    exec(code, globals())

    # Helper function to perform an individual test case.
    def check_case(test_input, expected_output):
        try:
            result = sum_of_list(test_input)
            return result == expected_output
        except:
            # If sum_of_list raises any exception, test fails.
            return False

    # Define the test cases
    test_cases = [
        ([1, 2, 3, 4], 10),  # Regular list
        ([], 0),             # Empty list
        ([5], 5),            # Single element list
    ]

    # Run each test case
    for test_input, expected_output in test_cases:
        if not check_case(test_input, expected_output):
            # If any of the test cases fails, return 0
            return 0

    # If all test cases passed, return 1
    return 1

# Example usage of the test function:
# code_to_test = '''
# def sum_of_list(numbers):
#     return sum(numbers)
# '''
# result = test(code_to_test)
# print(f'Test passed: {bool(result)}')