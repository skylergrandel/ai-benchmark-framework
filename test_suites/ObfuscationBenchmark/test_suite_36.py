import random

# Mock "randomize" function assuming it returns the list in a randomized order.
def randomize(lst):
    random.shuffle(lst)
    return lst

# The testing function itself; no dependency on unittest
def test(code):
    # Define the mock `randomize` function in global scope
    globals()['randomize'] = randomize

    # Execute the given solution code in the global context
    exec(code, globals())

    # Test cases
    try:
        # Regular list
        original_list = [1, 2, 3, 4, 5]
        randomized_list = randomize_list(original_list.copy())
        assert sorted(original_list) == sorted(randomized_list) and original_list != randomized_list
        
        # Empty list
        assert randomize_list([]) == []

        # Single element list
        assert randomize_list([1]) == [1]

    except AssertionError:
        # If any assertion fails, return 0
        return 0

    # If all tests pass, return 1
    return 1
