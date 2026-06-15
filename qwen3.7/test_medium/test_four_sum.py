import unittest


# --- 将你的算法封装为 Solution 类 ---
class Solution(object):
    def fourSum(self, nums, target):
        sumMapping = {}
        for index_i in range(len(nums) - 1):
            for index_j in range(index_i + 1, len(nums)):
                currSum = nums[index_i] + nums[index_j]
                if currSum in sumMapping:
                    sumMapping[currSum].append((index_i, index_j))
                else:
                    sumMapping[currSum] = [(index_i, index_j)]

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

        return list(result)


# --- 测试代码 ---
class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
            ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ]
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.solution.fourSum(nums, target)
                # 对结果和预期进行排序后比较，防止内部顺序差异导致断言失败
                self.assertEqual(sorted(result), sorted(expected))

    def test_no_valid_quadruplet(self):
        """测试没有任何四个数能满足 target 的情况"""
        nums = [1, 2, 3, 4]
        target = 100
        expected = []
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """测试包含负数且和为负数的情况"""
        nums = [-3, -2, -1, 0, 1, 2]
        target = -6
        expected = [[-3, -2, -1, 0]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_large_numbers(self):
        """测试大数相加（验证是否发生整数溢出，Python天然支持大数，但需确保逻辑正确）"""
        nums = [1000000000, -1000000000, 1000000000, -1000000000]
        target = 0
        expected = [[-1000000000, -1000000000, 1000000000, 1000000000]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_multiple_identical_pairs(self):
        """测试大量重复元素（验证去重逻辑）"""
        nums = [0, 0, 0, 0]
        target = 0
        expected = [[0, 0, 0, 0]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, expected)

    def test_mixed_positive_negative(self):
        """测试正负数混合抵消的情况"""
        nums = [-1, 1, -2, 2, 0]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        # 注意：上面这个例子其实凑不出[-2,0,0,2]和[-1,0,0,1]，因为没有两个0。
        # 修正预期：
        expected = [[-2, -1, 1, 2]]
        result = self.solution.fourSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
