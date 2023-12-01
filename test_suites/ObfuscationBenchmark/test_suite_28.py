def test(code):
    exec(code, globals())

    try:
        # Test regular case
        assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1], "Regular case failed"

        # Test case with negative numbers
        assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4], "Case with negative numbers failed"

        # Test case with no solution: This should raise a ValueError
        try:
            two_sum([1, 2, 3], 6)
            assert False, "No solution case failed: Expected a ValueError"
        except ValueError:
            pass  # Expected exception

    except AssertionError as e:
        print(str(e))
        return 0

    return 1
