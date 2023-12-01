def test(code):
    # Define a local dictionary to serve as the namespace for exec()
    local_namespace = {}

    # Load the code as a module
    exec(code, globals(), local_namespace)

    # Helper function to run a test case
    def run_test(input_list, expected_output):
        try:
            # Access the square_list function from the local namespace
            result = local_namespace['square_list'](input_list)
            return result == expected_output
        except Exception as e:
            print(f"Test failed with exception: {e}")
            return False

    # Test cases
    test_cases = [
        ([], []),                # Testing an empty list
        ([2], [4]),              # Testing a single element
        ([1, 2, 3], [1, 4, 9]),  # Testing multiple elements
        ([-1, -2], [1, 4])       # Testing negative elements
    ]

    # Running the test cases
    for input_list, expected_output in test_cases:
        if not run_test(input_list, expected_output):
            return 0  # Test failed

    return 1  # All tests passed
