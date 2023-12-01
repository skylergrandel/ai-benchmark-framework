def test(code):
    # Define a local dictionary to hold local variables after exec
    local_vars = {}
    exec(code, globals(), local_vars)
    
    # Retrieve the look_and_say function from the local_vars
    look_and_say = local_vars.get('look_and_say')
    if not callable(look_and_say):
        print("The provided code does not define a function named look_and_say.")
        return 0

    # Define the tests, a list of tuples (input, expected_output)
    tests = [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
    ]
    
    # Iterate through tests, checking if look_and_say function works as expected
    for n, expected in tests:
        output = look_and_say(n)
        if output != expected:
            print(f"Test failed for look_and_say({n}): Expected {expected}, got {output}")
            return 0
    
    print("All tests passed.")
    return 1
