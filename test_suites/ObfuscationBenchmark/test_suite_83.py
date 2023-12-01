def test(solution_code):
    # Define utility function to compare two lists regardless of order
    def compare_lists(a, b):
        return sorted(a) == sorted(b)

    # Execute the solution code to define the generate_parenthesis function
    exec(solution_code, globals())
    
    # Initialize tests passed as True. It will be set to False if any test fails.
    tests_passed = True

    # Define tests
    try:
        # Test 1: n is 3
        expected_3 = ['((()))', '(()())', '(())()', '()(())', '()()()']
        result_3 = generate_parenthesis(3)
        if not compare_lists(result_3, expected_3):
            print("Test 1 failed: expected", expected_3, "but got", result_3)
            tests_passed = False

        # Test 2: n is 1
        expected_1 = ['()']
        result_1 = generate_parenthesis(1)
        if not compare_lists(result_1, expected_1):
            print("Test 2 failed: expected", expected_1, "but got", result_1)
            tests_passed = False

        # Test 3: n is 0
        expected_0 = ['']
        result_0 = generate_parenthesis(0)
        if not compare_lists(result_0, expected_0):
            print("Test 3 failed: expected", expected_0, "but got", result_0)
            tests_passed = False

    except Exception as e:
        # If an exception is raised in any test, print the error and set tests_passed to False
        print("An error occurred during testing:", e)
        tests_passed = False

    # Return 1 if all tests passed, otherwise return 0
    return 1 if tests_passed else 0
