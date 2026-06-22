import unittest


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


class TestInterleavingString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))

    def test_example2(self):
        s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"
        self.assertFalse(self.sol.isInterleave(s1, s2, s3))

    def test_example3(self):
        s1, s2, s3 = "", "", ""
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))

    # ---------- 边界条件 ----------
    def test_one_empty(self):
        s1, s2, s3 = "", "abc", "abc"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        s1, s2, s3 = "abc", "", "abc"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        s1, s2, s3 = "", "abc", "abd"
        self.assertFalse(self.sol.isInterleave(s1, s2, s3))

    def test_length_mismatch(self):
        s1, s2, s3 = "ab", "cd", "abc"
        self.assertFalse(self.sol.isInterleave(s1, s2, s3))
        s1, s2, s3 = "ab", "cd", "abcd"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))

    def test_single_char(self):
        s1, s2, s3 = "a", "b", "ab"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        s1, s2, s3 = "a", "b", "ba"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        s1, s2, s3 = "a", "b", "ac"
        self.assertFalse(self.sol.isInterleave(s1, s2, s3))

    def test_all_same_char(self):
        s1, s2, s3 = "aaa", "aaa", "aaaaaa"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        s1, s2, s3 = "aaa", "aaa", "aaaaa"
        self.assertFalse(self.sol.isInterleave(s1, s2, s3))

    def test_interleaving_requires_choice(self):
        # s1 = "ab", s2 = "bc", s3 = "abbc" -> 可以: a(b) + bc? 实际上 "ab" + "bc" 可组成 "abbc" (ab + bc)
        s1, s2, s3 = "ab", "bc", "abbc"
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        # 但 "ac" 不行
        s1, s2, s3 = "ab", "bc", "acbb"
        self.assertFalse(self.sol.isInterleave(s1, s2, s3))

    # ---------- 随机对比 DFS 回溯（用于小规模验证）----------
    def test_random_compare_with_backtracking(self):
        """使用递归回溯验证小长度字符串的正确性"""

        def is_interleave_backtrack(s1, s2, s3, i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if k == len(s3):
                return False
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or is_interleave_backtrack(s1, s2, s3, i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                res = res or is_interleave_backtrack(s1, s2, s3, i, j + 1, k + 1)
            return res

        import random

        letters = ["a", "b", "c"]
        for _ in range(100):
            len1 = random.randint(0, 5)
            len2 = random.randint(0, 5)
            s1 = "".join(random.choice(letters) for __ in range(len1))
            s2 = "".join(random.choice(letters) for __ in range(len2))
            # 随机生成 s3 要么是交错，要么完全随机（不保证长度）
            if random.random() < 0.5:
                # 生成合法的交错
                inter = []
                i, j = 0, 0
                while i < len1 and j < len2:
                    if random.choice([True, False]):
                        inter.append(s1[i])
                        i += 1
                    else:
                        inter.append(s2[j])
                        j += 1
                inter.extend(s1[i:])
                inter.extend(s2[j:])
                s3 = "".join(inter)
            else:
                # 随机长度（可能不匹配）或随机字符
                s3_len = random.randint(0, len1 + len2)
                s3 = "".join(random.choice(letters) for __ in range(s3_len))
            expected = is_interleave_backtrack(s1, s2, s3, 0, 0, 0)
            result = self.sol.isInterleave(s1, s2, s3)
            self.assertEqual(result, expected, f"Mismatch: s1={s1}, s2={s2}, s3={s3}")

    # ---------- 性能测试（长度 <= 100）----------
    def test_performance(self):
        s1 = "a" * 100
        s2 = "b" * 100
        s3 = "ab" * 100  # 交替
        import time

        start = time.time()
        self.assertTrue(self.sol.isInterleave(s1, s2, s3))
        elapsed = time.time() - start
        self.assertLess(elapsed, 1.0, f"Performance too slow: {elapsed:.2f}s")

        s3_bad = "a" * 100 + "b" * 100
        start = time.time()
        self.assertTrue(self.sol.isInterleave(s1, s2, s3_bad))
        elapsed2 = time.time() - start
        self.assertLess(elapsed2, 1.0)


if __name__ == "__main__":
    unittest.main()
