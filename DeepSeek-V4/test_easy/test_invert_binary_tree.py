import unittest
from typing import List, Optional
from collections import deque


# ---------- 二叉树节点定义 ----------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------- 三种反转实现（复制自题目） ----------
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


# ---------- 辅助函数：根据层序遍历列表构建二叉树 ----------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """从层序遍历列表构建二叉树，None 表示空节点。例如 [4,2,7,1,3,6,9]"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        # 左孩子
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # 右孩子
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ---------- 辅助函数：将二叉树转换为层序遍历列表（便于比较）----------
def tree_to_level_order_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """返回层序遍历列表，包含 None 占位，直到最后一个非空节点"""
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
    # 去掉末尾连续的 None
    while result and result[-1] is None:
        result.pop()
    return result


# ---------- 测试类 ----------
class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        """定义三种待测试的算法"""
        self.algorithms = [
            ("递归", invert_tree),
            ("迭代 BFS (队列)", invert_tree_iterative),
            ("迭代 DFS (栈)", invert_tree_iterative_stack),
        ]

    def assert_tree_inverted(
        self, original_list: List[Optional[int]], expected_list: List[Optional[int]]
    ):
        """对给定的原始层序遍历列表，应用所有算法并验证结果是否与预期一致"""
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                root = build_tree(original_list)
                inverted_root = func(root)
                actual = tree_to_level_order_list(inverted_root)
                self.assertEqual(
                    actual,
                    expected_list,
                    f"Algorithm {name} failed: expected {expected_list}, got {actual}",
                )

    # ---------- 测试用例 ----------
    def test_example1(self):
        """示例1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]"""
        original = [4, 2, 7, 1, 3, 6, 9]
        expected = [4, 7, 2, 9, 6, 3, 1]
        self.assert_tree_inverted(original, expected)

    def test_example2(self):
        """示例2: [2,1,3] -> [2,3,1]"""
        original = [2, 1, 3]
        expected = [2, 3, 1]
        self.assert_tree_inverted(original, expected)

    def test_example3(self):
        """示例3: 空树 -> []"""
        original = []
        expected = []
        self.assert_tree_inverted(original, expected)

    def test_single_node(self):
        """单节点: [1] -> [1]"""
        original = [1]
        expected = [1]
        self.assert_tree_inverted(original, expected)

    def test_left_skewed(self):
        """左斜树: [1,2,None,3] -> 反转后应为右斜树 [1,None,2,None,None,None,3] 但层序表示为 [1,None,2,None,3]? 实际需要明确"""
        # 原始:    1
        #         /
        #        2
        #       /
        #      3
        # 反转后应为:
        #    1
        #     \
        #      2
        #       \
        #        3
        original = [1, 2, None, 3]
        # 反转后的层序遍历（保留 None 直到最后一个非空节点）: 1, None, 2, None, 3
        expected = [1, None, 2, None, 3]
        self.assert_tree_inverted(original, expected)

    def test_right_skewed(self):
        """右斜树: [1,None,2,None,3] -> 反转后左斜树 [1,2,None,3]"""
        original = [1, None, 2, None, 3]
        expected = [1, 2, None, 3]
        self.assert_tree_inverted(original, expected)

    def test_full_complete_tree(self):
        """完全二叉树: [1,2,3,4,5,6,7] -> [1,3,2,7,6,5,4]"""
        original = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 3, 2, 7, 6, 5, 4]
        self.assert_tree_inverted(original, expected)

    def test_negative_values(self):
        """包含负值: [-5, -10, -3, None, -15] -> [-5, -3, -10, -15, None]? 手动验证"""
        # 原始:      -5
        #           /  \
        #        -10   -3
        #          \
        #          -15
        original = [-5, -10, -3, None, -15]
        # 反转后:    -5
        #           /  \
        #         -3   -10
        #               \
        #               -15
        expected = [-5, -3, -10, None, -15]  # 层序: -5, -3, -10, None, -15
        self.assert_tree_inverted(original, expected)

    def test_unbalanced(self):
        """非平衡树: [5,3,6,2,4,None,7] -> [5,6,3,7,None,4,2]"""
        original = [5, 3, 6, 2, 4, None, 7]
        expected = [5, 6, 3, 7, None, 4, 2]
        self.assert_tree_inverted(original, expected)


if __name__ == "__main__":
    unittest.main()
