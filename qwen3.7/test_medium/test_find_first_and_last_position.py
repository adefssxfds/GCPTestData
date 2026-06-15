import unittest


# --- 将你的算法封装为 Solution 类 ---
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        # Find first position
        left, right = 0, len(nums) - 1
        first_pos = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1  # Continue searching left for first occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if first_pos == -1:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        last_pos = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first_pos, last_pos]


# --- 测试代码 ---
class TestSearchRange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 0, [-1, -1]),
        ]
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target):
                result = self.solution.searchRange(nums, target)
                self.assertEqual(result, expected)

    def test_single_element_found(self):
        """测试单元素数组且找到目标"""
        nums = [5]
        target = 5
        expected = [0, 0]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)

    def test_single_element_not_found(self):
        """测试单元素数组且未找到目标"""
        nums = [5]
        target = 3
        expected = [-1, -1]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)

    def test_all_same_elements(self):
        """测试数组中所有元素都相同的情况"""
        nums = [2, 2, 2, 2, 2]
        target = 2
        expected = [0, 4]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)

    def test_target_at_boundaries(self):
        """测试目标值在数组最左端和最右端的情况"""
        nums = [1, 2, 3, 4, 5]

        # 目标在最左端
        result_left = self.solution.searchRange(nums, 1)
        self.assertEqual(result_left, [0, 0])

        # 目标在最右端
        result_right = self.solution.searchRange(nums, 5)
        self.assertEqual(result_right, [4, 4])

    def test_target_smaller_than_all(self):
        """测试目标值比数组中最小元素还小"""
        nums = [2, 4, 6, 8]
        target = 1
        expected = [-1, -1]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)

    def test_target_larger_than_all(self):
        """测试目标值比数组中最大元素还大"""
        nums = [2, 4, 6, 8]
        target = 10
        expected = [-1, -1]
        result = self.solution.searchRange(nums, target)
        self.assertEqual(result, expected)

    def test_multiple_occurrences_at_edges(self):
        """测试目标值在数组两端都有多个重复的情况"""
        nums = [1, 1, 2, 3, 3, 3]

        # 目标在左端重复
        result_left = self.solution.searchRange(nums, 1)
        self.assertEqual(result_left, [0, 1])

        # 目标在右端重复
        result_right = self.solution.searchRange(nums, 3)
        self.assertEqual(result_right, [3, 5])


if __name__ == "__main__":
    unittest.main()
