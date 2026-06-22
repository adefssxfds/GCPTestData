from typing import List
def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0
    
    curr_sum, result = nums[0], nums[0]
    
    for index in range(1, len(nums)):
        # Either extend previous subarray or start new one
        curr_sum = max(nums[index], curr_sum + nums[index])
        result = max(result, curr_sum)
    
    return result


def max_sub_array_divide_conquer(nums: List[int]) -> int:
    def max_crossing_sum(nums: List[int], left: int, mid: int, right: int) -> int:
        left_sum = float('-inf')
        sum_val = 0
        for i in range(mid, left - 1, -1):
            sum_val += nums[i]
            left_sum = max(left_sum, sum_val)
        right_sum = float('-inf')
        sum_val = 0
        for i in range(mid + 1, right + 1):
            sum_val += nums[i]
            right_sum = max(right_sum, sum_val)
        
        return left_sum + right_sum
    
    def max_subarray_rec(nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        left_max = max_subarray_rec(nums, left, mid)
        right_max = max_subarray_rec(nums, mid + 1, right)
        cross_max = max_crossing_sum(nums, left, mid, right)
        
        return max(left_max, right_max, cross_max)
    
    if not nums:
        return 0
    
    return max_subarray_rec(nums, 0, len(nums) - 1)


def max_sub_array_with_indices(nums: List[int]) -> tuple[int, int, int]:
    if not nums:
        return 0, -1, -1
    
    max_sum = curr_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    
    return max_sum, start, end