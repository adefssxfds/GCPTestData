class TreeNode(object):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val
        self.count = 1
        
class Solution(object):
    def countSmaller(self, nums):
        if len(nums) == 0:
            return []
        node = TreeNode(nums[len(nums)-1])
        result = [0]
        for index in range(len(nums)-2, -1, -1):
            result.append(self.insertNode(node, nums[index]))
            
        return result[::-1]
    def insertNode(self, node, val):
        totalCount = 0
        while True:
            if val <= node.val:
                node.count += 1
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                totalCount += node.count
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
                    
        return totalCount