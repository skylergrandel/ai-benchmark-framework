def test(code):
    exec(code, globals())

    # Initialize a variable to keep track of test results
    tests_failed = 0

    # Define a helper function to check equality
    def assert_equal(actual, expected):
        return actual == expected

    # Test cases
    tests = [
        (reverse_list([]), []),
        (reverse_list([1]), [1]),
        (reverse_list([1, 2, 3]), [3, 2, 1]),
    ]

    # Run each test
    for i, (actual, expected) in enumerate(tests):
        if not assert_equal(actual, expected):
            print(f"Test {i+1} Failed: Expected {expected}, got {actual}")
            tests_failed += 1
        else:
            print(f"Test {i+1} Passed")

    # Return 1 if all tests pass, else return 0
    return 1 if tests_failed == 0 else 0

# Example usage:
# code = """
# def reverse_list(numbers):
#     return numbers[::-1]
# """
# print(test(code)) # Should print 1 if all the tests pass