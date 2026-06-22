
class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        if nums[0] <= 0:
            return 0
            
        steps, currentEnd, farthest = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == currentEnd:
                steps += 1
                currentEnd = farthest
                
                if currentEnd >= len(nums) - 1:
                    break

        return steps if farthest >= len(nums) - 1 else 0