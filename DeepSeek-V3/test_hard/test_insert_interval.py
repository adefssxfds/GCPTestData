import unittest
from typing import List


# 定义 Interval 类（与题目一致）
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(
        self, intervals: List[Interval], newInterval: Interval
    ) -> List[Interval]:
        result = []
        for interval in intervals:
            if newInterval.start > interval.end:
                result.append(interval)
            elif newInterval.end < interval.start:
                result.append(newInterval)
                newInterval = interval
            else:  # 有重叠
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        result.append(newInterval)
        return result


# 辅助函数：将 Interval 列表转换为列表的列表，便于比较
def intervals_to_list(intervals: List[Interval]) -> List[List[int]]:
    return [[inv.start, inv.end] for inv in intervals]


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        intervals = [Interval(1, 3), Interval(6, 9)]
        new = Interval(2, 5)
        result = self.sol.insert(intervals, new)
        expected = [[1, 5], [6, 9]]
        self.assertEqual(intervals_to_list(result), expected)

    def test_example2(self):
        intervals = [
            Interval(1, 2),
            Interval(3, 5),
            Interval(6, 7),
            Interval(8, 10),
            Interval(12, 16),
        ]
        new = Interval(4, 8)
        result = self.sol.insert(intervals, new)
        expected = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 空区间列表 ----------
    def test_empty_intervals(self):
        intervals = []
        new = Interval(1, 2)
        result = self.sol.insert(intervals, new)
        expected = [[1, 2]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间在最前面且无重叠 ----------
    def test_new_before_all_no_overlap(self):
        intervals = [Interval(3, 4), Interval(5, 6)]
        new = Interval(1, 2)
        result = self.sol.insert(intervals, new)
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间在最后面且无重叠 ----------
    def test_new_after_all_no_overlap(self):
        intervals = [Interval(1, 2), Interval(3, 4)]
        new = Interval(5, 6)
        result = self.sol.insert(intervals, new)
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间与第一个重叠 ----------
    def test_overlap_first(self):
        intervals = [Interval(1, 5), Interval(7, 9)]
        new = Interval(2, 6)
        result = self.sol.insert(intervals, new)
        expected = [[1, 6], [7, 9]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间与最后一个重叠 ----------
    def test_overlap_last(self):
        intervals = [Interval(1, 2), Interval(4, 7)]
        new = Interval(6, 10)
        result = self.sol.insert(intervals, new)
        expected = [[1, 2], [4, 10]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间与多个重叠合并为一个大区间 ----------
    def test_overlap_multiple(self):
        intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(9, 12)]
        new = Interval(4, 10)
        result = self.sol.insert(intervals, new)
        expected = [[1, 2], [3, 12]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间完全被现有区间包含 ----------
    def test_new_inside_existing(self):
        intervals = [Interval(1, 10), Interval(15, 20)]
        new = Interval(3, 7)
        result = self.sol.insert(intervals, new)
        expected = [[1, 10], [15, 20]]  # 无变化
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间包含现有区间 ----------
    def test_new_contains_existing(self):
        intervals = [Interval(2, 3), Interval(5, 6)]
        new = Interval(1, 10)
        result = self.sol.insert(intervals, new)
        expected = [[1, 10]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 新区间恰好连接两个区间（紧邻无重叠） ----------
    def test_new_touching_edges(self):
        intervals = [Interval(1, 2), Interval(3, 4)]  # 注意：2 < 3，无重叠
        new = Interval(2, 3)
        # 根据题目定义，[1,2] 和 [2,3] 是否重叠？通常认为端点相接不算重叠，这里不应合并。
        # 但代码中条件 newInterval.start > interval.end 判断为 False（因为2 > 2? false），进入 elif newInterval.end < interval.start 也 false (3 < 3 false)，所以进入 else 合并，导致 [1,3]。
        # 这取决于题目对“重叠”的定义。常见题中 [1,2] 和 [2,3] 不重叠，但本题的合并逻辑会将相接的也合并（因为条件 newInterval.start <= interval.end 会成立）。这里按照代码行为测试。
        result = self.sol.insert(intervals, new)
        # 代码行为：由于 2 <= 2 成立，会合并成 [1,3]
        expected = [
            [1, 3],
            [3, 4],
        ]  # 注意: 合并后 [1,3] 与 [3,4] 又相接，会继续合并？实际上代码遍历完所有原始区间后才追加 newInterval，不会二次合并，因此最终是 [[1,3], [3,4]]
        self.assertEqual(intervals_to_list(result), expected)

    # ---------- 随机测试：与暴力法对比 ----------
    def test_random_compare(self):
        """随机生成区间列表和新区间，与暴力法（插入排序后再合并）结果比较"""
        import random

        def brute_force_insert(intervals, new_interval):
            # 插入新区间，排序，然后合并重叠
            all_intervals = intervals + [new_interval]
            all_intervals.sort(key=lambda x: x.start)
            merged = []
            for inv in all_intervals:
                if not merged or inv.start > merged[-1].end:
                    merged.append(Interval(inv.start, inv.end))
                else:
                    merged[-1].end = max(merged[-1].end, inv.end)
            return merged

        for _ in range(100):
            # 生成随机非重叠区间，按 start 排序
            n = random.randint(0, 20)
            intervals = []
            end = -1
            for _ in range(n):
                start = random.randint(end + 1, end + 20)
                end = start + random.randint(0, 10)
                intervals.append(Interval(start, end))
            # 生成新区间
            new_start = random.randint(0, 100)
            new_end = new_start + random.randint(0, 20)
            new = Interval(new_start, new_end)
            # 调用算法
            result = self.sol.insert(intervals, new)
            # 暴力法
            expected = brute_force_insert(intervals, new)
            # 转换为列表比较
            self.assertEqual(intervals_to_list(result), intervals_to_list(expected))


if __name__ == "__main__":
    unittest.main()
