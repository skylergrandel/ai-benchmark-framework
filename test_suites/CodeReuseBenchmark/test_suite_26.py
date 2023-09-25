
def test(solution):
    # Define the solution functions
    exec(solution, globals())

    # Original test suite code
    def test_functions_26():
        score = 0
        code_reuse_score = 0
        if string_reverse_26('abc') == 'cba':
            score += 4
        if reverse_and_uppercase_26('abc') == 'CBA':
            score += 3
    
        # New Code reuse check
        if 'string_reverse_26' in globals().get('reverse_and_uppercase_26').__code__.co_names:
            code_reuse_score += 1
    
        return score, code_reuse_score

    # Get the scores from the original test suite
    score, code_reuse_score = test_functions_26()

    # Total points
    total_points = score + code_reuse_score
    return 1 if total_points >= 8 else 0, 1
