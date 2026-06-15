class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(currList)
                return

            for start in range(index, len(candidates)):
                recursive(
                    candidates,
                    target - candidates[start],
                    currList + [candidates[start]],
                    start,
                )

        recursive(candidates, target, [], 0)
        return result


import unittest


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        res = self.sol.combinationSum([2, 3, 6, 7], 7)
        expect = [[2, 2, 3], [7]]
        self.assertEqual(
            sorted([sorted(x) for x in res]), sorted([sorted(x) for x in expect])
        )

    def test_example2(self):
        res = self.sol.combinationSum([2, 3, 5], 8)
        expect = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(
            sorted([sorted(x) for x in res]), sorted([sorted(x) for x in expect])
        )

    def test_example3_no_solution(self):
        self.assertEqual(self.sol.combinationSum([2], 1), [])

    def test_single_exact_match(self):
        self.assertEqual(self.sol.combinationSum([5], 5), [[5]])


if __name__ == "__main__":
    unittest.main()
