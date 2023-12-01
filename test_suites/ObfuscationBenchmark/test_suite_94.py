
def product_except_self(nums):
    # This is a placeholder for the actual solution to be tested.
    pass


def test(code):
    # Execute the passed code.
    exec(code, globals())

    # Define test cases as a list of tuples.
    # Each tuple contains the input and expected output.
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([5], [1]),
        ([], [])
    ]

    # Initialize a variable to keep track of the test results.
    all_passed = True

    # Iterate through the test cases.
    for input_list, expected_output in test_cases:
        # Run the product_except_self function with the input.
        result = product_except_self(input_list)

        # If the result does not match the expected output,
        # set all_passed to False.
        if result != expected_output:
            all_passed = False
            break  # Exit the loop since one test already failed.

    # Return 1 if all tests have passed, 0 otherwise.
    return 1 if all_passed else 0
