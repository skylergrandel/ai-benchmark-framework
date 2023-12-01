def test(code):
    exec(code, globals())

    tests_passed = True

    # Test case: possible to reach the end
    try:
        assert can_jump_to_end([2, 3, 1, 1, 4]) == True
    except AssertionError:
        tests_passed = False

    # Test case: impossible to reach the end
    try:
        assert can_jump_to_end([3, 2, 1, 0, 4]) == False
    except AssertionError:
        tests_passed = False

    # Test case: single element
    try:
        assert can_jump_to_end([0]) == True
    except AssertionError:
        tests_passed = False

    # Return 1 if all tests passed, 0 otherwise
    return 1 if tests_passed else 0