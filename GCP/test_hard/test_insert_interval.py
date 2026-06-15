import pytest
from insert_interval import Interval, Solution


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if not isinstance(other, Interval):
            return False
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"


def test_insert_example1():
    solution = Solution()
    intervals = [Interval(1, 3), Interval(6, 9)]
    new_interval = Interval(2, 5)
    expected = [Interval(1, 5), Interval(6, 9)]
    result = [Interval(interval.start, interval.end) for interval in solution.insert(intervals, new_interval)]
    assert result == expected


def test_insert_example2():
    solution = Solution()
    intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    new_interval = Interval(4, 8)
    expected = [Interval(1, 2), Interval(3, 10), Interval(12, 16)]
    result = [Interval(interval.start, interval.end) for interval in solution.insert(intervals, new_interval)]
    assert result == expected


def test_insert_no_overlap():
    solution = Solution()
    intervals = [Interval(1, 5), Interval(10, 15)]
    new_interval = Interval(6, 9)
    expected = [Interval(1, 5), Interval(6, 9), Interval(10, 15)]
    result = [Interval(interval.start, interval.end) for interval in solution.insert(intervals, new_interval)]
    assert result == expected


def test_insert_full_overlap():
    solution = Solution()
    intervals = [Interval(1, 5), Interval(5, 10)]
    new_interval = Interval(3, 8)
    expected = [Interval(1, 8)]
    result = [Interval(interval.start, interval.end) for interval in solution.insert(intervals, new_interval)]
    assert result == expected


def test_insert_multiple_overlaps():
    solution = Solution()
    intervals = [Interval(1, 5), Interval(5, 10), Interval(10, 15)]
    new_interval = Interval(3, 20)
    expected = [Interval(1, 20)]
    result = [Interval(interval.start, interval.end) for interval in solution.insert(intervals, new_interval)]
    assert result == expected