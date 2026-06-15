import unittest


# --- 将你的算法放在这里 ---
class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        if nums[0] <= 0:
            return 0

        steps, currentEnd, farthest = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                steps += 1
                currentEnd = farthest

                if currentEnd >= len(nums) - 1:
                    break

        return steps if farthest >= len(nums) - 1 else 0


# --- 测试代码 ---
class TestJump(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([2, 3, 1, 1, 4], 2),
            ([2, 3, 0, 1, 4], 2),
            ([1, 1, 1, 1, 1], 4),  # 每次只能跳 1 步
        ]
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                result = self.solution.jump(nums)
                self.assertEqual(result, expected)

    def test_single_element(self):
        """测试只有一个元素的情况（已经在终点，不需要跳跃）"""
        nums = [0]
        expected = 0
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_two_elements(self):
        """测试只有两个元素的情况"""
        nums = [1, 0]
        expected = 1
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_can_jump_in_one_step(self):
        """测试一步就能跳到终点的情况"""
        nums = [5, 1, 1, 1, 1]
        expected = 1
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_cannot_reach_end(self):
        """测试无论如何也跳不到终点的情况（返回 0）"""
        nums = [1, 2, 0, 1]  # 最多只能到索引 2，然后卡住
        expected = 0
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_zero_at_start(self):
        """测试起点就是 0 且长度大于 1 的情况（无法移动）"""
        nums = [0, 2, 3]
        expected = 0
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_large_jump_in_middle(self):
        """测试中间有巨大跳跃能力的情况"""
        nums = [1, 1, 10, 1, 1, 1]
        expected = 2  # 0 -> 1 -> 5 (或者 0 -> 2 -> 5)
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_descending_steps(self):
        """测试递减的步数"""
        nums = [4, 3, 2, 1, 0]
        expected = 1  # 从索引 0 直接跳到索引 4
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
