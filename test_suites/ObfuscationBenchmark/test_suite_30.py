def test(solution_code):
    # Define the capitalize_words function from the solution code
    local_vars = {}
    exec(solution_code, globals(), local_vars)
    capitalize_words = local_vars['capitalize_words']
    
    # List of test cases: each is a tuple (input_string, expected_output)
    test_cases = [
        ('hello world', 'Hello World'),
        ('hELLo wORld', 'Hello World'),
        ('python', 'Python'),
        ('', '')
    ]
    
    # Run each test case
    for input_string, expected_output in test_cases:
        # Check if the result from the solution matches the expected output
        if capitalize_words(input_string) != expected_output:
            # If there is a mismatch, return 0 (indicating a failed test)
            return 0
    
    # If all tests pass, return 1
    return 1
