def test(code):
    # Define a local namespace to execute the code within
    local_namespace = {}
    exec(code, local_namespace)

    # Get the function from the local namespace
    zero_sum_pairs = local_namespace.get('zero_sum_pairs')
    if not callable(zero_sum_pairs):
        return 0  # The function doesn't exist or isn't callable

    try:
        # Performing tests
        # Test 1: normal case
        expected = [(-3, 3), (-2, 2), (-1, 1)]
        result = zero_sum_pairs([-3, -2, -1, 0, 1, 2, 3])
        if set(result) != set(expected) or len(result) != len(expected):
            return 0

        # Test 2: no zero sum pairs
        if zero_sum_pairs([1, 2, 3]) != []:
            return 0

        # Test 3: empty list
        if zero_sum_pairs([]) != []:
            return 0

    except Exception as e:
        # If there's an error running the tests, return 0
        return 0

    # If none of the tests failed, return 1
    return 1
