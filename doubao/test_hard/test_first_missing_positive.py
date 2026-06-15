import unittest


class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        index_i = 0
        for index_j in range(n):
            if nums[index_j] <= 0:
                nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
                index_i += 1

        for index in range(index_i, n):
            x = abs(nums[index])
            if 1 <= x <= n:
                pos = x - 1
                if nums[pos] > 0:
                    nums[pos] = -nums[pos]

        for idx in range(n):
            if nums[idx] > 0:
                return idx + 1
        return n + 1


class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 0]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 3)

    def test_case2(self):
        nums = [3, 4, -1, 1]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 2)

    def test_case3(self):
        nums = [7, 8, 9, 11, 12]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 1)

    def test_all_complete(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 5)

    def test_only_one_negative(self):
        nums = [-5]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 1)

    def test_only_one_pos(self):
        nums = [1]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 2)

    def test_dup_num(self):
        nums = [2, 2]
        self.assertEqual(self.sol.firstMissingPositive(nums.copy()), 1)


if __name__ == "__main__":
    unittest.main()
