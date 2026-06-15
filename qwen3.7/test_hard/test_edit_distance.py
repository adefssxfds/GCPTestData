import unittest


# --- 将你的算法放在这里 ---
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
                        dp[index_i - 1][index_j],
                        dp[index_i - 1][index_j - 1],
                        dp[index_i][index_j - 1],
                    )
        return dp[m][n]


# --- 测试代码 ---
class TestMinDistance(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [("horse", "ros", 3), ("intention", "execution", 5)]
        for word1, word2, expected in test_cases:
            with self.subTest(word1=word1, word2=word2):
                result = self.solution.minDistance(word1, word2)
                self.assertEqual(result, expected)

    def test_identical_strings(self):
        """测试两个字符串完全相同的情况（编辑距离为 0）"""
        word1 = "abc"
        word2 = "abc"
        expected = 0
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_empty_word1(self):
        """测试 word1 为空的情况（全部需要插入）"""
        word1 = ""
        word2 = "abc"
        expected = 3
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_empty_word2(self):
        """测试 word2 为空的情况（全部需要删除）"""
        word1 = "abc"
        word2 = ""
        expected = 3
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_both_empty(self):
        """测试两个字符串都为空的情况"""
        word1 = ""
        word2 = ""
        expected = 0
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_only_insertions(self):
        """测试只需要插入的情况"""
        word1 = "abc"
        word2 = "aXbYc"
        expected = 2  # 插入 X 和 Y
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_only_deletions(self):
        """测试只需要删除的情况"""
        word1 = "aXbYc"
        word2 = "abc"
        expected = 2  # 删除 X 和 Y
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_only_replacements(self):
        """测试只需要替换的情况"""
        word1 = "abc"
        word2 = "xyz"
        expected = 3  # a->x, b->y, c->z
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)

    def test_reversed_strings(self):
        """测试互为反转的字符串"""
        word1 = "abcd"
        word2 = "dcba"
        expected = 4  # 需要替换所有字符，或者通过插入/删除
        result = self.solution.minDistance(word1, word2)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
