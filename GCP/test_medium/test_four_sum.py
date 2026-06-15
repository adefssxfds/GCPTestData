import pytest
from four_sum import Solution

def test_fourSum_example1():
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    expected = [(-2, -1, 1, 2), (-1, 0, 0, 1), (-2, 0, 0, 2)]
    assert solution.fourSum(nums, target) == expected

def test_fourSum_example2():
    solution = Solution()
    nums = [2, 2, 2, 2, 2]
    target = 8
    expected = [(2, 2, 2, 2)]
    assert solution.fourSum(nums, target) == expected

def test_fourSum_empty_array():
    solution = Solution()
    nums = []
    target = 0
    expected = []
    assert solution.fourSum(nums, target) == expected

def test_fourSum_single_number():
    solution = Solution()
    nums = [1]
    target = 1
    expected = []
    assert solution.fourSum(nums, target) == expected

def test_fourSum_negative_numbers():
    solution = Solution()
    nums = [-1, -2, -3, -4]
    target = -6
    expected = [[-1, -2, -3, -4]]
    assert solution.fourSum(nums, target) == expected