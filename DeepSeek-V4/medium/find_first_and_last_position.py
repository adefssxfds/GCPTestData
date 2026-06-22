
class Solution(object):
    def searchRange(self, nums, target):
    
        if not nums:
            return [-1, -1]
        
        # Find first position
        left, right = 0, len(nums) - 1
        first_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1  # Continue searching left for first occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if first_pos == -1:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        last_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [first_pos, last_pos]