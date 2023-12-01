def test(code):
    # Define the local namespace to execute the solution code
    local_namespace = {}
    
    # Execute the solution code
    exec(code, {}, local_namespace)
    
    # Retrieve the solution function
    is_valid_number = local_namespace['is_valid_number']
    
    # Define the tests
    def test_valid_number():
        return (is_valid_number('10') and
                is_valid_number('-10.5') and
                is_valid_number('+5.5') and
                is_valid_number('0'))

    def test_invalid_number():
        return (not is_valid_number('a10') and
                not is_valid_number('10a') and
                not is_valid_number('10..5') and
                not is_valid_number('--10'))

    def test_edge_cases():
        return (not is_valid_number('') and
                is_valid_number('0'))

    # Run the tests
    all_tests_passed = (test_valid_number() and
                        test_invalid_number() and
                        test_edge_cases())

    # Return the result
    return 1 if all_tests_passed else 0
