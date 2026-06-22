from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    left_subtree = invert_tree(root.left)
    right_subtree = invert_tree(root.right)

    root.left = right_subtree
    root.right = left_subtree
    
    return root


def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        # Swap left and right children
        current.left, current.right = current.right, current.left
        
        # Add children to queue for processing
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return root


def invert_tree_iterative_stack(root: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root:
        return None
    
    stack = [root]
    
    while stack:
        current = stack.pop()
        
        # Swap left and right children
        current.left, current.right = current.right, current.left
        
        # Add children to stack for processing
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return root
