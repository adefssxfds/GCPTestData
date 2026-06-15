import unittest
from typing import List, Optional, Any
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# --- 将你的四个算法放在这里 ---
def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def helper(node: Optional[TreeNode]) -> None:
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result


def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    result, stack, current = [], [], root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


def inorder_traversal_morris(root: Optional[TreeNode]) -> List[int]:
    result, current = [], root
    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right
    return result


def inorder_traversal_iterative_simple(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result, stack = [], [(root, False)]
    while stack:
        node, is_processed = stack.pop()
        if is_processed:
            result.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
    return result


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
class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        # 将四种遍历算法统一管理，方便批量测试
        self.traversal_funcs = [
            inorder_traversal,
            inorder_traversal_iterative,
            inorder_traversal_morris,
            inorder_traversal_iterative_simple,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [([1, None, 2, 3], [1, 3, 2]), ([], []), ([1], [1])]
        for tree_vals, expected in test_cases:
            root = build_tree(tree_vals)
            for func in self.traversal_funcs:
                with self.subTest(func=func.__name__, tree=tree_vals):
                    self.assertEqual(func(root), expected)

    def test_complete_binary_tree(self):
        """测试完全二叉树: [1,2,3,4,5,6,7] -> 中序应为 [4,2,5,1,6,3,7]"""
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        expected = [4, 2, 5, 1, 6, 3, 7]
        for func in self.traversal_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_left_skewed_tree(self):
        """测试全左斜树: [1,2,3,None,None,4] -> 中序应为 [4,3,2,1]"""
        root = build_tree([1, 2, None, 3, None, 4])
        expected = [4, 3, 2, 1]
        for func in self.traversal_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_right_skewed_tree(self):
        """测试全右斜树: [1,None,2,None,3] -> 中序应为 [1,2,3]"""
        root = build_tree([1, None, 2, None, 3])
        expected = [1, 2, 3]
        for func in self.traversal_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_negative_values(self):
        """测试包含负数的节点"""
        root = build_tree([-1, -2, -3])
        expected = [-2, -1, -3]
        for func in self.traversal_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)


if __name__ == "__main__":
    unittest.main()
