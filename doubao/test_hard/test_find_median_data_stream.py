import heapq
from typing import List
import unittest


# 实现1
class MedianFinder:
    def __init__(self):
        self.max_heap: List[int] = []
        self.min_heap: List[int] = []

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


# 实现2
class MedianFinderAlternative:
    def __init__(self):
        self.small = []
        self.large = []

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


# 实现3
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


class TestMedianFinder(unittest.TestCase):
    def test_example_flow(self):
        # 原题样例流程
        finder1 = MedianFinder()
        finder2 = MedianFinderAlternative()
        finder3 = MedianFinderSorted()

        finder1.addNum(1)
        finder2.addNum(1)
        finder3.addNum(1)

        finder1.addNum(2)
        finder2.addNum(2)
        finder3.addNum(2)

        self.assertEqual(finder1.findMedian(), 1.5)
        self.assertEqual(finder2.findMedian(), 1.5)
        self.assertEqual(finder3.findMedian(), 1.5)

        finder1.addNum(3)
        finder2.addNum(3)
        finder3.addNum(3)

        self.assertEqual(finder1.findMedian(), 2.0)
        self.assertEqual(finder2.findMedian(), 2.0)
        self.assertEqual(finder3.findMedian(), 2.0)

    def test_odd_more_elements(self):
        mf = MedianFinderAlternative()
        for x in [4, 2, 7, 1, 3]:
            mf.addNum(x)
        self.assertEqual(mf.findMedian(), 3.0)

    def test_even_more_elements(self):
        mf = MedianFinderSorted()
        for x in [5, 1, 3, 9]:
            mf.addNum(x)
        self.assertEqual(mf.findMedian(), (3 + 5) / 2)

    def test_negative_number(self):
        mf = MedianFinder()
        mf.addNum(-1)
        mf.addNum(-2)
        self.assertEqual(mf.findMedian(), -1.5)


if __name__ == "__main__":
    unittest.main()
