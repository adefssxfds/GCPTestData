import unittest


# --- 将你的算法封装为 Solution 类 ---
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


# --- 测试代码 ---
class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
        ]
        for candidates, target, expected in test_cases:
            with self.subTest(candidates=candidates, target=target):
                result = self.solution.combinationSum(candidates, target)
                # 对结果和预期进行排序后比较，防止内部顺序差异导致断言失败
                self.assertEqual(sorted(result), sorted(expected))

    def test_no_valid_combination(self):
        """测试没有任何组合能满足 target 的情况"""
        candidates = [3, 4, 5]
        target = 2
        expected = []
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)

    def test_exact_match(self):
        """测试数组中刚好有元素等于 target 的情况"""
        candidates = [1, 2, 3, 4]
        target = 4
        expected = [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_element_match(self):
        """测试只有一个元素且刚好等于 target 的情况"""
        candidates = [5]
        target = 5
        expected = [[5]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)

    def test_single_element_no_match(self):
        """测试只有一个元素且无法整除 target 的情况"""
        candidates = [3]
        target = 5
        expected = []
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)

    def test_multiple_combinations(self):
        """测试能产生多种组合的情况"""
        candidates = [2, 3]
        target = 6
        expected = [[2, 2, 2], [3, 3]]
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
