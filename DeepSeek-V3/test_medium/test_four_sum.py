import unittest
from typing import List


# 原题提供的 Solution 类
class Solution(object):
    def fourSum(self, nums, target):
        sumMapping = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                currSum = nums[i] + nums[j]
                if currSum in sumMapping:
                    sumMapping[currSum].append((i, j))
                else:
                    sumMapping[currSum] = [(i, j)]

        result = set()
        for key, value in sumMapping.items():
            diff = target - key
            if diff in sumMapping:
                firstSet = value
                secondSet = sumMapping[diff]

                for i, j in firstSet:
                    for k, l in secondSet:
                        fourlet = [i, j, k, l]
                        if len(set(fourlet)) != len(fourlet):
                            continue
                        fourlist = [nums[i], nums[j], nums[k], nums[l]]
                        fourlist.sort()
                        result.add(tuple(fourlist))

        return [list(t) for t in result]


class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # 辅助方法：标准化输出（对每个四元组排序，再整体排序，便于比较）
    def normalize(self, quadruplets):
        return sorted([sorted(q) for q in quadruplets])

    # ---------- 题目示例 ----------
    def test_example1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        result = self.sol.fourSum(nums, target)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_example2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        expected = [[2, 2, 2, 2]]
        result = self.sol.fourSum(nums, target)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    # ---------- 边界情况 ----------
    def test_less_than_four_elements(self):
        nums = [1, 2, 3]
        target = 6
        self.assertEqual(self.sol.fourSum(nums, target), [])
        nums = [1, 2]
        self.assertEqual(self.sol.fourSum(nums, target), [])

    def test_empty_array(self):
        self.assertEqual(self.sol.fourSum([], 0), [])

    def test_all_elements_same(self):
        nums = [1, 1, 1, 1, 1]
        target = 4
        expected = [[1, 1, 1, 1]]
        result = self.sol.fourSum(nums, target)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_negative_numbers(self):
        nums = [-3, -2, -1, 0, 1, 2, 3]
        target = 0
        # 有多种组合，只检查部分已知组合存在
        result = self.sol.fourSum(nums, target)
        result_set = set(tuple(sorted(q)) for q in result)
        self.assertIn((-3, -1, 1, 3), result_set)
        self.assertIn((-2, -1, 1, 2), result_set)

    def test_large_values(self):
        nums = [1000000000, 1000000000, 1000000000, 1000000000]
        target = 4000000000
        expected = [[1000000000, 1000000000, 1000000000, 1000000000]]
        result = self.sol.fourSum(nums, target)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    # ---------- 随机测试（与暴力法对比，小规模）----------
    def test_random_compare_with_bruteforce(self):
        import random
        from itertools import combinations

        def brute_force_4sum(nums, target):
            n = len(nums)
            result_set = set()
            for indices in combinations(range(n), 4):
                a, b, c, d = indices
                if nums[a] + nums[b] + nums[c] + nums[d] == target:
                    quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                    result_set.add(tuple(quad))
            return [list(t) for t in result_set]

        for _ in range(50):
            length = random.randint(4, 8)  # 小规模，避免暴力超时
            nums = [random.randint(-20, 20) for _ in range(length)]
            target = random.randint(-40, 40)
            expected = brute_force_4sum(nums, target)
            result = self.sol.fourSum(nums, target)
            self.assertEqual(
                self.normalize(result),
                self.normalize(expected),
                f"Failed for nums={nums}, target={target}",
            )

    # ---------- 性能测试（约束内）----------
    def test_performance_max_length(self):
        # 长度 200，数值范围大，只检查不超时
        import time

        nums = list(range(-100, 100))  # 200 个不同的数
        target = 0
        start = time.time()
        result = self.sol.fourSum(nums, target)
        elapsed = time.time() - start
        # 预期结果数量较多，但不要求具体值，仅确保运行时间合理（如 < 5 秒）
        self.assertLess(elapsed, 5.0, f"Performance too slow: {elapsed:.2f}s")
        # 检查至少有一个解（如 -1,0,0,1 等，但 nums 里不一定有重复 0，实际情况可能没有，不做断言）
        # 只验证结果类型正确
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
