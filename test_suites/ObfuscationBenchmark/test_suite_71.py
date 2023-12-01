def test(solution):
    try:
        # Compile and execute the code provided in the solution string
        exec(solution, globals())
        
        # Define test cases and expected results
        test_cases = [
            ([2, 3, 10, 6, 4, 8, 1], 8),
            ([7, 7, 7, 7], 0),
            ([], 0),
            ([10, 3, 6, 8, 9, 4, 1], 6),
            ([-3, -2, -1, 0], 3)
        ]
        
        # Test the solution
        for nums, expected in test_cases:
            result = max_difference(nums)
            if result != expected:
                print(f"Test failed for input {nums}: expected {expected}, got {result}")
                return 0
                
        # If all tests passed
        return 1
    except Exception as e:
        # Catch any exceptions that arose while running the tests and report failure
        print(f"An error occurred: {e}")
        return 0
