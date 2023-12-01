def test(code):
    namespace = {}
    exec(code, namespace)

    # Check if the is_perfect_square function exists
    if 'is_perfect_square' not in namespace:
        print("Function is_perfect_square is not defined.")
        return 0

    # Get the is_perfect_square function from the namespace
    is_perfect_square = namespace['is_perfect_square']

    # List of test cases
    test_cases = [
        (16, True),      # perfect square
        (14, False),     # non-perfect square
        (0, True),       # zero as a perfect square (0 * 0)
        (-4, False),     # negative number, not a perfect square
        (1, True),       # 1 is a perfect square (1 * 1)
        (625, True),     # another perfect square (25 * 25)
        (-1, False),     # negative number, not a perfect square
        (2, False),      # prime number, not a perfect square
        (144, True),     # 12 * 12
    ]

    # Execute each test
    for number, expected in test_cases:
        try:
            result = is_perfect_square(number)
            if result != expected:
                print(f"Failed for input {number}: expected {expected}, got {result}")
                return 0
        except Exception as e:
            print(f"An exception occurred for input {number}: {e}")
            return 0

    # If all tests pass
    return 1

# Example usage (assuming the solution code as a string is stored in variable `solution_code`):
# result = test(solution_code)
# print("All tests passed!" if result == 1 else "Some tests failed.")