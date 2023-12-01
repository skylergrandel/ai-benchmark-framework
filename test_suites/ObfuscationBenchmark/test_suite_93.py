def test(code):
    # Execute the provided code to define evaluate_expression
    exec(code, globals())

    def test_evaluate_expression():
        try:
            # Test cases to verify the given solution
            test_cases = [
                ('2+3', 5),
                ('2+3*4-1', 13),
                ('10', 10),
            ]

            # Run through each test case and check the result
            for expr, expected in test_cases:
                result = evaluate_expression(expr)
                if result != expected:
                    return 0  # If any test case fails, return 0
            return 1  # If all test cases pass, return 1

        except Exception as e:
            # Return 0 if an exception occurs during testing
            print(f"An error occurred: {e}")
            return 0

    # Run the test suite using the evaluate_expression function defined in the provided code
    return test_evaluate_expression()

# Example usage
# code = "Your solution code as a string"
# result = test(code)
# print("Test Passed" if result == 1 else "Test Failed")
