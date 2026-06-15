import unittest
from typing import List


class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # 查找第一个位置
        left, right = 0, len(nums) - 1
        first_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if first_pos == -1:
            return [-1, -1]

        # 查找最后一个位置
        left, right = 0, len(nums) - 1
        last_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first_pos, last_pos]


class TestSearchRange(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(self.sol.searchRange(nums, target), [3, 4])

    def test_example2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual(self.sol.searchRange(nums, target), [-1, -1])

    def test_example3(self):
        nums = []
        target = 0
        self.assertEqual(self.sol.searchRange(nums, target), [-1, -1])

    # ---------- 边界情况 ----------
    def test_single_element_found(self):
        nums = [1]
        target = 1
        self.assertEqual(self.sol.searchRange(nums, target), [0, 0])

    def test_single_element_not_found(self):
        nums = [1]
        target = 2
        self.assertEqual(self.sol.searchRange(nums, target), [-1, -1])

    def test_target_at_beginning(self):
        nums = [1, 1, 2, 3, 4]
        target = 1
        self.assertEqual(self.sol.searchRange(nums, target), [0, 1])

    def test_target_at_end(self):
        nums = [1, 2, 3, 4, 4]
        target = 4
        self.assertEqual(self.sol.searchRange(nums, target), [3, 4])

    def test_all_elements_same(self):
        nums = [7, 7, 7, 7, 7]
        target = 7
        self.assertEqual(self.sol.searchRange(nums, target), [0, 4])

    def test_target_greater_than_all(self):
        nums = [1, 2, 3]
        target = 5
        self.assertEqual(self.sol.searchRange(nums, target), [-1, -1])

    def test_target_less_than_all(self):
        nums = [10, 20, 30]
        target = 5
        self.assertEqual(self.sol.searchRange(nums, target), [-1, -1])

    def test_empty_array(self):
        self.assertEqual(self.sol.searchRange([], 1), [-1, -1])

    # ---------- 随机测试（与线性扫描对比）----------
    def test_random_compare(self):
        import random

        def linear_search_range(nums, target):
            start, end = -1, -1
            for i, val in enumerate(nums):
                if val == target:
                    if start == -1:
                        start = i
                    end = i
            return [start, end]

        for _ in range(100):
            # 生成长度 0~20 的随机非递减数组
            length = random.randint(0, 20)
            if length == 0:
                nums = []
            else:
                nums = sorted([random.randint(-100, 100) for _ in range(length)])
            target = random.randint(-110, 110)
            expected = linear_search_range(nums, target)
            result = self.sol.searchRange(nums, target)
            self.assertEqual(
                result, expected, f"Failed for nums={nums}, target={target}"
            )

    # ---------- 性能测试（大数组）----------
    def test_performance_large(self):
        import time

        n = 100000
        nums = [1] * n  # 全相同
        target = 1
        start = time.time()
        result = self.sol.searchRange(nums, target)
        elapsed = time.time() - start
        self.assertEqual(result, [0, n - 1])
        self.assertLess(elapsed, 1.0, f"二分查找耗时 {elapsed:.2f}s 超过1秒")

        # 不存在的情况
        target = 2
        start = time.time()
        result = self.sol.searchRange(nums, target)
        elapsed = time.time() - start
        self.assertEqual(result, [-1, -1])
        self.assertLess(elapsed, 1.0)


if __name__ == "__main__":
    unittest.main()
