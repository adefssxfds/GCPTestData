from combination_sum import Solution

# 测试组合求和函数
def test_combinationSum_example1():
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    assert solution.combinationSum(candidates, target) == expected

def test_combinationSum_example2():
    solution = Solution()
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert solution.combinationSum(candidates, target) == expected

def test_combinationSum_example3():
    solution = Solution()
    candidates = [2]
    target = 1
    expected = []
    assert solution.combinationSum(candidates, target) == expected

def test_combinationSum_empty_candidates():
    solution = Solution()
    candidates = []
    target = 5
    expected = []
    assert solution.combinationSum(candidates, target) == expected

def test_combinationSum_single_candidate():
    solution = Solution()
    candidates = [5]
    target = 5
    expected = [[5]]
    assert solution.combinationSum(candidates, target) == expected

def test_combinationSum_large_target():
    solution = Solution()
    candidates = [2, 3, 5]
    target = 30
    expected = [[2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [5, 5, 5, 5, 5, 5], [2, 2, 2, 2, 2, 3], [2, 2, 2, 2, 2, 5], [2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 5, 5], [2, 2, 2, 3, 3, 3], [2, 2, 2, 3, 3, 5], [2, 2, 2, 3, 5, 5], [2, 2, 2, 5, 5, 5], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 3, 5], [2, 2, 3, 3, 5, 5], [2, 2, 3, 5, 5, 5], [2, 2, 5, 5, 5, 5], [2, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 5], [2, 3, 3, 3, 5, 5], [2, 3, 3, 5, 5, 5], [2, 3, 5, 5, 5, 5], [2, 5, 5, 5, 5, 5], [3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 5], [3, 3, 3, 3, 5, 5], [3, 3, 3, 5, 5, 5], [3, 3, 5, 5, 5, 5], [3, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5]]
    assert solution.combinationSum(candidates, target) == expected