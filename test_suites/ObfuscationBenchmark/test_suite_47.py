def test(code):
    # Use exec to define the provided solution as a function
    local_vars = {}
    exec(code, globals(), local_vars)
    min_chars_for_palindrome = local_vars.get('min_chars_for_palindrome')

    # Define the test cases as a list of tuples with the format (input, expected_output)
    test_cases = [
        ('abca', 1),
        ('racecar', 0),
        ('', 0),
    ]

    # Run the test cases and check if the function gives the correct output
    for test_input, expected_output in test_cases:
        try:
            actual_output = min_chars_for_palindrome(test_input)
            assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output} for input: {test_input}"
        except AssertionError as e:
            print(f"Test failed: {e}")
            return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    
    # If all test cases pass, return 1
    return 1