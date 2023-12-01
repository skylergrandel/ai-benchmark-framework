def test(code):
    # Define the solution function within the local scope of the test function
    exec(code, globals())

    # Define a list of test cases as tuples (input, expected_output)
    test_cases = [
        ('abcabcbb', 3),  # 'abc'
        ('bbbbb', 1),     # 'b'
        ('', 0),
        ('pwwkew', 3),    # 'wke'
        ('abba', 2),      # 'ab'
    ]

    try:
        # Iterate over the test cases and assert the output of the function
        for input_str, expected in test_cases:
            result = longest_substring_without_repeating(input_str)
            assert result == expected, f"Failed test for input: {input_str}, Expected: {expected}, Got: {result}"
    except AssertionError as e:
        # An assertion has failed, return 0 to indicate failure
        print(e)
        return 0

    # All tests have passed, return 1 to indicate success
    return 1
