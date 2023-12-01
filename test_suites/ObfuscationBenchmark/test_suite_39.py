'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes
'''

def test(solution_code):
    # Define a local dictionary to execute the solution code
    local_vars = {}
    # Execute the passed solution code
    exec(solution_code, globals(), local_vars)
    # Retrieve the function from local_vars after code execution
    tested_function = local_vars['first_n_primes']
    
    # Initialize a flag to True, indicating all tests pass until proven otherwise
    all_tests_pass = True

    # List of test cases
    test_cases = [
        (5, [2, 3, 5, 7, 11]),
        (1, [2]),
        (0, [])
    ]

    # Iterate over the test cases and test each one
    for n, expected_output in test_cases:
        # Run the tested function and get the result
        result = tested_function(n)

        # Check if the result matches the expected output
        if result != expected_output:
            # If there's a mismatch, set the flag to False and print an error message
            all_tests_pass = False
            print(f"Test failed for n={n}: Expected {expected_output}, got {result}")

    # Return 1 if all tests passed, 0 otherwise
    return 1 if all_tests_pass else 0
