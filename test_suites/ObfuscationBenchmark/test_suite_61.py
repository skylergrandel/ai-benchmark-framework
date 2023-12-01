def test(solution_code):
    # Execute the solution code within the global context
    # This defines the function add_binary() to be used later
    exec(solution_code, globals())
    
    # Define test cases as a list of tuples:
    # (input_a, input_b, expected_result)
    test_cases = [
        ('1010', '1011', '10101'),
        ('1', '0', '1'),
        ('11', '1', '100'),
    ]
    
    # Initialize a variable to keep track of the test results
    all_tests_pass = True
    
    # Run each test case
    for a, b, expected in test_cases:
        try:
            # Call the add_binary function and assert the result
            result = add_binary(a, b)
            if result != expected:
                print(f"Test failed: add_binary('{a}', '{b}') returned '{result}' instead of '{expected}'")
                all_tests_pass = False
        except Exception as e:
            # If an exception occurs, print it out and mark the test as failed
            print(f"Test raised an exception: {e}")
            all_tests_pass = False

    # Return 1 if all tests pass, 0 otherwise
    return 1 if all_tests_pass else 0