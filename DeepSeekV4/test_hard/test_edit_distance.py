import unittest


class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
        return dp[m][n]


class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        word1, word2 = "horse", "ros"
        self.assertEqual(self.sol.minDistance(word1, word2), 3)

    def test_example2(self):
        word1, word2 = "intention", "execution"
        self.assertEqual(self.sol.minDistance(word1, word2), 5)

    # ---------- 边界情况 ----------
    def test_both_empty(self):
        self.assertEqual(self.sol.minDistance("", ""), 0)

    def test_first_empty_second_nonempty(self):
        self.assertEqual(self.sol.minDistance("", "abc"), 3)  # 三次插入

    def test_first_nonempty_second_empty(self):
        self.assertEqual(self.sol.minDistance("abc", ""), 3)  # 三次删除

    def test_equal_strings(self):
        self.assertEqual(self.sol.minDistance("same", "same"), 0)
        self.assertEqual(self.sol.minDistance("", ""), 0)

    def test_single_character_same(self):
        self.assertEqual(self.sol.minDistance("a", "a"), 0)

    def test_single_character_different(self):
        self.assertEqual(self.sol.minDistance("a", "b"), 1)  # 替换

    # ---------- 常见场景 ----------
    def test_one_edit(self):
        self.assertEqual(self.sol.minDistance("cat", "cats"), 1)  # 插入
        self.assertEqual(self.sol.minDistance("cats", "cat"), 1)  # 删除
        self.assertEqual(self.sol.minDistance("cat", "bat"), 1)  # 替换

    def test_no_common_chars(self):
        self.assertEqual(self.sol.minDistance("abc", "def"), 3)  # 全部替换

    def test_reverse(self):
        self.assertEqual(
            self.sol.minDistance("abc", "cba"), 2
        )  # 例如 abc->cbc->cba 或 abc->ab->cb->cba

    # ---------- 随机对比暴力递归（仅限小长度）----------
    def test_random_small_against_recursive(self):
        """使用递归暴力枚举（指数复杂度）验证小长度字符串的正确性"""

        def recursive_distance(w1, w2):
            # 递归实现，仅用于正确性验证，长度不宜超过6
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)
            if w1[0] == w2[0]:
                return recursive_distance(w1[1:], w2[1:])
            else:
                insert = 1 + recursive_distance(w1, w2[1:])
                delete = 1 + recursive_distance(w1[1:], w2)
                replace = 1 + recursive_distance(w1[1:], w2[1:])
                return min(insert, delete, replace)

        import random

        letters = ["a", "b", "c", "d"]
        for _ in range(50):
            len1 = random.randint(0, 5)
            len2 = random.randint(0, 5)
            w1 = "".join(random.choice(letters) for __ in range(len1))
            w2 = "".join(random.choice(letters) for __ in range(len2))
            expected = recursive_distance(w1, w2)
            self.assertEqual(
                self.sol.minDistance(w1, w2), expected, f"Failed for w1={w1}, w2={w2}"
            )

    # ---------- 性能测试（长度上限500）----------
    def test_performance_max_length(self):
        """测试最长约束下的运行时间（约500，不会超时）"""
        import time

        w1 = "a" * 500
        w2 = "b" * 500
        start = time.time()
        dist = self.sol.minDistance(w1, w2)
        elapsed = time.time() - start
        self.assertEqual(dist, 500)  # 全部替换
        self.assertLess(elapsed, 1.0, f"Too slow: {elapsed:.2f}s")

    def test_performance_random_500(self):
        """随机500长度字符串，确保不超时"""
        import random
        import string

        letters = string.ascii_lowercase
        w1 = "".join(random.choice(letters) for _ in range(500))
        w2 = "".join(random.choice(letters) for _ in range(500))
        start = time.time()
        _ = self.sol.minDistance(w1, w2)
        elapsed = time.time() - start
        self.assertLess(elapsed, 2.0, f"Slow for random 500: {elapsed:.2f}s")


if __name__ == "__main__":
    unittest.main()
