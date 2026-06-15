import heapq
from typing import List
class MedianFinder:
    def __init__(self):
        self.max_heap: List[int] = []  # Stores smaller half (negated for max heap)
        self.min_heap: List[int] = []  # Stores larger half
    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        if self.max_heap:
            largest_small = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, largest_small)
        if len(self.min_heap) > len(self.max_heap):
            smallest_large = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smallest_large)
    
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


class MedianFinderAlternative:
    def __init__(self):
        self.small = []  # Max heap (negated values)
        self.large = []  # Min heap
    
    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return float(-self.small[0])


class MedianFinderSorted:
    
    def __init__(self):
        self.nums: List[int] = []
    
    def addNum(self, num: int) -> None:
        left, right = 0, len(self.nums)
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        self.nums.insert(left, num)
    
    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n // 2])
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0
