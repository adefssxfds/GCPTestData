import unittest
from typing import List, Optional

# 假设 TreeNode 定义和四种中序遍历函数已经提供（复制前面的代码）
# 这里为了测试代码完整性，再次列出（实际使用时可删除重复定义）


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


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def helper(node):
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


# ------------------ 测试类 ------------------
class TestInorderTraversal(unittest.TestCase):
    """测试二叉树中序遍历的多种实现"""

    def setUp(self):
        # 定义四种待测试的函数（按顺序列表）
        self.algorithms = [
            ("递归", inorder_traversal),
            ("迭代（标准）", inorder_traversal_iterative),
            ("Morris", inorder_traversal_morris),
            ("迭代（标记法）", inorder_traversal_iterative_simple),
        ]

    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """根据层序遍历列表构建二叉树（None 表示空节点）"""
        if not values:
            return None
        from collections import deque

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

    def run_test_on_all_algorithms(self, root: Optional[TreeNode], expected: List[int]):
        """用所有算法测试同一棵树"""
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(root)
                self.assertEqual(result, expected, f"Failed for {name}")

    # ---------- 测试用例 ----------
    def test_example1(self):
        """[1,null,2,3] -> [1,3,2]"""
        root = self.build_tree([1, None, 2, 3])
        self.run_test_on_all_algorithms(root, [1, 3, 2])

    def test_example2_empty(self):
        """空树 -> []"""
        root = None
        self.run_test_on_all_algorithms(root, [])

    def test_example3_single_node(self):
        """单节点 [1] -> [1]"""
        root = TreeNode(1)
        self.run_test_on_all_algorithms(root, [1])

    def test_left_skewed(self):
        """左斜树 1->2->3"""
        # 树结构: 3
        #        /
        #       2
        #      /
        #     1
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.run_test_on_all_algorithms(root, [1, 2, 3])

    def test_right_skewed(self):
        """右斜树 1->2->3"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.run_test_on_all_algorithms(root, [1, 2, 3])

    def test_full_tree(self):
        """完全二叉树: [4,2,6,1,3,5,7]"""
        root = self.build_tree([4, 2, 6, 1, 3, 5, 7])
        self.run_test_on_all_algorithms(root, [1, 2, 3, 4, 5, 6, 7])

    def test_negative_values(self):
        """包含负值: [-1, -2, -3]"""
        root = self.build_tree([-1, -2, -3])
        self.run_test_on_all_algorithms(root, [-2, -1, -3])

    def test_unbalanced(self):
        """非平衡树: [5,3,6,2,4,null,7]"""
        root = self.build_tree([5, 3, 6, 2, 4, None, 7])
        self.run_test_on_all_algorithms(root, [2, 3, 4, 5, 6, 7])

    def test_all_same_value(self):
        """所有节点值相同: [2,2,2]"""
        root = self.build_tree([2, 2, 2])
        self.run_test_on_all_algorithms(root, [2, 2, 2])


if __name__ == "__main__":
    unittest.main()
