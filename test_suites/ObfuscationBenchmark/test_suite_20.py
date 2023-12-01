def repeat_characters(s):
    return ''.join(c * 2 for c in s)

def test(solution_code):
    # First, we define a helper function to execute the code
    # and return the result after injecting our function into it.
    local_vars = {}
    exec(solution_code, globals(), local_vars)
    repeat_characters = local_vars['repeat_characters']

    def check_case(case_input, expected_output):
        """Helper function to check a single case."""
        try:
            return repeat_characters(case_input) == expected_output
        except Exception as e:
            print("Test failed due to an exception:", e)
            return False

    # Now, we define all the test cases.
    test_cases = [
        ('abc', 'aabbcc'),
        ('', ''),
        ('hello world', 'hheelllloo  wwoorrlldd'),
        # Additional test cases can be added here.
    ]

    # Execute all test cases.
    all_tests_passed = True
    for case_input, expected_output in test_cases:
        if not check_case(case_input, expected_output):
            all_tests_passed = False
            print(f"Test failed for input: '{case_input}'. Expected: '{expected_output}'")

    # Finally, we return 1 if all tests passed, 0 otherwise.
    return 1 if all_tests_passed else 0

