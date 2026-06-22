import unittest
import random
from typing import List


# 假设三个函数已经定义（复制自题目）
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


class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        # 待测试的函数（仅最大和）
        self.sum_algorithms = [
            ("Kadane", max_sub_array),
            ("Divide and Conquer", max_sub_array_divide_conquer),
        ]
        # 带索引的函数单独测试
        self.with_indices_func = max_sub_array_with_indices

    def test_examples(self):
        """题目提供的三个示例"""
        test_cases = [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
        ]
        for nums, expected in test_cases:
            for name, func in self.sum_algorithms:
                with self.subTest(nums=nums, algorithm=name):
                    self.assertEqual(func(nums), expected)
            # 测试带索引版本
            with self.subTest(nums=nums, algorithm="with_indices"):
                max_sum, start, end = self.with_indices_func(nums)
                self.assertEqual(max_sum, expected)
                # 可选：验证子数组和确实等于 max_sum（通过切片求和）
                if start != -1 and end != -1:
                    self.assertEqual(sum(nums[start : end + 1]), max_sum)

    def test_all_positive(self):
        """全正数数组：最大和为整个数组"""
        nums = [1, 2, 3, 4, 5]
        expected = 15
        for name, func in self.sum_algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(nums), expected)
        max_sum, start, end = self.with_indices_func(nums)
        self.assertEqual(max_sum, expected)
        self.assertEqual(start, 0)
        self.assertEqual(end, len(nums) - 1)

    def test_all_negative(self):
        """全负数数组：最大和为最大单个元素（最接近0）"""
        nums = [-5, -2, -8, -1, -3]
        expected = -1  # 最大子数组是 [-1]
        for name, func in self.sum_algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(nums), expected)
        max_sum, start, end = self.with_indices_func(nums)
        self.assertEqual(max_sum, expected)
        # 应该只有一个元素 -1 的位置
        self.assertEqual(nums[start], -1)
        self.assertEqual(start, end)

    def test_single_element(self):
        """单元素数组"""
        nums = [42]
        expected = 42
        for name, func in self.sum_algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(nums), expected)
        max_sum, start, end = self.with_indices_func(nums)
        self.assertEqual(max_sum, expected)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test_empty_input(self):
        """空数组（虽然约束说至少1个，但实现支持）"""
        nums = []
        expected = 0
        for name, func in self.sum_algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(nums), expected)
        max_sum, start, end = self.with_indices_func(nums)
        self.assertEqual(max_sum, 0)
        self.assertEqual(start, -1)
        self.assertEqual(end, -1)

    def test_mixed_with_zeros(self):
        """包含零和负数、正数的混合"""
        nums = [0, -2, 3, -1, 2, 0, -1, 4]
        expected = 8  # 子数组 [3,-1,2,0,-1,4]? 实际 [3,-1,2,0,-1,4] 和为 7，不如 [3,-1,2,4]? 让我们计算：最佳是 [3,-1,2,0,-1,4]? 不对，应该取最大连续和。手动：3+(-1)+2+0+(-1)+4=7；但 3+(-1)+2=4；2+0+(-1)+4=5；最好的是 4? 我们再分析。
        # 重新计算：从索引2的3开始：3-1+2=4; 3-1+2+0=4; 3-1+2+0-1+4=7; 从索引3的-1开始：-1+2=1; -1+2+0=1; -1+2+0-1+4=4; 从索引4的2开始：2+0-1+4=5; 2+0-1=1; 2+0=2; 2=2; 从索引5的0开始：0-1+4=3; 0-1=-1; 0=0; 从索引6的-1开始：-1+4=3; 从索引7的4开始：4。最大值为5（子数组 [2,0,-1,4]? 2+0-1+4=5）。实际上还有一个可能：从索引2到7: 3-1+2+0-1+4=7，大于5。检查：3-1=2, +2=4, +0=4, -1=3, +4=7。所以最大为7？但 [-2,3,-1,2,0,-1,4] 整体？整个数组 0-2+3-1+2+0-1+4 = 5。子数组 [3,-1,2,0,-1,4] 索引2到7 和 = 3-1+2+0-1+4=7。还有没有更大的？[3,-1,2,4]不是连续的。所以预期应为7。但题目测试不是重点，这里修正：
        # 正确最大子数组和应为7
        expected = 7
        for name, func in self.sum_algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(nums), expected)
        max_sum, start, end = self.with_indices_func(nums)
        self.assertEqual(max_sum, expected)
        self.assertEqual(sum(nums[start : end + 1]), expected)

    def test_large_negative_at_edges(self):
        """两端大负数，中间正数"""
        nums = [-10, 1, 2, 3, -10]
        expected = 6  # [1,2,3]
        for name, func in self.sum_algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(nums), expected)

    def test_random_consistency(self):
        """随机生成数组，比较 Kadane 和分治结果一致性"""
        for _ in range(100):
            length = random.randint(1, 50)
            nums = [random.randint(-100, 100) for _ in range(length)]
            kadane = max_sub_array(nums)
            divconq = max_sub_array_divide_conquer(nums)
            self.assertEqual(kadane, divconq, f"Mismatch for {nums}")

    def test_with_indices_correctness(self):
        """验证带索引函数返回的子数组和确实等于最大和"""
        for _ in range(100):
            length = random.randint(1, 30)
            nums = [random.randint(-50, 50) for _ in range(length)]
            max_sum, start, end = self.with_indices_func(nums)
            # 如果最大和为负数且所有元素为负，start, end 应指向最大元素（单个）
            computed_sum = sum(nums[start : end + 1])
            self.assertEqual(computed_sum, max_sum, f"Sum mismatch for {nums}")
            # 确保 start <= end
            self.assertLessEqual(start, end)
            # 确保索引范围有效
            if start != -1:
                self.assertGreaterEqual(start, 0)
                self.assertLess(end, length)

    def test_performance_large_input(self):
        """性能测试：10^5 长度的数组应快速完成（<1秒）"""
        import time

        nums = [random.randint(-10000, 10000) for _ in range(100000)]
        start_time = time.time()
        max_sub_array(nums)
        elapsed = time.time() - start_time
        self.assertLess(elapsed, 1.0, "Kadane took too long")
        # 分治法在 10^5 时可能较慢，但这里不强制测试分治，因为O(n log n)可能略慢，但通常也在1秒内。
        start_time = time.time()
        max_sub_array_divide_conquer(nums)
        elapsed2 = time.time() - start_time
        self.assertLess(elapsed2, 2.0, "Divide and conquer took too long")


if __name__ == "__main__":
    unittest.main()
