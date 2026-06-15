import unittest
from typing import Optional, List, Any
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- 将你的三个算法放在这里 ---
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    left_subtree = invert_tree(root.left)
    right_subtree = invert_tree(root.right)
    root.left = right_subtree
    root.right = left_subtree
    return root


def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    queue = deque([root])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root


def invert_tree_iterative_stack(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    stack = [root]
    while stack:
        current = stack.pop()
        current.left, current.right = current.right, current.left
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return root


# --- 辅助工具函数 ---
def build_tree(values: List[Any]) -> Optional[TreeNode]:
    """通过 LeetCode 风格的列表构建二叉树"""
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


def tree_to_list(root: Optional[TreeNode]) -> List[Any]:
    """将二叉树序列化为 LeetCode 风格的列表（去除末尾多余的 None）"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 去除末尾多余的 None
    while result and result[-1] is None:
        result.pop()
    return result


# --- 测试代码 ---
class TestInvertTree(unittest.TestCase):
    def setUp(self):
        # 统一管理三种翻转算法
        self.invert_funcs = [
            invert_tree,
            invert_tree_iterative,
            invert_tree_iterative_stack,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ]
        for input_vals, expected_vals in test_cases:
            for func in self.invert_funcs:
                with self.subTest(func=func.__name__, input=input_vals):
                    # 每次测试都需要重新构建树，因为翻转是原地修改
                    root = build_tree(input_vals)
                    inverted_root = func(root)
                    self.assertEqual(tree_to_list(inverted_root), expected_vals)

    def test_single_node(self):
        """测试只有一个节点的树"""
        root = build_tree([1])
        for func in self.invert_funcs:
            with self.subTest(func=func.__name__):
                # 重新构建以防原地修改影响
                test_root = build_tree([1])
                inverted_root = func(test_root)
                self.assertEqual(tree_to_list(inverted_root), [1])

    def test_left_skewed_tree(self):
        """测试全左斜树: 翻转后应变为全右斜树"""
        # [1, 2, None, 3] -> 翻转后 -> [1, None, 2, None, 3]
        input_vals = [1, 2, None, 3]
        expected_vals = [1, None, 2, None, 3]
        for func in self.invert_funcs:
            with self.subTest(func=func.__name__):
                root = build_tree(input_vals)
                inverted_root = func(root)
                self.assertEqual(tree_to_list(inverted_root), expected_vals)

    def test_right_skewed_tree(self):
        """测试全右斜树: 翻转后应变为全左斜树"""
        # [1, None, 2, None, 3] -> 翻转后 -> [1, 2, None, 3]
        input_vals = [1, None, 2, None, 3]
        expected_vals = [1, 2, None, 3]
        for func in self.invert_funcs:
            with self.subTest(func=func.__name__):
                root = build_tree(input_vals)
                inverted_root = func(root)
                self.assertEqual(tree_to_list(inverted_root), expected_vals)

    def test_unbalanced_tree(self):
        """测试极度不平衡的树"""
        # 只有左子树有深层节点
        input_vals = [1, 2, None, 3, None, 4]
        expected_vals = [1, None, 2, None, 3, None, 4]
        for func in self.invert_funcs:
            with self.subTest(func=func.__name__):
                root = build_tree(input_vals)
                inverted_root = func(root)
                self.assertEqual(tree_to_list(inverted_root), expected_vals)


if __name__ == "__main__":
    unittest.main()
