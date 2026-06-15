class Solution(object):
    def numDistinct(self, s, t):
        row, col = len(s), len(t)

        if col > row:
            return 0

        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for r in range(row + 1):
            for c in range(col + 1):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] = 0
                elif c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c]
                    if s[r - 1] == t[c - 1]:
                        dp[r][c] += dp[r - 1][c - 1]
        return dp[row][col]


import unittest


class TestNumDistinct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # 示例1
    def test_example1(self):
        self.assertEqual(self.sol.numDistinct("rabbbit", "rabbit"), 3)

    # 示例2
    def test_example2(self):
        self.assertEqual(self.sol.numDistinct("babgbag", "bag"), 5)

    # t更长，直接返回0
    def test_t_longer(self):
        self.assertEqual(self.sol.numDistinct("abc", "abcd"), 0)

    # s和t完全相同
    def test_equal_str(self):
        self.assertEqual(self.sol.numDistinct("abc", "abc"), 1)

    # 无匹配字符
    def test_no_match(self):
        self.assertEqual(self.sol.numDistinct("abcde", "f"), 0)

    # 单字符相等
    def test_single_equal(self):
        self.assertEqual(self.sol.numDistinct("a", "a"), 1)

    # 单字符不等
    def test_single_unequal(self):
        self.assertEqual(self.sol.numDistinct("a", "b"), 0)


if __name__ == "__main__":
    unittest.main()
