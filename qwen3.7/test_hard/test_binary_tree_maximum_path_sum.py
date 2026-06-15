import unittest


# ---------- 二叉树节点定义 ----------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------- 你的算法实现（已整合） ----------
# 1. 函数式闭包写法
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


# 2. 类方法写法
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


# ---------- 测试代码 ----------
class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        # 统一管理两种求解算法
        self.algorithms = [
            ("函数式", max_path_sum),
            ("类方法", lambda root: Solution().maxPathSum(root)),
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        # 示例 1: [1,2,3] -> 6
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)

        # 示例 2: [-10,9,20,null,null,15,7] -> 42
        root2 = TreeNode(-10)
        root2.left = TreeNode(9)
        root2.right = TreeNode(20)
        root2.right.left = TreeNode(15)
        root2.right.right = TreeNode(7)

        test_cases = [(root1, 6), (root2, 42)]

        for root, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name, expected=expected):
                    self.assertEqual(func(root), expected)

    def test_single_node(self):
        """测试单节点（正数与负数）"""
        test_cases = [(TreeNode(5), 5), (TreeNode(-3), -3)]
        for root, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name, val=root.val):
                    self.assertEqual(func(root), expected)

    def test_all_negative_nodes(self):
        """测试全负数节点（必须选择最大的那个负数）"""
        # 树: -10, -20, -30
        root = TreeNode(-10)
        root.left = TreeNode(-20)
        root.right = TreeNode(-30)
        expected = -10
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), expected)

    def test_path_not_through_root(self):
        """测试最大路径不经过根节点的情况"""
        #       -5
        #      /  \
        #     3    4
        #    / \    \
        #   1   2    5
        # 最大路径: 5+4=9
        root = TreeNode(-5)
        root.left = TreeNode(3)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(5)

        expected = 9
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), expected)

    def test_complex_mixed_tree(self):
        """测试复杂的正负混合树"""
        #        10
        #       /  \
        #      2    -25
        #     / \   / \
        #    20 1  3   4
        # 最大路径: 20 + 2 + 10 = 32
        root = TreeNode(10)
        root.left = TreeNode(2)
        root.right = TreeNode(-25)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)

        expected = 32
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), expected)

    def test_straight_line(self):
        """测试直线型树 (1 -> 2 -> 3 -> 4)"""
        n4 = TreeNode(4)
        n3 = TreeNode(3, None, n4)
        n2 = TreeNode(2, None, n3)
        root = TreeNode(1, None, n2)

        expected = 10  # 1+2+3+4
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), expected)


if __name__ == "__main__":
    unittest.main()
