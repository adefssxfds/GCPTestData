class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for row in range(m + 1):
            for col in range(n + 1):
                if row == 0 and col == 0:
                    dp[row][col] = True
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]
                else:
                    opt1 = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                    opt2 = dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]
                    dp[row][col] = opt1 or opt2
        return dp[m][n]


import unittest


class TestIsInterleave(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_true(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        self.assertEqual(self.sol.isInterleave(s1, s2, s3), True)

    def test_example2_false(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        self.assertEqual(self.sol.isInterleave(s1, s2, s3), False)

    def test_one_empty(self):
        self.assertEqual(self.sol.isInterleave("", "abc", "abc"), True)
        self.assertEqual(self.sol.isInterleave("abc", "", "abc"), True)

    def test_both_empty(self):
        self.assertEqual(self.sol.isInterleave("", "", ""), True)

    def test_len_mismatch(self):
        self.assertEqual(self.sol.isInterleave("a", "b", "abc"), False)

    def test_simple_interleave(self):
        self.assertEqual(self.sol.isInterleave("ab", "cd", "acbd"), True)


if __name__ == "__main__":
    unittest.main()
