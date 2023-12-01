def test(code):
    exec(code, globals())

    try:
        # Test 1: Regular case
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        result = sorted(map(sorted, four_sum(nums, target)))
        expected = sorted(map(sorted, expected))
        assert result == expected, "Test 1 Failed"

        # Test 2: No solution case
        assert four_sum([1, 2, 3, 4], 10) == [], "Test 2 Failed"

        # Test 3: Empty array case
        assert four_sum([], 0) == [], "Test 3 Failed"

    except AssertionError as e:
        print(e)  # Optionally, print the error for debugging
        return 0

    return 1