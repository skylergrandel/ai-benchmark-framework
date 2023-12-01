def test(code):
    # Define a function from the provided string code
    local_vars = {}
    exec(code, local_vars)
    remove_vowels = local_vars['remove_vowels']

    # Define test cases as tuples: (input, expected_output)
    test_cases = [
        ('Hello World', 'Hll Wrld'),
        ('AEIOUaeiou', ''),
        ('', '')
    ]

    # Run the test cases
    passed = True
    for input_str, expected_output in test_cases:
        actual_output = remove_vowels(input_str)
        if actual_output != expected_output:
            print(f"Failed for input '{input_str}': Expected '{expected_output}', got '{actual_output}'")
            passed = False

    # Return 1 if all tests passed, 0 otherwise
    return 1 if passed else 0
