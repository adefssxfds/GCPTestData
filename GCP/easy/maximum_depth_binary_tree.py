from typing import Optional
from collections import deque

class TreeNode:

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


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