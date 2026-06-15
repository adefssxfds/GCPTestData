import unittest


class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        steps = 0
        currentEnd = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                steps += 1
                currentEnd = farthest
                if currentEnd >= n - 1:
                    break
        return steps


class TestJump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.jump([2, 3, 1, 1, 4]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.jump([2, 1]), 1)

    def test_single_element(self):
        self.assertEqual(self.sol.jump([5]), 0)

    def test_all_one(self):
        self.assertEqual(self.sol.jump([1, 1, 1, 1]), 3)

    def test_first_jump_reach_end(self):
        self.assertEqual(self.sol.jump([5, 1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
