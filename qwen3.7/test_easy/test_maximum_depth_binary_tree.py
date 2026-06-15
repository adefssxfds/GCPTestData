import unittest
from typing import Optional, List, Any
from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# --- 将你的三个算法放在这里 ---
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def max_depth_iterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


def max_depth_dfs_stack(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stack = [(root, 1)]
    max_depth_found = 0
    while stack:
        node, current_depth = stack.pop()
        max_depth_found = max(max_depth_found, current_depth)
        if node.right:
            stack.append((node.right, current_depth + 1))
        if node.left:
            stack.append((node.left, current_depth + 1))
    return max_depth_found


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
class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        # 统一管理三种求解算法
        self.depth_funcs = [max_depth, max_depth_iterative, max_depth_dfs_stack]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [([3, 9, 20, None, None, 15, 7], 3), ([1, None, 2], 2)]
        for tree_vals, expected in test_cases:
            for func in self.depth_funcs:
                with self.subTest(func=func.__name__, tree=tree_vals):
                    root = build_tree(tree_vals)
                    self.assertEqual(func(root), expected)

    def test_empty_tree(self):
        """测试空树的情况"""
        root = build_tree([])
        expected = 0
        for func in self.depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_single_node(self):
        """测试只有一个根节点的树"""
        root = build_tree([1])
        expected = 1
        for func in self.depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_left_skewed_tree(self):
        """测试全左斜树: 深度应等于节点数"""
        # [1, 2, None, 3] 深度为 3
        root = build_tree([1, 2, None, 3])
        expected = 3
        for func in self.depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_right_skewed_tree(self):
        """测试全右斜树: 深度应等于节点数"""
        # [1, None, 2, None, 3, None, 4] 深度为 4
        root = build_tree([1, None, 2, None, 3, None, 4])
        expected = 4
        for func in self.depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)

    def test_complete_binary_tree(self):
        """测试完全二叉树: [1,2,3,4,5,6,7] 深度为 3"""
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        expected = 3
        for func in self.depth_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(root), expected)


if __name__ == "__main__":
    unittest.main()
