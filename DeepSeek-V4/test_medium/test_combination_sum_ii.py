import unittest
from typing import List


class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(
                    currList[:]
                )  # 注意：这里应复制列表，原代码直接追加 currList 可能会在后续被修改？但原代码 currList 是新列表，没问题。为安全起见，使用切片复制
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


class TestCombinationSum2(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        result = self.sol.combinationSum2(candidates, target)
        # 排序结果以便比较（题目输出顺序不限）
        result_sorted = sorted([sorted(comb) for comb in result])
        expected_sorted = sorted([sorted(comb) for comb in expected])
        self.assertEqual(result_sorted, expected_sorted)

    def test_example2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        result = self.sol.combinationSum2(candidates, target)
        result_sorted = sorted([sorted(comb) for comb in result])
        expected_sorted = sorted([sorted(comb) for comb in expected])
        self.assertEqual(result_sorted, expected_sorted)

    # ---------- 边界情况 ----------
    def test_no_combination(self):
        candidates = [2, 3, 4]
        target = 1
        self.assertEqual(self.sol.combinationSum2(candidates, target), [])

    def test_single_element_equal(self):
        candidates = [5]
        target = 5
        self.assertEqual(self.sol.combinationSum2(candidates, target), [[5]])

    def test_single_element_not_equal(self):
        candidates = [5]
        target = 3
        self.assertEqual(self.sol.combinationSum2(candidates, target), [])

    def test_duplicate_elements_but_unique_combinations(self):
        candidates = [1, 1, 1]
        target = 2
        expected = [[1, 1]]
        result = self.sol.combinationSum2(candidates, target)
        result_sorted = sorted([sorted(comb) for comb in result])
        expected_sorted = sorted([sorted(comb) for comb in expected])
        self.assertEqual(result_sorted, expected_sorted)

    def test_all_elements_same(self):
        candidates = [2, 2, 2, 2]
        target = 4
        expected = [[2, 2]]
        result = self.sol.combinationSum2(candidates, target)
        result_sorted = sorted([sorted(comb) for comb in result])
        expected_sorted = sorted([sorted(comb) for comb in expected])
        self.assertEqual(result_sorted, expected_sorted)

    def test_large_target_no_comb(self):
        candidates = [1, 2, 3]
        target = 10
        self.assertEqual(self.sol.combinationSum2(candidates, target), [])

    def test_target_zero(self):
        # 题目约束 target >= 1，但算法应能处理 target=0（返回空组合）
        candidates = [1, 2, 3]
        target = 0
        self.assertEqual(
            self.sol.combinationSum2(candidates, target), [[]]
        )  # 通常组合总和问题 target=0 返回包含空列表

    # ---------- 随机测试（与暴力回溯验证）----------
    def test_random_vs_bruteforce(self):
        import random
        from itertools import combinations

        def brute_force(candidates, target):
            # 生成所有非空子集，去重后求和等于 target
            n = len(candidates)
            res_set = set()
            for mask in range(1, 1 << n):
                subset = []
                total = 0
                for i in range(n):
                    if mask >> i & 1:
                        subset.append(candidates[i])
                        total += candidates[i]
                if total == target:
                    res_set.add(tuple(sorted(subset)))
            return [list(comb) for comb in res_set]

        for _ in range(50):
            size = random.randint(1, 10)
            candidates = [random.randint(1, 20) for _ in range(size)]
            target = random.randint(1, 40)
            expected = brute_force(candidates, target)
            result = self.sol.combinationSum2(candidates, target)
            # 排序比较
            result_sorted = sorted([sorted(comb) for comb in result])
            expected_sorted = sorted([sorted(comb) for comb in expected])
            self.assertEqual(
                result_sorted,
                expected_sorted,
                f"Failed for candidates={candidates}, target={target}",
            )

    # ---------- 性能测试（约束内）----------
    def test_performance_max_constraints(self):
        candidates = [i for i in range(1, 51)]  # 1..50，共50个
        target = 30
        import time

        start = time.time()
        result = self.sol.combinationSum2(candidates, target)
        elapsed = time.time() - start
        # 不要求具体结果，只检查时间
        self.assertLess(elapsed, 2.0, f"Performance too slow: {elapsed:.2f}s")
        # 简单验证结果非空（因为1+2+...+7=28, 再加2=30，应有组合）
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
