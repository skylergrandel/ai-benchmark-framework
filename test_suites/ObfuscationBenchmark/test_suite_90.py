def test(code):
    # Define a local dictionary to serve as the local namespace
    # when executing the provided code.
    local_namespace = {}

    # Execute the provided solution code within the local namespace.
    exec(code, {}, local_namespace)

    # Retrieve the function from the local namespace if it exists.
    reverse_string_keep_words_order = local_namespace.get('reverse_string_keep_words_order')

    # Check if the function exists.
    if not reverse_string_keep_words_order:
        print("No function 'reverse_string_keep_words_order' found in the provided code")
        return 0

    # Define the test cases, each as a (input, expected_output) pair.
    test_cases = [
        ('Hello World', 'olleH dlroW'),
        ('Python', 'nohtyP'),
        ('', ''),
        ('A long example with multiple words', 'A gnol elpmaxe htiw elpitlum sdrow'),  # An additional test case.
    ]

    # Run the test cases.
    for i, (input_str, expected) in enumerate(test_cases, 1):
        # Call the function with the input and compare to expected output.
        try:
            result = reverse_string_keep_words_order(input_str)
            if result != expected:
                # If the result doesn't match the expected output, return 0
                print(f"Test case {i} failed: Expected '{expected}', got '{result}'")
                return 0
        except Exception as e:
            # If the function raises an error during execution, the test fails
            print(f"Test case {i} raised an exception: {e}")
            return 0

    # If all tests passed, return 1
    print("All test cases passed.")
    return 1
