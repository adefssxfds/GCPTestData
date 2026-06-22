from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    
    def helper(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        # Traverse left subtree
        helper(node.left)
        
        # Process current node
        result.append(node.val)
        
        # Traverse right subtree
        helper(node.right)
    
    helper(root)
    return result


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


def inorder_traversal_morris(root: Optional[TreeNode]) -> List[int]:
    result = []
    current = root
    
    while current:
        if not current.left:
            # No left child, process current and move right
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