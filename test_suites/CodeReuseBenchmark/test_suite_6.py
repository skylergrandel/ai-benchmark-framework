
def test(solution):
    # Define the solution functions
    exec(solution, globals())

    # Original test suite code
    def test_functions_6():
        score = 0
        code_reuse_score = 0
        if sum_of_squares_6([1, 2, 3]) == 14:
            score += 4
        if sum_of_squares_of_evens_6([1, 2, 3]) == 4:
            score += 3
    
        # New Code reuse check
        if 'sum_of_squares_6' in globals().get('sum_of_squares_of_evens_6').__code__.co_names:
            code_reuse_score += 1
    
        return score, code_reuse_score

    # Get the scores from the original test suite
    score, code_reuse_score = test_functions_6()

    # Total points
    total_points = score + code_reuse_score
    return 1 if total_points >= 8 else 0, 1
