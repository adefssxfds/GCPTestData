import unittest


# --- 将你的算法封装为 Solution 类 ---
class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(currList)
                return

            previous = -1
            for start in range(index, len(candidates)):
                if previous != candidates[start]:
                    recursive(
                        candidates,
                        target - candidates[start],
                        currList + [candidates[start]],
                        start + 1,
                    )
                    previous = candidates[start]

        recursive(candidates, target, [], 0)
        return result


# --- 测试代码 ---
class TestCombinationSum2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
            ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ]
        for candidates, target, expected in test_cases:
            with self.subTest(candidates=candidates, target=target):
                result = self.solution.combinationSum2(candidates, target)
                # 对结果和预期进行排序后比较，防止内部顺序差异导致断言失败
                self.assertEqual(sorted(result), sorted(expected))

    def test_no_valid_combination(self):
        """测试没有任何组合能满足 target 的情况"""
        candidates = [1, 2, 3]
        target = 10
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)

    def test_all_duplicates(self):
        """测试全是重复元素的情况"""
        candidates = [2, 2, 2, 2]
        target = 4
        expected = [[2, 2]]  # 只能选两个2，且不能产生重复组合
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)

    def test_exact_match(self):
        """测试数组中刚好有元素等于 target 的情况"""
        candidates = [1, 2, 3, 4]
        target = 4
        expected = [[1, 3], [4]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_element(self):
        """测试只有一个元素的情况"""
        candidates = [5]
        target = 5
        expected = [[5]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)

    def test_target_smaller_than_all(self):
        """测试 target 比数组中最小元素还小的情况"""
        candidates = [3, 4, 5]
        target = 2
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
