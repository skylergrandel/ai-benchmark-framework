# Define the test function to evaluate the solution code
def test(code):
    # First, we'll define a local function to represent our test cases since the code will be imported into global scope
    def is_rotation(s1, s2):
        # Since the code variable is expected to be a string containing the definition of an is_rotation function,
        # We use exec to execute this string and define the function in global scope.
        exec(code, globals())

    # Initialize a variable to keep track of all the tests passing
    all_tests_passed = True

    # Define test cases
    test_cases = [
        # Format: (s1, s2, expected_result)
        ('abcde', 'deabc', True),    # valid rotation
        ('abcde', 'edcba', False),   # invalid rotation
        ('abc', 'abcd', False),      # different lengths
        ('', '', True),              # empty strings
    ]

    # Iterate over each test case and evaluate
    for s1, s2, expected_result in test_cases:
        try:
            # Invoke the is_rotation function and check if the result matches the expected result
            result = is_rotation(s1, s2)
            if result != expected_result:
                print(f"Test failed for is_rotation({s1!r}, {s2!r}): Expected {expected_result}, got {result}")
                all_tests_passed = False
        except Exception as e:
            # If an exception occurs during testing, print it out and mark the test as failed
            print(f"Test raised an exception for is_rotation({s1!r}, {s2!r}): {e}")
            all_tests_passed = False

    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_passed else 0

# To use this test function, you would call it with a string containing the solution code as follows:
# solution_code = """
# Paste the solution code here (e.g., the body of the is_rotation function).
# """
# result = test(solution_code)
# print(f"Test result: {'Passed' if result == 1 else 'Failed'}")