import unittest


# --- 将你的算法放在这里 ---
class Solution(object):
    def firstMissingPositive(self, nums):
        index_i = 0
        for index_j in range(len(nums)):
            if nums[index_j] <= 0:
                nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
                index_i += 1

        for index in range(index_i, len(nums)):
            if abs(nums[index]) - 1 < len(nums) and nums[abs(nums[index]) - 1] > 0:
                nums[abs(nums[index]) - 1] = -nums[abs(nums[index]) - 1]

        for index in range(len(nums)):
            if nums[index] > 0:
                return index + 1
        return len(nums) + 1


# --- 测试代码 ---
class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1)]
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                # 因为算法会原地修改数组，这里传入副本以防万一
                result = self.solution.firstMissingPositive(nums[:])
                self.assertEqual(result, expected)

    def test_contains_one(self):
        """测试包含 1 的情况"""
        nums = [1]
        expected = 2
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)

    def test_missing_one(self):
        """测试缺失 1 的情况（1 是缺失的最小正整数）"""
        nums = [2, 3, 4, 5]
        expected = 1
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)

    def test_with_duplicates(self):
        """测试包含大量重复元素的情况"""
        nums = [1, 1, 1, 1, 2, 2, 3]
        expected = 4
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)

    def test_all_negative(self):
        """测试全为负数的情况"""
        nums = [-1, -2, -3]
        expected = 1
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)

    def test_with_zeros(self):
        """测试包含大量 0 的情况"""
        nums = [0, 0, 0, 1]
        expected = 2
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)

    def test_consecutive_from_one(self):
        """测试从 1 开始的连续正整数"""
        nums = [1, 2, 3, 4, 5]
        expected = 6
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)

    def test_large_gap(self):
        """测试中间有巨大空缺的情况"""
        nums = [1, 2, 100]
        expected = 3
        result = self.solution.firstMissingPositive(nums[:])
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
