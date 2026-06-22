import unittest
import random


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 第一步：将非正数移到数组前面（实际上我们只关心正数）
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] <= 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        # 现在 nums[0:i] 都是非正数，nums[i:n] 都是正数
        # 只处理正数部分
        for idx in range(i, n):
            val = abs(nums[idx])
            if 1 <= val <= n - i:
                # 将对应位置的值标记为负数（表示 val 存在）
                if nums[i + val - 1] > 0:
                    nums[i + val - 1] = -nums[i + val - 1]

        # 查找第一个缺失的正数
        for idx in range(i, n):
            if nums[idx] > 0:
                return idx - i + 1
        return n - i + 1


class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        nums = [1, 2, 0]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_example2(self):
        nums = [3, 4, -1, 1]
        self.assertEqual(self.sol.firstMissingPositive(nums), 2)

    def test_example3(self):
        nums = [7, 8, 9, 11, 12]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    # ---------- 边界情况 ----------
    def test_single_positive_one(self):
        nums = [1]
        self.assertEqual(self.sol.firstMissingPositive(nums), 2)

    def test_single_positive_two(self):
        nums = [2]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_single_zero(self):
        nums = [0]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_single_negative(self):
        nums = [-5]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_all_positive_continuous(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.firstMissingPositive(nums), 6)

    def test_all_positive_missing_middle(self):
        nums = [1, 2, 4, 5]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_all_positive_missing_start(self):
        nums = [2, 3, 4, 5]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_mixed_with_duplicates(self):
        nums = [1, 1, 2, 2, 3]
        self.assertEqual(self.sol.firstMissingPositive(nums), 4)

    def test_mixed_negatives(self):
        nums = [-1, -2, -3, 1, 2, 3]
        self.assertEqual(self.sol.firstMissingPositive(nums), 4)

    def test_large_positive_and_negative(self):
        nums = [1000, -1000, 500, -500, 1]
        self.assertEqual(self.sol.firstMissingPositive(nums), 2)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    # ---------- 随机测试（与暴力法对比）----------
    def test_random_compare(self):
        """随机生成数组，用暴力法（从1开始查找）验证结果"""

        def brute_force(nums):
            s = set(nums)
            i = 1
            while i in s:
                i += 1
            return i

        for _ in range(100):
            length = random.randint(0, 100)
            nums = [random.randint(-1000, 1000) for _ in range(length)]
            # 复制数组，因为算法会修改原数组
            nums_copy = nums[:]
            expected = brute_force(nums_copy)
            result = self.sol.firstMissingPositive(nums)
            self.assertEqual(result, expected, f"Failed for {nums}")

    # ---------- 性能测试：大数组 O(n) 时间 ----------
    def test_performance_large(self):
        import time

        # 构造一个包含 1..1000000 的数组，缺失 500001
        n = 1000000
        nums = list(range(1, n + 1))
        missing = 500001
        nums[missing - 1] = n + 1  # 破坏一个位置
        # 随机打乱
        random.shuffle(nums)
        start = time.time()
        result = self.sol.firstMissingPositive(nums)
        elapsed = time.time() - start
        self.assertEqual(result, missing)
        self.assertLess(elapsed, 1.0, f"Too slow: {elapsed:.2f}s")


if __name__ == "__main__":
    unittest.main()
