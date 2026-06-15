from typing import List


# 你提供的三种解法
def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height

        max_water = max(max_water, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


def max_area_brute_force(height: List[int]) -> int:
    max_water = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            area = width * current_height
            max_water = max(max_water, area)

    return max_water


def max_area_optimized(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        left_height, right_height = height[left], height[right]
        width = right - left

        if left_height < right_height:
            area = left_height * width
            max_water = max(max_water, area)
            left += 1
        else:
            area = right_height * width
            max_water = max(max_water, area)
            right -= 1

    return max_water


# ===================== 测试用例 =====================
def test_all_solutions():
    test_cases = [
        # (输入height, 预期答案)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 10, 5, 7, 8, 9], 36),
        ([0, 2, 0], 0),
    ]

    functions = [
        ("标准双指针 max_area", max_area),
        ("优化双指针 max_area_optimized", max_area_optimized),
        ("暴力解法 max_area_brute_force", max_area_brute_force),
    ]

    for name, func in functions:
        print(f"===== 测试：{name} =====")
        for i, (h, expected) in enumerate(test_cases, 1):
            result = func(h)
            passed = "✅ 通过" if result == expected else "❌ 失败"
            print(f"用例{i}: height={h}")
            print(f"  预期：{expected} | 实际：{result} → {passed}\n")


if __name__ == "__main__":
    test_all_solutions()
