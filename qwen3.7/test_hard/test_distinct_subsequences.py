import unittest


# --- 将你的算法放在这里 ---
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


# --- 测试代码 ---
class TestNumDistinct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5)]
        for s, t, expected in test_cases:
            with self.subTest(s=s, t=t):
                result = self.solution.numDistinct(s, t)
                self.assertEqual(result, expected)

    def test_identical_strings(self):
        """测试两个字符串完全相同的情况（只有1种匹配方式）"""
        s = "abc"
        t = "abc"
        expected = 1
        result = self.solution.numDistinct(s, t)
        self.assertEqual(result, expected)

    def test_t_longer_than_s(self):
        """测试 t 的长度大于 s 的情况（直接返回 0）"""
        s = "abc"
        t = "abcd"
        expected = 0
        result = self.solution.numDistinct(s, t)
        self.assertEqual(result, expected)

    def test_no_match(self):
        """测试完全没有匹配的情况"""
        s = "abc"
        t = "d"
        expected = 0
        result = self.solution.numDistinct(s, t)
        self.assertEqual(result, expected)

    def test_t_is_empty(self):
        """测试 t 为空字符串的情况（任何字符串都有1个空子序列）"""
        s = "abc"
        t = ""
        expected = 1
        result = self.solution.numDistinct(s, t)
        self.assertEqual(result, expected)

    def test_repeated_characters(self):
        """测试包含大量重复字符的情况"""
        # s = "aaaa", t = "aa"
        # 匹配方式: C(4,2) = 6
        s = "aaaa"
        t = "aa"
        expected = 6
        result = self.solution.numDistinct(s, t)
        self.assertEqual(result, expected)

    def test_single_char_match(self):
        """测试单字符匹配的情况"""
        s = "ababa"
        t = "a"
        expected = 3  # 有3个 'a'
        result = self.solution.numDistinct(s, t)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
