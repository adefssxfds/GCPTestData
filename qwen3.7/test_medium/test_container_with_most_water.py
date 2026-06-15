import unittest
from typing import List


# --- 将你的三个算法放在这里 ---
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


# --- 测试代码 ---
class TestMaxArea(unittest.TestCase):
    def setUp(self):
        # 统一管理三种求解算法
        self.area_funcs = [max_area, max_area_brute_force, max_area_optimized]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
        for height, expected in test_cases:
            for func in self.area_funcs:
                with self.subTest(func=func.__name__, height=height):
                    self.assertEqual(func(height), expected)

    def test_ascending_heights(self):
        """测试单调递增的高度"""
        height = [1, 2, 3, 4, 5]
        expected = 6  # 选择 index=0(1) 和 index=4(5), 宽度4 * 高度1 = 4?
        # 不对，选 index=1(2) 和 index=4(5), 宽度3 * 高度2 = 6
        for func in self.area_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(height), expected)

    def test_descending_heights(self):
        """测试单调递减的高度"""
        height = [5, 4, 3, 2, 1]
        expected = 6  # 选择 index=0(5) 和 index=3(2), 宽度3 * 高度2 = 6
        for func in self.area_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(height), expected)

    def test_uniform_heights(self):
        """测试所有高度相同的情况"""
        height = [3, 3, 3, 3, 3]
        expected = 12  # 选择最外侧的两个，宽度4 * 高度3 = 12
        for func in self.area_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(height), expected)

    def test_minimum_length(self):
        """测试最小长度 (n=2) 的情况"""
        height = [4, 7]
        expected = 4  # 宽度1 * min(4,7) = 4
        for func in self.area_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(height), expected)

    def test_with_zero_height(self):
        """测试包含高度为 0 的情况"""
        height = [0, 5, 0, 5]
        expected = 5  # 选择 index=1(5) 和 index=3(5), 宽度2 * 高度5 = 10
        # 等等，重新算：index=1 和 index=3 宽度是 2，面积是 10。
        # 修正预期：
        expected = 10
        for func in self.area_funcs:
            with self.subTest(func=func.__name__):
                self.assertEqual(func(height), expected)


if __name__ == "__main__":
    unittest.main()
