class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        # 查找左边界
        left, right = 0, len(nums) - 1
        first_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if first_pos == -1:
            return [-1, -1]
        
        # 查找右边界
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


import unittest

class TestSearchRange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # 题目示例1：目标存在且重复
    def test_example1(self):
        self.assertEqual(self.solution.searchRange([5,7,7,8,8,10], 8), [3, 4])

    # 题目示例2：目标不存在
    def test_example2(self):
        self.assertEqual(self.solution.searchRange([5,7,7,8,8,10], 6), [-1, -1])

    # 题目示例3：空数组
    def test_example3(self):
        self.assertEqual(self.solution.searchRange([], 0), [-1, -1])

    # 单元素数组，元素等于目标
    def test_single_element_match(self):
        self.assertEqual(self.solution.searchRange([9], 9), [0, 0])

    # 单元素数组，元素不等于目标
    def test_single_element_not_match(self):
        self.assertEqual(self.solution.searchRange([9], 2), [-1, -1])

    # 数组全部元素都是目标值
    def test_all_same_elements(self):
        self.assertEqual(self.solution.searchRange([2,2,2,2], 2), [0, 3])

    # 目标出现在数组最左端
    def test_target_at_left(self):
        self.assertEqual(self.solution.searchRange([1,1,2,3,4], 1), [0, 1])

    # 目标出现在数组最右端
    def test_target_at_right(self):
        self.assertEqual(self.solution.searchRange([1,2,3,4,4], 4), [3, 4])

    # 目标仅出现一次（数组中间）
    def test_target_once_middle(self):
        self.assertEqual(self.solution.searchRange([1,3,5,7,9], 5), [2, 2])

if __name__ == '__main__':
    unittest.main()