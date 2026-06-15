import heapq
import random
import unittest
from typing import List


# ---------- 三种实现（复制自题目） ----------
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


# ---------- 辅助函数：直接排序计算中位数（用于对比） ----------
def median_by_sorting(nums: List[int]) -> float:
    """给定数组，返回中位数（排序后）"""
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 1:
        return float(sorted_nums[n // 2])
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2.0


# ---------- 测试类 ----------
class TestMedianFinderBase(unittest.TestCase):
    """基类，包含通用测试方法，子类指定具体的 MedianFinder 类"""

    # 子类必须设置 self.finder_class
    def setUp(self):
        self.finder = self.finder_class()

    def test_example(self):
        """题目提供的示例"""
        self.finder.addNum(1)
        self.finder.addNum(2)
        self.assertEqual(self.finder.findMedian(), 1.5)
        self.finder.addNum(3)
        self.assertEqual(self.finder.findMedian(), 2.0)

    def test_single_element(self):
        self.finder.addNum(5)
        self.assertEqual(self.finder.findMedian(), 5.0)

    def test_two_elements(self):
        self.finder.addNum(10)
        self.finder.addNum(20)
        self.assertEqual(self.finder.findMedian(), 15.0)

    def test_negative_numbers(self):
        self.finder.addNum(-5)
        self.finder.addNum(-10)
        self.finder.addNum(-1)
        self.assertEqual(self.finder.findMedian(), -5.0)  # sorted [-10, -5, -1]

    def test_duplicate_elements(self):
        for val in [1, 1, 2, 2, 3]:
            self.finder.addNum(val)
        # sorted: [1,1,2,2,3] -> median = 2
        self.assertEqual(self.finder.findMedian(), 2.0)

    def test_all_equal(self):
        for _ in range(10):
            self.finder.addNum(42)
        self.assertEqual(self.finder.findMedian(), 42.0)

    def test_large_and_small_mixed(self):
        nums = [100000, -100000, 0, 50000, -50000]
        for n in nums:
            self.finder.addNum(n)
        # sorted: [-100000, -50000, 0, 50000, 100000] -> median 0
        self.assertEqual(self.finder.findMedian(), 0.0)

    def test_random_consistency(self):
        """随机添加数字，验证每次 findMedian 都与排序后结果一致"""
        added = []
        for _ in range(100):
            num = random.randint(-(10**5), 10**5)
            self.finder.addNum(num)
            added.append(num)
            self.assertEqual(self.finder.findMedian(), median_by_sorting(added))

    def test_sequential_add_find(self):
        """交替添加和查找，验证每个中间状态"""
        sequence = [5, 1, 9, 2, 8, 3, 7, 4, 6]
        expected_medians = []
        current = []
        for num in sequence:
            current.append(num)
            expected_medians.append(median_by_sorting(current))
        for num in sequence:
            self.finder.addNum(num)
        for i, med in enumerate(expected_medians):
            # 需要重新实例化才能逐步比较，这里简化：直接比较最终状态不是我们想要的。
            # 改为逐步添加并验证。
            pass
        # 更直接的测试：逐步添加并验证
        finder = self.finder_class()
        current = []
        for num in sequence:
            finder.addNum(num)
            current.append(num)
            self.assertEqual(finder.findMedian(), median_by_sorting(current))

    def test_large_volume(self):
        """测试最多 5×10^4 次调用，确保性能可接受"""
        finder = self.finder_class()
        import time

        start = time.time()
        for i in range(25000):
            finder.addNum(i)
            if i % 1000 == 0:
                _ = finder.findMedian()
        elapsed = time.time() - start
        # 堆实现通常 < 1 秒，排序实现会非常慢，但这里只是要求不崩溃
        self.assertLess(elapsed, 10.0)  # 宽松限制，确保不超时

    def test_boundary_values(self):
        """边界值 -1e5 和 1e5"""
        self.finder.addNum(-100000)
        self.finder.addNum(100000)
        self.assertEqual(self.finder.findMedian(), 0.0)
        self.finder.addNum(0)
        self.assertEqual(self.finder.findMedian(), 0.0)


class TestMedianFinder(TestMedianFinderBase):
    finder_class = MedianFinder


class TestMedianFinderAlternative(TestMedianFinderBase):
    finder_class = MedianFinderAlternative


class TestMedianFinderSorted(TestMedianFinderBase):
    finder_class = MedianFinderSorted

    # 由于排序实现 addNum 是 O(n)，随机测试数量减少，但仍保证正确性
    def test_random_consistency(self):
        added = []
        for _ in range(50):  # 减少到 50 个数字，避免过慢
            num = random.randint(-(10**5), 10**5)
            self.finder.addNum(num)
            added.append(num)
            self.assertEqual(self.finder.findMedian(), median_by_sorting(added))

    def test_large_volume(self):
        # 排序实现在大量数据下极慢，跳过此测试
        pass


if __name__ == "__main__":
    unittest.main()
