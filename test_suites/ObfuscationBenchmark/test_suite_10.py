def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b

def test(solution_code):
    # Execute the solution code to bring `fibonacci` into scope
    local_vars = {}
    exec(solution_code, globals(), local_vars)
    fibonacci_function = local_vars.get("fibonacci")

    if not fibonacci_function:
        print("No fibonacci function defined.")
        return 0

    # Test cases
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55),
        # Add more test cases as needed
    ]

    # Run tests
    all_tests_passed = True
    for n, expected in test_cases:
        actual = fibonacci_function(n)
        if actual != expected:
            print(f"Test failed for fibonacci({n}): expected {expected}, got {actual}")
            all_tests_passed = False

    # Return result
    return 1 if all_tests_passed else 0
