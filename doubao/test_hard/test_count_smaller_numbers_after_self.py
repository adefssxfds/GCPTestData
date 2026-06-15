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


import unittest


class TestCountSmaller(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        nums = [5, 2, 6, 1]
        self.assertEqual(self.sol.countSmaller(nums), [2, 1, 1, 0])

    def test_example2_single(self):
        nums = [-1]
        self.assertEqual(self.sol.countSmaller(nums), [0])

    def test_example3_two_same_neg(self):
        nums = [-1, -1]
        self.assertEqual(self.sol.countSmaller(nums), [0, 0])

    def test_all_asc(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.sol.countSmaller(nums), [0, 0, 0, 0])

    def test_all_desc(self):
        nums = [4, 3, 2, 1]
        self.assertEqual(self.sol.countSmaller(nums), [3, 2, 1, 0])

    def test_mixed_neg_pos(self):
        nums = [3, -2, -1, 0]
        self.assertEqual(self.sol.countSmaller(nums), [3, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
