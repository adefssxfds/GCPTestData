from typing import Optional, List
from collections import deque


# 二叉树节点定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归翻转
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    left_subtree = invert_tree(root.left)
    right_subtree = invert_tree(root.right)

    root.left = right_subtree
    root.right = left_subtree

    return root


# 迭代 BFS 翻转
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


# 迭代 DFS 栈翻转
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


# ==================== 工具函数 ====================
# 列表构建二叉树（层序）
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        # 左孩子
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            q.append(node.left)
        i += 1
        # 右孩子
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            q.append(node.right)
        i += 1
    return root


# 层序遍历打印树（方便对比结果）
def level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试用例：(输入列表, 预期输出列表)
    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),  # 示例1
        ([2, 1, 3], [2, 3, 1]),  # 示例2
        ([], []),  # 空树
        ([1], [1]),  # 单节点
        ([1, 2, None, 3], [1, None, 2, None, 3]),  # 左斜树
    ]

    # 三个要测试的函数
    functions = [
        ("递归版本", invert_tree),
        ("BFS迭代版本", invert_tree_iterative),
        ("DFS栈迭代版本", invert_tree_iterative_stack),
    ]

    print("===== 翻转二叉树 测试开始 =====\n")

    for idx, (input_list, expect_list) in enumerate(test_cases, 1):
        print(f"测试用例 {idx}")
        print(f"输入：{input_list}")
        print(f"预期：{expect_list}")

        for name, func in test_cases:
            # 每次都重新构建树，避免互相影响
            root = build_tree(input_list)
            inverted = func(root)
            output = level_order(inverted)
            ok = "✅ 通过" if output == expect_list else "❌ 失败"
            print(f"  {name}：输出 {output} → {ok}")

        print("-" * 50)

    print("\n===== 所有测试完成 =====")
