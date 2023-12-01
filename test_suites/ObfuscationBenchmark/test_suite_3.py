def test(code):
    # A dictionary to store the test cases: input -> expected output
    test_cases = {
        '': True,  # Empty string should be a palindrome
        'a': True, # Single character should be a palindrome
        'racecar': True,  # Palindrome word
        'hello': False,   # Not a palindrome word
    }

    # Dynamically execute the code for the passed-in solution
    exec(code, globals())  # This will define 'is_palindrome' function in the global namespace

    # Check if 'is_palindrome' function exists after executing code
    if 'is_palindrome' not in globals():
        print("The solution does not define 'is_palindrome'.")
        return 0

    all_tests_passed = True  # Flag to check if all tests pass

    # Loop over the test cases to verify the output
    for word, expected_result in test_cases.items():
        try:
            result = is_palindrome(word)
        except Exception as e:
            print(f"Running the function 'is_palindrome' raised an exception with input '{word}': {e}")
            all_tests_passed = False
            break  # Stop testing on first failure

        # Verify that the result matches the expected outcome
        if result != expected_result:
            print(f"Test case failed: is_palindrome('{word}') should be {expected_result}, got {result} instead.")
            all_tests_passed = False
            break  # Stop testing on first failure

    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_passed else 0