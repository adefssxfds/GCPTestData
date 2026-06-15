import unittest


# --- 将你的算法放在这里 ---
class TreeNode(object):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val
        self.count = 1


class Solution(object):
    def countSmaller(self, nums):
        if len(nums) == 0:
            return []
        node = TreeNode(nums[len(nums) - 1])
        result = [0]
        for index in range(len(nums) - 2, -1, -1):
            result.append(self.insertNode(node, nums[index]))

        return result[::-1]

    def insertNode(self, node, val):
        totalCount = 0
        while True:
            if val <= node.val:
                node.count += 1
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                totalCount += node.count
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right

        return totalCount


# --- 测试代码 ---
class TestCountSmaller(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [([5, 2, 6, 1], [2, 1, 1, 0]), ([-1], [0]), ([-1, -1], [0, 0])]
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                result = self.solution.countSmaller(nums)
                self.assertEqual(result, expected)

    def test_empty_array(self):
        """测试空数组的情况"""
        nums = []
        expected = []
        result = self.solution.countSmaller(nums)
        self.assertEqual(result, expected)

    def test_sorted_ascending(self):
        """测试完全升序的数组（右侧没有比当前小的元素）"""
        nums = [1, 2, 3, 4, 5]
        expected = [0, 0, 0, 0, 0]
        result = self.solution.countSmaller(nums)
        self.assertEqual(result, expected)

    def test_sorted_descending(self):
        """测试完全降序的数组（最坏情况，右侧全比当前小）"""
        nums = [5, 4, 3, 2, 1]
        expected = [4, 3, 2, 1, 0]
        result = self.solution.countSmaller(nums)
        self.assertEqual(result, expected)

    def test_duplicate_elements(self):
        """测试包含大量重复元素的情况"""
        nums = [2, 1, 2, 1, 2]
        # 索引0的2: 右侧有 1, 1 -> 2个
        # 索引1的1: 右侧没有比1小的 -> 0个
        # 索引2的2: 右侧有 1 -> 1个
        # 索引3的1: 右侧没有比1小的 -> 0个
        # 索引4的2: 右侧没有元素 -> 0个
        expected = [2, 0, 1, 0, 0]
        result = self.solution.countSmaller(nums)
        self.assertEqual(result, expected)

    def test_mixed_positive_negative(self):
        """测试包含正负数的混合数组"""
        nums = [-2, 5, -1, 0, -3]
        # -2: 右侧只有 -3 比它小 -> 1
        # 5: 右侧有 -1, 0, -3 比它小 -> 3
        # -1: 右侧只有 -3 比它小 -> 1
        # 0: 右侧只有 -3 比它小 -> 1
        # -3: 0
        expected = [1, 3, 1, 1, 0]
        result = self.solution.countSmaller(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
