def trap_rain_water(heights):
    # The code that solves the problem should go here.
    pass

def test(code):
    # Execute the code in the global scope to define the trap_rain_water function
    exec(code, globals())

    tests_passed = 0
    total_tests = 3

    # Test 1: Regular case
    if trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6:
        tests_passed += 1

    # Test 2: Flat surface
    if trap_rain_water([1, 1, 1, 1]) == 0:
        tests_passed += 1

    # Test 3: Increasing heights
    if trap_rain_water([1, 2, 3, 4]) == 0:
        tests_passed += 1

    # Return 1 if all tests passed, 0 otherwise
    return 1 if tests_passed == total_tests else 0
