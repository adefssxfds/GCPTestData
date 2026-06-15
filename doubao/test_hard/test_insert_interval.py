import unittest


class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        ns, ne = newInterval[0], newInterval[1]

        for s, e in intervals:
            if e < ns:
                res.append([s, e])
            elif s > ne:
                res.append([ns, ne])
                ns, ne = s, e
            else:
                ns = min(ns, s)
                ne = max(ne, e)
        res.append([ns, ne])
        return res


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        intervals = [[1, 3], [6, 9]]
        newInt = [2, 5]
        self.assertEqual(self.sol.insert(intervals, newInt), [[1, 5], [6, 9]])

    def test_example2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInt = [4, 8]
        self.assertEqual(
            self.sol.insert(intervals, newInt), [[1, 2], [3, 10], [12, 16]]
        )

    def test_new_at_left(self):
        intervals = [[3, 5], [7, 9]]
        newInt = [1, 2]
        self.assertEqual(self.sol.insert(intervals, newInt), [[1, 2], [3, 5], [7, 9]])

    def test_new_at_right(self):
        intervals = [[1, 2], [3, 5]]
        newInt = [6, 8]
        self.assertEqual(self.sol.insert(intervals, newInt), [[1, 2], [3, 5], [6, 8]])

    def test_empty_intervals(self):
        intervals = []
        newInt = [5, 7]
        self.assertEqual(self.sol.insert(intervals, newInt), [[5, 7]])

    def test_fully_cover_all(self):
        intervals = [[2, 3], [4, 5], [6, 7]]
        newInt = [1, 8]
        self.assertEqual(self.sol.insert(intervals, newInt), [[1, 8]])


if __name__ == "__main__":
    unittest.main()
