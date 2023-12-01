def test(code):
    # Define a local dictionary to capture the exec environment after executing the code
    local_env = {}
    exec(code, globals(), local_env)
    
    # Retrieve the function from the local environment
    binary_to_decimal = local_env.get("binary_to_decimal")
    
    # Check if the function is correctly defined
    if not binary_to_decimal or not callable(binary_to_decimal):
        print("The provided code does not define the required 'binary_to_decimal' function.")
        return 0

    # Define the test cases as tuples of (input, expected output)
    test_cases = [
        ('101', 5),
        ('11010', 26),
        ('0', 0),
        ('1', 1),
        ('1111', 15),
        ('100000', 32),
        ('11111111', 255)
    ]

    # Run the test cases
    try:
        for binary_str, expected in test_cases:
            # Run the provided function and assert its output
            result = binary_to_decimal(binary_str)
            assert result == expected, f"Test failed for input {binary_str}: Expected {expected}, got {result}."
    except AssertionError as e:
        # If an assertion fails, print the error message and return 0
        print(e)
        return 0
    
    # If all tests pass, return 1
    return 1