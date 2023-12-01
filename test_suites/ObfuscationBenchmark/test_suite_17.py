def test(code):
    # Execute the provided code string
    exec(code, globals())

    # Define our test cases
    test_cases = [
        (1, 10, 30),   # regular range, sum should be 30
        (-4, 2, -2),   # negative range, sum should be -2
        (4, 4, 4),     # single even number, sum should be 4
        (1, 1, 0)      # no even numbers, sum should be 0
    ]

    # Run the test cases
    all_passed = True
    for start, end, expected in test_cases:
        if sum_even_in_range(start, end) != expected:
            all_passed = False
            break

    # Return the result
    return 1 if all_passed else 0

