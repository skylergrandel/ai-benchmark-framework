def test(solution_code):
    # Define a dictionary to serve as the local namespace for execution
    local_namespace = {}
    
    # Execute the solution code in the local namespace
    exec(solution_code, local_namespace)
    
    # Retrieve the function from the namespace after execution
    int_to_binary = local_namespace.get("int_to_binary")
    
    # Check if the function exists
    if not int_to_binary:
        print("The int_to_binary function is not defined correctly.")
        return 0

    # Define test cases as a list of tuples (input, expected output)
    test_cases = [
        (5, '101'),
        (0, '0'),
        (1023, '1111111111'),
    ]

    # Iterate over test cases and check for correctness
    for case_input, expected_output in test_cases:
        try:
            # Call the int_to_binary function with the test input
            result = int_to_binary(case_input)
            
            # Check if the result matches the expected output
            if result == expected_output:
                continue
            else:
                print(f"Test failed for input {case_input}: Expected {expected_output}, got {result}")
                return 0
        except Exception as e:
            # If an exception occurs while testing, consider the test failed
            print(f"Test failed for input {case_input} with exception: {e}")
            return 0
    
    # If all tests passed, return 1
    return 1
