import unittest


# --- 将你的算法和 Interval 类放在这里 ---
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        for interval in intervals:
            if newInterval.start > interval.end:
                result.append(interval)
            elif newInterval.end < interval.start:
                result.append(newInterval)
                newInterval = interval
            elif newInterval.start <= interval.end or newInterval.end >= interval.start:
                newInterval = Interval(
                    min(newInterval.start, interval.start),
                    max(interval.end, newInterval.end),
                )
        result.append(newInterval)
        return result


# --- 测试代码 ---
class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _to_interval_list(self, lst):
        """辅助方法：将二维列表转换为 Interval 对象列表"""
        return [Interval(s, e) for s, e in lst]

    def _to_list_of_lists(self, intervals):
        """辅助方法：将 Interval 对象列表转换回二维列表，方便断言"""
        return [[i.start, i.end] for i in intervals]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            (
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                [4, 8],
                [[1, 2], [3, 10], [12, 16]],
            ),
        ]
        for intervals_list, new_interval, expected in test_cases:
            with self.subTest(intervals=intervals_list, newInterval=new_interval):
                intervals = self._to_interval_list(intervals_list)
                new_int = Interval(new_interval[0], new_interval[1])
                result = self.solution.insert(intervals, new_int)
                self.assertEqual(self._to_list_of_lists(result), expected)

    def test_empty_intervals(self):
        """测试原区间列表为空的情况"""
        intervals = []
        new_interval = [5, 7]
        expected = [[5, 7]]

        intervals = self._to_interval_list(intervals)
        new_int = Interval(new_interval[0], new_interval[1])
        result = self.solution.insert(intervals, new_int)
        self.assertEqual(self._to_list_of_lists(result), expected)

    def test_no_overlap_insert_at_beginning(self):
        """测试无重叠，且新区间插入到最前面的情况"""
        intervals = [[3, 5], [6, 9]]
        new_interval = [1, 2]
        expected = [[1, 2], [3, 5], [6, 9]]

        intervals = self._to_interval_list(intervals)
        new_int = Interval(new_interval[0], new_interval[1])
        result = self.solution.insert(intervals, new_int)
        self.assertEqual(self._to_list_of_lists(result), expected)

    def test_no_overlap_insert_at_end(self):
        """测试无重叠，且新区间插入到最后面的情况"""
        intervals = [[1, 2], [3, 5]]
        new_interval = [6, 8]
        expected = [[1, 2], [3, 5], [6, 8]]

        intervals = self._to_interval_list(intervals)
        new_int = Interval(new_interval[0], new_interval[1])
        result = self.solution.insert(intervals, new_int)
        self.assertEqual(self._to_list_of_lists(result), expected)

    def test_merge_all(self):
        """测试新区间覆盖了所有原有区间的情况"""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10]]
        new_interval = [0, 15]
        expected = [[0, 15]]

        intervals = self._to_interval_list(intervals)
        new_int = Interval(new_interval[0], new_interval[1])
        result = self.solution.insert(intervals, new_int)
        self.assertEqual(self._to_list_of_lists(result), expected)

    def test_exact_boundary_touch(self):
        """测试区间刚好首尾相接的情况（例如 [1,2] 和 [3,4] 不重叠，但 [1,3] 和 [3,4] 会重叠）"""
        intervals = [[1, 2], [4, 5]]
        new_interval = [2, 4]  # 与 [1,2] 和 [4,5] 都产生边界重叠
        expected = [[1, 5]]

        intervals = self._to_interval_list(intervals)
        new_int = Interval(new_interval[0], new_interval[1])
        result = self.solution.insert(intervals, new_int)
        self.assertEqual(self._to_list_of_lists(result), expected)

    def test_single_interval_merge(self):
        """测试原列表只有一个区间且发生合并的情况"""
        intervals = [[2, 5]]
        new_interval = [1, 3]
        expected = [[1, 5]]

        intervals = self._to_interval_list(intervals)
        new_int = Interval(new_interval[0], new_interval[1])
        result = self.solution.insert(intervals, new_int)
        self.assertEqual(self._to_list_of_lists(result), expected)


if __name__ == "__main__":
    unittest.main()
