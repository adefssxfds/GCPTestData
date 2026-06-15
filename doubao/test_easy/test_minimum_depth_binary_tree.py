from typing import Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS 层序遍历
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


# 递归 DFS
def min_depth_recursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left:
        return min_depth_recursive(root.right) + 1
    if not root.right:
        return min_depth_recursive(root.left) + 1
    return min(min_depth_recursive(root.left), min_depth_recursive(root.right)) + 1


# 迭代 DFS（栈）
def min_depth_iterative_dfs(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    min_depth_found = float("inf")

    while stack:
        node, depth = stack.pop()
        if not node.left and not node.right:
            min_depth_found = min(min_depth_found, depth)
        else:
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
    return min_depth_found


# ---------------------- 工具函数 ----------------------
def build_tree(nodes: list[Optional[int]]) -> Optional[TreeNode]:
    """层序列表构建二叉树"""
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = deque([root])
    idx = 1
    while q and idx < len(nodes):
        cur = q.popleft()
        if idx < len(nodes) and nodes[idx] is not None:
            cur.left = TreeNode(nodes[idx])
            q.append(cur.left)
        idx += 1
        if idx < len(nodes) and nodes[idx] is not None:
            cur.right = TreeNode(nodes[idx])
            q.append(cur.right)
        idx += 1
    return root


# ---------------------- 测试代码 ----------------------
if __name__ == "__main__":
    # 测试用例：(树节点列表, 预期最小深度)
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 2),  # 示例1
        ([2, None, 3, None, 4, None, 5, None, 6], 5),  # 示例2
        ([], 0),  # 空树
        ([1], 1),  # 单节点叶子
        ([1, 2, None], 2),  # 只有左子树
        ([1, None, 2], 2),  # 只有右子树
    ]

    func_list = [
        ("BFS层序", min_depth),
        ("递归DFS", min_depth_recursive),
        ("迭代DFS", min_depth_iterative_dfs),
    ]

    print("===== 二叉树最小深度 测试 =====\n")
    all_pass = True

    for case_id, node_list, expect in [(i + 1, *tc) for i, tc in enumerate(test_cases)]:
        print(f"测试用例 {case_id}")
        print(f"输入树: {node_list}，预期深度: {expect}")
        for name, func in func_list:
            tree = build_tree(node_list)
            res = func(tree)
            status = "✅ 通过" if res == expect else "❌ 失败"
            if res != expect:
                all_pass = False
            print(f"  {name} → {res} {status}")
        print("-" * 45)

    print("\n测试结果：", "全部用例通过" if all_pass else "存在用例失败")
