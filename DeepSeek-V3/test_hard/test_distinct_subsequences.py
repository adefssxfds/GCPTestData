import unittest


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


class TestNumDistinct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        s, t = "rabbbit", "rabbit"
        self.assertEqual(self.sol.numDistinct(s, t), 3)

    def test_example2(self):
        s, t = "babgbag", "bag"
        self.assertEqual(self.sol.numDistinct(s, t), 5)

    # ---------- 边界情况 ----------
    def test_t_longer_than_s(self):
        s, t = "abc", "abcd"
        self.assertEqual(self.sol.numDistinct(s, t), 0)

    def test_empty_t(self):
        s, t = "anything", ""
        self.assertEqual(self.sol.numDistinct(s, t), 1)

    def test_empty_s_nonempty_t(self):
        s, t = "", "a"
        self.assertEqual(self.sol.numDistinct(s, t), 0)

    def test_both_empty(self):
        s, t = "", ""
        self.assertEqual(self.sol.numDistinct(s, t), 1)

    # ---------- 单字符 ----------
    def test_single_char_match(self):
        s, t = "a", "a"
        self.assertEqual(self.sol.numDistinct(s, t), 1)

    def test_single_char_no_match(self):
        s, t = "a", "b"
        self.assertEqual(self.sol.numDistinct(s, t), 0)

    # ---------- 重复字符 ----------
    def test_repeated_chars(self):
        s, t = "aaa", "aa"
        # 从三个 a 中选两个位置，C(3,2)=3
        self.assertEqual(self.sol.numDistinct(s, t), 3)

    def test_repeated_chars2(self):
        s, t = "aaaa", "aa"
        self.assertEqual(self.sol.numDistinct(s, t), 6)  # C(4,2)=6

    # ---------- 无匹配 ----------
    def test_no_subsequence(self):
        s, t = "abcde", "f"
        self.assertEqual(self.sol.numDistinct(s, t), 0)

    # ---------- 完全匹配 ----------
    def test_whole_string_match(self):
        s, t = "hello", "hello"
        self.assertEqual(self.sol.numDistinct(s, t), 1)

    # ---------- 部分重叠 ----------
    def test_overlap(self):
        s, t = "aaaa", "aa"
        self.assertEqual(self.sol.numDistinct(s, t), 6)

    # ---------- 随机测试（对比递归暴力验证小规模）----------
    def test_random_small(self):
        """小规模随机字符串，对比 DP 结果与递归枚举（仅限长度 ≤6 以确保效率）"""
        import itertools

        def brute_force(s, t):
            # 枚举所有子序列，统计等于 t 的个数（仅用于小规模验证）
            n = len(s)
            count = 0
            for mask in range(1 << n):
                subseq = "".join(s[i] for i in range(n) if (mask >> i) & 1)
                if subseq == t:
                    count += 1
            return count

        import random

        letters = ["a", "b", "c", "d"]
        for _ in range(20):
            len_s = random.randint(1, 6)
            len_t = random.randint(0, min(4, len_s))
            s = "".join(random.choice(letters) for __ in range(len_s))
            t = "".join(random.choice(letters) for __ in range(len_t))
            expected = brute_force(s, t)
            self.assertEqual(self.sol.numDistinct(s, t), expected, f"s={s}, t={t}")

    # ---------- 大型边界测试（性能）----------
    def test_large_strings(self):
        """长字符串但只包含相同字符，验证组合数结果（避免整型溢出，但 Python 自动处理）"""
        s = "a" * 1000
        t = "a" * 500
        # 结果应为 C(1000, 500)，远超 32 位但 Python 自动处理
        # 我们只测试算法不崩溃并返回正确的大整数（Python 无限精度）
        result = self.sol.numDistinct(s, t)
        # 验证组合数：C(1000,500) 可以使用 math.comb
        import math

        expected = math.comb(1000, 500)
        self.assertEqual(result, expected)

    def test_large_with_mixed_chars(self):
        """随机大字符串，确保 DP 矩阵构建正确"""
        import random

        s = "".join(random.choice("abcdefghij") for _ in range(500))
        t = "".join(random.choice("abcdefghij") for _ in range(50))
        # 只测试不崩溃，并返回整数
        result = self.sol.numDistinct(s, t)
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()
