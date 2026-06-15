import unittest
from typing import Optional, List
from collections import deque


# ---------- 二叉树节点定义 ----------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------- 三种实现（复制自题目） ----------
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
class TestMinDepth(unittest.TestCase):
    def setUp(self):
        self.algorithms = [
            ("BFS", min_depth),
            ("递归DFS", min_depth_recursive),
            ("迭代DFS", min_depth_iterative_dfs),
        ]

    def test_example1(self):
        """示例1: [3,9,20,null,null,15,7] -> 2"""
        root = build_tree([3, 9, 20, None, None, 15, 7])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 2)

    def test_example2(self):
        """示例2: [2,null,3,null,4,null,5,null,6] -> 5 (链状)"""
        root = build_tree([2, None, 3, None, 4, None, 5, None, 6])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 5)

    def test_empty_tree(self):
        """空树 -> 0"""
        root = None
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 0)

    def test_single_node(self):
        """单节点 -> 1"""
        root = TreeNode(1)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 1)

    def test_complete_tree_min_depth_not_root(self):
        """完全二叉树，最小深度为2（根节点非叶子）"""
        # 根节点 1 有左右孩子，叶子在第二层
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 2)

    def test_left_skewed(self):
        """左斜树: 1->2->3->4，最小深度为4（唯一叶子在最底层）"""
        # 构造: 1.left=2, 2.left=3, 3.left=4
        root = build_tree([1, 2, None, 3, None, None, None, 4])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 4)

    def test_right_skewed(self):
        """右斜树: 1->2->3->4，最小深度为4"""
        root = build_tree([1, None, 2, None, 3, None, 4])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 4)

    def test_one_child_missing(self):
        """根节点只有一个左孩子，该孩子是叶子 -> 深度2"""
        root = TreeNode(1, TreeNode(2))
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 2)

    def test_negative_values(self):
        """节点值为负数，不影响深度"""
        root = build_tree([-10, -20, None, -30])
        # 树: -10
        #     /
        #   -20
        #   /
        # -30
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 3)

    def test_large_tree_performance(self):
        """性能测试：链状树深度 100000，BFS 会很快找到叶子吗？注意：BFS 在链状树时实际上会遍历所有层才找到叶子，但这里深度大，测试时间不宜过长，仅验证不崩溃。"""
        # 构造右斜树深度 1000（避免过慢）
        root = None
        current = None
        for i in range(1000):
            node = TreeNode(i)
            if not root:
                root = node
                current = node
            else:
                current.right = node
                current = node
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                # 最小深度应为 1000
                depth = func(root)
                self.assertEqual(depth, 1000)

    def test_random_trees_consistency(self):
        """随机生成小树，验证三种实现结果一致"""
        import random

        for _ in range(50):
            # 随机生成二叉树（简化：随机深度3以内的完全或不完全树）
            # 为简化，直接生成随机层序遍历列表
            size = random.randint(1, 20)
            values = []
            for _ in range(size):
                if random.random() < 0.7:
                    values.append(random.randint(-100, 100))
                else:
                    values.append(None)
            # 确保根节点非空
            if values[0] is None:
                values[0] = 0
            root = build_tree(values)
            depths = [func(root) for _, func in self.algorithms]
            self.assertEqual(
                len(set(depths)), 1, f"Inconsistent depths {depths} for tree {values}"
            )


if __name__ == "__main__":
    unittest.main()
