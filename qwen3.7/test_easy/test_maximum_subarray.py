import unittest
from typing import List


# --- 将你的三个算法放在这里 ---
def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0
    curr_sum, result = nums[0], nums[0]
    for index in range(1, len(nums)):
        curr_sum = max(nums[index], curr_sum + nums[index])
        result = max(result, curr_sum)
    return result


def max_sub_array_divide_conquer(nums: List[int]) -> int:
    def max_crossing_sum(nums: List[int], left: int, mid: int, right: int) -> int:
        left_sum = float("-inf")
        sum_val = 0
        for i in range(mid, left - 1, -1):
            sum_val += nums[i]
            left_sum = max(left_sum, sum_val)
        right_sum = float("-inf")
        sum_val = 0
        for i in range(mid + 1, right + 1):
            sum_val += nums[i]
            right_sum = max(right_sum, sum_val)
        return left_sum + right_sum

    def max_subarray_rec(nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_max = max_subarray_rec(nums, left, mid)
        right_max = max_subarray_rec(nums, mid + 1, right)
        cross_max = max_crossing_sum(nums, left, mid, right)
        return max(left_max, right_max, cross_max)

    if not nums:
        return 0
    return max_subarray_rec(nums, 0, len(nums) - 1)


def max_sub_array_with_indices(nums: List[int]) -> tuple[int, int, int]:
    if not nums:
        return 0, -1, -1
    max_sum = curr_sum = nums[0]
    start = end = temp_start = 0
    for i in range(1, len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    return max_sum, start, end


# --- 测试代码 ---
class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        # 统一管理返回最大和的两种算法
        self.sum_funcs = [max_sub_array, max_sub_array_divide_conquer]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
        ]
        for nums, expected in test_cases:
            for func in self.sum_funcs:
                with self.subTest(func=func.__name__, nums=nums):
                    self.assertEqual(func(nums), expected)

    def test_all_negative(self):
        """测试全负数数组: 应返回最大的那个负数"""
        nums = [-3, -2, -5, -1]
        expected = -1
        for func in self.sum_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(nums), expected)

    def test_all_positive(self):
        """测试全正数数组: 应返回整个数组的和"""
        nums = [1, 2, 3, 4]
        expected = 10
        for func in self.sum_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(nums), expected)

    def test_with_zeros(self):
        """测试包含 0 的数组"""
        nums = [0, -1, 0, 2, -1]
        expected = 2
        for func in self.sum_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(nums), expected)


class TestMaxSubArrayWithIndices(unittest.TestCase):
    """专门测试返回最大和及起止索引的函数"""

    def test_basic_indices(self):
        """测试示例1的索引"""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = (6, 3, 6)  # 和为6, 从索引3到6
        self.assertEqual(max_sub_array_with_indices(nums), expected)

    def test_single_element(self):
        """测试单元素数组的索引"""
        nums = [5]
        expected = (5, 0, 0)
        self.assertEqual(max_sub_array_with_indices(nums), expected)

    def test_all_negative_indices(self):
        """测试全负数数组的索引"""
        nums = [-3, -2, -5, -1]
        expected = (-1, 3, 3)  # 最大为-1，在索引3
        self.assertEqual(max_sub_array_with_indices(nums), expected)

    def test_entire_array_indices(self):
        """测试最大子数组为整个数组的情况"""
        nums = [5, 4, -1, 7, 8]
        expected = (23, 0, 4)
        self.assertEqual(max_sub_array_with_indices(nums), expected)


if __name__ == "__main__":
    unittest.main()
