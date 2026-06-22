import unittest
from typing import List


class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(currList[:])  # 复制列表，避免后续修改
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


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = self.sol.combinationSum(candidates, target)
        # 排序后比较（顺序无关）
        result_sorted = sorted([sorted(comb) for comb in result])
        expected_sorted = sorted([sorted(comb) for comb in expected])
        self.assertEqual(result_sorted, expected_sorted)

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result = self.sol.combinationSum(candidates, target)
        result_sorted = sorted([sorted(comb) for comb in result])
        expected_sorted = sorted([sorted(comb) for comb in expected])
        self.assertEqual(result_sorted, expected_sorted)

    def test_example3(self):
        candidates = [2]
        target = 1
        expected = []
        self.assertEqual(self.sol.combinationSum(candidates, target), expected)

    # ---------- 边界情况 ----------
    def test_target_equal_candidate(self):
        candidates = [4, 5, 6]
        target = 5
        expected = [[5]]
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, expected)

    def test_target_zero(self):
        # 根据题目描述 target >= 1，但算法应能处理 target=0（返回 [[]] 或 []？通常返回 [] 或 [[]]？）
        # 这里按算法实际行为：递归到 target==0 时加入当前列表，初始 currList=[]，所以会返回 [[]]
        candidates = [2, 3]
        target = 0
        expected = [[]]  # 空组合
        self.assertEqual(self.sol.combinationSum(candidates, target), expected)

    def test_no_combination(self):
        candidates = [3, 4]
        target = 5
        self.assertEqual(self.sol.combinationSum(candidates, target), [])

    def test_all_candidates_greater_than_target(self):
        candidates = [5, 6, 7]
        target = 4
        self.assertEqual(self.sol.combinationSum(candidates, target), [])

    # ---------- 重复使用同一数字（基础）----------
    def test_single_candidate_multiple_use(self):
        candidates = [2]
        target = 6
        expected = [[2, 2, 2]]
        self.assertEqual(self.sol.combinationSum(candidates, target), expected)

    # ---------- 随机测试与暴力递归对比（小规模）----------
    def test_random_compare_with_bruteforce(self):
        import random
        from itertools import combinations_with_replacement

        def brute_force(candidates, target):
            # 暴力枚举所有可能的组合（使用重复组合），因为 candidates 长度小，target<=40
            result_set = set()
            # 最大重复次数为 target // min(candidates)
            max_count = target // min(candidates) if candidates else 0
            for length in range(1, max_count + 1):
                for comb in combinations_with_replacement(candidates, length):
                    if sum(comb) == target:
                        result_set.add(tuple(sorted(comb)))
            return [list(comb) for comb in result_set]

        for _ in range(50):
            # 随机生成 distinct candidates，长度 1~5，值 2~20
            size = random.randint(1, 5)
            candidates = sorted(set(random.randint(2, 20) for _ in range(size)))
            target = random.randint(1, 30)
            expected = brute_force(candidates, target)
            result = self.sol.combinationSum(candidates, target)
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
        candidates = list(range(2, 42))  # 2..41，共40个
        target = 40
        import time

        start = time.time()
        result = self.sol.combinationSum(candidates, target)
        elapsed = time.time() - start
        # 确保结果数量不超过 150（题目保证）
        self.assertLessEqual(len(result), 150)
        self.assertLess(elapsed, 2.0, f"Performance too slow: {elapsed:.2f}s")
        # 简单验证几个已知组合
        self.assertTrue(any(comb == [40] for comb in result))


if __name__ == "__main__":
    unittest.main()
