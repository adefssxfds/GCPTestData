from combination_sum_ii import Solution

def test_combinationSum2_example1():
    candidates = [10,1,2,7,6,1,5]
    target = 8
    expected = [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert result == expected

def test_combinationSum2_example2():
    candidates = [2,5,2,1,2]
    target = 5
    expected = [
        [1,2,2],
        [5]
    ]
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert result == expected

def test_combinationSum2_with_duplicates():
    candidates = [2,3,2,2,1,2,1]
    target = 5
    expected = [
        [1,2,2],
        [2,3],
        [2,1,2],
        [2,2,1],
        [1,2,2],
        [1,1,3],
        [1,2,2]
    ]
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert len(result) == len(set(map(tuple, result)))  # Check for duplicates

def test_combinationSum2_with_large_candidates():
    candidates = [1] * 100
    target = 100
    expected = [[1]*100]
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert result == expected

def test_combinationSum2_with_large_target():
    candidates = [1,2,3]
    target = 300
    expected = []
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert result == expected

def test_combinationSum2_with_negative_candidates():
    candidates = [-1, -2, -3]
    target = -6
    expected = [[-3, -3]]
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    assert result == expected