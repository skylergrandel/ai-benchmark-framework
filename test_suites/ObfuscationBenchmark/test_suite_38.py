def test(code):
    # Define the global scope where the executed code can define the function
    global_scope = {}
    
    # Execute the code to define the function in the global_scope
    exec(code, global_scope)
    
    # Retrieve the function from the scope
    shift_characters = global_scope.get('shift_characters')
    
    # If the function does not exist, the test has failed
    if not shift_characters or not callable(shift_characters):
        return 0
    
    # Define a series of test cases as tuples of input and expected output
    test_cases = [
        ('abcd', 'bcde'),
        ('xyz', 'yza'),
        ('', ''),
        ('Hello', 'Ifmmp'),
    ]
    
    # Check each test case
    for input_string, expected_output in test_cases:
        # Obtain the actual output from the function
        try:
            result = shift_characters(input_string)
        except Exception as e:
            print(f"Test failed with input: {input_string}. Exception occurred: {e}")
            return 0
        
        # Check if the actual output matches the expected output
        if result != expected_output:
            print(f"Test failed with input: {input_string}. Expected: {expected_output}, but got: {result}")
            return 0
    
    # If all tests pass, return 1
    return 1
