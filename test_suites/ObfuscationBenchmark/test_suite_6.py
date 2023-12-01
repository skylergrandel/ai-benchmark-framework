def test(code):
    # Inject the provided code string into the global namespace as the roman_to_int function
    exec(code, globals())

    try:
        # Define tests as tuples of input and expected output
        tests = [
            ('I', 1),
            ('MMXVII', 2017),
            # Additional test - assuming 4000 is the expected output for invalid 'MMMM'
            # Otherwise, remove this test or adjust as necessary by raising an exception or returning a specific value.
            ('MMMM', 4000),
        ]

        # Run each test and check if the results are as expected
        for roman, expected in tests:
            result = roman_to_int(roman)
            if result != expected:
                # Test failed, return 0
                return 0

        # All tests passed, return 1
        return 1

    except Exception as e:
        # An exception occurred while running the tests, return 0
        print(f"An exception occurred: {e}")
        return 0
