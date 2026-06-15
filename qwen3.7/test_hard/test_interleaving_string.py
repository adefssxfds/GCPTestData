import unittest


# --- 将你的算法放在这里 ---
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for row in range(len(s1) + 1):
            for col in range(len(s2) + 1):
                if row == 0 and col == 0:
                    dp[row][col] = True
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]
                else:
                    dp[row][col] = (
                        dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                    ) or (dp[row - 1][col] and s1[row - 1] == s3[row + col - 1])

        return dp[len(s1)][len(s2)]


# --- 测试代码 ---
class TestIsInterleave(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ("aabcc", "dbbca", "aadbbcbcac", True),
            ("aabcc", "dbbca", "aadbbbaccc", False),
            ("", "", "", True),
        ]
        for s1, s2, s3, expected in test_cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.isInterleave(s1, s2, s3)
                self.assertEqual(result, expected)

    def test_length_mismatch(self):
        """测试长度不匹配的情况（前置剪枝）"""
        s1 = "abc"
        s2 = "def"
        s3 = "abcd"  # 长度不够
        expected = False
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)

    def test_empty_s1(self):
        """测试 s1 为空的情况"""
        s1 = ""
        s2 = "abc"
        s3 = "abc"
        expected = True
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)

    def test_empty_s2(self):
        """测试 s2 为空的情况"""
        s1 = "abc"
        s2 = ""
        s3 = "abc"
        expected = True
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)

    def test_no_interleave(self):
        """测试完全无法交错的情况"""
        s1 = "abc"
        s2 = "def"
        s3 = "abcdefg"  # 长度匹配但字符不对
        expected = False
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)

    def test_complex_interleave(self):
        """测试复杂的交错情况"""
        s1 = "a"
        s2 = "b"
        s3 = "ab"
        expected = True
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)

    def test_repeated_chars(self):
        """测试包含大量重复字符的情况"""
        s1 = "aa"
        s2 = "aa"
        s3 = "aaaa"
        expected = True
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)

    def test_partial_match_fail(self):
        """测试前缀匹配但后缀失败的情况"""
        s1 = "abc"
        s2 = "def"
        s3 = "abxdef"  # 前缀 ab 匹配，但 x 导致失败
        expected = False
        result = self.solution.isInterleave(s1, s2, s3)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
