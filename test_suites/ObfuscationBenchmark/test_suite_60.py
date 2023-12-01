'''
def sum_of_others(nums):
    return [sum(nums) - num for num in nums]
'''

def test(solution_code):
    # Define context where solution_code will be executed
    local_context = {}
    exec(solution_code, globals(), local_context)
    # Retrieve the solution function from the local_context
    sum_of_others_solution = local_context['sum_of_others']

    # Flag to track whether the tests passed
    all_tests_passed = True

    # Helper function to assert the equality
    def assert_equal(actual, expected):
        return actual == expected

    # Test cases
    test_cases = [
        ([1, 2, 3], [5, 4, 3]),
        ([7], [0]),
        ([], [])
    ]

    for input_data, expected_output in test_cases:
        # Compare expected output to the output from sum_of_others_solution
        if not assert_equal(sum_of_others_solution(input_data), expected_output):
            all_tests_passed = False
            print(f"Test failed: input {input_data} expected {expected_output} got {sum_of_others_solution(input_data)}")
            break  # Exit early as one test failed

    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_passed else 0
