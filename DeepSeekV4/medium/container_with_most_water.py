from typing import List
def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_water = max(max_water, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


def max_area_brute_force(height: List[int]) -> int:
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            area = width * current_height
            max_water = max(max_water, area)
    
    return max_water


def max_area_optimized(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        left_height, right_height = height[left], height[right]
        width = right - left
        
        if left_height < right_height:
            area = left_height * width
            max_water = max(max_water, area)
            left += 1
        else:
            area = right_height * width
            max_water = max(max_water, area)
            right -= 1
    
    return max_water
