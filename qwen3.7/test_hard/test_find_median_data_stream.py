import unittest
from typing import List

# --- 将你的三种算法放在这里 ---
import heapq


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


# --- 测试代码 ---
class TestMedianFinder(unittest.TestCase):
    def setUp(self):
        # 统一管理三种求解算法
        self.algorithms = [
            ("双堆交替法", MedianFinder),
            ("经典双堆法", MedianFinderAlternative),
            ("二分查找法", MedianFinderSorted),
        ]

    def _run_operations(self, cls, operations, values):
        """
        辅助方法：模拟 LeetCode 的输入格式
        operations: ["MedianFinder", "addNum", "findMedian", ...]
        values: [[], [1], [], ...]
        """
        results = []
        obj = None
        for op, val in zip(operations, values):
            if op == "MedianFinder":
                obj = cls()
                results.append(None)
            elif op == "addNum":
                obj.addNum(val[0])
                results.append(None)
            elif op == "findMedian":
                results.append(obj.findMedian())
        return results

    def test_example_1(self):
        """测试题目给定的示例 1"""
        operations = [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian",
        ]
        values = [[], [1], [2], [], [3], []]
        expected = [None, None, None, 1.5, None, 2.0]

        for name, cls in self.algorithms:
            with self.subTest(algorithm=name):
                result = self._run_operations(cls, operations, values)
                self.assertEqual(result, expected)

    def test_example_2(self):
        """测试题目给定的示例 2"""
        operations = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian"]
        values = [[], [2], [], [3], []]
        expected = [None, None, 2.0, None, 2.5]

        for name, cls in self.algorithms:
            with self.subTest(algorithm=name):
                result = self._run_operations(cls, operations, values)
                self.assertEqual(result, expected)

    def test_single_element(self):
        """测试只添加一个元素的情况"""
        operations = ["MedianFinder", "addNum", "findMedian"]
        values = [[], [5], []]
        expected = [None, None, 5.0]

        for name, cls in self.algorithms:
            with self.subTest(algorithm=name):
                result = self._run_operations(cls, operations, values)
                self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """测试包含负数的情况"""
        operations = [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian",
        ]
        values = [[], [-1], [-2], [], [-3], []]
        # 排序后: [-3, -2, -1] -> 中位数是 -2
        expected = [None, None, None, -1.5, None, -2.0]

        for name, cls in self.algorithms:
            with self.subTest(algorithm=name):
                result = self._run_operations(cls, operations, values)
                self.assertEqual(result, expected)

    def test_duplicate_elements(self):
        """测试包含大量重复元素的情况"""
        operations = ["MedianFinder", "addNum", "addNum", "addNum", "findMedian"]
        values = [[], [1], [1], [1], []]
        expected = [None, None, None, None, 1.0]

        for name, cls in self.algorithms:
            with self.subTest(algorithm=name):
                result = self._run_operations(cls, operations, values)
                self.assertEqual(result, expected)

    def test_alternating_large_small(self):
        """测试交替添加极大和极小值（考验堆的平衡能力）"""
        operations = [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "addNum",
            "findMedian",
        ]
        values = [[], [100], [-100], [50], [-50], []]
        # 排序后: [-100, -50, 50, 100] -> 中位数是 (-50 + 50) / 2 = 0
        expected = [None, None, None, None, None, 0.0]

        for name, cls in self.algorithms:
            with self.subTest(algorithm=name):
                result = self._run_operations(cls, operations, values)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
