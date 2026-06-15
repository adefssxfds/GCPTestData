from typing import Optional
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


# 递归 DFS
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


# BFS 层序遍历
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


# DFS 栈迭代
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


# ---------------------- 工具函数：列表构建二叉树 ----------------------
def build_tree(nodes: list[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    q = deque([root])
    idx = 1
    while q and idx < len(nodes):
        node = q.popleft()
        if idx < len(nodes) and nodes[idx] is not None:
            node.left = TreeNode(nodes[idx])
            q.append(node.left)
        idx += 1
        if idx < len(nodes) and nodes[idx] is not None:
            node.right = TreeNode(nodes[idx])
            q.append(node.right)
        idx += 1
    return root


# ---------------------- 测试代码 ----------------------
if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),  # 示例1
        ([1, None, 2], 2),  # 示例2
        ([], 0),  # 空树
        ([5], 1),  # 单个节点
        ([1, 2, None, 3], 3),  # 左斜树
    ]

    funcs = [
        ("递归DFS", max_depth),
        ("BFS层序", max_depth_iterative),
        ("DFS栈迭代", max_depth_dfs_stack),
    ]

    print("===== 二叉树最大深度 测试 =====\n")
    all_pass = True

    for case_id, node_list, expect in [(i + 1, *tc) for i, tc in enumerate(test_cases)]:
        print(f"测试用例 {case_id}")
        print(f"输入树: {node_list}, 预期深度: {expect}")
        for name, func in funcs:
            tree = build_tree(node_list)
            res = func(tree)
            status = "✅ 通过" if res == expect else "❌ 失败"
            if res != expect:
                all_pass = False
            print(f"  {name} → {res} {status}")
        print("-" * 40)

    print("\n全部测试结果：", "全部通过" if all_pass else "存在失败用例")
