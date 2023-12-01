def first_non_repeating_char(s):
    # User's function or code to be inserted here
    pass  # Placeholder, replace with actual code to solve the problem

def test_user_solution(user_solution):
    # Define the first_non_repeating_char function based on the user_solution
    exec(user_solution, globals())

    # Define tests
    tests = {
        'swiss': 'w',
        'aabbcc': None,
        '': None,
    }

    # Run tests
    for input_str, expected_output in tests.items():
        if first_non_repeating_char(input_str) != expected_output:
            return 0  # Test failed

    # If all tests passed return 1
    return 1
