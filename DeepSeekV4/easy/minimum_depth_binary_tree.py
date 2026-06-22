from typing import Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth using BFS (level-order traversal).
    
    BFS is optimal for finding minimum depth because it explores nodes
    level by level and returns as soon as the first leaf is found.
    
    Time complexity: O(n) in worst case, but often much better
    Space complexity: O(w) where w is maximum width of tree
    
    Args:
        root: Root of the binary tree
        
    Returns:
        Minimum depth of the tree
    """
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        # If this is a leaf node, return its depth
        if not node.left and not node.right:
            return depth
        
        # Add children to queue with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0  # Should never reach here for valid input


def min_depth_recursive(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth using recursive DFS approach.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        Minimum depth of the tree
    """
    if not root:
        return 0
    
    # If one subtree is empty, return depth of the other + 1
    if not root.left:
        return min_depth_recursive(root.right) + 1
    if not root.right:
        return min_depth_recursive(root.left) + 1
    
    # Both subtrees exist, return minimum of both + 1
    return min(min_depth_recursive(root.left), 
               min_depth_recursive(root.right)) + 1


def min_depth_iterative_dfs(root: Optional[TreeNode]) -> int:
    """
    Find minimum depth using iterative DFS with stack.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        Minimum depth of the tree
    """
    if not root:
        return 0
    
    stack = [(root, 1)]
    min_depth_found = float('inf')
    
    while stack:
        node, depth = stack.pop()
        
        if node:
            # If leaf node, update minimum depth
            if not node.left and not node.right:
                min_depth_found = min(min_depth_found, depth)
            else:
                # Add children to stack
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
    
    return min_depth_found if min_depth_found != float('inf') else 0
