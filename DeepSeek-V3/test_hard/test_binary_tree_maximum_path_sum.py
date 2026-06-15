import unittest
from typing import Optional, List
from collections import deque


# ---------- 二叉树节点定义 ----------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------- 两种实现（复制自题目） ----------
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
class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        # 待测试的两种方式
        self.algorithms = [
            ("函数式", max_path_sum),
            ("类方法", lambda root: Solution().maxPathSum(root)),
        ]

    def test_example1(self):
        """示例1: [1,2,3] -> 6"""
        root = build_tree([1, 2, 3])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 6)

    def test_example2(self):
        """示例2: [-10,9,20,null,null,15,7] -> 42"""
        root = build_tree([-10, 9, 20, None, None, 15, 7])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 42)

    def test_single_node_positive(self):
        """单节点正数 -> 节点值"""
        root = TreeNode(5)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 5)

    def test_single_node_negative(self):
        """单节点负数 -> 节点值（必须选非空路径）"""
        root = TreeNode(-3)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), -3)

    def test_all_negative(self):
        """所有节点为负数 -> 最大值即为最大的那个节点值"""
        # 树: -10, -20, -30 构成的完全二叉树
        root = build_tree([-10, -20, -30])
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), -10)

    def test_left_skewed(self):
        """左斜树: 5 -> 4 -> 3 -> 2 -> 1，最大路径为所有节点和（因为全是正数）"""
        # 构建链状: 5.left=4, 4.left=3, 3.left=2, 2.left=1
        root = build_tree(
            [
                5,
                4,
                None,
                3,
                None,
                None,
                None,
                2,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                1,
            ]
        )
        # 实际更方便用循环构建
        # 重新用直接连接方式
        node1 = TreeNode(1)
        node2 = TreeNode(2, node1)
        node3 = TreeNode(3, node2)
        node4 = TreeNode(4, node3)
        root2 = TreeNode(5, node4)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root2), 5 + 4 + 3 + 2 + 1)

    def test_right_skewed(self):
        """右斜树: 1 -> 2 -> 3 -> 4 -> 5，路径和也是全部和"""
        node5 = TreeNode(5)
        node4 = TreeNode(4, None, node5)
        node3 = TreeNode(3, None, node4)
        node2 = TreeNode(2, None, node3)
        root = TreeNode(1, None, node2)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 15)

    def test_path_that_does_not_go_through_root(self):
        """最大路径不经过根节点的情况"""
        # 构造树: 根为 -1，左子树为 [10, -5, 5]，右子树为 [2]
        # 实际上左子树的内部路径 5 -> -5 -> 10 和为10？不对，需要计算。
        # 更典型的例子：根为负数，左右子树各自内部有较大正和。
        # 例如:
        #        -5
        #       /  \
        #      3    4
        #     / \    \
        #    1   2    5
        # 最大路径可能在右子树: 4+5=9，或者左子树内部 3+1+2=6？最大是9，不经过根。
        # 但左子树内部路径 1->3->2 和为6。根加左右负值会降低。所以最大为9。
        root = TreeNode(-5)
        root.left = TreeNode(3)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(5)
        # 最大路径: 5+4=9 或者 1+3+2=6，取9
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 9)

    def test_mixed_positive_negative(self):
        """混合正负的复杂树"""
        # 示例2 已经覆盖，再添加一个:
        #        10
        #       /  \
        #      2    -25
        #     / \   / \
        #    20 1  3  4
        # 最大路径: 20 + 2 + 10 = 32? 或者 20+2+1=23? 或 3+(-25)+4 = -18? 显然 32 最大
        root = TreeNode(10)
        root.left = TreeNode(2)
        root.right = TreeNode(-25)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        expected = 20 + 2 + 10  # =32
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), expected)

    def test_straight_line_positive(self):
        """直线全正数: 1-2-3-4，路径和应为 10"""
        # 构建链表: 1.right=2, 2.right=3, 3.right=4
        n4 = TreeNode(4)
        n3 = TreeNode(3, None, n4)
        n2 = TreeNode(2, None, n3)
        root = TreeNode(1, None, n2)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 10)

    def test_straight_line_mixed(self):
        """直线混合: 5 -> -2 -> 3，最大路径可能是 5+(-2)+3=6 或 5 或 3，选6"""
        n3 = TreeNode(3)
        n2 = TreeNode(-2, None, n3)
        root = TreeNode(5, None, n2)
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 6)

    def test_large_negative_root_with_positive_leaves(self):
        """根很大负数，但左右叶子正数，最大路径可能只取一个叶子"""
        root = TreeNode(-100)
        root.left = TreeNode(50)
        root.right = TreeNode(50)
        # 最大路径可能是 50 或 50，取 50
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(root), 50)

    def test_random_consistency(self):
        """随机小树验证两种实现结果一致"""
        import random

        for _ in range(100):
            # 生成随机层序遍历列表，深度不超过4，节点数不超过15
            size = random.randint(1, 15)
            values = []
            for _ in range(size):
                if random.random() < 0.8:
                    values.append(random.randint(-100, 100))
                else:
                    values.append(None)
            # 确保根非空
            if values[0] is None:
                values[0] = random.randint(-100, 100)
            root = build_tree(values)
            res1 = max_path_sum(root)
            res2 = Solution().maxPathSum(root)
            self.assertEqual(
                res1, res2, f"Mismatch for tree {values}: {res1} vs {res2}"
            )

    def test_large_tree_performance(self):
        """性能测试：节点数 30000 的链状树（但为了时间，只测 10000）"""
        # 构建右斜链，值全为 1，最大路径和应为节点数
        n = 10000
        root = TreeNode(1)
        current = root
        for _ in range(1, n):
            current.right = TreeNode(1)
            current = current.right
        import time

        start = time.time()
        res = max_path_sum(root)
        elapsed = time.time() - start
        self.assertEqual(res, n)
        self.assertLess(elapsed, 2.0, f"Took {elapsed:.2f}s, too slow")


if __name__ == "__main__":
    unittest.main()
