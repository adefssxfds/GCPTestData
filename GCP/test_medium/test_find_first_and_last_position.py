from find_first_and_last_position import Solution

def test_searchRange_example1():
    """Test with Example 1 input"""
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_example2():
    """Test with Example 2 input"""
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    expected = [-1, -1]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_emptyArray():
    """Test with empty array"""
    nums = []
    target = 0
    expected = [-1, -1]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_singleElementArray():
    """Test with single element array"""
    nums = [5]
    target = 5
    expected = [0, 0]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_targetNotInArray():
    """Test with target not in array"""
    nums = [5, 7, 7, 8, 8, 10]
    target = 3
    expected = [-1, -1]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_targetAtBeginning():
    """Test with target at the beginning of array"""
    nums = [5, 7, 7, 8, 8, 10]
    target = 5
    expected = [0, 0]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_targetAtEnd():
    """Test with target at the end of array"""
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    expected = [5, 5]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected

def test_searchRange_targetInMiddle():
    """Test with target in the middle of array"""
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    expected = [2, 2]
    solution = Solution()
    result = solution.searchRange(nums, target)
    assert result == expected