class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for index_i in range(m + 1):
            for index_j in range(n + 1):
                if index_i == 0:
                    dp[index_i][index_j] = index_j
                elif index_j == 0:
                    dp[index_i][index_j] = index_i
                elif word1[index_i - 1] == word2[index_j - 1]:
                    dp[index_i][index_j] = dp[index_i - 1][index_j - 1]
                else:
                    dp[index_i][index_j] = 1 + min(
                        dp[index_i - 1][index_j],  # 删除word1字符
                        dp[index_i - 1][index_j - 1],  # 替换
                        dp[index_i][index_j - 1],  # 插入字符到word1
                    )
        return dp[m][n]


import unittest


class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # 题目样例1
    def test_example1(self):
        self.assertEqual(self.sol.minDistance("horse", "ros"), 3)

    # 题目样例2
    def test_example2(self):
        self.assertEqual(self.sol.minDistance("intention", "execution"), 5)

    # word1为空串
    def test_w1_empty(self):
        self.assertEqual(self.sol.minDistance("", "abc"), 3)

    # word2为空串
    def test_w2_empty(self):
        self.assertEqual(self.sol.minDistance("abc", ""), 3)

    # 两个字符串完全一致
    def test_same_str(self):
        self.assertEqual(self.sol.minDistance("abcde", "abcde"), 0)

    # 单字符替换
    def test_single_replace(self):
        self.assertEqual(self.sol.minDistance("a", "z"), 1)

    # 仅插入一个字符
    def test_only_insert(self):
        self.assertEqual(self.sol.minDistance("k", "ke"), 1)

    # 仅删除一个字符
    def test_only_delete(self):
        self.assertEqual(self.sol.minDistance("ke", "k"), 1)


if __name__ == "__main__":
    unittest.main()
