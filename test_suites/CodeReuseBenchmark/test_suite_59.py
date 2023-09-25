
def test(solution):
    # Define the solution functions
    exec(solution, globals())

    # Original test suite code
    def test_functions_59():
        score = 0
        code_reuse_score = 0
        if factorial_59(5) == 120:
            score += 4
        if factorial_of_sum_59(2, 1) == factorial_59(3):
            score += 3
    
        # New Code reuse check
        if 'factorial_59' in globals().get('factorial_of_sum_59').__code__.co_names:
            code_reuse_score += 1
    
        return score, code_reuse_score

    # Get the scores from the original test suite
    score, code_reuse_score = test_functions_59()

    # Total points
    total_points = score + code_reuse_score
    return 1 if total_points >= 8 else 0, 1
