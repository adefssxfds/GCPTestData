import unittest
from typing import Optional, List
from collections import deque


# ---------- 二叉树节点定义 ----------
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


# ---------- 三种最大深度实现（复制自题目） ----------
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


# ---------- 辅助函数：根据层序遍历列表构建二叉树 ----------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """从层序遍历列表构建二叉树，None 表示空节点"""
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


# ---------- 测试类 ----------
class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        """三种待测试的算法"""
        self.algorithms = [
            ("递归", max_depth),
            ("迭代 BFS", max_depth_iterative),
            ("迭代 DFS 栈", max_depth_dfs_stack),
        ]

    def assert_depth(self, tree_values: List[Optional[int]], expected_depth: int):
        """构建树并使用所有算法验证深度"""
        root = build_tree(tree_values)
        for name, func in self.algorithms:
            with self.subTest(tree=tree_values, algorithm=name):
                self.assertEqual(func(root), expected_depth)

    # ---------- 测试用例 ----------
    def test_example1(self):
        """示例1: [3,9,20,null,null,15,7] -> 深度3"""
        self.assert_depth([3, 9, 20, None, None, 15, 7], 3)

    def test_example2(self):
        """示例2: [1,null,2] -> 深度2"""
        self.assert_depth([1, None, 2], 2)

    def test_empty_tree(self):
        """空树 -> 深度0"""
        self.assert_depth([], 0)

    def test_single_node(self):
        """单节点 -> 深度1"""
        self.assert_depth([1], 1)

    def test_left_skewed(self):
        """左斜树 1->2->3->4"""
        self.assert_depth([1, 2, None, 3, None, None, None, 4], 4)

    def test_right_skewed(self):
        """右斜树 1->2->3->4"""
        self.assert_depth([1, None, 2, None, 3, None, 4], 4)

    def test_full_complete_tree(self):
        """完全二叉树 3层"""
        #     1
        #    / \
        #   2   3
        #  / \ / \
        # 4  5 6 7
        self.assert_depth([1, 2, 3, 4, 5, 6, 7], 3)

    def test_unbalanced(self):
        """非平衡树：左子树深，右子树浅"""
        #       1
        #      / \
        #     2   3
        #    /
        #   4
        #  /
        # 5
        self.assert_depth([1, 2, 3, 4, None, None, None, 5], 4)

    def test_negative_values(self):
        """节点值包含负数，不影响深度"""
        self.assert_depth([-1, -2, -3, None, -4], 3)

    def test_large_tree_performance(self):
        """性能测试：构造深度为100的左斜树，验证不超时"""
        # 手工构建深度100的左斜树
        root = TreeNode(0)
        current = root
        for i in range(1, 100):
            current.left = TreeNode(i)
            current = current.left
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 100)

    def test_all_algorithms_identical(self):
        """随机树测试，确保所有方法结果一致"""
        import random

        for _ in range(50):
            # 随机生成深度为1~5的二叉树（简化，避免复杂构造）
            # 使用层序列表随机生成，None表示空
            size = random.randint(1, 20)
            values = []
            for _ in range(size):
                if random.random() < 0.7:  # 70%概率为非空节点值
                    values.append(random.randint(-100, 100))
                else:
                    values.append(None)
            # 确保至少有一个非None
            if all(v is None for v in values):
                values[0] = random.randint(-100, 100)
            root = build_tree(values)
            # 计算深度
            depths = [func(root) for _, func in self.algorithms]
            self.assertEqual(
                len(set(depths)), 1, f"Inconsistent depths: {depths} for tree {values}"
            )


if __name__ == "__main__":
    unittest.main()
