from typing import List


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0

    curr_sum, result = nums[0], nums[0]

    for index in range(1, len(nums)):
        curr_sum = max(nums[index], curr_sum + nums[index])
        result = max(result, curr_sum)

    return result


def max_sub_array_divide_conquer(nums: List[int]) -> int:
    def max_crossing_sum(nums: List[int], left: int, mid: int, right: int) -> int:
        left_sum = float("-inf")
        sum_val = 0
        for i in range(mid, left - 1, -1):
            sum_val += nums[i]
            left_sum = max(left_sum, sum_val)
        right_sum = float("-inf")
        sum_val = 0
        for i in range(mid + 1, right + 1):
            sum_val += nums[i]
            right_sum = max(right_sum, sum_val)

        return left_sum + right_sum

    def max_subarray_rec(nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        left_max = max_subarray_rec(nums, left, mid)
        right_max = max_subarray_rec(nums, mid + 1, right)
        cross_max = max_crossing_sum(nums, left, mid, right)

        return max(left_max, right_max, cross_max)

    if not nums:
        return 0

    return max_subarray_rec(nums, 0, len(nums) - 1)


def max_sub_array_with_indices(nums: List[int]) -> tuple[int, int, int]:
    if not nums:
        return 0, -1, -1

    max_sum = curr_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return max_sum, start, end


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试用例：(输入数组, 预期最大和)
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # 示例1
        ([1], 1),  # 示例2
        ([5, 4, -1, 7, 8], 23),  # 示例3
        ([-1], -1),  # 全负数
        ([-5, -3, -2], -2),  # 全负数
        ([2, -1, 2], 3),  # 中间起伏
        ([1, -2, 3, -1, 2], 4),  # 常规测试
    ]

    print("===== 最大子数组和 测试开始 =====\n")

    for idx, (nums, expect) in enumerate(test_cases, 1):
        print(f"测试用例 {idx}")
        print(f"输入: {nums}")
        print(f"预期最大和: {expect}")

        # 测试 Kadane 算法
        res1 = max_sub_array(nums)
        print(f"  Kadane算法: {res1} {'✅ 通过' if res1 == expect else '❌ 失败'}")

        # 测试分治法
        res2 = max_sub_array_divide_conquer(nums)
        print(f"  分治法: {res2} {'✅ 通过' if res2 == expect else '❌ 失败'}")

        # 测试带坐标版本
        res3, start, end = max_sub_array_with_indices(nums)
        print(
            f"  带下标版本: 和={res3}, 起始={start}, 结束={end} {'✅ 通过' if res3 == expect else '❌ 失败'}"
        )

        print("-" * 50)

    print("\n===== 所有测试完成 =====")
