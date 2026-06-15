import unittest
from typing import Optional, List, Any
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- 将你的三个算法放在这里 ---
def min_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return 0


def min_depth_recursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left:
        return min_depth_recursive(root.right) + 1
    if not root.right:
        return min_depth_recursive(root.left) + 1
    return min(min_depth_recursive(root.left), min_depth_recursive(root.right)) + 1


def min_depth_iterative_dfs(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stack = [(root, 1)]
    min_depth_found = float("inf")
    while stack:
        node, depth = stack.pop()
        if node:
            if not node.left and not node.right:
                min_depth_found = min(min_depth_found, depth)
            else:
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
    return min_depth_found if min_depth_found != float("inf") else 0


# --- 辅助工具：通过 LeetCode 风格列表构建树 ---
def build_tree(values: List[Any]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# --- 测试代码 ---
class TestMinDepth(unittest.TestCase):
    def setUp(self):
        # 统一管理三种求解算法
        self.min_depth_funcs = [min_depth, min_depth_recursive, min_depth_iterative_dfs]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([3, 9, 20, None, None, 15, 7], 2),
            ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ]
        for tree_vals, expected in test_cases:
            for func in self.min_depth_funcs:
                with self.subTest(func=func.__name__, tree=tree_vals):
                    root = build_tree(tree_vals)
                    self.assertEqual(func(root), expected)

    def test_empty_tree(self):
        """测试空树的情况"""
        root = build_tree([])
        expected = 0
        for func in self.min_depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_single_node(self):
        """测试只有一个根节点的树"""
        root = build_tree([1])
        expected = 1
        for func in self.min_depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_left_skewed_tree(self):
        """测试全左斜树: 最小深度应等于节点数"""
        # [1, 2, None, 3] 最小深度为 3
        root = build_tree([1, 2, None, 3])
        expected = 3
        for func in self.min_depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_right_skewed_tree(self):
        """测试全右斜树: 最小深度应等于节点数"""
        # [1, None, 2, None, 3, None, 4] 最小深度为 4
        root = build_tree([1, None, 2, None, 3, None, 4])
        expected = 4
        for func in self.min_depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_unbalanced_tree(self):
        """测试极度不平衡的树（左子树极深，右子树极浅）"""
        # 左子树深4，右子树深2，最小深度应为 2
        # [1, 2, 3, 4, None, None, None, 5]
        root = build_tree([1, 2, 3, 4, None, None, None, 5])
        expected = 2
        for func in self.min_depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)


if __name__ == "__main__":
    unittest.main()
