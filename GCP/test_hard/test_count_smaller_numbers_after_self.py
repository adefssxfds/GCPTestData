from count_smaller_numbers_after_self import Solution

def test_count_smaller_example1():
    nums = [5,2,6,1]
    expected = [2,1,1,0]
    solution = Solution()
    assert solution.countSmaller(nums) == expected

def test_count_smaller_example2():
    nums = [-1]
    expected = [0]
    solution = Solution()
    assert solution.countSmaller(nums) == expected

def test_count_smaller_example3():
    nums = [-1,-1]
    expected = [0,0]
    solution = Solution()
    assert solution.countSmaller(nums) == expected

def test_count_smaller_empty():
    nums = []
    expected = []
    solution = Solution()
    assert solution.countSmaller(nums) == expected

def test_count_smaller_all_same():
    nums = [1,1,1,1]
    expected = [0,0,0,0]
    solution = Solution()
    assert solution.countSmaller(nums) == expected

def test_count_smaller_single_element():
    nums = [1]
    expected = [0]
    solution = Solution()
    assert solution.countSmaller(nums) == expected