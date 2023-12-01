def test(code):
    # Execute the solution code within the global scope.
    exec(code, globals())
    
    # Define a list of test cases with inputs and the expected output.
    test_cases = [
        (['apple', 'apply', 'tuple', 'poplar'], 'a?pl?', ['apple', 'apply']),
        (['cat', 'dog', 'bird'], 'f?sh', []),
        (['hello', 'hallo', 'hxllo'], 'hello', ['hello']),
    ]
    
    # Run each test case.
    for strings, pattern, expected in test_cases:
        # Call the match_pattern function with the current test case input.
        result = match_pattern(strings, pattern)
        # Check if the result matches the expected output.
        if sorted(result) != sorted(expected):
            # If any test case fails, return 0.
            return 0
    
    # If all test cases pass, return 1.
    return 1
