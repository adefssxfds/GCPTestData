from typing import List, Optional
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


# 递归中序遍历
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


# 迭代中序遍历（标准栈）
def inorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


# Morris 中序遍历（无栈 O(1) 空间）
def inorder_traversal_morris(root: Optional[TreeNode]) -> List[int]:
    result = []
    current = root

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


# 标记法迭代遍历（简单通用）
def inorder_traversal_iterative_simple(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    stack = [(root, False)]

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


# ==================== 工具函数 ====================
# 层序数组构建二叉树
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        # 左节点
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            q.append(node.left)
        i += 1
        # 右节点
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            q.append(node.right)
        i += 1
    return root


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试用例：(输入层序数组, 预期中序遍历结果)
    test_cases = [
        ([1, None, 2, 3], [1, 3, 2]),  # 示例1
        ([], []),  # 示例2：空树
        ([1], [1]),  # 示例3：单节点
    ]

    # 四个遍历函数
    functions = [
        ("递归版本", inorder_traversal),
        ("标准迭代", inorder_traversal_iterative),
        ("Morris遍历", inorder_traversal_morris),
        ("标记法迭代", inorder_traversal_iterative_simple),
    ]

    print("===== 二叉树中序遍历 测试开始 =====\n")

    for idx, (input_arr, expect) in enumerate(test_cases, 1):
        print(f"测试用例 {idx}")
        print(f"输入：{input_arr}")
        print(f"预期中序：{expect}")

        for name, func in functions:
            root = build_tree(input_arr)
            output = func(root)
            status = "✅ 通过" if output == expect else "❌ 失败"
            print(f"  {name} → {output} {status}")

        print("-" * 50)

    print("\n===== 所有测试完成 =====")
