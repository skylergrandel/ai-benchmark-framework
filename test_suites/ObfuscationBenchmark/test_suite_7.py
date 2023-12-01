def test(code):
    # Define a dictionary to serve as the local namespace for execution
    local_namespace = {}
    
    # Execute the given code in the local namespace
    exec(code, local_namespace)

    # Get the is_prime function from the local namespace
    is_prime_func = local_namespace.get('is_prime')
    if not is_prime_func:
        print("No is_prime function found.")
        return 0
    
    # Define the test cases
    test_cases = [
        (2, True),
        (7, True),
        (10, False),
        (1, False),
        (13, True),
        (4, False)
        # ... you can add more test cases here
    ]
    
    # Run the test cases
    try:
        for number, expected in test_cases:
            # Check if the output of is_prime matches the expected result
            if is_prime_func(number) != expected:
                print(f"Test case failed for: is_prime({number})")
                return 0
        return 1  # All test cases passed
    except Exception as e:
        # If there's an error during the test execution, print it and return 0
        print(f"An error occurred during tests: {e}")
        return 0
