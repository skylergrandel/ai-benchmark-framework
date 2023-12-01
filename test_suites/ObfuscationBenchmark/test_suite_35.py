def test(code):
    # Define the global scope where the exec function will define has_duplicates
    global_scope = {}
    
    # Execute the provided code which should define has_duplicates
    exec(code, global_scope)
    
    # Retrieve the has_duplicates function from the global scope
    has_duplicates_test = global_scope.get('has_duplicates', None)
    
    # Function to run all tests, returns True if all tests pass, False otherwise
    def run_tests():
        try:
            assert has_duplicates_test('programming') == True, "Failed test_with_duplicates"
            assert has_duplicates_test('python') == False, "Failed test_no_duplicates"
            assert has_duplicates_test('') == False, "Failed test_empty_string"
        except AssertionError as e:
            print(e)
            return False
        return True

    # Run the tests
    return 1 if run_tests() else 0
