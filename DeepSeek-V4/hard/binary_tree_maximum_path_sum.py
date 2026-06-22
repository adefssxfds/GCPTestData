from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    max_sum = float('-inf')
    
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
        self.max_sum = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
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
