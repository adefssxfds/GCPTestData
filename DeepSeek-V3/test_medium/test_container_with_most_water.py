import unittest
import random
from typing import List

# 三种实现（复制自题目）
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


class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        # 定义待测试的算法（暴力法仅用于小规模验证）
        self.algorithms = [
            ("双指针标准", max_area),
            ("双指针优化", max_area_optimized)
        ]
        self.brute_force = max_area_brute_force

    # ---------- 题目示例 ----------
    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_example2(self):
        height = [1, 1]
        expected = 1
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    # ---------- 边界情况 ----------
    def test_min_length(self):
        height = [2, 3]
        expected = 2  # min(2,3) * 1 = 2
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_increasing_heights(self):
        height = [1, 2, 3, 4, 5]
        # 最大面积：5和1? 实际应选两端？计算：左1右5 -> min=1, width=4 -> 4; 左2右5 -> min=2, width=3 -> 6; 左3右5 -> 3*2=6; 左4右5 -> 4*1=4. 所以最大6。
        expected = 6
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_decreasing_heights(self):
        height = [5, 4, 3, 2, 1]
        # 对称，最大面积也是6
        expected = 6
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_same_height(self):
        height = [5, 5, 5, 5]
        expected = 15  # width=3, min=5
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_zeros(self):
        height = [0, 0, 0]
        expected = 0
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_single_zero_and_positive(self):
        height = [0, 5, 0]
        # 最大面积：5和0得0，或5和0得0，或两个0得0
        expected = 0
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height), expected)

    def test_large_peak_in_middle(self):
        height = [1, 2, 100, 2, 1]
        # 最大面积：两端1*4=4，但用100和2? 实际100和2距离3得6，100和1距离4得4，所以最大6？但100与2（位置1和3）min=2, width=2 -> 4；100与1（位置0和2）min=1, width=2->2；实际更优的是100与右侧2（位置2和3）min=2, width=1 -> 2。所以不如两端？计算两端1和1 width=4 -> 4。但内部100和另一端？最大应该是100和2（索引2和4）min=2, width=2 -> 4。实际上最大是4。不过我们考虑[1,8,6,2,5,4,8,3,7]已经很大了。这个用例只是展示。
        # 改为更有代表性的：输入[1,100,1] -> 1*2=2；[1,100,2] -> min(1,2)*2=2；[2,100,1] -> min(2,1)*2=2。所以最大在两端。
        # 这里保持简单，不纠结。
        height2 = [1, 100, 1]
        expected = 2
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                self.assertEqual(func(height2), expected)

    # ---------- 随机对比（小规模，与暴力法）----------
    def test_random_small_compare_with_bruteforce(self):
        """随机生成小数组（长度 ≤ 20），对比双指针与暴力法结果"""
        for _ in range(100):
            length = random.randint(2, 20)
            height = [random.randint(0, 100) for _ in range(length)]
            expected = self.brute_force(height)
            for name, func in self.algorithms:
                with self.subTest(algorithm=name, height=height):
                    self.assertEqual(func(height), expected)

    # ---------- 性能测试（大数组）----------
    def test_performance_large(self):
        import time
        n = 100000
        height = [random.randint(0, 10000) for _ in range(n)]
        start = time.time()
        result = max_area(height)
        elapsed = time.time() - start
        self.assertLess(elapsed, 1.0, f"双指针算法耗时 {elapsed:.2f}s 超过1秒")
        # 结果应为非负整数
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()