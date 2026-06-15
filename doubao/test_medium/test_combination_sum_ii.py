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


# ===================== 测试用例代码 =====================
def test_combinationSum2():
    sol = Solution()

    # 定义所有测试用例 (候选数组, 目标, 预期结果)
    test_cases = [
        # 官方示例 1
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        # 官方示例 2
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        # 边界测试：无结果
        ([2, 3, 7], 1, []),
        # 边界测试：全重复元素
        ([1, 1, 1], 2, [[1, 1]]),
        # 边界测试：单个元素
        ([5], 5, [[5]]),
    ]

    # 执行测试
    for idx, (candidates, target, expected) in enumerate(test_cases, 1):
        output = sol.combinationSum2(candidates, target)

        # 排序后比较，避免顺序不同导致误判
        output_sorted = sorted([sorted(item) for item in output])
        expected_sorted = sorted([sorted(item) for item in expected])
        passed = output_sorted == expected_sorted

        print(f"【测试用例 {idx}】")
        print(f"候选数: {candidates}")
        print(f"目标值: {target}")
        print(f"实际输出: {output}")
        print(f"预期输出: {expected}")
        print(f"测试结果: {'✅ 通过' if passed else '❌ 失败'}\n")


if __name__ == "__main__":
    test_combinationSum2()
