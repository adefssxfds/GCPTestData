from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 函数版实现
def max_path_sum(root: Optional[TreeNode]) -> int:
    max_sum = float("-inf")

    def max_path_helper(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0
        left_max = max(0, max_path_helper(node.left))
        right_max = max(0, max_path_helper(node.right))
        current_max = node.val + left_max + right_max
        max_sum = max(max_sum, current_max)
        return node.val + max(left_max, right_max)

    max_path_helper(root)
    return max_sum


# Class解法
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self._dfs(root)
        return self.max_sum

    def _dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_gain = max(0, self._dfs(node.left))
        right_gain = max(0, self._dfs(node.right))
        path_sum = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, path_sum)
        return node.val + max(left_gain, right_gain)


# 辅助：数组层序构建二叉树
def build_tree(arr):
    if not arr:
        return None
    from collections import deque

    q = deque()
    root = TreeNode(arr[0])
    q.append(root)
    idx = 1
    while q and idx < len(arr):
        cur = q.popleft()
        if arr[idx] is not None:
            cur.left = TreeNode(arr[idx])
            q.append(cur.left)
        idx += 1
        if idx < len(arr) and arr[idx] is not None:
            cur.right = TreeNode(arr[idx])
            q.append(cur.right)
        idx += 1
    return root


# 单元测试
class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        root = build_tree([1, 2, 3])
        self.assertEqual(max_path_sum(root), 6)
        self.assertEqual(self.sol.maxPathSum(root), 6)

    def test_example2(self):
        root = build_tree([-10, 9, 20, None, None, 15, 7])
        self.assertEqual(max_path_sum(root), 42)
        self.assertEqual(self.sol.maxPathSum(root), 42)

    def test_single_node(self):
        root = TreeNode(-5)
        self.assertEqual(max_path_sum(root), -5)
        self.assertEqual(self.sol.maxPathSum(root), -5)

    def test_all_negative(self):
        root = build_tree([-3, -2, -1])
        self.assertEqual(max_path_sum(root), -1)
        self.assertEqual(self.sol.maxPathSum(root), -1)


if __name__ == "__main__":
    unittest.main()
