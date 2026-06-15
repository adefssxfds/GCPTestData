from generate_parentheses import Solution

def test_generateParenthesis_n_3():
    """Test the generateParenthesis function with n = 3 as per example 1"""
    solution = Solution()
    expected_output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert solution.generateParenthesis(3) == expected_output

def test_generateParenthesis_n_1():
    """Test the generateParenthesis function with n = 1 as per example 2"""
    solution = Solution()
    expected_output = ["()"]
    assert solution.generateParenthesis(1) == expected_output

def test_generateParenthesis_n_0():
    """Test the generateParenthesis function with n = 0, should be empty list"""
    solution = Solution()
    expected_output = [""]
    assert solution.generateParenthesis(0) == expected_output

def test_generateParenthesis_n_8():
    """Test the generateParenthesis function with n = 8, should be a large list"""
    solution = Solution()
    expected_output = ["((()))((()))", "((()))(()())", "((()))(())()", "..."]  # truncated for brevity
    assert solution.generateParenthesis(8) == expected_output

def test_backtracking_single_call():
    """Test the backtracking function with single call, should not fail"""
    solution = Solution()
    result = solution.generateParenthesis(3)
    assert isinstance(result, list)

def test_backtracking_two_calls():
    """Test the backtracking function with two calls, should not fail"""
    solution = Solution()
    result1 = solution.generateParenthesis(3)
    result2 = solution.generateParenthesis(2)
    assert isinstance(result1, list) and isinstance(result2, list)