def test_solution(code):
    # Define a namespace for executing the function
    local_namespace = {}
    try:
        # Execute the given code string
        exec(code, globals(), local_namespace)
        # Retrieve the function after execution
        second_largest = local_namespace.get('second_largest')
        
        if not second_largest:
            # The solution did not define the required function
            print("The provided code does not define 'second_largest'.")
            return 0

        # Test cases to check the second_largest function
        test_cases = [
            ([1, 3, 4, 5], 4),
            ([1, 5, 5, 6, 6], 5),
            ([1, 2, 3, 4, 5], 4),
            ([5, 4, 3, 2, 1], 4)
        ]
        
        # Iterate through all the test cases
        for nums, expected in test_cases:
            # Get the result from the solution's second_largest function
            result = second_largest(nums)
            # Check if the result matches the expected outcome
            if result != expected:
                # Test fails
                print(f"Test failed: Expected second_largest({nums}) to be {expected}, got {result} instead.")
                return 0

        # If all tests pass, return 1
        return 1

    except Exception as e:
        # If any exception is raised during the test execution, report failure
        print(f"An exception occurred while testing the solution: {e}")
        return 0
